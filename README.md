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

- 日期: 2026-10-26
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 9
- 日报: `papers/2026-10-26.md`
- 周报: `digests/weekly-2026-10-26.md`

## 今日最值得看

- [InferSlice: A Reference Architecture for SLO-driven LLM Inference over a Telco Wide-Area Network](https://arxiv.org/abs/2610.32638)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《InferSlice: A Reference Architecture for SLO-driven LLM Inference over a Telco Wide-Area Network》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Our results show that, on a general-purpose telco network, tiers yield distinct latency-throughput regimes, and weight streaming shortens scale-out time.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [MoE-SpAc: Efficient MoE Inference Based on Speculative Activation Utility in Heterogeneous Edge Scenarios](https://arxiv.org/abs/2603.09983)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《MoE-SpAc: Efficient MoE Inference Based on Speculative Activation Utility in Heterogeneous Edge Scenarios》在 arXiv cs.CL 这一方向上的推进。强调异构硬件协同推理。从实验上看，Extensive experiments on seven benchmarks demonstrate that MoE-SpAc achieves a 42% improvement in TPS over the SOTA SD-based baseline, and an average 4.04x speedup over all standard baselines.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：42%、4.04x。
- [KVStream: Adaptive Parallel Storage Management for KV Caching in Large-Scale LLM Serving](https://arxiv.org/abs/2610.31827)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《KVStream: Adaptive Parallel Storage Management for KV Caching in Large-Scale LLM Serving》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Plugged into LMCache and evaluated on four models, six datasets, and up to 128 GPUs, KVStream retrieves within 5% of the bound, delivers up to 1.49$\times$ higher offline throughput than LMCache, and lowers mean TTFT by up to 6.1$\times$ under bursty arrivals.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：5%。
- [HAWK: Heterogeneity-Aware KV Cache Transfer for Efficient GPU-NPU Phase-Disaggregated LLM Inference](https://arxiv.org/abs/2610.29873)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《HAWK: Heterogeneity-Aware KV Cache Transfer for Efficient GPU-NPU Phase-Disaggregated LLM Inference》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，We implement and evaluate HAWK on a system built with commercially available GPUs and NPUs, demonstrating performance within 7.88% of a GPU-only system under the same SLO constraints while achieving up to 1.26$\times$ higher power efficiency and 1.72$\times$ higher cost efficiency.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：7.88%。
- [Learning Structured Sparsity for Large Models: Bridging Model Compressibility and Efficient Inference](https://arxiv.org/abs/2610.31897)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Learning Structured Sparsity for Large Models: Bridging Model Compressibility and Efficient Inference》在 arXiv cs.AI 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，These results show that structured learning can translate elastic compressibility into reduced memory requirements and lower inference latency, enabling practical deployment of large models on edge devices.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Rethinking Multi-View Fusion for Urban Representation Learning](https://arxiv.org/abs/2610.31850)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Rethinking Multi-View Fusion for Urban Representation Learning》在 arXiv cs.AI 这一方向上的推进。强调异构硬件协同推理。从实验上看，Experiments on three large-scale urban datasets show that PRISM achieves competitive performance compared with strong multi-view baselines, while providing more stable optimization behavior and more balanced region representations.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [NgramRL: Accelerating RL Post-Training for Structured Generation via Rollout-Aware N-gram Speculative Decoding](https://arxiv.org/abs/2610.32881)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《NgramRL: Accelerating RL Post-Training for Structured Generation via Rollout-Aware N-gram Speculative Decoding》在 arXiv cs.AI 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，On Spider, the prefetcher covers 96.6% of Qwen3-8B outcomes at a candidate budget of 16 and improves measured rollout throughput by 1.38x over synchronous NgramRL, approaching its 1.40x overlap ceiling.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：96.6%、1.38x、1.40x。
- [OpenDraco: A Platform for Engineering and Experimenting with Configurable Multi-Agent Architectures for Software Engineering](https://arxiv.org/abs/2610.32686v1)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《OpenDraco: A Platform for Engineering and Experimenting with Configurable Multi-Agent Architectures for Software Engineering》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，OpenDraco supports iterative experimentation with heterogeneous MAS configurations, enabling researchers to examine their outcomes and costs within a common environment.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：77 S。
- [Training an MoE LLM in MXFP4: How We Closed the Gap to BF16](https://arxiv.org/abs/2610.32229)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Training an MoE LLM in MXFP4: How We Closed the Gap to BF16》在 arXiv cs.AI 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，Measured by steps to reach the MLPerf quality target (validation loss 3.34), de-oscillation cuts the FP4 convergence overhead relative to BF16 from +20.0% to +5.0%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：20.0%、5.0%、128 s。
- [Measuring the Energy Cost of Completing Tasks with Quantized Language-Model Agents](https://arxiv.org/abs/2610.32417v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Measuring the Energy Cost of Completing Tasks with Quantized Language-Model Agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，These findings offer actionable guidance for developers and operators choosing model precision for agents, showing how tokens per completed task, set against the per-token saving, reveal whether lower precision completes the work with less energy.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

