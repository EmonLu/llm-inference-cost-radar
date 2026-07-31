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

- 日期: 2026-07-31
- 今日新论文: 15
- 今日新权威来源更新: 2
- 本周精选论文: 25
- 本周精选权威来源更新: 5
- 日报: `papers/2026-07-31.md`
- 周报: `digests/weekly-2026-07-31.md`

## 今日最值得看

- [SpecPrefetch: Parameter-Efficient Expert Prefetching for Sparse MoE Foundation Models](https://arxiv.org/abs/2607.24787)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《SpecPrefetch: Parameter-Efficient Expert Prefetching for Sparse MoE Foundation Models》在 arXiv cs.LG 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，On a Snapdragon 8 Elite device, SpecPrefetch further improves decoding throughput by up to \(20\%\) over a compute-optimized offloading runtime, demonstrating practical benefits for storage-constrained MoE deployment.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [RedKnot: Efficient Long-Context LLM Serving with Head-Aware KV Reuse and SegPagedAttention](https://arxiv.org/abs/2606.06256)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《RedKnot: Efficient Long-Context LLM Serving with Head-Aware KV Reuse and SegPagedAttention》在 arXiv cs.AI 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，This head-level decomposition turns the KV cache from a monolithic tensor abstraction into a structured memory object, enabling RedKnot to uniformly support position-independent KV reuse, prefix KV compression, hot/cold KV separation, and distributed KV placement while preserving output fidelity and improving resource efficiency, without requiring model retraining or fine-tuning.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Where Is the Cost of Third-Party API Routers in Agentic Software Development?](https://arxiv.org/abs/2607.23624)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、LLM routing，核心内容是《Where Is the Cost of Third-Party API Routers in Agentic Software Development?》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，In coding-agent workflows, high-autonomy operation is widely adopted because it reduces interaction overhead.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Agent Team Work Zone: An Automated, Persistent Workspace for Long-Lived Claude Code Agent Teams](https://arxiv.org/abs/2607.22917)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing，核心内容是《Agent Team Work Zone: An Automated, Persistent Workspace for Long-Lived Claude Code Agent Teams》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Claude Code, in particular, is one of the most powerful LLM coding agents and is capable of conducting complex coding tasks.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [SmartGen: Seamless Disaggregated LLM Inference with Selective KV Cache Transfer](https://arxiv.org/abs/2607.28150)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《SmartGen: Seamless Disaggregated LLM Inference with Selective KV Cache Transfer》在 arXiv cs.DC 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，Experimental results show that SmartGen reduces time-to-second-token by up to 4.3x compared with the typical full KV cache transfer approach while offering comparable subsequent decoding performance and accuracy.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：4.3x。
- [Heterogeneous Ranking in Industrial-Scale Recommender Systems: A Case Study](https://arxiv.org/abs/2607.27577)
  - 主题: Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference，核心内容是《Heterogeneous Ranking in Industrial-Scale Recommender Systems: A Case Study》在 arXiv cs.LG 这一方向上的推进。强调异构硬件协同推理。从实验上看，Furthermore, online A/B testing confirms gains in feed activity and exploration metrics.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [$Σ$-Mem: An Online Reliability Memory for LLM-based Multi-Agent Systems](https://arxiv.org/abs/2607.27958v1)
  - 主题: Agent systems and multi-agent efficiency, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、LLM routing，核心内容是《$Σ$-Mem: An Online Reliability Memory for LLM-based Multi-Agent Systems》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Direct memory readouts also outperform majority voting and the best fixed peer over the full OOD evaluation set.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [AgenticER: the next frontier in Entity Resolution](https://arxiv.org/abs/2607.27435v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《AgenticER: the next frontier in Entity Resolution》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，These agents actively plan ER strategies, acquire external evidence, decide when to query additional sources or humans, and optimize trade-offs between accuracy, cost, and latency.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Linguistic Firewall: Geometry as Defense in Multi-Agent Systems Routing](https://arxiv.org/abs/2606.30555)
  - 主题: Agent systems and multi-agent efficiency, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、LLM routing，核心内容是《Linguistic Firewall: Geometry as Defense in Multi-Agent Systems Routing》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，In our experiments, ANTAP achieves near-zero ASR against description-based injection attacks, compared to 67.3\% and above for the description-based router baseline.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [IDP AutoOpt: Agent-Driven Optimization of Document Processing Pipeline Configurations](https://arxiv.org/abs/2607.26075)
  - 主题: Agent systems and multi-agent efficiency
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency，核心内容是《IDP AutoOpt: Agent-Driven Optimization of Document Processing Pipeline Configurations》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across extraction, classification, and packet-splitting tasks deployed in healthcare, marketing-intelligence, and financial-services settings, IDP AutoOpt matches or exceeds human-expert accuracy at equal or lower cost (on an extraction benchmark, 90.2% vs 81.6% at 4.6 x lower per-page cost), cutting configuration time from weeks to under two hours.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：90.2%、81.6%、4.6 x。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

