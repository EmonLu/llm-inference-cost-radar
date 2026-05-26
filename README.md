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

- 日期: 2026-05-26
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 0
- 日报: `papers/2026-05-26.md`
- 周报: `digests/weekly-2026-05-26.md`

## 今日最值得看

- [Adaptive KV Cache Reuse for Fast Long-Context LLM Serving](https://arxiv.org/abs/2605.24022)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Adaptive KV Cache Reuse for Fast Long-Context LLM Serving》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Evaluations on mainstream LLMs and long-context tasks show that CacheTune achieves 3.72x-4.86x TTFT speedup and 3.93x-6.21x higher throughput while maintaining generation quality close to full recompute.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：3.72x、4.86x、3.93x。
- [DisagFusion: Asynchronous Pipeline Parallelism and Elastic Scheduling for Disaggregated Diffusion Serving](https://arxiv.org/abs/2605.25550)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《DisagFusion: Asynchronous Pipeline Parallelism and Elastic Scheduling for Disaggregated Diffusion Serving》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Compared to a monolithic baseline, DisagFusion improves throughput by 3.4x-20.5x and reduces end-to-end latency by 18.5x, while enabling flexible, cost-efficient deployment across heterogeneous GPUs.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：3.4x、20.5x、18.5x。
- [Fast-dDrive: Efficient Block-Diffusion VLM for Autonomous Driving](https://arxiv.org/abs/2605.23163)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Fast-dDrive: Efficient Block-Diffusion VLM for Autonomous Driving》在 arXiv cs.CL 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On the WOD-E2E test set, Fast-dDrive achieves SOTA ADE@3s and ADE@5s, alongside the highest RFS among diffusion-based VLAs; on nuScenes, it reduces average L2 error to $0.32$m (a $22\%$ improvement).
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：3s、5s。
- [Bandwidth-Aware LLM Inference on Heterogeneous Many-Core Supercomputers](https://arxiv.org/abs/2605.25655)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Bandwidth-Aware LLM Inference on Heterogeneous Many-Core Supercomputers》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Experiments on the Llama model series show that THInfer improves throughput on the 7B model by 62 percent to 73 percent over DeepSpeed on two V100S GPUs and by 67 percent to 84 percent over the A800 GPU.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：100S。
- [LA-IMR: Latency-Aware, Predictive In-Memory Routing and Proactive Autoscaling for Tail-Latency-Sensitive Cloud Robotics](https://arxiv.org/abs/2505.07417)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《LA-IMR: Latency-Aware, Predictive In-Memory Routing and Proactive Autoscaling for Tail-Latency-Sensitive Cloud Robotics》在 arXiv cs.DC 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Across representative vision workloads (YOLOv5m and EfficientDet) and bursty arrival traces, LA-IMR reduces P99 latency by up to 20.7 percent compared to traditional latency-only autoscaling, laying a principled foundation for next-generation, tail-tolerant cloud-edge inference services.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Influence-Inspired Spectral Rotations for Extreme Low-Bit LLM Quantization](https://arxiv.org/abs/2605.25203)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Influence-Inspired Spectral Rotations for Extreme Low-Bit LLM Quantization》在 arXiv cs.LG 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，On four pretrained decoder-only models from 135M to 1.5B parameters, BBT-spectral reduces wikitext-2 perplexity by 15-58% relative to vanilla auto-round at W2A16; we also report a TinyLlama-1.1B auxiliary data point.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：58%。
- [Shepherd: A Runtime Substrate Empowering Meta-Agents with a Formalized Execution Trace](https://arxiv.org/abs/2605.10913)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing，核心内容是《Shepherd: A Runtime Substrate Empowering Meta-Agents with a Formalized Execution Trace》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Three example use cases show Shepherd's versatility: (1) a supervisor agent prevents conflicts among parallel coding agents, lifting CooperBench performance from 28.8% to 54.7%; (2) a counterfactual optimizer repairs agent workflows by proposing edits and replaying runs from the point of changed behavior, outperforming MetaHarness on TerminalBench-2 with 58% lower wall-clock; (3) a meta-agent picks fork points during rollouts to improve credit assignment in long-horizon agentic RL, doubling GRPO's gains on TerminalBench-2.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：28.8%、54.7%、58%。
- [ConceptM$^3$oE: Concept-Guided Multimodal Mixture of Experts for Interpretable Computational Pathology](https://arxiv.org/abs/2605.24399)
  - 主题: Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference，核心内容是《ConceptM$^3$oE: Concept-Guided Multimodal Mixture of Experts for Interpretable Computational Pathology》在 arXiv cs.AI 这一方向上的推进。强调异构硬件协同推理。从实验上看，In data-limited regimes, ConceptM$^3$oE improves limited-data performance, increasing macro-F1 from 56.41% to 66.70% at small training sizes compared to non-concept-informed baselines, while also showing faster training convergence consistent with the regularizing effect of concept learning.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：56.41%、66.70%。
- [RepetitionCurse: Measuring and Understanding Router Imbalance in Mixture-of-Experts LLMs under DoS Stress](https://arxiv.org/abs/2512.23995)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《RepetitionCurse: Measuring and Understanding Router Imbalance in Mixture-of-Experts LLMs under DoS Stress》在 arXiv cs.LG 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，On widely deployed MoE models like Mixtral-8x7B, our method increases end-to-end inference latency by 3.063x, degrading service availability significantly.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：8x、3.063x。
- [Multi-Agent Systems are Mixtures of Experts: Who Becomes an Influencer?](https://arxiv.org/abs/2605.25929v1)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference、LLM routing，核心内容是《Multi-Agent Systems are Mixtures of Experts: Who Becomes an Influencer?》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，This perspective implies that multi-agent systems can outperform single agents and static ensembles when routing reflects agent competence.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

