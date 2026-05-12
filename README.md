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

- 日期: 2026-05-12
- 今日新论文: 15
- 今日新权威来源更新: 2
- 本周精选论文: 25
- 本周精选权威来源更新: 4
- 日报: `papers/2026-05-12.md`
- 周报: `digests/weekly-2026-05-12.md`

## 今日最值得看

- [HMACE: Heterogeneous Multi-Agent Collaborative Evolution for Combinatorial Optimization](https://arxiv.org/abs/2605.07214)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《HMACE: Heterogeneous Multi-Agent Collaborative Evolution for Combinatorial Optimization》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，By coupling behavior-aware retrieval, lightweight candidate filtering, and fitness-grounded archive updates, HMACE guides the search toward diverse and promising heuristic behaviors while avoiding redundant evaluations.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Multi-Objective Multi-Agent Bandits: From Learning Efficiency to Fairness Optimization](https://arxiv.org/abs/2605.06864)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《Multi-Objective Multi-Agent Bandits: From Learning Efficiency to Fairness Optimization》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，This separation reveals the cost of imposing the fairness constraint to our efficiency objective: fairness limits information aggregation and slows convergence.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [QHyer: Q-conditioned Hybrid Attention-mamba Transformer for Offline Goal-conditioned RL](https://arxiv.org/abs/2605.01862)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《QHyer: Q-conditioned Hybrid Attention-mamba Transformer for Offline Goal-conditioned RL》在 arXiv cs.LG 这一方向上的推进。强调异构硬件协同推理。从实验上看，Extensive experiments demonstrate that \textbf{QHyer} achieves state-of-the-art performance on both non-Markovian and Markovian datasets, validating its effectiveness for diverse scenarios.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Sparse Attention as a Range Searching Problem: Towards an Inference-Efficient Index for KV Cache](https://arxiv.org/abs/2605.06763)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Sparse Attention as a Range Searching Problem: Towards an Inference-Efficient Index for KV Cache》在 arXiv cs.LG 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Our experiments demonstrate that Louver outperforms prior sparse attention methods in both accuracy and runtime, and is faster than highly optimized dense attentions such as FlashAttention.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [HexiSeq: Accommodating Long Context Training of LLMs over Heterogeneous Hardware](https://arxiv.org/abs/2605.07569)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《HexiSeq: Accommodating Long Context Training of LLMs over Heterogeneous Hardware》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，On FLOP-comparable pairs against homogeneous clusters, HexiSeq reaches throughput close to the strongest homogeneous baseline, showing that heterogeneous clusters can be used efficiently for long-context LLM training.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Direction for Detection: A Survey of Automated Vulnerability Detection and all of its Pain Points](https://arxiv.org/abs/2412.11194)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing，核心内容是《Direction for Detection: A Survey of Automated Vulnerability Detection and all of its Pain Points》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，We first systematize the field through a survey of 87 influential works based on their problem formulation, input and detection granularity, target programming languages, evaluation metrics, datasets, and detection approach.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [MACS: Modality-Aware Capacity Scaling for Efficient Multimodal MoE Inference](https://arxiv.org/abs/2605.05225)
  - 主题: Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference，核心内容是《MACS: Modality-Aware Capacity Scaling for Efficient Multimodal MoE Inference》在 arXiv cs.LG 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，Extensive experiments demonstrate that MACS significantly outperforms existing methods on various multimodal benchmarks, providing a novel and robust solution for the efficient deployment of MoE MLLMs in EP inference.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [GASim: A Graph-Accelerated Hybrid Framework for Social Simulation](https://arxiv.org/abs/2605.07692)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《GASim: A Graph-Accelerated Hybrid Framework for Social Simulation》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Extensive experiments show that GASim not only delivers a substantial 9.94-fold end-to-end speedup over the traditional hybrid framework but also consumes less than 20% of baseline tokens, significantly reducing costs while preserving strong alignment with real-world public opinion trends.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：20%。
- [Agentic AI and the Industrialization of Cyber Offense: Forecast, Consequences, and Defensive Priorities for Enterprises and the Mittelstand](https://arxiv.org/abs/2605.06713)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《Agentic AI and the Industrialization of Cyber Offense: Forecast, Consequences, and Defensive Priorities for Enterprises and the Mittelstand》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The central near-term risk is not that every low-skill criminal immediately becomes a frontier exploit researcher; it is that agentic AI compresses the attack lifecycle by lowering the cost of reconnaissance, phishing, credential abuse, vulnerability triage, exploit adaptation, and post-compromise decision support.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [RRCM: Ranking-Driven Retrieval over Collaborative and Meta Memories for LLM Recommendation](https://arxiv.org/abs/2605.07129)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《RRCM: Ranking-Driven Retrieval over Collaborative and Meta Memories for LLM Recommendation》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Extensive experiments show that RRCM significantly outperforms traditional baselines and diverse LLM-based recommendation approaches.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

