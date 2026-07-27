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

- 日期: 2026-07-27
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 23
- 本周精选权威来源更新: 5
- 日报: `papers/2026-07-27.md`
- 周报: `digests/weekly-2026-07-27.md`

## 今日最值得看

- [Agentic CPU-GPU Scheduling for Heterogeneous AI Workloads](https://arxiv.org/abs/2607.22242)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Agentic CPU-GPU Scheduling for Heterogeneous AI Workloads》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across 13 scenarios spanning serial execution, parallel contention, and memory-constrained execution, the agentic scheduler reaches the brute-force optimal mapping in all 13 scenarios, matching the best classical baseline on mapping accuracy while avoiding bandit-style exploration over complete mappings, and outperforming HEFT, StarPU, and the all-GPU policy while requiring zero offline training.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：13 s。
- [TENT: A Declarative Slice Spraying Engine for Performant and Resilient Data Movement in Disaggregated LLM Serving](https://arxiv.org/abs/2604.00368)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《TENT: A Declarative Slice Spraying Engine for Performant and Resilient Data Movement in Disaggregated LLM Serving》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，In LLM inference with SGLang HiCache, TE+ achieves up to 1.36x higher throughput and 26% lower P90 time-to-first-token (TTFT) than Mooncake TE.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.36x、26%。
- [Unified Static-Dynamic Pruning for Efficient LLM Inference](https://arxiv.org/abs/2607.21985)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Unified Static-Dynamic Pruning for Efficient LLM Inference》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Comprehensive evaluations on inference-optimized GPUs demonstrate that SPDP achieves 1.24x-1.37x average speedup (up to 2.51x) over state-of-the- art sparse frameworks such as SpInfer, while matching.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.24x、1.37x、2.51x。
- [MoE$^2$-LoRA: When MoE Models Meet MoE-style Low-Rank Adaptation](https://arxiv.org/abs/2607.21978)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《MoE$^2$-LoRA: When MoE Models Meet MoE-style Low-Rank Adaptation》在 arXiv cs.CL 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，Evaluated on multiple MoE backbones with varying scales and expert granularities, MoE$^2$-LoRA consistently achieves state-of-the-art downstream accuracy while retaining stronger general capabilities.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [PRISM: Evaluating POSIX Storage Systems for AI Research Workflows](https://arxiv.org/abs/2607.21746)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《PRISM: Evaluating POSIX Storage Systems for AI Research Workflows》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，As a specific case study in our environment we observed that a flash backed NFS solution outperformed the flash backed Lustre solution by up to 3x for the distributed checkpoint load usecase which helped us make an informed cluster design
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：3x。
- [NUMA balancing hampering performance of spiking network simulations](https://arxiv.org/abs/2607.22275)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《NUMA balancing hampering performance of spiking network simulations》在 arXiv cs.DC 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，We show that turning off automatic NUMA balancing may reduce energy consumption by 30%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：30%。
- [Multi-Agent Debate and Visual Information Extraction for SeePhys Pro: A 1st-Place Technical Report from ICML 2026 AI4Math Track 3 Challenge](https://arxiv.org/abs/2607.21946)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《Multi-Agent Debate and Visual Information Extraction for SeePhys Pro: A 1st-Place Technical Report from ICML 2026 AI4Math Track 3 Challenge》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The resulting pipeline improves overall accuracy over a single-agent baseline from 0.643 to 0.802 on the public split, and won 1st place on both the public and the private leaderboard (private overall 0.743).
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1s。
- [Scalable Explainability-as-a-Service (XaaS) for Edge AI Systems](https://arxiv.org/abs/2602.04120)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Scalable Explainability-as-a-Service (XaaS) for Edge AI Systems》在 arXiv cs.DC 这一方向上的推进。强调异构硬件协同推理。从实验上看，Experimental results show that XaaS reduces latency by 38% while maintaining high explanation quality across three real-world deployments.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：38%。
- [TRACE-ROUTER: Task-Consistent and Adaptive Online Routing for Agentic AI](https://arxiv.org/abs/2607.22465)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、LLM routing，核心内容是《TRACE-ROUTER: Task-Consistent and Adaptive Online Routing for Agentic AI》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On tau2-Bench, it outperforms latency-matched interpolation between individual models by 7-8 accuracy points, while on Terminal-Bench it achieves 7.1 higher accuracy points than the strongest single model baseline with 36% lower latency.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：36%。
- [TileSight: A First-Principles Tile-Centric Analytical GPU Performance Model from Cores to Clusters](https://arxiv.org/abs/2607.22432)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《TileSight: A First-Principles Tile-Centric Analytical GPU Performance Model from Cores to Clusters》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，On A100, H200, B200, and B6000, TileSight predicts single-GPU kernel latency with 12.35% pooled mean absolute percentage error (MAPE), outperforming state-of-the-art baselines and transferring better across architectures.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：12.35%、16.18%、13.52%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

