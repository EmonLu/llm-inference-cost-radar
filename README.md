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

- 日期: 2026-10-19
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 9
- 日报: `papers/2026-10-19.md`
- 周报: `digests/weekly-2026-10-19.md`

## 今日最值得看

- [Efficient CPU-GPU collaborative MoE inference via Adaptive Expert Assignment](https://arxiv.org/abs/2610.23006v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Efficient CPU-GPU collaborative MoE inference via Adaptive Expert Assignment》在 arXiv API 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Extensive experiments on three representative MoE LLMs show that \method improves prefill speed by up to 51.9\% and decode throughput by up to 39.5\% over the strongest baseline across the evaluated batch sizes, with consistent gains under different GPU-memory budgets.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [DLite: History-free Speculative Decoding for Agentic AI](https://arxiv.org/abs/2610.23787v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《DLite: History-free Speculative Decoding for Agentic AI》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experiments on general-purpose, long-context and agentic workloads show that DLite achieves 2-6 acceptance length and outperforms the state-of-the-art speculative decoding method, DSpark, up to 70%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：70%、80%。
- [Is Your NPU Ready for LLMs? Dissecting the Hidden Efficiency Bottlenecks in Mobile LLM Inference](https://arxiv.org/abs/2607.05475)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Is Your NPU Ready for LLMs? Dissecting the Hidden Efficiency Bottlenecks in Mobile LLM Inference》在 arXiv cs.AI 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，We further conduct hardware microbenchmarks to characterize the memory-system performance and compute capabilities of mobile CPUs, GPUs, and NPUs.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [OxyGen: Unified KV Cache Management for VLA Inference under Multi-Task Parallelism](https://arxiv.org/abs/2603.14371)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《OxyGen: Unified KV Cache Management for VLA Inference under Multi-Task Parallelism》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，OxyGen achieves up to 3.7$\times$ speedup over isolated execution, delivering over 200 tokens/s language throughput and 70 Hz action frequency simultaneously on RTX 4090.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：200 tokens/s。
- [Agentic AI for Heterogeneous System Design Across Chip, Scale-Up, and Scale-Out Domains](https://arxiv.org/abs/2610.23724)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Agentic AI for Heterogeneous System Design Across Chip, Scale-Up, and Scale-Out Domains》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On a mixed AI+HPC workload under a 1 MW power budget, ArchAgent discovers heterogeneous designs that achieve a 1.93x weighted geometric mean speedup over a homogeneous GPU baseline, while requiring only 18 evaluations compared with 100 evaluations for hill climbing, which achieves 1.65x speedup.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.93x、1.65x。
- [Who Pays for Efficient Inference? Confidence-Based Small-to-Large LLM Routing Across Tasks and Languages](https://arxiv.org/abs/2610.23249v1)
  - 主题: Cost-efficient LLM inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、LLM routing，核心内容是《Who Pays for Efficient Inference? Confidence-Based Small-to-Large LLM Routing Across Tasks and Languages》在 arXiv API 这一方向上的推进。聚焦大模型路由/小模型分流，直接相关。从实验上看，At 50% escalation, it improves over random routing by 1.40--4.67 percentage points on Belebele and 2.54--5.63 points on SIB-200.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：50%。
- [Enforcing Code Reasoning in Agentic Scaffold for More Effective Issue Resolution](https://arxiv.org/abs/2610.23782v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing，核心内容是《Enforcing Code Reasoning in Agentic Scaffold for More Effective Issue Resolution》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On 731 SWE-bench-Pro instances, DeskCheck improves resolution rates over mini-SWE-Agent and Claude Code by 6.29% to 10.53%, at an additional cost of $0.02-$0.28 per instance (average: $0.14).
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：731 S、6.29%、10.53%。
- [RoutePack: Replay-Guided Expert Placement and Rollout Trajectory Scheduling for MoE Reinforcement Learning](https://arxiv.org/abs/2608.12146)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《RoutePack: Replay-Guided Expert Placement and Rollout Trajectory Scheduling for MoE Reinforcement Learning》在 arXiv cs.DC 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，Within the Megatron training region, RoutePack achieves 4.44-11.85% higher throughput than a DP-local first-fit-decreasing baseline and 1.33-5.28% higher throughput than expert rerouting alone.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：11.85%、5.28%。
- [ScoutRoute: Efficient Mixture-of-Experts Routing Using Internal Language Model Signals](https://arxiv.org/abs/2610.23443v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《ScoutRoute: Efficient Mixture-of-Experts Routing Using Internal Language Model Signals》在 arXiv API 这一方向上的推进。强调异构硬件协同推理。从实验上看，Experimental results show that ScoutRoute consistently outperforms individual routing signals while requiring only a single scout-model inference.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Chance-Constrained Personalized LLM Routing with Online Preference Learning](https://arxiv.org/abs/2610.22695)
  - 主题: Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference、LLM routing，核心内容是《Chance-Constrained Personalized LLM Routing with Online Preference Learning》在 arXiv cs.LG 这一方向上的推进。强调异构硬件协同推理。从实验上看，We formulate this problem as a constrained contextual bandit and develop an algorithm that learns preferences while balancing cost and quality.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

