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

- 日期: 2026-11-25
- 今日新论文: 15
- 今日新权威来源更新: 1
- 本周精选论文: 25
- 本周精选权威来源更新: 4
- 日报: `papers/2026-11-25.md`
- 周报: `digests/weekly-2026-11-25.md`

## 今日最值得看

- [RankServe: Rank-Aware CPU-GPU Scheduling for Memory-Constrained MoE Serving](https://arxiv.org/abs/2611.31869v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《RankServe: Rank-Aware CPU-GPU Scheduling for Memory-Constrained MoE Serving》在 arXiv API 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Implemented on vLLM, RankServe is evaluated on three MoE models against six serving systems on a single CPU-GPU platform.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [LoomKV: Lossless KV Cache Compression from GPU Memory to SSD for LLM Serving](https://arxiv.org/abs/2611.32954v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《LoomKV: Lossless KV Cache Compression from GPU Memory to SSD for LLM Serving》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Where raw capacity suffices, compression costs at most 2.2% throughput; tier mode is bit-exact with raw tiers, and pool mode matches FlashAttention-3's numerical accuracy.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：2.2%、1.4x、3.6x。
- [Breaking Routing And Inter-device Dependencies in Mixture-of-Experts](https://arxiv.org/abs/2611.32572v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Breaking Routing And Inter-device Dependencies in Mixture-of-Experts》在 arXiv API 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，On Qwen3-shaped MoEs with 0.4B-A0.1B and 2.5B-A0.5B parameters, BRAID closely matches sequential training at matched compute, with validation-loss increases of only 1% and 0.5%, respectively.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1%、0.5%。
- [The Control-Flow Tax: Specialized Decision Routing for LLM Agent Workflows](https://arxiv.org/abs/2611.32365v1)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference、LLM routing，核心内容是《The Control-Flow Tax: Specialized Decision Routing for LLM Agent Workflows》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across three further tasks, cost reductions are 40.5% to 42.9% and concurrent elapsed-time reductions are 12.9% to 14.4%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：40.5%、42.9%、12.9%。
- [Mayfly: Lifecycle-Aware High-Bandwidth Flash for Recursive Self-Improvement](https://arxiv.org/abs/2611.32264v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Mayfly: Lifecycle-Aware High-Bandwidth Flash for Recursive Self-Improvement》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experimental results show that, at 128 sessions per generation on four added HBF sites, Mayfly finishes 34% sooner than parking the same KV on HBF and 23% sooner than reading it from HBF whenever HBM is full; its gain over parking grows with concurrency, to 55% at 256 sessions on eight sites.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：128 s、34%、23%。
- [From Rule-based to Agentic: LLM Agent based Real-time Control of Urban Drainage Systems for Flooding and Sewer Overflow Mitigation](https://arxiv.org/abs/2611.32046v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《From Rule-based to Agentic: LLM Agent based Real-time Control of Urban Drainage Systems for Flooding and Sewer Overflow Mitigation》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Validated via simulation studies of a combined sewer catchment in eastern China across 10 real-world rainfall events, the AgenticAI-Control achieved 69.1-90.6% reduction in aggregated flood and overflow volumes compared to the rule-based baseline control.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：90.6%。
- [Norn: Context-Length-Aware Optimization of Weight and KV Cache Placement for Offloaded LLM Inference](https://arxiv.org/abs/2611.32295v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Norn: Context-Length-Aware Optimization of Weight and KV Cache Placement for Offloaded LLM Inference》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Experiments with Qwen3-14B and Qwen3-32B on two single-GPU systems show up to a 16.8$\times$ speedup in end-to-end latency over Pipelined Sharding and a 4.2$\times$ speedup over its oracle variant with known input and output lengths.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Fix How It Acts, Not How It Thinks: Surgical Fine-Tuning of Frontier LLMs](https://arxiv.org/abs/2611.32064v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《Fix How It Acts, Not How It Thinks: Surgical Fine-Tuning of Frontier LLMs》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，When the same adapter is merged into the mixed FP8/NVFP4 release of the same model, 93% of the update disappears.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：93%、1.5%。
- [RePrism: Joint Request and Representation Scheduling for LLM Agent Serving](https://arxiv.org/abs/2611.32545v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《RePrism: Joint Request and Representation Scheduling for LLM Agent Serving》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On a controlled workload, RePrism's joint scoring achieves 2.7% higher request throughput and 12.3% lower mean SCT than a policy that ranks requests before selecting their representations.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：2.7%、12.3%。
- [GreenDynaMix: Thermal-Aware Dynamic Mixed-Precision MoE LLM Inference Systems](https://arxiv.org/abs/2611.31737v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《GreenDynaMix: Thermal-Aware Dynamic Mixed-Precision MoE LLM Inference Systems》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Experiments on server, desktop, and embedded platforms demonstrate that GreenDynaMix reduces the temperature-induced aging rate of GPUs during LLM inference by 25-33%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：33%、1.6%、9.4%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

