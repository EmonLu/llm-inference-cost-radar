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

- 日期: 2026-08-19
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 3
- 日报: `papers/2026-08-19.md`
- 周报: `digests/weekly-2026-08-19.md`

## 今日最值得看

- [FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution](https://arxiv.org/abs/2608.16157)
  - 主题: Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Coding agent routing、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，FreeToken supports more than 20 MoE models and real coding and tool-using agents across hardware ranging from an 8GB laptop GPU to a single workstation GPU.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：8GB。
- [Agentic Kernel Optimization: Generating State-of-the-Art GPU Kernels Without Hand-Written CUDA](https://arxiv.org/abs/2608.14560)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《Agentic Kernel Optimization: Generating State-of-the-Art GPU Kernels Without Hand-Written CUDA》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，In the official evaluation of the MLSys 2026 FlashInfer AI Kernel Generation Contest, our generated Fused MoE kernel achieves a 1.71x speedup over the FlashInfer baseline, exceeding the top result of the Fused MoE agent-assisted track, which reports a 1.68x speedup.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.71x、1.68x、92.68x。
- [MAPLE: MoE Adaptive Plug-and-play Layer-wise Expert allocation](https://arxiv.org/abs/2608.15299)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《MAPLE: MoE Adaptive Plug-and-play Layer-wise Expert allocation》在 arXiv cs.LG 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，These accuracy gains translate into measured deployment efficiency: implementing MAPLE in SGLang reduces single-GPU end-to-end serving latency by 32.2% and improves throughput by 47.4%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：32.2%、47.4%、75%。
- [GraniKV: Asymmetric Granularity KV-Cache Paging for Multi-Agent Systems with Long Shared Prefix](https://arxiv.org/abs/2608.15584)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《GraniKV: Asymmetric Granularity KV-Cache Paging for Multi-Agent Systems with Long Shared Prefix》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The gain decomposes: cascade attention integration contributes the majority at saturation; the asymmetric storage layer adds $1.05$--$1.15\times$ end-to-end while being what makes the batched-GEMM prefix backend possible at all.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Beyond Binary Priorities: Multi-Tier SLA Scheduling for Large Language Model Serving](https://arxiv.org/abs/2608.16336)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Beyond Binary Priorities: Multi-Tier SLA Scheduling for Large Language Model Serving》在 arXiv cs.DC 这一方向上的推进。强调异构硬件协同推理。从实验上看，Our experiments demonstrate that four priority tiers yields the best cost-effectiveness tradeoff, achieving prefill mean speedups of up to 8.3x and end-to-end P99 speedups of up to 3.1x over INFaaS with cost-per-latency improvements of 46 to 68%, while preserving strong SLO differentiation across tiers.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：8.3x、99 s、3.1x。
- [Large Models for Small Devices: Recent Advances and Empirical Analysis of Edge AI Deployment](https://arxiv.org/abs/2608.15693)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Large Models for Small Devices: Recent Advances and Empirical Analysis of Edge AI Deployment》在 arXiv cs.LG 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，For question answering, Qwen3.5 0.8B reaches 93.85 SQuAD F1 and 92 EM under Q5_K_M GGUF quantization, while structured pruning at the same precision costs 16 F1 at a 1% ratio.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：93.85 S、1%、49%。
- [CodeQuant: Unified Clustering and Quantization for Enhanced Outlier Smoothing in Low-Precision Mixture-of-Experts](https://arxiv.org/abs/2604.10496)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《CodeQuant: Unified Clustering and Quantization for Enhanced Outlier Smoothing in Low-Precision Mixture-of-Experts》在 arXiv cs.LG 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Coupled with a dedicated kernel design for GPU and CPU, CodeQuant achieves up to $4.15\times$ speedup while delivering significantly higher accuracy than state-of-the-art quantization approaches across diverse MoE models.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [MoE Router-Guided Clustering for Heterogeneous Federated Instruction Tuning](https://arxiv.org/abs/2608.15311)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《MoE Router-Guided Clustering for Heterogeneous Federated Instruction Tuning》在 arXiv cs.AI 这一方向上的推进。强调异构硬件协同推理。从实验上看，Experimental results show that routing-aware collaboration consistently improves personalized performance compared to conventional federated averaging and local training, while maintaining the same communication cost.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Analytical Provisioning for Attention-FFN Disaggregated LLM Serving under Stochastic Workloads](https://arxiv.org/abs/2601.21351)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Analytical Provisioning for Attention-FFN Disaggregated LLM Serving under Stochastic Workloads》在 arXiv cs.LG 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，A trace-calibrated AFD simulator supports the framework across workloads: the predicted optimal ratio matches the simulation-optimal within 10%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：10%。
- [Self-Routed Tensor Adapters for Parameter-Efficient Universal Visual Adaptation](https://arxiv.org/abs/2608.16384)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Self-Routed Tensor Adapters for Parameter-Efficient Universal Visual Adaptation》在 arXiv cs.LG 这一方向上的推进。强调异构硬件协同推理。从实验上看，Across five heterogeneous multi-domain visual classification benchmarks, SRTA achieves competitive or slightly stronger average accuracy than MoE-style PEFT baselines while using substantially fewer trainable parameters.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

