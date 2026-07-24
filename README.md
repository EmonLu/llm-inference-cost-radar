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

- 日期: 2026-07-24
- 今日新论文: 15
- 今日新权威来源更新: 2
- 本周精选论文: 25
- 本周精选权威来源更新: 5
- 日报: `papers/2026-07-24.md`
- 周报: `digests/weekly-2026-07-24.md`

## 今日最值得看

- [Efficient and Privacy Aware Edge Cloud Collaborative Inference for Large Language Models](https://arxiv.org/abs/2607.13093)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Efficient and Privacy Aware Edge Cloud Collaborative Inference for Large Language Models》在 arXiv cs.AI 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Evaluations demonstrate that the framework reduces per-token latency by up to 46.1\% and downlink payloads by up to 67.4\% over baseline split inference, retaining comparable performance to full cloud inference.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Beyond Independent Optimization: Compression, MoE Routing, and Quantization Interactions in Multimodal Edge Intelligence](https://arxiv.org/abs/2607.20981v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Beyond Independent Optimization: Compression, MoE Routing, and Quantization Interactions in Multimodal Edge Intelligence》在 arXiv API 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，Efficient multimodal inference is increasingly constrained not only by model quality or FLOP count, but also by the cost of preserving, moving, routing, caching, and quantizing multimodal representations under latency, memory, and energy constraints.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [FineServe: A Fine-Grained Dataset and Characterization of Global LLM Serving Workloads](https://arxiv.org/abs/2607.19349)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《FineServe: A Fine-Grained Dataset and Characterization of Global LLM Serving Workloads》在 arXiv cs.AI 这一方向上的推进。强调异构硬件协同推理。从实验上看，Achieving low latency and high throughput under volatile demand requires deep understanding of real-world serving workloads, yet existing studies often rely on proxy traces or coarse-grained characterizations that fail to capture the heterogeneity of modern multi-model LLM platforms.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Fine-grained Computation-Communication Overlap via Tile-level Signaling and Scheduling for Mixture-of-Experts](https://arxiv.org/abs/2607.19539)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Fine-grained Computation-Communication Overlap via Tile-level Signaling and Scheduling for Mixture-of-Experts》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，On a 4-A100 GPU platform, evaluated on three MoE models against four state-of-the-art MoE systems, our approach achieves up to 2.64x end-to-end speedup and 2.74x MoE-layer speedup.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：2.64x、2.74x。
- [PRO-LONG: Programmatic Memory Enables Long-Horizon Reasoning](https://arxiv.org/abs/2607.20064v2)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《PRO-LONG: Programmatic Memory Enables Long-Horizon Reasoning》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On the full ARC-AGI-3 public game set, PRO-LONG improves over a base coding agent by an average of 18.0 percentage points across frontier models, and matches or exceeds state-of-the-art specialized harnesses (up to 76.1% pass@1) while using 4.2-5.8x fewer tokens.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：76.1%、5.8x、97.4%。
- [Examining QRMI as a Unified Interface for Quantum-HPC Integration](https://arxiv.org/abs/2607.19591)
  - 主题: Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference，核心内容是《Examining QRMI as a Unified Interface for Quantum-HPC Integration》在 arXiv cs.DC 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，arXiv:2607.19591v1 Announce Type: cross Abstract: The efficient and scalable integration of quantum resources into high-performance computing (HPC) environments requires standardized mechanisms for resource management, scheduling, and workflow orchestration across diverse and heterogeneous infrastructures.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Edge Intelligence in Civil Aviation: Paradigms, Techniques, and Applications](https://arxiv.org/abs/2607.19676)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Edge Intelligence in Civil Aviation: Paradigms, Techniques, and Applications》在 arXiv cs.AI 这一方向上的推进。强调异构硬件协同推理。从实验上看，We argue that a refined edge solution can complement cloud foundations to deliver low latency, privacy preserving, and resilient AI services across the civil aviation lifecycle.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [AgentCgroup: Understanding and Controlling OS Resources of AI Agents](https://arxiv.org/abs/2602.09345)
  - 主题: Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Coding agent routing、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《AgentCgroup: Understanding and Controlling OS Resources of AI Agents》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Our measurements reveal that (1) OS-level execution (tool calls, container and agent initialization) accounts for 55-60% of end-to-end task latency; (2) memory, not CPU, is the concurrency bottleneck; (3) memory spikes are tool-call-driven with a up to 15.4x peak-to-average ratio; and (4) resource demands are highly unpredictable across tasks, runs, and models.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：60%、15.4x。
- [TempoNet: Slack-Quantized Transformer-Guided Reinforcement Scheduler for Adaptive Deadline-Centric Real-Time Dispatchs](https://arxiv.org/abs/2602.18109)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《TempoNet: Slack-Quantized Transformer-Guided Reinforcement Scheduler for Adaptive Deadline-Centric Real-Time Dispatchs》在 arXiv cs.LG 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，Extensive evaluations on industrial mixed-criticality traces and large multiprocessor settings show consistent gains in deadline fulfillment over analytic schedulers and neural baselines, together with improved optimization stability.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [ETPDesigner: Multi-Agent Orchestration for Interactive Multimodal Electronic Theater Program](https://arxiv.org/abs/2607.19947v1)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《ETPDesigner: Multi-Agent Orchestration for Interactive Multimodal Electronic Theater Program》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，To rigorously benchmark this task, we construct ETP-Pro, a domain-specific benchmark of professional theater posters and high-quality character portraits.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

