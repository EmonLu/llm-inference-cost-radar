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

- 日期: 2026-08-06
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 2
- 日报: `papers/2026-08-06.md`
- 周报: `digests/weekly-2026-08-06.md`

## 今日最值得看

- [Architectural Implications of Agentic AI Workflows](https://arxiv.org/abs/2608.04458v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Architectural Implications of Agentic AI Workflows》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Agora dynamically harvests idle CPU cores for co-located throughput work, while protecting agentic tail latency against tool spikes.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [AcceptMoE: Commitment-Weighted Self-Sizing Verifier Expert Sets for Efficient MoE Speculative Decoding](https://arxiv.org/abs/2608.02989)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《AcceptMoE: Commitment-Weighted Self-Sizing Verifier Expert Sets for Efficient MoE Speculative Decoding》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Although constraining target-expert eligibility changes the model distribution, across 12 model-task pairs spanning three MoE targets and four benchmarks, AcceptMoE's mean accuracy is 0.27 percentage points lower than that of EAGLE-3 speculative decoding with natural routing.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：3 s。
- [AuroraRL: Fast, Fault-Tolerant, and Cost-Efficient Reinforcement Learning over Decentralized Network](https://arxiv.org/abs/2602.11456)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《AuroraRL: Fast, Fault-Tolerant, and Cost-Efficient Reinforcement Learning over Decentralized Network》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Across Qwen3 4B--14B models deployed in up to four geographic regions, AuroraRL shrinks per-step weight transfer by 79$\times$ on Qwen3-8B, delivers 1.3--9.5$\times$ higher throughput than dense-broadcast baselines (PrimeRL-Full, async-tolerant, multi-stream variants), and brings end-to-end training within 8.91\% of an ideal RDMA single-datacenter baseline, while transparently tolerating common failures and preserving training accuracy.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [MUSE: A Heterogeneity-Aware Multimedia Search Engine for Mobile SoCs](https://arxiv.org/abs/2511.19192)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《MUSE: A Heterogeneity-Aware Multimedia Search Engine for Mobile SoCs》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Evaluated on Snapdragon 8-series SoCs using real-world multimodal datasets, MUSE improves query throughput by up to 1.4x at matched recall, achieves up to 7x faster index construction, and delivers up to 6x higher insertion throughput under concurrent streaming.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.4x、7x、6x。
- [Scrouting: Cost-Aware Routing of Coding Agents by Scouting the Repository First](https://arxiv.org/abs/2608.04804v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Heterogeneous MoE inference，核心内容是《Scrouting: Cost-Aware Routing of Coding Agents by Scouting the Repository First》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，A no-router ablation, always the cheapest fixer with the handoff, ties the routed system on this benchmark, so the handoff rather than the routing decision carries the result.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [EvolveNet: Collaborative Harness Evolution for Agent Self-Improvement](https://arxiv.org/abs/2608.04968v1)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《EvolveNet: Collaborative Harness Evolution for Agent Self-Improvement》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across five settings spanning text-to-SQL, data-science coding, competitive programming, software engineering, and agentic workflows, EvolveNet improves the shared harness in all five, with the largest gains under heterogeneous workloads, and ablations attribute the improvement to composition of adaptations from different agents rather than to selecting among them.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [CURATE: Leveraging LLM Agents to Compose, Catalog, and Deploy Reproducible Workflows](https://arxiv.org/abs/2608.04270v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing，核心内容是《CURATE: Leveraging LLM Agents to Compose, Catalog, and Deploy Reproducible Workflows》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，We demonstrate the feasibility of our system with an initial prototype using Claude Opus 4.8, comprising 6 experiments: reproducing and adapting 4 workflows derived from the SeBS-Flow benchmark suite, and automating the development and scaling of a workflow that leverages a complex mechanistic model in environmental engineering used to simulate anaerobic digestion.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [EASy: Towards Efficient LLM-Based Agentic System](https://arxiv.org/abs/2608.04588v1)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference、LLM routing，核心内容是《EASy: Towards Efficient LLM-Based Agentic System》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Extensive experiments on mathematical reasoning, embodied decision-making, and deep research benchmarks show that EASy consistently achieves stronger performance-efficiency trade-offs than strong agentic baselines.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [FedCritic-MIMO: Communication-Efficient Serverless Federated Critic Learning for Massive-MIMO Resource Control in Open and Disaggregated 6G RANs](https://arxiv.org/abs/2608.03852)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《FedCritic-MIMO: Communication-Efficient Serverless Federated Critic Learning for Massive-MIMO Resource Control in Open and Disaggregated 6G RANs》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，It achieves the highest held-out throughput, improves user-rate distribution and mean SINR, increases QoS satisfaction, and attains the lowest interference cost per delivered bit among learning baselines.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [$S^3$: Improving Agent Safety through Multi-Stage Defense](https://arxiv.org/abs/2608.02683)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《$S^3$: Improving Agent Safety through Multi-Stage Defense》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experimental results show that $S^3$ consistently outperforms representative state-of-the-art baselines in both safety effectiveness and utility preservation.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

