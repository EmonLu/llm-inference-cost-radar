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

- 日期: 2026-07-19
- 今日新论文: 4
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 4
- 日报: `papers/2026-07-19.md`
- 周报: `digests/weekly-2026-07-19.md`

## 今日最值得看

- [OmniaBench: Benchmarking General AI Agents Across Diverse Scenarios](https://arxiv.org/abs/2607.14989v1)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《OmniaBench: Benchmarking General AI Agents Across Diverse Scenarios》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The resulting dataset contains 1,431 tasks, together with a challenging subset of 644 tasks designed to reduce evaluation cost and mitigate potential contamination of the full set after public release.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [The Energy Society: A Simulation Environment for Studying Agent Cooperation under Survival Pressure](https://arxiv.org/abs/2607.14865v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《The Energy Society: A Simulation Environment for Studying Agent Cooperation under Survival Pressure》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across experiments, larger models consistently consume the most energy and spend more energy than they gain, even in those settings where token cost is not size-dependent.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [FlowGuard: From Signals to Evidence for MCP Security Detection](https://arxiv.org/abs/2607.14754v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《FlowGuard: From Signals to Evidence for MCP Security Detection》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Compared with existing dynamic scanners, FlowGuard reduces end-to-end latency by up to 2.23x.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：2.23x。
- [SmartRAG: Native Graph-Based RAG for Mobile Device](https://arxiv.org/abs/2607.14661v1)
  - 主题: Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference，核心内容是《SmartRAG: Native Graph-Based RAG for Mobile Device》在 arXiv API 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，Experiments on four QA benchmarks (TriviaQA, Natural Questions, HotpotQA, MultiHopQA) show that SmartRAG with a quantized 1.7B-parameter backbone achieves multi-hop reasoning performance competitive with models up to 18$\times$ larger, while running entirely on commodity smartphones within practical memory and latency envelopes.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

