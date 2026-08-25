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

- 日期: 2026-08-25
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 3
- 日报: `papers/2026-08-25.md`
- 周报: `digests/weekly-2026-08-25.md`

## 今日最值得看

- [DAOP: Data-Aware Offloading and Predictive Pre-Calculation for Efficient MoE Inference](https://arxiv.org/abs/2501.10375)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《DAOP: Data-Aware Offloading and Predictive Pre-Calculation for Efficient MoE Inference》在 arXiv cs.DC 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Comprehensive evaluations across various datasets show that DAOP outperforms traditional expert caching and prefetching methods by up to 8.20x and offloading techniques by 1.35x while maintaining accuracy.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：8.20x、1.35x。
- [TokenCake: A KV-Cache-centric Serving Framework for LLM-based Multi-Agent Applications](https://arxiv.org/abs/2510.18586)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《TokenCake: A KV-Cache-centric Serving Framework for LLM-based Multi-Agent Applications》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Our evaluation on representative multi-agent benchmarks shows that TokenCake reduces end-to-end latency by over 47.06% and improves effective GPU memory utilization by up to 16.9% compared to vLLM.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：47.06%、16.9%。
- [FL-MAESTRO: Multi-Agent LLM Orchestration for Resource-Constrained Federated Learning](https://arxiv.org/abs/2608.20518)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《FL-MAESTRO: Multi-Agent LLM Orchestration for Resource-Constrained Federated Learning》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On a non-IID CIFAR-10 benchmark, FL-MAESTRO matches the accuracy of the strongest energy-aware baseline while cutting wasted round energy from over a third to near zero.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Benchmarking LLM Serving Systems for Agentic AI Workloads with XPerf](https://arxiv.org/abs/2608.20370)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《Benchmarking LLM Serving Systems for Agentic AI Workloads with XPerf》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Benchmarking LLM serving systems under agentic workloads is challenging - agentic applications rely on nondeterministic LLM outputs to guide their control flow; therefore, workload patterns vary unpredictably from run to run.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [RARE: Decoupling Representation Steering from Expert Routing in Mixture-of-Experts Language Models](https://arxiv.org/abs/2608.21236)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《RARE: Decoupling Representation Steering from Expert Routing in Mixture-of-Experts Language Models》在 arXiv cs.CL 这一方向上的推进。强调异构硬件协同推理。从实验上看，It further improves average TruthfulQA MC1 accuracy from 41.0% to 58.6% and CounterFact efficacy from 16.8% to 96.3%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：41.0%、58.6%、16.8%。
- [DeepStack: Facilitating Co-Design Exploration of 3D DRAM-Stacked Accelerators for Distributed LLM Inference](https://arxiv.org/abs/2604.04750)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《DeepStack: Facilitating Co-Design Exploration of 3D DRAM-Stacked Accelerators for Distributed LLM Inference》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，A search-space ablation shows that restricted DSE baselines can miss up to 9.5x modeled throughput.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：9.5x、000x。
- [Graph Engineering in the Era of LLM Agents: From Individual Intelligence to System Intelligence](https://arxiv.org/abs/2608.21156)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《Graph Engineering in the Era of LLM Agents: From Individual Intelligence to System Intelligence》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，These abstractions provide a unified foundation for organizing complex objectives, orchestrating heterogeneous agents, modeling system dynamics, and enabling scalable agent evolution.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Themis: Efficient Sparse Model Training Through Fully Sharded Sparse Data Parallelism](https://arxiv.org/abs/2502.02581)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Themis: Efficient Sparse Model Training Through Fully Sharded Sparse Data Parallelism》在 arXiv cs.DC 这一方向上的推进。强调异构硬件协同推理。从实验上看，Across 2 clusters and diverse workloads, Themis achieves 1.26-2.42x speedup over state-of-the-art expert-rearrangement systems.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：2.42x。
- [RouteScan: A Non-Intrusive Approach to Auditing MoE LLMs Safety via Expert Routing Telemetry](https://arxiv.org/abs/2605.24817)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《RouteScan: A Non-Intrusive Approach to Auditing MoE LLMs Safety via Expert Routing Telemetry》在 arXiv cs.CL 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Comprehensive evaluations on four open-source MoE LLMs with distinct routing designs demonstrate that RouteScan achieves strong generalization, with an AUROC exceeding 0.91 on unseen harmful domains.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Specification Portability Across LLM Development Agents: Cross-Agent Compatibility in Specification-Driven Software Migration](https://arxiv.org/abs/2608.21208)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Specification Portability Across LLM Development Agents: Cross-Agent Compatibility in Specification-Driven Software Migration》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The strongest replicated case occurred when Gemini directly consumed a Kiro-origin specification, producing a Token F1 of 0.035, SQL syntax validity of 2.33%, and AST mean similarity of 0.015.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：2.33%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

