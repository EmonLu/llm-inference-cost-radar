import datetime as dt
import json
import re
import ssl
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / 'config' / 'topics.json'
SEEN_PAPERS_PATH = ROOT / 'data' / 'seen_papers.json'
SEEN_FEEDS_PATH = ROOT / 'data' / 'seen_feed_items.json'
PAPERS_DIR = ROOT / 'papers'
DIGESTS_DIR = ROOT / 'digests'
README_PATH = ROOT / 'README.md'
ENV_PATH = Path('~/.hermes/.env').expanduser()

ATOM_NS = {'a': 'http://www.w3.org/2005/Atom'}
RSS_DATE_FORMATS = [
    '%a, %d %b %Y %H:%M:%S %z',
    '%a, %d %b %Y %H:%M:%S GMT',
    '%Y-%m-%dT%H:%M:%S%z',
    '%Y-%m-%dT%H:%M:%SZ',
]

TOPIC_KEYWORDS = {
    'LLM routing': [
        ('llmrouter', 10), ('routellm', 10), ('llm routing', 10), ('model routing', 9),
        ('router', 4), ('routing', 4), ('escalation', 3), ('local-to-cloud', 6),
        ('small model', 2), ('confidence estimation', 3), ('token allocator', 5)
    ],
    'Coding agent routing': [
        ('coding agent', 10), ('code agent', 10), ('software engineering agent', 10),
        ('swe-agent', 11), ('repo-level agent', 9), ('agentic coding', 8),
        ('repository-level', 5), ('tool-using agent', 4), ('programming agent', 7),
        ('failing test', 4), ('developer asking a coding agent', 8)
    ],
    'Agent systems and multi-agent efficiency': [
        ('multi-agent', 8), ('agentic workflow', 7), ('agent systems', 6), ('agent memory', 3),
        ('llm agent', 7), ('autonomous agent', 5), ('orchestrator', 4), ('delegation', 3),
        ('collaborating agents', 7), ('agentic ai', 7), ('agent workflow', 6),
        ('agentic workloads', 10), ('token allocation', 8)
    ],
    'Heterogeneous MoE inference': [
        ('mixture of experts', 10), ('moe', 9), ('expert parallelism', 9), ('heterogeneous', 8),
        ('cpu', 4), ('gpu', 4), ('offload', 7), ('offloading', 7), ('scheduling', 5),
        ('disaggregated', 6), ('hybrid inference', 8), ('expert substitution', 8),
        ('edge hardware', 5), ('prefill-decode disaggregation', 9)
    ],
    'Cost-efficient LLM inference': [
        ('cost-efficient', 8), ('cost effective', 8), ('efficient inference', 9), ('llm serving', 8),
        ('latency', 4), ('throughput', 4), ('quantization', 8), ('speculative decoding', 9),
        ('kv cache', 8), ('cache reuse', 5), ('serving', 4), ('memory bandwidth', 4),
        ('compression', 5), ('low-rank', 3), ('sparse', 3), ('edge device', 3), ('local model', 3),
        ('fault-tolerant', 3), ('checkpointing', 3), ('fp8', 7), ('disaggregation', 6),
        ('prefix cache', 7), ('prefill', 4), ('decode', 4)
    ],
}

SOURCE_HINTS = {
    'NVIDIA Generative AI Blog': [('nvidia', 3), ('gb300', 3), ('gb200', 3), ('inference', 3), ('moe', 4)],
    'NVIDIA TensorRT-LLM Blog': [('tensorrt-llm', 8), ('nvidia', 3), ('inference', 4), ('latency', 3), ('throughput', 3)],
    'PyTorch Blog': [('pytorch', 2), ('serving', 3), ('inference', 3), ('vllm', 4), ('deepspeed', 4)],
    'GitHub Blog': [('agent', 2), ('copilot', 3), ('coding', 2), ('developer', 2)],
    'LMSYS Blog': [('sglang', 8), ('inference', 4), ('moe', 5), ('hybrid inference', 6), ('cpu kernels', 6)],
    'vLLM Blog': [('vllm', 9), ('kv cache', 6), ('disaggregation', 6), ('prefill', 4), ('decode', 4)],
    'SemiAnalysis': [('gpu cluster', 5), ('cluster tco', 7), ('tco', 7), ('gpu', 3), ('inference', 2), ('coding assistant', 5)],
    'DeepSpeed': [('deepspeed', 9), ('mii', 5), ('deepspeed-inference', 8), ('fastgen', 8), ('inference', 4)],
    'arXiv cs.DC': [('systems', 2), ('serving', 2), ('scheduling', 3), ('distributed', 2)],
}

CN_PHRASES = {
    'llm routing': '聚焦大模型路由/小模型分流，直接相关。',
    'model routing': '直接讨论模型选择或路由策略，与你的主线高度一致。',
    'coding agent': '面向 coding agent 或软件工程 agent 的系统优化，相关性较高。',
    'code agent': '面向 coding agent 或软件工程 agent 的系统优化，相关性较高。',
    'software engineering agent': '研究软件工程智能体的能力或效率，与你关注方向贴近。',
    'swe-agent': '直接涉及 SWE-agent / 代码智能体场景，强相关。',
    'mixture of experts': '围绕 MoE 模型推理/部署优化，强相关。',
    'moe': '围绕 MoE 模型推理/部署优化，强相关。',
    'cpu': '涉及 CPU 侧参与推理或加速。',
    'gpu': '涉及 GPU 侧推理优化。',
    'heterogeneous': '强调异构硬件协同推理。',
    'offload': '涉及 KV/参数/专家的卸载策略，可节约显存或成本。',
    'quantization': '通过量化降低部署成本或加速推理。',
    'speculative decoding': '通过 speculative decoding 提升吞吐并降低单次推理成本。',
    'kv cache': '通过 KV cache 优化长上下文推理成本。',
    'serving': '关注在线 serving 系统优化，适合成本控制。',
    'latency': '重点优化延迟，通常可带来更高性价比。',
    'throughput': '重点优化吞吐，通常有助于降低单位成本。',
    'agent': '与 agent 系统/工作流有关，纳入重点跟踪。',
    'hybrid inference': '直接讨论混合/异构推理路径，与你关注 CPU/GPU 协同很贴近。',
    'sglang': '来自 SGLang/LMSYS 生态，通常具有较高工程参考价值。',
    'vllm': '来自 vLLM 官方生态，通常代表推理引擎的一线工程实践。',
    'deepspeed': '来自 DeepSpeed 生态，偏向高吞吐推理与系统优化。',
    'tensorrt-llm': '来自 TensorRT-LLM 生态，偏向 NVIDIA 推理栈的前沿实践。',
    'cluster tco': '直接讨论集群成本/TCO，与你降低推理成本的目标一致。',
}


def load_json(path, default):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding='utf-8'))


def save_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def normalize_text(text):
    return re.sub(r'\s+', ' ', unescape(text or '')).strip()


def strip_html(text):
    text = re.sub(r'<[^>]+>', ' ', text or '')
    return normalize_text(text)


def fetch_url(url, retries=3):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 Hermes-Agent'})
    last_error = None
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read().decode('utf-8', 'ignore')
        except Exception as e:
            last_error = e
            if isinstance(e, urllib.error.URLError) and 'CERTIFICATE_VERIFY_FAILED' in str(e):
                try:
                    insecure = ssl._create_unverified_context()
                    with urllib.request.urlopen(req, timeout=60, context=insecure) as r:
                        return r.read().decode('utf-8', 'ignore')
                except Exception as insecure_err:
                    last_error = insecure_err
            if attempt < retries - 1:
                time.sleep(2 * (attempt + 1))
    raise last_error


def load_copilot_token():
    for key in ['COPILOT_GITHUB_TOKEN', 'GITHUB_TOKEN', 'GH_TOKEN']:
        value = re.search(rf'^(?!\s*#)\s*{re.escape(key)}=(.+)$', ENV_PATH.read_text(encoding='utf-8', errors='ignore') if ENV_PATH.exists() else '', re.M)
        if value:
            token = value.group(1).strip().strip('"').strip("'")
            if token:
                return token
    return ''


def copilot_headers(token):
    return {
        'Authorization': f'Bearer {token}',
        'Editor-Version': 'vscode/1.104.1',
        'User-Agent': 'HermesAgent/1.0',
        'Openai-Intent': 'conversation-edits',
        'x-initiator': 'agent',
        'Content-Type': 'application/json',
    }


def llm_summarize_cn(title, summary, source, categories):
    token = load_copilot_token()
    if not token:
        return ''
    prompt = (
        '你是一个研究雷达助手。请只输出一句中文总结，不超过38个字。'
        '要点：1) 点出这项工作最核心的系统/成本价值；'
        '2) 如果和 routing、agent、MoE、CPU/GPU 异构、KV cache、量化、推理优化有关，要明确说出来；'
        '3) 不要使用编号、引号、前缀。'
    )
    user = (
        f'标题：{title}\n'
        f'来源：{source}\n'
        f'分类：{", ".join(categories[:8])}\n'
        f'摘要：{short_summary(summary, 900)}'
    )
    payload = {
        'model': 'gpt-4.1',
        'messages': [
            {'role': 'system', 'content': prompt},
            {'role': 'user', 'content': user},
        ],
        'temperature': 0.2,
        'max_tokens': 80,
    }
    req = urllib.request.Request(
        'https://api.githubcopilot.com/chat/completions',
        headers=copilot_headers(token),
        data=json.dumps(payload).encode('utf-8'),
        method='POST',
    )
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            data = json.loads(r.read().decode('utf-8', 'ignore'))
        text = normalize_text(data['choices'][0]['message']['content'])
        text = re.sub(r'^[\-•\d\.:：\s]+', '', text)
        return short_summary(text, 60)
    except Exception:
        return ''


def arxiv_search(query, max_results=20, start=0):
    params = {
        'search_query': query,
        'start': start,
        'max_results': max_results,
        'sortBy': 'submittedDate',
        'sortOrder': 'descending',
    }
    url = 'https://export.arxiv.org/api/query?' + urllib.parse.urlencode(params)
    return fetch_url(url)


def parse_feed_datetime(value):
    value = normalize_text(value)
    if not value:
        return None
    for fmt in RSS_DATE_FORMATS:
        try:
            parsed = dt.datetime.strptime(value, fmt)
            if parsed.tzinfo is None:
                parsed = parsed.replace(tzinfo=dt.timezone.utc)
            return parsed.astimezone(dt.timezone.utc)
        except Exception:
            continue
    try:
        parsed = dt.datetime.fromisoformat(value.replace('Z', '+00:00'))
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=dt.timezone.utc)
        return parsed.astimezone(dt.timezone.utc)
    except Exception:
        return None


def parse_arxiv_atom(xml_text, topic_name):
    root = ET.fromstring(xml_text)
    items = []
    for entry in root.findall('a:entry', ATOM_NS):
        entry_id = normalize_text(entry.findtext('a:id', default='', namespaces=ATOM_NS))
        title = normalize_text(entry.findtext('a:title', default='', namespaces=ATOM_NS))
        summary = normalize_text(entry.findtext('a:summary', default='', namespaces=ATOM_NS))
        published = normalize_text(entry.findtext('a:published', default='', namespaces=ATOM_NS))
        updated = normalize_text(entry.findtext('a:updated', default='', namespaces=ATOM_NS))
        authors = [normalize_text(a.findtext('a:name', default='', namespaces=ATOM_NS)) for a in entry.findall('a:author', ATOM_NS)]
        categories = [c.attrib.get('term', '') for c in entry.findall('a:category', ATOM_NS)]
        paper_id = entry_id.rsplit('/', 1)[-1]
        items.append({
            'id': paper_id,
            'paper_id': paper_id,
            'entry_id': entry_id,
            'title': title,
            'summary': summary,
            'published': published,
            'updated': updated,
            'published_dt': parse_feed_datetime(published),
            'authors': authors,
            'categories': categories,
            'topic': topic_name,
            'source': 'arXiv API',
            'source_type': 'paper',
            'pdf_url': f'https://arxiv.org/pdf/{paper_id}',
            'url': f'https://arxiv.org/abs/{paper_id}',
        })
    return items


def canonical_paper_id(raw_id, link=''):
    raw_id = normalize_text(raw_id)
    link = normalize_text(link)
    if re.match(r'^\d{4}\.\d{4,5}(v\d+)?$', raw_id):
        return raw_id
    if raw_id.startswith('oai:arXiv.org:'):
        return raw_id.split(':')[-1]
    for candidate in [link, raw_id]:
        m = re.search(r'arxiv\.org/(?:abs|pdf)/([^/?#]+)', candidate)
        if m:
            return m.group(1)
    return raw_id or link


def parse_rss_feed(xml_text, source_name, category='blog'):
    root = ET.fromstring(xml_text)
    channel = root.find('channel')
    if channel is None:
        return []
    items = []
    for item in channel.findall('item'):
        title = normalize_text(item.findtext('title', default=''))
        link = normalize_text(item.findtext('link', default=''))
        desc = strip_html(item.findtext('description', default=''))
        guid = normalize_text(item.findtext('guid', default=link or title))
        pub = normalize_text(item.findtext('pubDate', default=''))
        categories = [normalize_text(c.text) for c in item.findall('category') if normalize_text(c.text)]
        item_id = canonical_paper_id(guid, link) if 'arxiv.org' in (guid + ' ' + link).lower() else (guid or link or title)
        paper_id = item_id if re.match(r'^\d{4}\.\d{4,5}(v\d+)?$', item_id) else ''
        items.append({
            'id': item_id,
            'paper_id': paper_id,
            'title': title,
            'summary': desc,
            'published': pub,
            'updated': pub,
            'published_dt': parse_feed_datetime(pub),
            'authors': [],
            'categories': categories,
            'source': source_name,
            'source_type': category,
            'url': link,
            'pdf_url': f'https://arxiv.org/pdf/{paper_id}' if paper_id else '',
        })
    return items


def parse_atom_feed(xml_text, source_name, category='blog'):
    root = ET.fromstring(xml_text)
    ns = {'atom': 'http://www.w3.org/2005/Atom'}
    entries = root.findall('atom:entry', ns)
    items = []
    for entry in entries:
        title = normalize_text(entry.findtext('atom:title', default='', namespaces=ns))
        summary = normalize_text(entry.findtext('atom:summary', default='', namespaces=ns))
        if not summary:
            summary = strip_html(entry.findtext('atom:content', default='', namespaces=ns))
        published = normalize_text(entry.findtext('atom:published', default='', namespaces=ns))
        updated = normalize_text(entry.findtext('atom:updated', default='', namespaces=ns))
        item_id = normalize_text(entry.findtext('atom:id', default='', namespaces=ns))
        author = normalize_text(entry.findtext('atom:author/atom:name', default='', namespaces=ns))
        categories = [normalize_text(node.attrib.get('term', '')) for node in entry.findall('atom:category', ns)]
        link = ''
        for node in entry.findall('atom:link', ns):
            href = normalize_text(node.attrib.get('href', ''))
            rel = normalize_text(node.attrib.get('rel', 'alternate'))
            if href and rel in ('alternate', ''):
                link = href
                break
        if not link:
            link = item_id
        items.append({
            'id': item_id or link or title,
            'title': title,
            'summary': summary,
            'published': published,
            'updated': updated,
            'published_dt': parse_feed_datetime(published or updated),
            'authors': [author] if author else [],
            'categories': [c for c in categories if c],
            'source': source_name,
            'source_type': category,
            'url': link,
            'pdf_url': '',
        })
    return items


def parse_lmsys_blog(html_text):
    pattern = re.compile(r'/blog/(\d{4}-\d{2}-\d{2}-[^/\"#?]+)/')
    found = []
    seen = set()
    for slug in pattern.findall(html_text):
        if slug in seen:
            continue
        seen.add(slug)
        title = slug.split('-', 3)[-1].replace('-', ' ')
        date_part = '-'.join(slug.split('-')[:3])
        found.append({
            'id': f'https://www.lmsys.org/blog/{slug}/',
            'title': title.title(),
            'summary': 'LMSYS / SGLang 官方博客更新，通常包含推理优化、MoE、量化、混合推理或系统工程进展。',
            'published': date_part,
            'updated': date_part,
            'published_dt': parse_feed_datetime(date_part + 'T00:00:00Z'),
            'authors': [],
            'categories': ['LMSYS', 'SGLang'],
            'source': 'LMSYS Blog',
            'source_type': 'blog',
            'url': f'https://www.lmsys.org/blog/{slug}/',
            'pdf_url': '',
        })
    return found


def is_recent(dt_obj, days_back):
    if not dt_obj:
        return False
    now = dt.datetime.now(dt.timezone.utc)
    return dt_obj >= now - dt.timedelta(days=days_back)


def short_summary(text, width=260):
    text = normalize_text(text)
    if len(text) <= width:
        return text
    return text[: width - 1].rstrip() + '…'


def infer_topics_and_score(item):
    hay = f"{item['title']} {item['summary']} {' '.join(item.get('categories', []))} {item.get('source', '')}".lower()
    score = 0
    matched_topics = set(item.get('matched_topics', []))
    reason_hits = []

    for topic, pairs in TOPIC_KEYWORDS.items():
        local = 0
        for phrase, weight in pairs:
            if phrase in hay:
                local += weight
                reason_hits.append(phrase)
        if local > 0:
            matched_topics.add(topic)
            score += local

    for phrase, weight in SOURCE_HINTS.get(item.get('source', ''), []):
        if phrase in hay:
            score += weight
            reason_hits.append(phrase)

    score += 3 if item.get('source_type') == 'paper' else 1

    if 'agent' in hay:
        score += 4
        reason_hits.append('agent')
    if 'coding' in hay and 'agent' in hay:
        score += 5
        reason_hits.append('coding agent')
    if ('cpu' in hay and 'gpu' in hay) or 'heterogeneous' in hay or 'hybrid inference' in hay:
        score += 6
        reason_hits.append('heterogeneous')
    if 'mixture of experts' in hay or re.search(r'\bmoe\b', hay):
        score += 6
        reason_hits.append('moe')
    if 'cost' in hay or 'efficient' in hay or 'optimization' in hay:
        score += 2

    item['matched_topics'] = sorted(matched_topics)
    item['reason_hits'] = sorted(set(reason_hits))
    item['relevance_score'] = score
    return item


def chinese_one_liner(item):
    llm_text = llm_summarize_cn(item['title'], item['summary'], item['source'], item.get('categories', []))
    if llm_text:
        return llm_text
    hits = item.get('reason_hits', [])
    phrases = []
    for hit in hits:
        if hit in CN_PHRASES and CN_PHRASES[hit] not in phrases:
            phrases.append(CN_PHRASES[hit])
    if item.get('source_type') == 'blog':
        phrases.append('这是权威技术博客/官方工程更新，可帮助补充学术论文之外的工程趋势。')
    if not phrases:
        phrases.append('这篇内容与大模型推理效率或 agent 系统优化相关，建议关注。')
    return ' '.join(phrases[:2])


def collect_arxiv(config, days_back):
    max_results = int(config.get('max_results_per_query', 20))
    all_items = {}
    for q in config.get('queries', []):
        xml_text = arxiv_search(q['query'], max_results=max_results)
        time.sleep(3)
        for item in parse_arxiv_atom(xml_text, q['name']):
            if not is_recent(item['published_dt'], days_back):
                continue
            existing = all_items.get(item['id'])
            if existing:
                topics = set(existing.get('matched_topics', []))
                topics.add(item['topic'])
                existing['matched_topics'] = sorted(topics)
            else:
                item['matched_topics'] = [item['topic']]
                all_items[item['id']] = item
    return list(all_items.values())


def collect_feeds(config, days_back):
    all_items = {}
    for feed in config.get('source_feeds', []):
        xml_text = fetch_url(feed['url'])
        time.sleep(1)
        if feed.get('type') == 'html-lmsys':
            parsed = parse_lmsys_blog(xml_text)
        elif feed.get('type') == 'atom':
            parsed = parse_atom_feed(xml_text, feed['name'], feed.get('category', 'blog'))
        else:
            parsed = parse_rss_feed(xml_text, feed['name'], feed.get('category', 'blog'))
        for item in parsed:
            if not is_recent(item['published_dt'], days_back):
                continue
            item['authority'] = float(feed.get('authority', 1.0))
            all_items[item['id']] = item
    return list(all_items.values())


def split_items(items):
    papers = [x for x in items if x.get('source_type') == 'paper']
    feeds = [x for x in items if x.get('source_type') != 'paper']
    return papers, feeds


def filter_new_items(items, seen_ids):
    return [item for item in items if item['id'] not in seen_ids]


def passes_quality_gate(item):
    hay = f"{item['title']} {item['summary']} {' '.join(item.get('categories', []))}".lower()
    core_terms = [
        'llm', 'language model', 'transformer', 'mixture of experts', 'moe', 'inference',
        'serving', 'router', 'routing', 'kv cache', 'quantization', 'speculative decoding',
        'coding agent', 'code agent', 'software engineering agent', 'swe-agent', 'gpu', 'cpu',
        'vllm', 'sglang', 'deepspeed', 'tensorrt-llm'
    ]
    agent_terms = ['agent', 'agentic', 'multi-agent']
    agent_efficiency_terms = [
        'cost', 'efficient', 'efficiency', 'routing', 'router', 'inference', 'serving',
        'scheduling', 'latency', 'throughput', 'token allocation', 'workflow', 'gpu cluster',
        'resource', 'planning', 'orchestration', 'model selection', 'kv cache', 'prefix cache'
    ]
    has_core = any(term in hay for term in core_terms)
    has_agent = any(term in hay for term in agent_terms)
    has_agent_efficiency = any(term in hay for term in agent_efficiency_terms)

    if item.get('source_type') == 'blog':
        if item.get('source') in {'vLLM Blog', 'LMSYS Blog', 'NVIDIA TensorRT-LLM Blog', 'DeepSpeed', 'SemiAnalysis'}:
            return item.get('relevance_score', 0) >= 5
        return bool(item.get('matched_topics')) or item.get('relevance_score', 0) >= 5

    if has_agent and not has_agent_efficiency:
        return False
    if 'heterogeneous' in hay and not any(term in hay for term in ['llm', 'language model', 'moe', 'inference', 'serving', 'gpu', 'cpu']):
        return False
    if not has_core and item.get('relevance_score', 0) < 18:
        return False
    return item.get('relevance_score', 0) >= 18


def prepare_items(config, days_back):
    paper_candidates = collect_arxiv(config, days_back)
    feed_candidates = collect_feeds(config, days_back)
    prepared_map = {}
    for item in paper_candidates + feed_candidates:
        item = infer_topics_and_score(item)
        if item['relevance_score'] <= 0:
            continue
        if not passes_quality_gate(item):
            continue
        item['score_with_authority'] = round(item['relevance_score'] * float(item.get('authority', 1.0)), 2)
        item['cn_summary'] = chinese_one_liner(item)
        existing = prepared_map.get(item['id'])
        if existing is None or item['score_with_authority'] > existing['score_with_authority']:
            prepared_map[item['id']] = item
    prepared = list(prepared_map.values())
    prepared.sort(key=lambda x: (x['score_with_authority'], x['published_dt'] or dt.datetime.min.replace(tzinfo=dt.timezone.utc)), reverse=True)
    return prepared


def render_item_block(item, idx=None):
    lines = []
    prefix = f'## {idx}. ' if idx is not None else '## '
    lines.append(f"{prefix}{item['title']}")
    lines.append('')
    if item.get('paper_id'):
        lines.append(f"- arXiv ID: `{item['paper_id']}`")
    lines.append(f"- 来源: {item['source']}")
    lines.append(f"- 类型: {item['source_type']}")
    lines.append(f"- 发布时间: {(item['published_dt'].date().isoformat() if item.get('published_dt') else item.get('published', '未知'))}")
    lines.append(f"- 相关度得分: {item.get('score_with_authority', item.get('relevance_score', 0))}")
    lines.append(f"- 匹配主题: {', '.join(item.get('matched_topics', []))}")
    if item.get('authors'):
        lines.append(f"- 作者: {', '.join(item['authors'][:8])}")
    if item.get('categories'):
        lines.append(f"- 分类: {', '.join(item['categories'][:8])}")
    lines.append(f"- 中文一句话: {item['cn_summary']}")
    lines.append(f"- 摘要: {short_summary(item['summary'], 420)}")
    if item.get('pdf_url'):
        lines.append(f"- 链接: [abs]({item['url']}) | [pdf]({item['pdf_url']})")
    else:
        lines.append(f"- 链接: {item['url']}")
    lines.append('')
    return lines


def render_daily_report(date_str, papers, feeds):
    lines = [f'# 每日研究雷达 {date_str}', '']
    lines.append(f'- 新论文数: {len(papers)}')
    lines.append(f'- 新权威来源更新数: {len(feeds)}')
    lines.append('')
    lines.append('## 今日重点论文')
    lines.append('')
    if not papers:
        lines.append('今日没有新匹配论文。')
        lines.append('')
    else:
        for idx, item in enumerate(papers, 1):
            lines.extend(render_item_block(item, idx))
    lines.append('## 今日权威来源更新')
    lines.append('')
    if not feeds:
        lines.append('今日没有新匹配的权威来源更新。')
        lines.append('')
    else:
        for idx, item in enumerate(feeds, 1):
            lines.extend(render_item_block(item, idx))
    return '\n'.join(lines)


def render_weekly_report(end_date_str, papers, feeds):
    lines = [f'# 每周精选 {end_date_str}', '']
    lines.append(f'- 周内精选论文: {len(papers)}')
    lines.append(f'- 周内精选权威来源更新: {len(feeds)}')
    lines.append('')
    lines.append('## 本周论文精选')
    lines.append('')
    if not papers:
        lines.append('本周没有匹配论文。')
        lines.append('')
    else:
        for idx, item in enumerate(papers, 1):
            lines.extend(render_item_block(item, idx))
    lines.append('## 本周权威来源精选')
    lines.append('')
    if not feeds:
        lines.append('本周没有匹配的权威来源更新。')
        lines.append('')
    else:
        for idx, item in enumerate(feeds, 1):
            lines.extend(render_item_block(item, idx))
    return '\n'.join(lines)


def render_readme(today, daily_papers, daily_feeds, weekly_papers, weekly_feeds):
    lines = ['# LLM Inference Cost Radar', '']
    lines.extend([
        'A daily-updated research radar for:',
        '- LLMRouter and LLM routing',
        '- model routing inside coding agents',
        '- CPU/GPU heterogeneous inference for MoE models',
        '- cost-saving LLM inference, serving, scheduling, and optimization',
        '- agent systems / multi-agent efficiency and routing-related work',
        '',
        'Now includes:',
        '- 每日论文雷达',
        '- 每周精选',
        '- 权威工程来源更新（NVIDIA / PyTorch / GitHub Blog / LMSYS / vLLM / SemiAnalysis / DeepSpeed）',
        '- 基于 LLM 的中文一句话摘要',
        '',
        '## 最新更新',
        '',
        f'- 日期: {today}',
        f'- 今日新论文: {len(daily_papers)}',
        f'- 今日新权威来源更新: {len(daily_feeds)}',
        f'- 本周精选论文: {len(weekly_papers)}',
        f'- 本周精选权威来源更新: {len(weekly_feeds)}',
        f'- 日报: `papers/{today}.md`',
        f'- 周报: `digests/weekly-{today}.md`',
        '',
        '## 今日最值得看',
        ''
    ])
    top = (daily_papers + daily_feeds)[:10]
    if not top:
        lines.append('暂无新内容。')
    else:
        for item in top:
            lines.append(f"- [{item['title']}]({item['url']})")
            lines.append(f"  - 主题: {', '.join(item.get('matched_topics', []))}")
            lines.append(f"  - 中文一句话: {item['cn_summary']}")
    lines.extend([
        '',
        '## 配置',
        '',
        '- 搜索规则: `config/topics.json`',
        '- 论文去重状态: `data/seen_papers.json`',
        '- 来源去重状态: `data/seen_feed_items.json`',
        '- 抓取脚本: `scripts/fetch_arxiv_radar.py`',
        ''
    ])
    return '\n'.join(lines)


def main():
    config = load_json(CONFIG_PATH, {})
    PAPERS_DIR.mkdir(parents=True, exist_ok=True)
    DIGESTS_DIR.mkdir(parents=True, exist_ok=True)

    seen_papers = set(load_json(SEEN_PAPERS_PATH, []))
    seen_feeds = set(load_json(SEEN_FEEDS_PATH, []))

    today = dt.datetime.now(dt.timezone.utc).date().isoformat()

    daily_items = prepare_items(config, int(config.get('days_back', 3)))
    daily_papers_all, daily_feeds_all = split_items(daily_items)
    daily_papers = filter_new_items(daily_papers_all, seen_papers)[: int(config.get('top_n_daily', 15))]
    daily_feeds = filter_new_items(daily_feeds_all, seen_feeds)[: int(config.get('top_n_daily', 15))]

    weekly_items = prepare_items(config, int(config.get('weekly_days_back', 7)))
    weekly_papers_all, weekly_feeds_all = split_items(weekly_items)
    weekly_papers = weekly_papers_all[: int(config.get('top_n_weekly', 25))]
    weekly_feeds = weekly_feeds_all[: int(config.get('top_n_weekly', 25))]

    (PAPERS_DIR / f'{today}.md').write_text(render_daily_report(today, daily_papers, daily_feeds) + '\n', encoding='utf-8')
    (DIGESTS_DIR / f'weekly-{today}.md').write_text(render_weekly_report(today, weekly_papers, weekly_feeds) + '\n', encoding='utf-8')
    README_PATH.write_text(render_readme(today, daily_papers, daily_feeds, weekly_papers, weekly_feeds) + '\n', encoding='utf-8')

    save_json(SEEN_PAPERS_PATH, sorted(seen_papers | {item['id'] for item in daily_papers}))
    save_json(SEEN_FEEDS_PATH, sorted(seen_feeds | {item['id'] for item in daily_feeds}))

    print(f'Daily papers: {len(daily_papers)}')
    print(f'Daily feed updates: {len(daily_feeds)}')
    print(f'Weekly papers: {len(weekly_papers)}')
    print(f'Weekly feed updates: {len(weekly_feeds)}')


if __name__ == '__main__':
    main()
