import importlib.util
from pathlib import Path
import unittest


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


if __name__ == '__main__':
    unittest.main()
