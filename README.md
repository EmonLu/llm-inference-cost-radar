# LLM Inference Cost Radar

一个面向以下方向的每日更新研究雷达：
- LLMRouter 与 LLM 路由
- coding agent 内部的模型路由与调度
- 面向 MoE 的 CPU/GPU 异构推理
- 降低大模型推理成本的 serving / scheduling / optimization 工作
- agent 系统与多智能体效率相关工作

当前能力包括：
- 每日论文雷达
- 每周精选
- 权威工程来源更新（NVIDIA / PyTorch / GitHub Blog / LMSYS / vLLM / SemiAnalysis / DeepSpeed）
- 中文多句解读、中文摘要与中文实验结论提炼

## 最新更新

- 日期: 2026-06-28
- 今日新论文: 4
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 2
- 日报: `papers/2026-06-28.md`
- 周报: `digests/weekly-2026-06-28.md`

## 今日最值得看

- [Confidence-Aware Tool Orchestration for Robust Video Understanding](https://arxiv.org/abs/2606.26904v1)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《Confidence-Aware Tool Orchestration for Robust Video Understanding》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On two video reasoning benchmarks spanning eight tasks, Robust-TO achieves 56.4% average accuracy on clean inputs, surpassing the strongest open-source baseline by 10.6%p and outperforming Gemini-2.5-Pro (46.2%).
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：56.4%、10.6%、46.2%。
- [EGG: An Expert-Guided Agent Framework for Kernel Generation](https://arxiv.org/abs/2606.26758v1)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《EGG: An Expert-Guided Agent Framework for Kernel Generation》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experiments on KernelBench and real-world workloads show that EGG achieves a 2.13x average speedup over PyTorch, outperforming existing agent-based and RL-based approaches.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：2.13x。
- [How Much Static Structure Do Code Agents Need? A Study of Deterministic Anchoring](https://arxiv.org/abs/2606.26979v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing，核心内容是《How Much Static Structure Do Code Agents Need? A Study of Deterministic Anchoring》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Three observations support this finding: (1) Anchoring works: lightweight call/inheritance topology improves function-level localization (+2.2pp Func@5) and shortens trajectories (-1.6 interaction rounds); (2) Anchoring is scale-sensitive: the optimal granularity and directionality depend on repository characteristics, where denser semantics show diminishing returns and hub-heavy projects benefit from inverse-only links that expose "who-calls-me" without forward edges; (3) Anchoring stabilizes: tags raise link-following rate from 0.15-0.18 to 0.21-0.24, roughly halve run-to-run variance, and improve single-run reliability (Pass@1 +3.4 pp) on medium-scale repositories, at the cost of roughly 10% more input tokens.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：10%。
- [Cascaded Multi-Granularity Pruning for On-Device LLM Inference in Industrial IoT](https://arxiv.org/abs/2606.26861v1)
  - 主题: Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference，核心内容是《Cascaded Multi-Granularity Pruning for On-Device LLM Inference in Industrial IoT》在 arXiv API 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，Deployed on an industrial slewing bearing fault diagnosis platform with NVIDIA DGX Spark, compressed models reduce inference latency by up to 67.2% and peak memory by 62.5%, demonstrating viability for IIoT edge inference.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：67.2%、62.5%、83.82%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

