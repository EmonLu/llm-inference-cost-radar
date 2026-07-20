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

- 日期: 2026-07-20
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 3
- 日报: `papers/2026-07-20.md`
- 周报: `digests/weekly-2026-07-20.md`

## 今日最值得看

- [PagedWeight: Efficient MoE LLM Serving with Dynamic Quality-Aware Weight Quantization](https://arxiv.org/abs/2607.16184)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《PagedWeight: Efficient MoE LLM Serving with Dynamic Quality-Aware Weight Quantization》在 arXiv cs.LG 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，PagedWeight achieves FP16-equivalent accuracy with up to 72.0% GPU memory savings and 1.94$\times$ throughput improvement, and improves quality over quantization methods by up to 39.3% at a similar memory budget with at most 4.1% throughput loss.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：72.0%、39.3%、4.1%。
- [Efficient and Privacy Aware Edge Cloud Collaborative Inference for Large Language Models](https://arxiv.org/abs/2607.13093)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Efficient and Privacy Aware Edge Cloud Collaborative Inference for Large Language Models》在 arXiv cs.AI 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Evaluations demonstrate that the framework reduces per-token latency by up to 46.1\% and downlink payloads by up to 67.4\% over baseline split inference, retaining comparable performance to full cloud inference.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [QUADS: Stabilizing NVFP4 Reinforcement Learning for MoE via QUantization-error Alignment across Dual Sides](https://arxiv.org/abs/2607.15810v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《QUADS: Stabilizing NVFP4 Reinforcement Learning for MoE via QUantization-error Alignment across Dual Sides》在 arXiv API 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，In our MoE RL experiments on several benchmarks, QUADS achieves BF16-level accuracy, improves average pass@1 by 21.49 points over naive NVFP4 RL, and delivers ~16% higher rollout throughput than FP8.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：16%。
- [ContinuityBench: A Benchmark and Systems Study of Stateful Failover in Multi-Provider LLM Routing](https://arxiv.org/abs/2607.15899v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《ContinuityBench: A Benchmark and Systems Study of Stateful Failover in Multi-Provider LLM Routing》在 arXiv API 这一方向上的推进。强调异构硬件协同推理。从实验上看，Finally, we characterize failover latency distributions, identifying the critical necessity of asynchronous exponential backoff with jitter to prevent cascading retry storms against strict-limit fallback APIs.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Scalable LLM Agent Tool Access in the Cloud](https://arxiv.org/abs/2607.15593)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Scalable LLM Agent Tool Access in the Cloud》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Hybrid retrieval sustains 98% Top-15 recall; it scales agent tool access to 3,000+ with high tool selection accuracy, and reduces tool selection time by $8.9\times$ and token usage by $23.8\times$, with low per-call overhead, stable under scale-out.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：98%。
- [JoyNexus: Service-Oriented Multi-Tenant Post-Training for VLA Models](https://arxiv.org/abs/2607.16074)
  - 主题: Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference，核心内容是《JoyNexus: Service-Oriented Multi-Tenant Post-Training for VLA Models》在 arXiv cs.DC 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Results show that, compared with isolated single-tenant execution, JoyNexus reduces aggregate GPU time and improves service utilization via cross-tenant scheduling on shared resources.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [RhinoVLA Technical Report](https://arxiv.org/abs/2606.07383)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《RhinoVLA Technical Report》在 arXiv cs.LG 这一方向上的推进。强调异构硬件协同推理。从实验上看，Experiments show that RhinoVLA achieves downstream performance comparable to {\pi}0.5 at a similar parameter scale, while reaching 11.69 Hz end-to-end inference on Huixi R1, meeting the 10 Hz real-time closedloop control target.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [A JoLT for the KV Cache: Near-Lossless KV Cache Compression via Joint Tucker and JL-Residual Allocation for LLMs](https://arxiv.org/abs/2607.12550)
  - 主题: Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference，核心内容是《A JoLT for the KV Cache: Near-Lossless KV Cache Compression via Joint Tucker and JL-Residual Allocation for LLMs》在 arXiv cs.CL 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，A randomized-SVD variant, FlashJoLT, delivers a 5-13x compression-time speedup at 1024-token context and matched quality.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：13x、2x、3x。
- [Diagnosing Overhead in Dispatch Operations: Cross-architecture Observatory](https://arxiv.org/abs/2605.20982)
  - 主题: Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference、LLM routing，核心内容是《Diagnosing Overhead in Dispatch Operations: Cross-architecture Observatory》在 arXiv cs.DC 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，All four rest on two assumptions about the workload: that routing imbalance is correctable by the system layer, and that the mock-token benchmarks evaluating them faithfully represent production routing.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [PASs-MoE: Mitigating Misaligned Co-drift among Router and Experts via Pathway Activation Subspaces for Continual Learning](https://arxiv.org/abs/2601.13020)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《PASs-MoE: Mitigating Misaligned Co-drift among Router and Experts via Pathway Activation Subspaces for Continual Learning》在 arXiv cs.LG 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，Experiments on a CIT benchmark show that our approach consistently outperforms a range of conventional continual learning baselines and MoE--LoRA variants in both accuracy and resistance to forgetting, without increasing model parameters.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

