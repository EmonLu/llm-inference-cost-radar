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

- 日期: 2026-11-16
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 7
- 日报: `papers/2026-11-16.md`
- 周报: `digests/weekly-2026-11-16.md`

## 今日最值得看

- [Callo: Serving Cache-Miss Requests with Speculative Decoding on Invalidated KV under Prefill-Decode Disaggregation](https://arxiv.org/abs/2611.18459)
  - 主题: Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Coding agent routing、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Callo: Serving Cache-Miss Requests with Speculative Decoding on Invalidated KV under Prefill-Decode Disaggregation》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，We evaluated Callo on a two-GPU testbed using SWE-agent sessions across three model families, observing all-request speedups of 1.05-1.19x over vLLM at moderate load.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.19x。
- [Fuse-All MoE Inference Kernel with Load Balancing on TPUs](https://arxiv.org/abs/2611.17857v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Fuse-All MoE Inference Kernel with Load Balancing on TPUs》在 arXiv API 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，With accompanying serving stack optimizations, the integrated system improves serving throughput by up to 34.5% over the Megablox EP16 baseline.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：34.5%、2.3x、1.09x。
- [VelServe: Taming Decode Jitters in LLM Inference with Tail-Calibrated Scheduling](https://arxiv.org/abs/2611.18392v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《VelServe: Taming Decode Jitters in LLM Inference with Tail-Calibrated Scheduling》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Disaggregation meets average TBT targets at a cost in capacity, yet the steps that admit new requests still run late.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [ForeSpark: Joint Draft and Verification Budget Scheduling for Parallel Speculative Decoding](https://arxiv.org/abs/2611.13442)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《ForeSpark: Joint Draft and Verification Budget Scheduling for Parallel Speculative Decoding》在 arXiv cs.DC 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，Implemented on vLLM, ForeSpark improves throughput by up to 1.77x over the state-of-the-art DSpark and by 2.49x over autoregressive decoding at a matched per-request generation rate, without changing the output distribution.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.77x、2.49x、1.51x。
- [Programmable Distributions of Semantics-Preserving Variants for Evaluating Code Agents](https://arxiv.org/abs/2608.18389)
  - 主题: Coding agent routing, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Coding agent routing、Cost-efficient LLM inference，核心内容是《Programmable Distributions of Semantics-Preserving Variants for Evaluating Code Agents》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，For our evaluation, we use it to define a generic distribution that is not targeted at any particular failure mode.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [JFinBench: A Continuously Refreshable Japanese Financial Benchmark from the Latest Certification Exams](https://arxiv.org/abs/2611.18130v1)
  - 主题: Coding agent routing, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Coding agent routing、Heterogeneous MoE inference，核心内容是《JFinBench: A Continuously Refreshable Japanese Financial Benchmark from the Latest Certification Exams》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Evaluating 12 recent LLMs, we find that Claude Fable 5 and GPT-6 Astra exceed 93% overall, while even the best open-weight model, Kimi K3.1 Pro, trails Claude Fable 5 by 12 percentage points.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：93%。
- [Large Language Model-Empowered Intelligent Agent for Adaptive Fast-Charging Control of Lithium-Ion Batteries](https://arxiv.org/abs/2611.18140)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Large Language Model-Empowered Intelligent Agent for Adaptive Fast-Charging Control of Lithium-Ion Batteries》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，GRPO aligns the agent with a multi-objective control objective covering energy throughput, degradation mitigation, and operational constraints.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [User-Schedulable Approximations for Quantized Tensor Programs](https://arxiv.org/abs/2611.17526)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《User-Schedulable Approximations for Quantized Tensor Programs》在 arXiv cs.LG 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，A port to x86 with Intel's AMX adds 793 lines of code and matches GGML in 83.5% of its cases.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：83.5%、95%、91.0%。
- [Coordinated Cooling and Compute Management for AI Datacenters](https://arxiv.org/abs/2601.08113)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Coordinated Cooling and Compute Management for AI Datacenters》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Since GPU-intensive inference generates substantial heat that can degrade datacenter performance, ignoring thermal effects can increase total energy consumption and reduce the efficiency of LLM serving.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [LEGIT: Live Eligibility Gating over Identifier Tries for Constrained Decoding of Heterogeneous Pages](https://arxiv.org/abs/2611.10357)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《LEGIT: Live Eligibility Gating over Identifier Tries for Constrained Decoding of Heterogeneous Pages》在 arXiv cs.LG 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Our fastest implementation walks the trie on the CPU while the GPU runs the model, needs no custom kernel, and cuts time per output token by 65.9 percent against the direct GPU implementation, to about 1.7 times the unconstrained cost.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

