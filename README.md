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

- 日期: 2026-08-04
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 4
- 日报: `papers/2026-08-04.md`
- 周报: `digests/weekly-2026-08-04.md`

## 今日最值得看

- [HetRoute Heterogeneous and Cost-aware Collaborative Routing Framework for Distributed Edge MoE Inference](https://arxiv.org/abs/2608.00577v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《HetRoute Heterogeneous and Cost-aware Collaborative Routing Framework for Distributed Edge MoE Inference》在 arXiv API 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Trace-driven evaluation on three MoE models over a heterogeneous 10-server edge testbed shows that HetRoute reduces average inference latency by up to 59.0% and P99 latency by up to 58.0%, cuts cross-server traffic by up to 72.1%, and achieves 2.13x throughput improvement compared with representative baselines, while keeping quality degradation within the configured budget.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：59.0%、58.0%、72.1%。
- [Bole: Efficient Tree Speculation for Hybrid-Attention Language Models](https://arxiv.org/abs/2608.01651v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Bole: Efficient Tree Speculation for Hybrid-Attention Language Models》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Under online agent workloads, it reduces TTFT and TPOT by up to $67.6%$ and $49.9%$, respectively, over the strongest tree-speculative baseline.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：67.6%、49.9%。
- [TrimMoE A communication aware and adaptive depth framework for distributed edge inference](https://arxiv.org/abs/2608.00573v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《TrimMoE A communication aware and adaptive depth framework for distributed edge inference》在 arXiv API 这一方向上的推进。强调异构硬件协同推理。从实验上看，On a heterogeneous 10-server testbed with Switch-Base-8E, Qwen-MoE-A2.7B, and Mixtral-8x7B, TrimMoE reduces the average latency by up to 62.8%, lowers the cross-server traffic and the remote-execution ratio, and sustains high throughput under load, while keeping the task-quality degradation within a 2% bound.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：8x、62.8%、2%。
- [REFLEX: Rethinking MoE Inference as Refinement-Aware Compute Allocation in Diffusion Language Models](https://arxiv.org/abs/2608.01784v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《REFLEX: Rethinking MoE Inference as Refinement-Aware Compute Allocation in Diffusion Language Models》在 arXiv API 这一方向上的推进。强调异构硬件协同推理。从实验上看，Across multiple widely used benchmarks on two representative MoE-based DLMs, LLaDA-MoE and LLaDA2.0-mini, REFLEX reduces allocated expert computation by 15\% on average while preserving or even improving generation quality on most benchmarks relative to default routing.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Securing Agentic AI: From Per-Action Checks to Trajectory Assurance](https://arxiv.org/abs/2608.01558v1)
  - 主题: Agent systems and multi-agent efficiency, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、LLM routing，核心内容是《Securing Agentic AI: From Per-Action Checks to Trajectory Assurance》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，At the single-agent level, untrusted inputs through prompts, memory, retrieved knowledge, and tool interfaces create attack surfaces.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Tevatron Meets Megatron: Expert-Parallel LLM Reranker Training on an Academic Budget](https://arxiv.org/abs/2608.00916v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Tevatron Meets Megatron: Expert-Parallel LLM Reranker Training on an Academic Budget》在 arXiv API 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，We benchmark existing distributed training configurations against the new backend, showing that Megatron matches FSDP reranker quality and training efficiency under comparable data-parallel settings, is up to 22% faster in the recommended single-node configuration, and supports both LoRA and full-parameter fine-tuning.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：22%。
- [An eightfold equivalence-preserving speedup of the JUNO OMILREC vertex and energy reconstruction](https://arxiv.org/abs/2608.00461v1)
  - 主题: Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Coding agent routing、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《An eightfold equivalence-preserving speedup of the JUNO OMILREC vertex and energy reconstruction》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Profiling shows that the production algorithm is latency-bound, sustaining only $9.9%$ of scalar floating-point peak because of virtual-function dispatch, ROOT-histogram pointer chasing, and repeated computation.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：9.9%。
- [An Internet for the KV Cache: Rethinking Classical Infrastructure Boundaries in the LLM Inference Age](https://arxiv.org/abs/2608.01526v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《An Internet for the KV Cache: Rethinking Classical Infrastructure Boundaries in the LLM Inference Age》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，However, model-side advances that shrink the KV Cache and system-side advances that reduce compute, storage, and transfer costs are evolve independently within legacy cloud boundaries.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Broadcast Rate Limits in Wi-Fi: A Forgotten Bottleneck for Collaborative Edge LLM Inference](https://arxiv.org/abs/2608.02341v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Broadcast Rate Limits in Wi-Fi: A Forgotten Bottleneck for Collaborative Edge LLM Inference》在 arXiv API 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，NS-3 simulations at distances 1m, 2m and 5m show that the optimal rates are much higher (64x, 43x, and 32x, respectively) than the 54 Mbps cap applied in standard.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：3 s、64x、43x。
- [Smoothing the Ramp, Not the Peak: Scheduling-Induced Power Dynamics of LLM Inference and Their Grid-Scale Consequences](https://arxiv.org/abs/2608.01250v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Smoothing the Ramp, Not the Peak: Scheduling-Induced Power Dynamics of LLM Inference and Their Grid-Scale Consequences》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，At a representative operating point, this translates to an estimated 20.3-22.7% reduction in the fast-ramping reserve capacity a grid operator would need to provision, across reliability levels from 95% to 99.9%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：22.7%、95%、99.9%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

