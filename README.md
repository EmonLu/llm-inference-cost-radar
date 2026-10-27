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

- 日期: 2026-10-27
- 今日新论文: 15
- 今日新权威来源更新: 1
- 本周精选论文: 25
- 本周精选权威来源更新: 8
- 日报: `papers/2026-10-27.md`
- 周报: `digests/weekly-2026-10-27.md`

## 今日最值得看

- [OasisKV: Scaling In-Decode KV Cache Beyond HBM with Lookahead Sparse Prefetching](https://arxiv.org/abs/2608.08097)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《OasisKV: Scaling In-Decode KV Cache Beyond HBM with Lookahead Sparse Prefetching》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Synthetic long-context workloads further show up to 2.2x higher throughput in multi-GPU serving.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：2.2x、2.29x、2.42x。
- [LLMs in Cloud: A Discussion on Architecture, Orchestration, and Inference](https://arxiv.org/abs/2610.33475)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《LLMs in Cloud: A Discussion on Architecture, Orchestration, and Inference》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Finally, we formalize the multi-dimensional Pareto trade-offs governing throughput, latency, monetary cost, and confidentiality, outlining a forward-looking research roadmap spanning Compute Express Link (CXL) memory pooling, in-memory computing, and autonomous multi-agent control planes to guide future cloud LLM infrastructure.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [DualPace: Decoupled Scheduling and Cooperative GPU--CPU Decoding for LLM Serving](https://arxiv.org/abs/2610.33501)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《DualPace: Decoupled Scheduling and Cooperative GPU--CPU Decoding for LLM Serving》在 arXiv cs.DC 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Our evaluations show that, in decode-oriented scenarios, DualPace improves serving throughput by 6.9--43.2\% over NEO, a state-of-the-art open-source CPU-offloading system, and by 11.5--90.6\% over vLLM, a widely used GPU serving system, while maintaining the same level of latency.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [COPE: Composable Performance Emulation for Mixture-of-Experts Offloading Policies](https://arxiv.org/abs/2610.33404)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《COPE: Composable Performance Emulation for Mixture-of-Experts Offloading Policies》在 arXiv cs.DC 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Compared with the evaluated baselines, COPE improves fastest-policy selection accuracy by 24%-100% and reduces performance-prediction error by $1.7\times$ to $6.8\times$.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：24%、100%、74%。
- [Prefetch-Steered Routing: Deterministic Cache-Aware Expert Selection for Offloaded Mixture-of-Experts Decoding](https://arxiv.org/abs/2610.34721)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Prefetch-Steered Routing: Deterministic Cache-Aware Expert Selection for Offloaded Mixture-of-Experts Decoding》在 arXiv cs.AI 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，On Moonlight-16B-A3B, PSR is 1.9x faster than exact routing with LRU at 37.5% residency and, at the latency of Cache-Prior, significantly better on three of eight benchmarks.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.9x、37.5%、50%。
- [Multi-Agentic AI for Fairness-Aware and Accelerated Multi-modal Large Model Inference in Real-world Mobile Edge Networks](https://arxiv.org/abs/2602.07215)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Multi-Agentic AI for Fairness-Aware and Accelerated Multi-modal Large Model Inference in Real-world Mobile Edge Networks》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experiments demonstrate that our solution reduces average end-to-end latency by 42.9% compared with a state-of-the-art online-learning baseline and by 80.6% compared with the full-activation baseline, while maintaining a mean service-type Jain's index of 0.925.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：42.9%、80.6%。
- [HobbyLM: A Sparse Mixture-of-Experts Model Family on a Hobby Budget](https://arxiv.org/abs/2610.34582v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《HobbyLM: A Sparse Mixture-of-Experts Model Family on a Hobby Budget》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Finally, we describe HobbyLM-Image, a 333M-parameter flow-matching diffusion transformer that generates 1024x1024 images in a 32x-compressed latent space, together with a dependency-light CPU implementation of the full text-to-image pipeline.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1024x、32x。
- [EvoRouter: Cost-Efficient Multi-Agent Routing via Insight-Guided On-Policy Distillation](https://arxiv.org/abs/2610.35690v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、LLM routing，核心内容是《EvoRouter: Cost-Efficient Multi-Agent Routing via Insight-Guided On-Policy Distillation》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，EvoRouter achieves an average in-domain accuracy of 68.69%, outperforming the strongest routing baseline by 7.23 percentage points while reducing inference compute cost by 50.95%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：68.69%、50.95%。
- [The Physical Cost of Context: Quality-Constrained Resource Accounting for Coding Agents](https://arxiv.org/abs/2610.34763v1)
  - 主题: Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Coding agent routing、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《The Physical Cost of Context: Quality-Constrained Resource Accounting for Coding Agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，In a separate 900-cell study, Eager cuts model calls by 35.7% and the GPU-energy proxy by 33.2% against on-demand search (Grep); Compact saves nothing further.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：35.7%、33.2%、8.3%。
- [TwinRouterBench: Fast Static and Live Dynamic Evaluation for Realistic Agentic LLM Routing](https://arxiv.org/abs/2605.18859)
  - 主题: Coding agent routing, LLM routing
  - 中文解读: 这项工作主要关注Coding agent routing、LLM routing，核心内容是《TwinRouterBench: Fast Static and Live Dynamic Evaluation for Realistic Agentic LLM Routing》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Routing each call to the cheapest sufficient model can cut costs without sacrificing quality, yet existing router benchmarks evaluate routers only on one-shot prompts.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

