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

- 日期: 2026-07-09
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 2
- 日报: `papers/2026-07-09.md`
- 周报: `digests/weekly-2026-07-09.md`

## 今日最值得看

- [TriRoute: Unified Learned Routing for Joint Adaptive Attention, Experts, and KV-Cache Allocation](https://arxiv.org/abs/2607.06601v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《TriRoute: Unified Learned Routing for Joint Adaptive Attention, Experts, and KV-Cache Allocation》在 arXiv API 这一方向上的推进。强调异构硬件协同推理。从实验上看，The controller trains end-to-end via a heterogeneous relaxation (Gumbel-Softmax with straight-through estimation for categorical decisions and load-balanced top-k gating for experts) under a Lagrangian budget constraint that turns the average compute and memory cost into a controllable knob.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Think Before You Grid-Search: Floor-First Triage for LLM Serving](https://arxiv.org/abs/2607.05876v2)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Think Before You Grid-Search: Floor-First Triage for LLM Serving》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The floors show TP16 decoding is KV-capacity-limited to ~70 concurrent 8K requests; sparse attention removes the KV-bandwidth term but not the capacity wall; an EP16+DP-attention layout accepts slightly worse same-batch weight traffic for an order-of-magnitude higher capacity wall (~644) -- while single-stream latency favors TP by 2.4x.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：2.4x。
- [ButterflyMoE: Compression-Scalable Ternary Experts via Structured Butterfly Orbits](https://arxiv.org/abs/2601.13563)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《ButterflyMoE: Compression-Scalable Ternary Experts via Structured Butterfly Orbits》在 arXiv cs.LG 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，Across language modeling benchmarks, ButterflyMoE achieves 80$\times$ memory reduction at 8 experts with a highly favorable memory-accuracy tradeoff.At this 80x compression ButterflyMoE outperforms an equal memory dense baseline, showing that orbital parameterization extracts fundamentally more utility per byte.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：80x。
- [ProMoE-FL: Prototype-conditioned Mixture of Experts for Multimodal Federated Learning with Missing Modalities](https://arxiv.org/abs/2607.06633)
  - 主题: Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference、LLM routing，核心内容是《ProMoE-FL: Prototype-conditioned Mixture of Experts for Multimodal Federated Learning with Missing Modalities》在 arXiv cs.AI 这一方向上的推进。强调异构硬件协同推理。从实验上看，We perform extensive quantitative and qualitative evaluations on four public chest X-ray datasets (MIMIC-CXR, NIH Open-I, PadChest, and CheXpert) and demonstrate that ProMoE-FL consistently outperforms state-of-the-art methods in both homogeneous as well as the more challenging heterogeneous settings.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [SpaR3D-MoE: Adaptive 3D Spatial Reasoning from Sparse Views Meets Geometry-Inductive Mixture-of-Experts](https://arxiv.org/abs/2607.06620)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《SpaR3D-MoE: Adaptive 3D Spatial Reasoning from Sparse Views Meets Geometry-Inductive Mixture-of-Experts》在 arXiv cs.AI 这一方向上的推进。强调异构硬件协同推理。从实验上看，Notably, SpaR3D-MoE achieves the highest average score of 63.5 on VSI-Bench, outperforming the strongest baseline by 7.8 absolute points, alongside relative improvements of 35.4% and 51.4% in Route Plan and Relative Direction tasks, respectively.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：35.4%、51.4%。
- [Fractal KV-Cache Archives: Lossless Symbolic Storage with In-Place Retrieval for Long-Context LLM Inference](https://arxiv.org/abs/2607.07144v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Fractal KV-Cache Archives: Lossless Symbolic Storage with In-Place Retrieval for Long-Context LLM Inference》在 arXiv API 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Keeping a small exact window (4 attention sinks + 32 recent tokens) and archiving the rest, per-head residual vector quantization reduces the archived cache by 36-54x relative to an fp16 cache at a perplexity cost of 11-15%, and we quantify a sharp key/value asymmetry -- quantizing keys is roughly 4x more damaging than quantizing values, consistent with prior low-bit KV work -- and use it to allocate bits in a hybrid scheme.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：54x、15%、4x。
- [UBEP: Re-architecting Expert Parallelism Communication Library for Production Superpods](https://arxiv.org/abs/2607.06202)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《UBEP: Re-architecting Expert Parallelism Communication Library for Production Superpods》在 arXiv cs.DC 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，Through large scale experiments, UBEP reduces All-to-All latency by up to 52.4% and MoE inference Time Per Output Token (TPOT) by up to 11.1%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：52.4%、11.1%。
- [Latency-Constrained Hardware-Aware Quantum Error Correction Co-Design with Adaptive Confidence-Gated Neural Decoding for the Rotated Surface Code](https://arxiv.org/abs/2607.05814)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Latency-Constrained Hardware-Aware Quantum Error Correction Co-Design with Adaptive Confidence-Gated Neural Decoding for the Rotated Surface Code》在 arXiv cs.LG 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Routing only 3.3%-6.2% of syndromes to the refinement stage improves logical accuracy from 99.21% for the neural-only baseline to 99.81% at a confidence threshold of 0.95 while incurring only a bounded increase in average decoding cost.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：3.3%、6.2%、99.21%。
- [NEST: Tackling Dataset-Level Distribution Shifts via Regime-Oriented Mixture-of-Experts](https://arxiv.org/abs/2607.06607)
  - 主题: Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference、LLM routing，核心内容是《NEST: Tackling Dataset-Level Distribution Shifts via Regime-Oriented Mixture-of-Experts》在 arXiv cs.LG 这一方向上的推进。强调异构硬件协同推理。从实验上看，Extensive evaluations on diverse benchmarks, including heterogeneous network traffic and physical phenomena, demonstrate that NEST consistently achieves state-of-the-art performance.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [HiMoE-VLA: Hierarchical Mixture-of-Experts for Generalist Vision-Language-Action Policies](https://arxiv.org/abs/2512.05693)
  - 主题: Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference，核心内容是《HiMoE-VLA: Hierarchical Mixture-of-Experts for Generalist Vision-Language-Action Policies》在 arXiv cs.AI 这一方向上的推进。强调异构硬件协同推理。从实验上看，HiMoE-VLA reaches 3.98 on CALVIN, 98.0\% on LIBERO, and 75.0\% and 63.7\% average success on real xArm7 and ALOHA tasks; under controlled heterogeneous co-training, it turns the negative transfer observed in strong baselines into positive transfer.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

