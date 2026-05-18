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

- 日期: 2026-05-18
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 1
- 日报: `papers/2026-05-18.md`
- 周报: `digests/weekly-2026-05-18.md`

## 今日最值得看

- [MoE-Prefill: Zero Redundancy Overheads in MoE Prefill Serving](https://arxiv.org/abs/2605.02960)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《MoE-Prefill: Zero Redundancy Overheads in MoE Prefill Serving》在 arXiv cs.LG 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，On Qwen3-235B-A22B across four hardware/precision configurations, MoE-Prefill delivers 1.35-1.37x throughput over the strongest distributed baseline on real-world workloads and up to 1.59x on long-context synthetic workloads, sustaining 29.8-36.2% per-GPU model FLOPs utilization.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.37x、1.59x、36.2%。
- [TokenButler: Token Importance is Predictable](https://arxiv.org/abs/2503.07518)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《TokenButler: Token Importance is Predictable》在 arXiv cs.CL 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Furthermore, TokenButler achieves competitive or superior performance on long-context benchmarks (RULER, LongBench), up to $\approx1.6\times$ on-GPU speedup using our proposed *prediction interval with neighbor fetching* that amortizes predictor cost while maintaining accuracy within $\approx$1.1\%, and up to 7.6$\times$ reduction in latency compared to Dense Attention with CPU offloading.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [TopoEvo: A Topology-Aware Self-Evolving Multi-Agent Framework for Root Cause Analysis in Microservices](https://arxiv.org/abs/2605.15611)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《TopoEvo: A Topology-Aware Self-Evolving Multi-Agent Framework for Root Cause Analysis in Microservices》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Finally, a \emph{Self-Evolving Mechanism} refreshes hierarchical incident memory and performs conservative test-time adaptation with high-confidence pseudo-labels to maintain robustness under drift.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [AgentStop: Terminating Local AI Agents Early to Save Energy in Consumer Devices](https://arxiv.org/abs/2605.15206)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《AgentStop: Terminating Local AI Agents Early to Save Energy in Consumer Devices》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Leveraging low-cost execution signals, such as token-level log probabilities, AgentStop can reduce wasted energy by 15-20% with minimal impact on task performance (<5% utility drop) for challenging web-based question answering and coding benchmarks.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：20%、5%。
- [IO-SVD: Input-Output Whitened SVD for Adaptive-Rank LLM Compression](https://arxiv.org/abs/2605.15626)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《IO-SVD: Input-Output Whitened SVD for Adaptive-Rank LLM Compression》在 arXiv cs.LG 这一方向上的推进。强调异构硬件协同推理。从实验上看，Extensive experiments across diverse LLM and VLM families, and inference-time analysis shows that IO-SVD compresses LLMs with minimal performance degradation while delivering practical inference speedups.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Context Pruning for Coding Agents via Multi-Rubric Latent Reasoning](https://arxiv.org/abs/2605.15315)
  - 主题: Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Coding agent routing、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Context Pruning for Coding Agents via Multi-Rubric Latent Reasoning》在 arXiv cs.CL 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，It saves up to 31% more tokens on multi-turn agent tasks and improves Exact Match by up to +3.5 on single-turn tasks, while performance is frequently enhanced by denoising the context, and any remaining drops are marginal.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：31%。
- [KV Cache Offloading for Context-Intensive Tasks](https://arxiv.org/abs/2604.08426)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《KV Cache Offloading for Context-Intensive Tasks》在 arXiv cs.CL 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，Recently, KV-cache offloading has emerged as a promising approach to reduce memory footprint and inference latency while preserving accuracy.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [CascadeInfer: Length-Aware Scheduling of LLM Serving with Low Latency and Load Balancing](https://arxiv.org/abs/2512.19179)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《CascadeInfer: Length-Aware Scheduling of LLM Serving with Low Latency and Load Balancing》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Our evaluation shows that, under the same configuration, CascadeInfer reduces end-to-end latency by up to 67% and tail latency by up to 69%, while improving overall system throughput by up to 2.89 times compared to the state-of-the-art multi-instance scheduling systems.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：67%、69%。
- [STAR: Failure-Aware Markovian Routing for Multi-Agent Spatiotemporal Reasoning](https://arxiv.org/abs/2605.10057)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference、LLM routing，核心内容是《STAR: Failure-Aware Markovian Routing for Multi-Agent Spatiotemporal Reasoning》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across three spatiotemporal benchmarks and eight backbone LLMs, STAR improves over multiple baselines with the clearest gains on queries whose execution deviates from the nominal routing path.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [SimPersona: Learning Discrete Buyer Personas from Raw Clickstreams for Grounded E-Commerce Agents](https://arxiv.org/abs/2605.14205)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《SimPersona: Learning Discrete Buyer Personas from Raw Clickstreams for Grounded E-Commerce Agents》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Evaluated on $8.37$M buyers across $42$ held-out live storefronts, SimPersona achieves $78\%$ conversion-rate alignment with real buyers, exhibits interpretable behavioral variation across buyer types, and outperforms a baseline with $8\times$ more parameters on goal-oriented shopping tasks.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

