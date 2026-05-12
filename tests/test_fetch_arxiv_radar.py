import importlib.util
import os
from pathlib import Path
import tempfile
import unittest
from unittest import mock


SCRIPT_PATH = Path(__file__).resolve().parents[1] / 'scripts' / 'fetch_arxiv_radar.py'
spec = importlib.util.spec_from_file_location('fetch_arxiv_radar', SCRIPT_PATH)
radar = importlib.util.module_from_spec(spec)
spec.loader.exec_module(radar)


class FetchArxivRadarTests(unittest.TestCase):
    def test_extract_experiment_takeaways_prefers_result_sentences(self):
        summary = (
            'We introduce a routing policy for cost-efficient reasoning. '
            'Experiments on AIME and GSM8K show 28% lower latency and 1.6x higher throughput than vLLM. '
            'The method also outperforms a larger baseline on reasoning accuracy while reducing serving cost by 35%. '
            'We release code and models.'
        )
        takeaways = radar.extract_experiment_takeaways(summary)
        self.assertIn('28% lower latency', takeaways)
        self.assertIn('1.6x higher throughput', takeaways)
        self.assertIn('35%', takeaways)
        self.assertNotIn('We release code and models', takeaways)

    def test_extract_experiment_takeaways_avoids_background_sentences(self):
        summary = (
            'Large language model workflows compose specialized agents for hard tasks. '
            'Experiments on three workflow benchmarks show that PBKV achieves up to 1.85x speedup over LRU '
            'and 1.26x speedup over KVFlow. '
            'Based on the predictions, PBKV keeps high-potential KV cache entries in GPU memory.'
        )
        takeaways = radar.extract_experiment_takeaways(summary)
        self.assertIn('1.85x speedup', takeaways)
        self.assertIn('1.26x speedup', takeaways)
        self.assertNotIn('Large language model workflows compose specialized agents', takeaways)
        self.assertNotIn('keeps high-potential KV cache entries in GPU memory', takeaways)

    def test_build_cn_brief_fallback_returns_two_or_three_sentences(self):
        item = {
            'title': 'SplitZip: Ultra Fast Lossless KV Compression for Disaggregated LLM Serving',
            'summary': (
                'Experiments show 2.1x throughput improvement and 34% lower transfer time '
                'for disaggregated serving while preserving model quality.'
            ),
            'source': 'arXiv API',
            'source_type': 'paper',
            'categories': ['cs.DC'],
            'matched_topics': ['Cost-efficient LLM inference', 'Heterogeneous MoE inference'],
            'reason_hits': ['kv cache', 'disaggregation'],
        }
        brief = radar.build_cn_brief(item, llm_text='')
        self.assertGreaterEqual(brief.count('。'), 2)
        self.assertIn('实验', brief)

    def test_render_item_block_uses_chinese_first_layout(self):
        full_summary = 'English summary sentence one. English summary sentence two.'
        item = {
            'title': 'Example Paper',
            'paper_id': '2605.00001v1',
            'source': 'arXiv API',
            'source_type': 'paper',
            'published_dt': None,
            'published': '2026-05-10',
            'score_with_authority': 42,
            'matched_topics': ['LLM routing'],
            'authors': ['Alice'],
            'categories': ['cs.AI'],
            'cn_summary': '第一句。第二句。第三句。',
            'cn_abstract': '这是一段较完整的中文摘要。',
            'summary': full_summary,
            'cn_experiment_takeaways': '实验显示延迟下降 28%，吞吐提升 1.6x。',
            'experiment_takeaways': 'Latency drops by 28% and throughput increases by 1.6x.',
            'url': 'https://arxiv.org/abs/2605.00001',
            'pdf_url': 'https://arxiv.org/pdf/2605.00001v1',
        }
        rendered = '\n'.join(radar.render_item_block(item, 1))
        self.assertIn('- 中文解读: 第一句。第二句。第三句。', rendered)
        self.assertIn('- 中文摘要: 这是一段较完整的中文摘要。', rendered)
        self.assertIn('- 中文实验结论: 实验显示延迟下降 28%，吞吐提升 1.6x。', rendered)
        self.assertIn(f'- 英文原摘要: {full_summary}', rendered)
        self.assertNotIn('- 完整摘要:', rendered)

    def test_render_readme_is_chinese_first(self):
        readme = radar.render_readme('2026-05-10', [], [], [], [])
        self.assertIn('一个面向以下方向的每日更新研究雷达：', readme)
        self.assertIn('当前能力包括：', readme)
        self.assertIn('中文多句解读、中文摘要与中文实验结论提炼', readme)
        self.assertNotIn('A daily-updated research radar for:', readme)

    def test_load_copilot_token_prefers_env_over_file(self):
        with tempfile.NamedTemporaryFile('w', delete=False, encoding='utf-8') as tmp:
            tmp.write('GITHUB_TOKEN=file_token\n')
            env_path = tmp.name
        try:
            with mock.patch.object(radar, 'ENV_PATH', Path(env_path)):
                with mock.patch.dict(os.environ, {'GITHUB_TOKEN': 'env_token'}, clear=False):
                    self.assertEqual(radar.load_copilot_token(), 'env_token')
        finally:
            Path(env_path).unlink(missing_ok=True)

    def test_load_copilot_token_supports_legacy_secret_name_without_underscores(self):
        with mock.patch.object(radar, 'ENV_PATH', Path('/tmp/nonexistent-hermes-env-for-test')):
            with mock.patch.dict(os.environ, {'COPILOTGITHUBTOKEN': 'legacy_token'}, clear=True):
                self.assertEqual(radar.load_copilot_token(), 'legacy_token')

    def test_copilot_headers_include_github_copilot_markers(self):
        headers = radar.copilot_headers('legacy_token')
        self.assertEqual(headers['Authorization'], 'Bearer legacy_token')
        self.assertIn('Editor-Version', headers)
        self.assertIn('Copilot-Integration-Id', headers)
        self.assertIn('X-Request-Id', headers)

    def test_build_cn_abstract_fallback_is_not_raw_english(self):
        item = {
            'summary': 'This system reduces TTFT by 40% and improves throughput by 1.8x on long-context serving.',
        }
        with mock.patch.object(radar, 'llm_translate_cn', return_value=''):
            translated = radar.build_cn_abstract(item)
        self.assertNotIn('This system reduces TTFT', translated)
        self.assertIn('40%', translated)
        self.assertIn('1.8x', translated)
        self.assertTrue(any(ch >= '\u4e00' and ch <= '\u9fff' for ch in translated))

    def test_build_cn_experiment_takeaways_fallback_is_not_raw_english(self):
        item = {
            'experiment_takeaways': 'Latency drops by 28% and throughput increases by 1.6x compared with vLLM.',
        }
        with mock.patch.object(radar, 'llm_translate_cn', return_value=''):
            translated = radar.build_cn_experiment_takeaways(item)
        self.assertNotIn('Latency drops by 28%', translated)
        self.assertIn('28%', translated)
        self.assertTrue(any(ch >= '\u4e00' and ch <= '\u9fff' for ch in translated))

    def test_collect_arxiv_skips_rate_limited_query_and_keeps_other_results(self):
        config = {
            'max_results_per_query': 5,
            'queries': [
                {'name': 'q1', 'query': 'first'},
                {'name': 'q2', 'query': 'second'},
            ],
        }
        xml_ok = '''
        <feed xmlns="http://www.w3.org/2005/Atom">
          <entry>
            <id>http://arxiv.org/abs/2605.00001v1</id>
            <title>Test Paper</title>
            <summary>Test summary</summary>
            <published>2026-05-10T00:00:00Z</published>
            <updated>2026-05-10T00:00:00Z</updated>
            <author><name>Alice</name></author>
            <category term="cs.AI" />
          </entry>
        </feed>
        '''
        rate_limit = radar.urllib.error.HTTPError(
            'https://export.arxiv.org/api/query', 429, 'Too Many Requests', None, None
        )
        with mock.patch.object(radar, 'arxiv_search', side_effect=[rate_limit, xml_ok]):
            with mock.patch.object(radar.time, 'sleep', return_value=None):
                items = radar.collect_arxiv(config, days_back=30)
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]['title'], 'Test Paper')

    def test_collect_arxiv_skips_rate_limited_query_and_keeps_other_results(self):
        config = {
            'max_results_per_query': 5,
            'queries': [
                {'name': 'q1', 'query': 'first'},
                {'name': 'q2', 'query': 'second'},
            ],
        }
        xml_ok = '''
        <feed xmlns="http://www.w3.org/2005/Atom">
          <entry>
            <id>http://arxiv.org/abs/2605.00001v1</id>
            <title>Test Paper</title>
            <summary>Test summary</summary>
            <published>2026-05-10T00:00:00Z</published>
            <updated>2026-05-10T00:00:00Z</updated>
            <author><name>Alice</name></author>
            <category term="cs.AI" />
          </entry>
        </feed>
        '''
        rate_limit = radar.urllib.error.HTTPError(
            'https://export.arxiv.org/api/query', 429, 'Too Many Requests', None, None
        )
        with mock.patch.object(radar, 'arxiv_search', side_effect=[rate_limit, xml_ok]):
            with mock.patch.object(radar.time, 'sleep', return_value=None):
                items = radar.collect_arxiv(config, days_back=30)
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]['title'], 'Test Paper')

    def test_collect_arxiv_skips_503_query_and_keeps_other_results(self):
        config = {
            'max_results_per_query': 5,
            'queries': [
                {'name': 'q1', 'query': 'first'},
                {'name': 'q2', 'query': 'second'},
            ],
        }
        xml_ok = '''
        <feed xmlns="http://www.w3.org/2005/Atom">
          <entry>
            <id>http://arxiv.org/abs/2605.00003v1</id>
            <title>Recovered After 503</title>
            <summary>Test summary</summary>
            <published>2026-05-10T00:00:00Z</published>
            <updated>2026-05-10T00:00:00Z</updated>
            <author><name>Carol</name></author>
            <category term="cs.AI" />
          </entry>
        </feed>
        '''
        svc_unavail = radar.urllib.error.HTTPError(
            'https://export.arxiv.org/api/query', 503, 'Service Unavailable', None, None
        )
        with mock.patch.object(radar, 'arxiv_search', side_effect=[svc_unavail, xml_ok]):
            with mock.patch.object(radar.time, 'sleep', return_value=None):
                items = radar.collect_arxiv(config, days_back=30)
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]['title'], 'Recovered After 503')

    def test_collect_arxiv_skips_network_error_query_and_keeps_other_results(self):
        config = {
            'max_results_per_query': 5,
            'queries': [
                {'name': 'q1', 'query': 'first'},
                {'name': 'q2', 'query': 'second'},
            ],
        }
        xml_ok = '''
        <feed xmlns="http://www.w3.org/2005/Atom">
          <entry>
            <id>http://arxiv.org/abs/2605.00002v1</id>
            <title>Recovered Paper</title>
            <summary>Test summary</summary>
            <published>2026-05-10T00:00:00Z</published>
            <updated>2026-05-10T00:00:00Z</updated>
            <author><name>Bob</name></author>
            <category term="cs.AI" />
          </entry>
        </feed>
        '''
        url_err = radar.urllib.error.URLError('Remote end closed connection without response')
        with mock.patch.object(radar, 'arxiv_search', side_effect=[url_err, xml_ok]):
            with mock.patch.object(radar.time, 'sleep', return_value=None):
                items = radar.collect_arxiv(config, days_back=30)
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]['title'], 'Recovered Paper')

    def test_collect_arxiv_skips_timeout_query_and_keeps_other_results(self):
        config = {
            'max_results_per_query': 5,
            'queries': [
                {'name': 'q1', 'query': 'first'},
                {'name': 'q2', 'query': 'second'},
            ],
        }
        xml_ok = '''
        <feed xmlns="http://www.w3.org/2005/Atom">
          <entry>
            <id>http://arxiv.org/abs/2605.00004v1</id>
            <title>Recovered After Timeout</title>
            <summary>Test summary</summary>
            <published>2026-05-10T00:00:00Z</published>
            <updated>2026-05-10T00:00:00Z</updated>
            <author><name>Dave</name></author>
            <category term="cs.AI" />
          </entry>
        </feed>
        '''
        with mock.patch.object(radar, 'arxiv_search', side_effect=[TimeoutError('read timed out'), xml_ok]):
            with mock.patch.object(radar.time, 'sleep', return_value=None):
                items = radar.collect_arxiv(config, days_back=30)
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]['title'], 'Recovered After Timeout')

    def test_prepare_items_survives_arxiv_rate_limit(self):
        config = {'days_back': 3}
        feed_item = {
            'id': 'feed-1',
            'title': 'vLLM released a new scheduling optimization',
            'summary': 'This update improves throughput by 1.4x and reduces latency by 20%.',
            'published_dt': radar.dt.datetime.now(radar.dt.timezone.utc),
            'published': '2026-05-11',
            'source': 'vLLM Blog',
            'source_type': 'blog',
            'categories': [],
            'matched_topics': ['Cost-efficient LLM inference'],
            'authority': 2.0,
            'url': 'https://example.com',
        }
        rate_limit = radar.urllib.error.HTTPError(
            'https://export.arxiv.org/api/query', 429, 'Too Many Requests', None, None
        )
        with mock.patch.object(radar, 'collect_arxiv', side_effect=rate_limit):
            with mock.patch.object(radar, 'collect_feeds', return_value=[feed_item]):
                with mock.patch.object(radar, 'chinese_one_liner', return_value='中文解读。第二句。'):
                    with mock.patch.object(radar, 'build_cn_abstract', return_value='中文摘要'):
                        with mock.patch.object(radar, 'build_cn_experiment_takeaways', return_value='中文实验结论'):
                            items = radar.prepare_items(config, days_back=3)
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]['source'], 'vLLM Blog')

    def test_prepare_items_survives_arxiv_urlerror(self):
        config = {'days_back': 3}
        feed_item = {
            'id': 'feed-2',
            'title': 'SGLang improved prefix caching',
            'summary': 'This update reduces TTFT by 18% and improves throughput by 1.3x.',
            'published_dt': radar.dt.datetime.now(radar.dt.timezone.utc),
            'published': '2026-05-11',
            'source': 'LMSYS Blog',
            'source_type': 'blog',
            'categories': [],
            'matched_topics': ['Cost-efficient LLM inference'],
            'authority': 2.0,
            'url': 'https://example.com/2',
        }
        url_err = radar.urllib.error.URLError('Remote end closed connection without response')
        with mock.patch.object(radar, 'collect_arxiv', side_effect=url_err):
            with mock.patch.object(radar, 'collect_feeds', return_value=[feed_item]):
                with mock.patch.object(radar, 'chinese_one_liner', return_value='中文解读。第二句。'):
                    with mock.patch.object(radar, 'build_cn_abstract', return_value='中文摘要'):
                        with mock.patch.object(radar, 'build_cn_experiment_takeaways', return_value='中文实验结论'):
                            items = radar.prepare_items(config, days_back=3)
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]['source'], 'LMSYS Blog')


if __name__ == '__main__':
    unittest.main()
