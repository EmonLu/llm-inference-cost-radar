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

- 日期: 2026-06-17
- 今日新论文: 15
- 今日新权威来源更新: 1
- 本周精选论文: 25
- 本周精选权威来源更新: 3
- 日报: `papers/2026-06-17.md`
- 周报: `digests/weekly-2026-06-17.md`

## 今日最值得看

- [RouteBalance: Fused Model Routing and Load Balancing for Heterogeneous LLM Serving](https://arxiv.org/abs/2606.17949)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《RouteBalance: Fused Model Routing and Load Balancing for Heterogeneous LLM Serving》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，A batched in-process predictor stack and dead-reckoned instance state keep the joint decision cheap on the request hot path ($\approx$32 ms at 12 req/s).
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：32 ms。
- [ITME: Inference Tiered Memory Expansion with Disaggregated CXL-Hybrid Memories](https://arxiv.org/abs/2606.12556)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《ITME: Inference Tiered Memory Expansion with Disaggregated CXL-Hybrid Memories》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Overall, ITME enhances conventional CPU-offloading by providing additional remote memory expansion to accommodate large KV cache footprints beyond host memory limits, achieving up to a 35.7\% throughput improvement.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Evaluating LLM Coding Agents on SZ-Family Lossy Compression Across Architectures](https://arxiv.org/abs/2606.17058)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《Evaluating LLM Coding Agents on SZ-Family Lossy Compression Across Architectures》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On GPUs, stronger models can achieve substantially higher throughput but exhibit increased sensitivity to prompt precision and optimization guidance, whereas on Cerebras the dominant challenge lies in producing runnable programs under a PE-centric spatial execution model.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [The Price of Anarchy in Disaggregated Inference](https://arxiv.org/abs/2606.17081)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《The Price of Anarchy in Disaggregated Inference》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Our strongest result is on the 70B 1P/5D topology, where PoA-hat drops 3.1x (66.4 to 21.5) in the saturated phase at a 13% throughput cost.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：3.1x、13%、2.2x。
- [Prefill/Decode-Aware Evaluation of LLM Inference on Emerging AI Accelerators](https://arxiv.org/abs/2606.17104)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Prefill/Decode-Aware Evaluation of LLM Inference on Emerging AI Accelerators》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，However, GPUs regain an advantage in Decode throughput as batch size increases.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Models Take Notes at Prefill: KV Cache Can Be Editable and Composable](https://arxiv.org/abs/2606.17107)
  - 主题: Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference，核心内容是《Models Take Notes at Prefill: KV Cache Can Be Editable and Composable》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，A unified edit+compose agent stays decision-identical to recompute at up to 14.9x lower latency.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：14.9x、98.5%、398x。
- [MODE: Modality-Decomposed Expert-Level Mixed-Precision Quantization for MoE Multimodal LLMs](https://arxiv.org/abs/2606.17118)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《MODE: Modality-Decomposed Expert-Level Mixed-Precision Quantization for MoE Multimodal LLMs》在 arXiv cs.LG 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Extensive experiments show that MODE is particularly well-suited for MoE-MLLMs, limiting average performance loss to within 2.9% at W3A16, with larger gains at the extreme 2-bit setting.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：2.9%。
- [OmniPlan: An Adaptive Framework for Timely and Near-Optimal Network Planning Optimization](https://arxiv.org/abs/2606.18105v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《OmniPlan: An Adaptive Framework for Timely and Near-Optimal Network Planning Optimization》在 arXiv API 这一方向上的推进。强调异构硬件协同推理。从实验上看，Our experiments on a real-world testbed indicate that OmniPlan achieves near-optimal and low-execution-time offloading for real-world ML inference tasks, reducing latency by up to 97.8\% and network device resource consumption by up to 11.5\%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Agent trajectories as programs: fingerprinting and programming coding-agent behavior](https://arxiv.org/abs/2606.16988v1)
  - 主题: Coding agent routing, LLM routing
  - 中文解读: 这项工作主要关注Coding agent routing、LLM routing，核心内容是《Agent trajectories as programs: fingerprinting and programming coding-agent behavior》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，We compare ten agents and find that they are identifiable by their behavioral habits, which we define as fingerprints: a probe over these procedural signatures attributes an unseen trajectory to the correct agent at 85.7% accuracy, controlling for leakage across tasks.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：85.7%。
- [LLM-Aided Joint Secrecy Precoding and Trajectory for RSMA-Based Heterogeneous UAV Networks](https://arxiv.org/abs/2507.17188)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《LLM-Aided Joint Secrecy Precoding and Trajectory for RSMA-Based Heterogeneous UAV Networks》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The inner layer uses a semidefinite relaxation (SDR)-based S2DC algorithm combining penalty functions and difference-of-convex (D.C.) programming to solve the secrecy precoding problem with fixed UAV positions.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

