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

- 日期: 2026-10-16
- 今日新论文: 15
- 今日新权威来源更新: 5
- 本周精选论文: 25
- 本周精选权威来源更新: 8
- 日报: `papers/2026-10-16.md`
- 周报: `digests/weekly-2026-10-16.md`

## 今日最值得看

- [When the KV Cache Is Slower Than the GPU: Scaling Remote KV Tiers for Context-Parallel Prefill](https://arxiv.org/abs/2610.21500)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《When the KV Cache Is Slower Than the GPU: Scaling Remote KV Tiers for Context-Parallel Prefill》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Replaying a production request stream on an isolated engine, we find that a remote hit took 0.88 s against 0.31 s to recompute the prompt, and that synchronous loading turned a hit-heavy stream into an unstable queue: p99 83.32 s with the GPUs 7% busy.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：0.88 s、0.31 s、83.32 s。
- [PrefixFlow: Training-Time KV Caching for Schedule-Level Prefix Reuse in LLM RL Training](https://arxiv.org/abs/2606.01143)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《PrefixFlow: Training-Time KV Caching for Schedule-Level Prefix Reuse in LLM RL Training》在 arXiv cs.DC 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，In controlled sweeps, actor-side speedup grows with prefix ratio and group size, reaching $4.4\times$ at an 83% prefix ratio, while suffix-dominated splits gain little; offloading dormant prefix activations lowers Phase-B peak HBM by up to 59% and extends trainable sequences by $1.66\times$.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：83%、59%。
- [From Long Context to Selective Memory:A Survey of Memory-Centric Compression for Large Language Models](https://arxiv.org/abs/2610.21165v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《From Long Context to Selective Memory:A Survey of Memory-Centric Compression for Large Language Models》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，We further summarize evaluation dimensions, benchmark gaps, and open challenges, and argue that future research should move from static, pointwise compression toward dynamic, governable, lifecycle-aware memory management.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [PriorityFEC: Deadline-Aware Streaming FEC for KV-Cache Handoff in Edge Multi-Agent Systems](https://arxiv.org/abs/2610.21390v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《PriorityFEC: Deadline-Aware Streaming FEC for KV-Cache Handoff in Edge Multi-Agent Systems》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Multi-agent large language model (LLM) systems are increasingly deployed at the edge to support complex tasks that require collaboration and information exchange among multiple agents.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Exact Makespan Bounds and the GPipe Homogeneity Bias for Heterogeneous LLM Inference Pipelines](https://arxiv.org/abs/2610.21815)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Exact Makespan Bounds and the GPipe Homogeneity Bias for Heterogeneous LLM Inference Pipelines》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，These results quantify the GPipe overestimate, decompose the bias into a homogeneity term Sum_j (tau_max - tau_j) and a communication-ignoring term Sum_j d_j, and imply that balancing per-stage compute dominates communication reduction for steady-state throughput.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [RouteWeaver: Weaving Mode Selection and Execution into Unified LLM Routing](https://arxiv.org/abs/2610.19705v2)
  - 主题: Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference、LLM routing，核心内容是《RouteWeaver: Weaving Mode Selection and Execution into Unified LLM Routing》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，RouteWeaver achieves an average accuracy of 61.4%, an 11.03% relative improvement over the strongest baseline, and outperforms all compared baselines in each of the five domains.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：61.4%、11.03%。
- [Mind the Delay: Latency-aware Query Routing for Heterogeneous LLM pools](https://arxiv.org/abs/2607.18253)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Mind the Delay: Latency-aware Query Routing for Heterogeneous LLM pools》在 arXiv cs.AI 这一方向上的推进。强调异构硬件协同推理。从实验上看，Against seven baselines, BEAR improves the utility of responses delivered within their targets by 63% on average over existing latency-aware routers, and by 30.5% over the best baseline at each arrival rate.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：63%、30.5%、5%。
- [SCARCE: Emergent Institutions in Long-Horizon Multi-Agent Coding Systems](https://arxiv.org/abs/2610.21029v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing，核心内容是《SCARCE: Emergent Institutions in Long-Horizon Multi-Agent Coding Systems》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Yet prior studies of agent negotiation often use stylized games and simulated bargaining, leaving open how these behaviors develop during sustained, long-horizon tasks.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [ZenFlow: Enabling Stall-Free Offloading for LLM Training](https://arxiv.org/abs/2505.12242)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《ZenFlow: Enabling Stall-Free Offloading for LLM Training》在 arXiv cs.DC 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Evaluation shows that ZenFlow achieves up to 5x end-to-end speedup, 2x lower PCIe traffic, 85% less GPU stalls, and up to 72% lower cloud GPU cost, all while preserving accuracy.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：5x、2x、85%。
- [Architecting for Hardware Diversity: Meta's End-to-End Co-Design for High-Performance AI Training on AMD GPUs](https://arxiv.org/abs/2610.22230)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Architecting for Hardware Diversity: Meta's End-to-End Co-Design for High-Performance AI Training on AMD GPUs》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Compared to the directly ported baseline, these methods deliver up to 1.5x improvement in end-to-end training throughput.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.5x、350X。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

