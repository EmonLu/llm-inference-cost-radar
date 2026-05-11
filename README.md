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

- 日期: 2026-05-11
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 2
- 日报: `papers/2026-05-11.md`
- 周报: `digests/weekly-2026-05-11.md`

## 今日最值得看

- [Tackling the Data-Parallel Load Balancing Bottleneck in LLM Serving: Practical Online Routing at Scale](https://arxiv.org/abs/2605.06113)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Tackling the Data-Parallel Load Balancing Bottleneck in LLM Serving: Practical Online Routing at Scale》在 arXiv cs.DC 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，Across both workloads, BalanceRoute substantially reduces average DP imbalance and improves end-to-end serving throughput.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Relay Buffer Independent Communication over Pooled HBM for Efficient MoE Inference on Ascend](https://arxiv.org/abs/2605.06055)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Relay Buffer Independent Communication over Pooled HBM for Efficient MoE Inference on Ascend》在 arXiv cs.DC 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，Experiments on Ascend-based MoE workloads show reduced dispatch and combine latency in both settings.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Star Elastic: Many-in-One Reasoning LLMs with Efficient Budget Control](https://arxiv.org/abs/2605.07182)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Star Elastic: Many-in-One Reasoning LLMs with Efficient Budget Control》在 arXiv cs.LG 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，Crucially, elastic budget control advances the accuracy-latency Pareto frontier, achieving up to 16% higher accuracy and 1.9x lower latency via dynamic per-phase model selection.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：16%、1.9x、360x。
- [An Efficient Hybrid Sparse Attention with CPU-GPU Parallelism for Long-Context Inference](https://arxiv.org/abs/2605.07719)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《An Efficient Hybrid Sparse Attention with CPU-GPU Parallelism for Long-Context Inference》在 arXiv cs.LG 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Across 2 models, 3 benchmarks, and 40 tasks, Fluxion preserves quality well -- the worst average degradation is only -0.26 relative to FULL, while delivering 1.5$\times$-3.7$\times$ speedup over the strongest fixed sparse hybrid baseline, whose KV budget is only 0.05.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Deadline-Driven Hierarchical Agentic Resource Sharing for AI Services and RAN Functions in AI-RAN](https://arxiv.org/abs/2605.07547)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《Deadline-Driven Hierarchical Agentic Resource Sharing for AI Services and RAN Functions in AI-RAN》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experimental results show that HAF reaches 90.0% overall SLO fulfillment, a 20.5% improvement over the strongest baseline, and raises AI service request fulfillment from 51% to 85.3%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：90.0%、20.5%、51%。
- [KV Cache Offloading for Context-Intensive Tasks](https://arxiv.org/abs/2604.08426)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《KV Cache Offloading for Context-Intensive Tasks》在 arXiv cs.CL 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，Recently, KV-cache offloading has emerged as a promising approach to reduce memory footprint and inference latency while preserving accuracy.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Regulating Branch Parallelism in LLM Serving](https://arxiv.org/abs/2605.06914)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Regulating Branch Parallelism in LLM Serving》在 arXiv cs.DC 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，On Qwen3-32B, TAPER improves goodput by $1.77\times$ over IRP-Off and by $1.48\times$ over IRP-Eager, while maintaining over $95\%$ SLO attainment.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Switchcraft: AI Model Router for Agentic Tool Calling](https://arxiv.org/abs/2605.07112)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、LLM routing，核心内容是《Switchcraft: AI Model Router for Agentic Tool Calling》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Switchcraft achieves 82.9% accuracy -- matching or exceeding the best individual model -- while reducing inference cost by 84%, saving over $3,600 per million queries.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：82.9%、84%。
- [SparseRL-Sync: Lossless Weight Synchronization with ~100x Less Communication](https://arxiv.org/abs/2605.07330)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《SparseRL-Sync: Lossless Weight Synchronization with ~100x Less Communication》在 arXiv cs.DC 这一方向上的推进。强调异构硬件协同推理。从实验上看，Under a simplified cost model, sparse synchronization reduces the per-update communication volume from S to approximately S/X; with 99% sparsity (X ~ 100), this yields about a 100x reduction in transmitted data.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：99%、100x。
- [FATE: Future-State-Aware Scheduling for Heterogeneous LLM Workflows](https://arxiv.org/abs/2605.07238)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《FATE: Future-State-Aware Scheduling for Heterogeneous LLM Workflows》在 arXiv cs.DC 这一方向上的推进。强调异构硬件协同推理。从实验上看，On the real-DAG benchmark, it achieves normalized makespan and normalized P95 latency of 0.675 and 0.677, reducing them by 32.5% and 32.3% over RoundRobin and by 8.9% and 8.8% over the strongest non-FATE baseline.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：32.5%、32.3%、8.9%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

