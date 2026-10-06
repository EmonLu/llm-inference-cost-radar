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

- 日期: 2026-10-06
- 今日新论文: 15
- 今日新权威来源更新: 1
- 本周精选论文: 25
- 本周精选权威来源更新: 2
- 日报: `papers/2026-10-06.md`
- 周报: `digests/weekly-2026-10-06.md`

## 今日最值得看

- [HiNa-MoE: High-Performance, Non-Intrusive MoE Inference on CPUs with Matrix Engines](https://arxiv.org/abs/2610.05123v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《HiNa-MoE: High-Performance, Non-Intrusive MoE Inference on CPUs with Matrix Engines》在 arXiv API 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Across multiple MoE models, HiNa-MoE achieves up to 3.37x speedup for FFN kernels and up to 2.09x end-to-end inference speedup over state-of-the-art baselines, while remaining plug-and-play with existing frameworks and deployment workflows.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：3.37x、2.09x。
- [PhaseGate: Phase-Aware CPU Retrieval Scheduling for On-Device LLMs on Unified Memory](https://arxiv.org/abs/2610.04537v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《PhaseGate: Phase-Aware CPU Retrieval Scheduling for On-Device LLMs on Unified Memory》在 arXiv API 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Under a saturated local-retrieval workload, four concurrent retrieval workers raise 95th-percentile (p95) decode latency by 60-61% on two M4 systems, whereas prefill latency rises by only 5.7-6.9%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：61%、4 s、6.9%。
- [MemPilot: Orchestrating On-Demand Multimodal Memory Curation for LLM Agents](https://arxiv.org/abs/2610.06830v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《MemPilot: Orchestrating On-Demand Multimodal Memory Curation for LLM Agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experiments on five multimodal agent-memory benchmarks demonstrate favorable performance--cost--latency trade-offs across optimization preferences, with preference sweeps yielding broader frontiers than existing trade-off-aware baselines.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Recursive Improvement of a Differentiable Scientific Software Ecosystem](https://arxiv.org/abs/2610.04561v1)
  - 主题: Coding agent routing, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Coding agent routing、Heterogeneous MoE inference，核心内容是《Recursive Improvement of a Differentiable Scientific Software Ecosystem》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Benchmarks demonstrate computational savings over finite differences in gradient evaluation and complete parameter estimation.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [MOLT: A Fine-Grained GPU Memory Sharing System for LLM Serving with Opportunistic Fine-Tuning](https://arxiv.org/abs/2610.05748v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《MOLT: A Fine-Grained GPU Memory Sharing System for LLM Serving with Opportunistic Fine-Tuning》在 arXiv API 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，On four model deployments (24B--70B) across H100 SXM and B200 GPUs under trace-driven workloads, MOLT keeps inference SLO attainment at or above 99.7% and completes 1.9--3.3x the tuning work of discard-based memory sharing.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：100 S、99.7%、3.3x。
- [What Does a Harness Buy? Tokens, Mostly](https://arxiv.org/abs/2610.04433v1)
  - 主题: Coding agent routing
  - 中文解读: 这项工作主要关注Coding agent routing，核心内容是《What Does a Harness Buy? Tokens, Mostly》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The rerun data also give the resolution a harness comparison needs: at the discordance we observe, 45 tasks catch a 13-point gap only half the time and no gap with 80% power, and 447 tasks resolve 5 points, still coarser than the gains many harness changes claim.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：80%、3x。
- [Characterizing Parallelism Strategies in LLM Inference: Fundamental Compute-Communication Trade-offs](https://arxiv.org/abs/2610.05305v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Characterizing Parallelism Strategies in LLM Inference: Fundamental Compute-Communication Trade-offs》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Experiments with modern LLMs on multi-GPU platforms validate the model and confirm the fundamental compute-communication trade-off across parallelism strategies.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Breaking the Tie: A Cluster-Aware Routing Framework for Large Language Models](https://arxiv.org/abs/2610.05982v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Breaking the Tie: A Cluster-Aware Routing Framework for Large Language Models》在 arXiv API 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，Specifically, the framework not only demonstrates superior accuracy on multiple benchmarks, but also outperforms Llama-3.3-70B-Instruct by 7.80% in overall average performance.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：7.80%、1.13s。
- [AgentDiscover: Autonomous Discovery with Minimal Search Scaffolding](https://arxiv.org/abs/2610.05334v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《AgentDiscover: Autonomous Discovery with Minimal Search Scaffolding》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，In our experiments, AgentDiscover is more cost-efficient than existing frameworks, reaching better scores at lower cost.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [MedPrune: Topology-Efficient Multimodal Multi-Agent Communication Evolution for Medical VQA Tasks](https://arxiv.org/abs/2610.06695v1)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《MedPrune: Topology-Efficient Multimodal Multi-Agent Communication Evolution for Medical VQA Tasks》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Extensive medical VQA experiments under full-set and few-shot training settings prove MedPrune surpasses multi-agent baselines and boosts token efficiency with strong adversarial robustness.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

