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

- 日期: 2026-06-03
- 今日新论文: 15
- 今日新权威来源更新: 2
- 本周精选论文: 25
- 本周精选权威来源更新: 10
- 日报: `papers/2026-06-03.md`
- 周报: `digests/weekly-2026-06-03.md`

## 今日最值得看

- [MAVEN-T: Reinforced Heterogeneous Distillation for Real-Time Multi-Agent Trajectory Prediction](https://arxiv.org/abs/2604.10169)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《MAVEN-T: Reinforced Heterogeneous Distillation for Real-Time Multi-Agent Trajectory Prediction》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experiments on NGSIM, HighD, MoCAD, Argoverse~2, and the Waymo Open Motion Dataset evaluate accuracy, efficiency, generalization, robustness, and closed-loop safety.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [E2LLM: Towards Efficient LLM Serving in Heterogeneous Edge/Fog Environments](https://arxiv.org/abs/2606.03770v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《E2LLM: Towards Efficient LLM Serving in Heterogeneous Edge/Fog Environments》在 arXiv API 这一方向上的推进。强调异构硬件协同推理。从实验上看，Compared to the Splitwise baseline, E2LLM reduces average waiting time by over 50% under high-demand conditions
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：50%。
- [Cross-Lingual Token Arbitrage: Optimizing Code Agent Context Windows via Local LLM Preprocessing](https://arxiv.org/abs/2606.03618v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《Cross-Lingual Token Arbitrage: Optimizing Code Agent Context Windows via Local LLM Preprocessing》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Ablation studies show that gains arise primarily from the rewriting stage rather than simple function-name extraction.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [DriftSched: Adaptive QoS-Aware Scheduling under Runtime Token Drift for Multi-Tenant GPU Inference](https://arxiv.org/abs/2606.02982)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《DriftSched: Adaptive QoS-Aware Scheduling under Runtime Token Drift for Multi-Tenant GPU Inference》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Among all evaluated schedulers, SJF achieves the best overall performance, reducing median end-to-end latency by approximately 42% and P99 latency by approximately 16% relative to FIFO under sustained GPU contention.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：42%、16%、38.8%。
- [PR2: Predictive Routing Replay for MoE-Based LLM Reinforcement Learning](https://arxiv.org/abs/2606.00395)
  - 主题: Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference、LLM routing，核心内容是《PR2: Predictive Routing Replay for MoE-Based LLM Reinforcement Learning》在 arXiv cs.LG 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，Theoretical analysis and experiments support that PR2 reduces routing-induced mismatch, improves RL stability, and yields stronger performance across various reasoning benchmarks.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Spike-Aware C++ INT8 Inference for Sparse Spiking Language Models on Commodity CPUs](https://arxiv.org/abs/2606.03026v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Spike-Aware C++ INT8 Inference for Sparse Spiking Language Models on Commodity CPUs》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Thread scaling reaches 47.90 tokens/s at four CPU threads, and 512-token prefill improves from 29.86 to 94.68 tokens/s from one to eight threads.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：47.90 tokens/s、94.68 tokens/s、22.63 tokens/s。
- [vLLM Semantic Router: Signal Driven Decision Routing for Mixture-of-Modality Models](https://arxiv.org/abs/2603.04444)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《vLLM Semantic Router: Signal Driven Decision Routing for Mixture-of-Modality Models》在 arXiv cs.AI 这一方向上的推进。强调异构硬件协同推理。从实验上看，Different deployment scenarios -- multi-cloud enterprise, privacy-regulated, cost-optimized, latency-sensitive -- are expressed as different signal-decision configurations over the same architecture, without code changes.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [NetKV: Network-Aware Decode Instance Selection for Disaggregated LLM Inference](https://arxiv.org/abs/2606.03910)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《NetKV: Network-Aware Decode Instance Selection for Disaggregated LLM Inference》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，On a 64-GPU four-tier fat-tree simulator driven by Mooncake traces, NetKV reduces mean TTFT by up to 21.2% over round-robin and 17.6% over a tuned cache+load-aware scheduler, lifts SLO attainment by up to 20.1 percentage points, and keeps the Time Between Tokens overhead below 0.5 ms in every condition tested, with no changes to the transport, inference engine, or hardware.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：21.2%、17.6%、0.5 ms。
- [Rethinking the Role of Tensor Decompositions in Post-Training LLM Compression](https://arxiv.org/abs/2606.03465)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Rethinking the Role of Tensor Decompositions in Post-Training LLM Compression》在 arXiv cs.LG 这一方向上的推进。强调异构硬件协同推理。从实验上看，arXiv:2606.03465v1 Announce Type: new Abstract: Post-training compression is essential for deploying large language models (LLMs) under tight resource constraints.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [DOT-MoE: Differentiable Optimal Transport for MoEfication](https://arxiv.org/abs/2606.01666v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《DOT-MoE: Differentiable Optimal Transport for MoEfication》在 arXiv API 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，Extensive experiments across multiple architectures and benchmarks demonstrate that DOT-MoE significantly outperforms structured pruning, heuristic clustering, and random-split baselines, retaining 90% of the original dense model's performance while reducing active parameters by 50%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：90%、50%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

