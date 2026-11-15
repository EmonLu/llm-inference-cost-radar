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

- 日期: 2026-11-15
- 今日新论文: 5
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 7
- 日报: `papers/2026-11-15.md`
- 周报: `digests/weekly-2026-11-15.md`

## 今日最值得看

- [CoReMem: Cost-Internalizing Memory for Successive Coding Tasks with Prospective Valuation](https://arxiv.org/abs/2611.17316v1)
  - 主题: Coding agent routing
  - 中文解读: 这项工作主要关注Coding agent routing，核心内容是《CoReMem: Cost-Internalizing Memory for Successive Coding Tasks with Prospective Valuation》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On ChainSWE, CoReMem raises the 27B actor's resolve rate from 21.0% to 25.7%, with 17% fewer steps and 11% fewer total cache-aware tokens, including memory-module calls, relative to the untrained actor model without memory.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：21.0%、25.7%、17%。
- [ACE-CaP-0: Real-World Code-as-Policies in the Era of Experience](https://arxiv.org/abs/2611.16872v1)
  - 主题: Coding agent routing
  - 中文解读: 这项工作主要关注Coding agent routing，核心内容是《ACE-CaP-0: Real-World Code-as-Policies in the Era of Experience》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Developing reliable code policies while limiting the cost of physical experimentation remains a central challenge.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Infrastructure for Verifiable AI: Where Proof Costs Go and How Hardware Can Help](https://arxiv.org/abs/2611.17042v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Infrastructure for Verifiable AI: Where Proof Costs Go and How Hardware Can Help》在 arXiv API 这一方向上的推进。强调异构硬件协同推理。从实验上看，Hardware acceleration research often reports gains for individual cryptographic operations, leaving their effect on the full cost of proving neural-network workloads, particularly large transformer models, unclear.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [AnalogLayoutWorld: An Open Benchmark for Agentic Analog Layout Design](https://arxiv.org/abs/2611.16991v1)
  - 主题: Coding agent routing
  - 中文解读: 这项工作主要关注Coding agent routing，核心内容是《AnalogLayoutWorld: An Open Benchmark for Agentic Analog Layout Design》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across 13 model--harness configurations, 91.1\% of attempts produce GDS layouts, but only 23.0\% satisfy the benchmark's acceptance criteria.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Ballad: Bandit-Based LLM Routing for Automated Heuristic Discovery](https://arxiv.org/abs/2611.17241v1)
  - 主题: LLM routing
  - 中文解读: 这项工作主要关注LLM routing，核心内容是《Ballad: Bandit-Based LLM Routing for Automated Heuristic Discovery》在 arXiv API 这一方向上的推进。聚焦大模型路由/小模型分流，直接相关。从实验上看，Across five NP-hard combinatorial optimization problems and a pool of four models of varying capability and cost, Ballad not only matches the best individual LLM in hindsight but, in several cases, surpasses every individual model while reducing API cost by up to 65.6% relative to always using the strongest model.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：65.6%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

