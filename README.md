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

- 日期: 2026-09-02
- 今日新论文: 15
- 今日新权威来源更新: 1
- 本周精选论文: 25
- 本周精选权威来源更新: 2
- 日报: `papers/2026-09-02.md`
- 周报: `digests/weekly-2026-09-02.md`

## 今日最值得看

- [LLM Inference on IMC-NoC Architecture with Balanced Dataflow and Fine-Grained Parallelism](https://arxiv.org/abs/2609.00857v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《LLM Inference on IMC-NoC Architecture with Balanced Dataflow and Fine-Grained Parallelism》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Compared to commercial GPU platforms, the proposed architecture provides a throughput and an energy efficiency improvement of $\geq{}1.52\times$ and $24.91\times$, respectively.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [GeoPAR: Large-Scale Multi-Agent Combinatorial Optimization with Geometry-Guided Parallel Autoregressive Learning](https://arxiv.org/abs/2609.00577)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《GeoPAR: Large-Scale Multi-Agent Combinatorial Optimization with Geometry-Guided Parallel Autoregressive Learning》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experiments on heterogeneous vehicle routing and open multi-depot pickup-and-delivery problems show that GeoPAR improves large-scale zero-shot generalization while substantially reducing rollout steps and maintaining efficient inference.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [WiSDoM: Wireless Sparse Decision Transformer with Mixture-of-Experts for Multi-Task Mobile Network Optimization](https://arxiv.org/abs/2609.00284v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《WiSDoM: Wireless Sparse Decision Transformer with Mixture-of-Experts for Multi-Task Mobile Network Optimization》在 arXiv API 这一方向上的推进。强调异构硬件协同推理。从实验上看，Experimental results show that WiSDoM consistently outperforms heuristic methods, single-task models, and conventional multi-task DTs, improving quality of experience (QoE) by up to 55% while activating approximately one-third of the parameters of its dense counterpart during inference.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：55%。
- [Reliable LLM-Generated Programs for High-Energy Physics Experiments through Graph-Grounded Software Knowledge](https://arxiv.org/abs/2609.01095v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《Reliable LLM-Generated Programs for High-Energy Physics Experiments through Graph-Grounded Software Knowledge》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On a benchmark of 275 ROOT tasks, grounding improves first-attempt execution from 58.5% to 76.0% under Claude Code orchestration and from 51.3% to 64.0% under standalone orchestration.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：58.5%、76.0%、51.3%。
- [AInfer-PD: Communication-Safe In-Place Prefill-Decode Multiplexing for Distributed MoE Rollouts](https://arxiv.org/abs/2609.00993)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《AInfer-PD: Communication-Safe In-Place Prefill-Decode Multiplexing for Distributed MoE Rollouts》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，In a same-engine ablation, fine-grained boundaries reduce completion time by a further 8.6-19.8% over whole-epoch asynchronous enqueue.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：19.8%、35.3%、31.8%。
- [KV Cache Offloading for Context-Intensive Tasks](https://arxiv.org/abs/2604.08426)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《KV Cache Offloading for Context-Intensive Tasks》在 arXiv cs.CL 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，Recently, KV-cache offloading has emerged as a promising approach to reduce memory footprint and inference latency while preserving accuracy.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Drift-Aware LLM Routing with Sparse Contexts and Shared Budgets](https://arxiv.org/abs/2609.00662v1)
  - 主题: Cost-efficient LLM inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、LLM routing，核心内容是《Drift-Aware LLM Routing with Sparse Contexts and Shared Budgets》在 arXiv API 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，A multi-model language service must route each request while preserving workload-level budgets for compute, latency, memory, or monetary cost.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [DRLM: Deep Reinforcement Learning-Based LLM Query Orchestration in Edge Environments](https://arxiv.org/abs/2609.00442v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《DRLM: Deep Reinforcement Learning-Based LLM Query Orchestration in Edge Environments》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Evaluation on a 64-node edge cluster and comparison with three baselines and two state-of-the-art methods show that DRLM reduces inference latency by up to 51% and queuing delay by up to 67 %, while incurring at most 8% accuracy loss.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：51%、67 %、8%。
- [DynaNDE: Dynamic Near-Data Expert Scheduling for Batched MoE Inference](https://arxiv.org/abs/2609.00407v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《DynaNDE: Dynamic Near-Data Expert Scheduling for Batched MoE Inference》在 arXiv API 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，Experimental results show that DynaNDE achieves substantial throughput improvements over the state-of-the-art NPU-NDP MoE serving framework, with average speedups of 2.6$\times$ and 2.2$\times$ for the prefill and decoding stages, respectively.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Jailbreaking Text-to-Image Models Through Cracks: Navigating Heterogeneous Safety Filters via Multi-Agent Debate](https://arxiv.org/abs/2609.01168)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Jailbreaking Text-to-Image Models Through Cracks: Navigating Heterogeneous Safety Filters via Multi-Agent Debate》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Extensive experiments across multiple T2I models, datasets, and safety configurations show that CRACK achieves Attack Success Rates (ASR) of up to 99.63\% under composite defenses, while requiring fewer queries than existing methods and maintaining semantic fidelity.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

