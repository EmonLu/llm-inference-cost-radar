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

- 日期: 2026-08-05
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 3
- 日报: `papers/2026-08-05.md`
- 周报: `digests/weekly-2026-08-05.md`

## 今日最值得看

- [Heterogeneous LLM Serving with General-Purpose Processing-Near-Memory for Retrieval-Based Sparse Attention](https://arxiv.org/abs/2608.03555v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Heterogeneous LLM Serving with General-Purpose Processing-Near-Memory for Retrieval-Based Sparse Attention》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across three state-of-the-art models and real agentic traces, our proposed system improves throughput per TDP under a service-level objective by 2.09-6.13x over a GPU-only baseline and runs training-free sparse attention methods with 1.36-3.21x improvements.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：6.13x、3.21x。
- [When Does Disaggregation Pay? Simulating Prefill--Decode--Attention--FFN Specialization for Agentic LLM Inference](https://arxiv.org/abs/2608.03741v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《When Does Disaggregation Pay? Simulating Prefill--Decode--Attention--FFN Specialization for Agentic LLM Inference》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，We also investigate the relationship between model architecture and gain from disaggregation by running a set of ablation studies.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [HERALD: High-Throughput Block Diffusion LLM Serving via CPU-GPU Cooperative KV Cache Retrieval](https://arxiv.org/abs/2606.21633)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《HERALD: High-Throughput Block Diffusion LLM Serving via CPU-GPU Cooperative KV Cache Retrieval》在 arXiv cs.LG 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，On two production block dLLMs, HERALD sustains near-lossless accuracy at a 5% KV budget and reaches up to 2.28x the decode throughput of GPU-only serving, with gains that widen with context length.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：5%、2.28x。
- [Efficiency and Cost Alignment in Batched LLM Serving via Resource-Fair Scheduling](https://arxiv.org/abs/2608.02244)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Efficiency and Cost Alignment in Batched LLM Serving via Resource-Fair Scheduling》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Numerical experiments show that ISJL occupies a favorable middle ground between FCFS, which has large batching externalities, and LJF, which is cost-aligned but sacrifices batching flexibility.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Agentic Coding in the Wild: Characterizing GitHub Copilot Traces at Production Scale](https://arxiv.org/abs/2608.00101)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《Agentic Coding in the Wild: Characterizing GitHub Copilot Traces at Production Scale》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，This structure yields KV cache hit rates averaging 90% within a turn, but falling to 55\% across turn boundaries and drastically invalidated after events like model switches or context compaction.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：90%。
- [ThAME: 3D Memory-Enabled Heterogeneous Accelerator for LLM Mixture of Experts](https://arxiv.org/abs/2607.17074)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《ThAME: 3D Memory-Enabled Heterogeneous Accelerator for LLM Mixture of Experts》在 arXiv cs.DC 这一方向上的推进。强调异构硬件协同推理。从实验上看，Experimental results demonstrate that ThAME outperforms state-of-the-art counterparts by up to 15.7x in terms of speedup and improves energy efficiency by up to 9.8x.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：15.7x、9.8x。
- [TokTier: Exact Stateful CPU+GPU Tokenization for Agentic LLM Serving](https://arxiv.org/abs/2607.29678)
  - 主题: Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Coding agent routing、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《TokTier: Exact Stateful CPU+GPU Tokenization for Agentic LLM Serving》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，At the fleet's 94.1% prompt-cache hit rate approaching 0.99, tokenization grows from 10% to 64% of time to first token.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：94.1%、10%、64%。
- [MoPET: Parameter-Efficient Mixture-of-Experts for Unified Medical Image Classification](https://arxiv.org/abs/2607.29462)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《MoPET: Parameter-Efficient Mixture-of-Experts for Unified Medical Image Classification》在 arXiv cs.LG 这一方向上的推进。强调异构硬件协同推理。从实验上看，Through selected evaluations on the MedMNIST benchmark, we first establish that PEFT outperforms full network updates, improving average accuracy from 86.50% to 88.97%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：86.50%、88.97%、81.58%。
- [The Agent Operating System (AOS): A Reference Operating Architecture for Distributed Agentic Systems](https://arxiv.org/abs/2608.03214v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《The Agent Operating System (AOS): A Reference Operating Architecture for Distributed Agentic Systems》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Platform services, Linux or Windows, container runtimes, and physical infrastructure remain outside the AOS boundary and are integrated through explicit interfaces.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [HorizonServe: Coordinating Request Scheduling with GPU Sharing for Omni-Model Serving](https://arxiv.org/abs/2608.01785)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《HorizonServe: Coordinating Request Scheduling with GPU Sharing for Omni-Model Serving》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Across three omni-model workloads and two GPU platforms, HorizonServe improves SLO attainment by up to 4.9$\times$ in arrival-rate sweeps and 7.0$\times$ under downstream-heavy traffic, and reduces per-class first-response latency by 38.4--63.7\%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

