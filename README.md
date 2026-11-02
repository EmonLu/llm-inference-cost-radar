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

- 日期: 2026-11-02
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 2
- 日报: `papers/2026-11-02.md`
- 周报: `digests/weekly-2026-11-02.md`

## 今日最值得看

- [AMMA: A Multi-Chiplet Memory-Centric Architecture for Low-Latency 1M Context Attention Serving](https://arxiv.org/abs/2604.26103)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《AMMA: A Multi-Chiplet Memory-Centric Architecture for Low-Latency 1M Context Attention Serving》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Evaluations show that AMMA achieves 15.5X lower attention latency and 6.9X lower energy consumption compared with the NVIDIA H100.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：15.5X、6.9X。
- [LEAP: Efficient LLM Inference Scheduling with Generalizable Length Prediction](https://arxiv.org/abs/2610.41359v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《LEAP: Efficient LLM Inference Scheduling with Generalizable Length Prediction》在 arXiv API 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Serving experiments show that LEAP reduces average per-token latency by 15.9--40.8\% compared with the evaluated length predictors, while achieving 1.9\% higher throughput with $30{,}569\times$ fewer predictor parameters than the strongest evaluated baseline.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [HiState: Hierarchical Prefix Cache Management for Hybrid LLM Serving in Agentic Workloads](https://arxiv.org/abs/2610.41508)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《HiState: Hierarchical Prefix Cache Management for Hybrid LLM Serving in Agentic Workloads》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On real agent traces, HiState achieves up to 5.73x and 5.44x speedups in p99 TTFT over vLLM-Marconi and SGLang-HiCache, respectively.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：5.73x、5.44x。
- [What We Keep of What We Forget: Replacement Operators and Routing Semantics in Training-Free MoE Expert Pruning](https://arxiv.org/abs/2610.41366)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《What We Keep of What We Forget: Replacement Operators and Routing Semantics in Training-Free MoE Expert Pruning》在 arXiv cs.CL 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，At 50% pruning it adds 1.2-1.8% parameters and gains 3.45 and 1.37 points over the constant on OLMoE and Moonlight, stable across calibration draws and largely unchanged by 4- and 3-bit quantization.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：50%、1.8%、25%。
- [RetryRoute: Retry-Aware Model Routing for Agentic Image Editing Services](https://arxiv.org/abs/2610.41460)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《RetryRoute: Retry-Aware Model Routing for Agentic Image Editing Services》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，We identify sticky failures, meaning that a retry after a failure succeeds only 17-53% as often as a first try across six open models, three benchmarks and two judges.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：53%。
- [Subquadratic Attention with a Hierarchical Tree-Structured Indexer](https://arxiv.org/abs/2610.42112v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《Subquadratic Attention with a Hierarchical Tree-Structured Indexer》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Crucially, by iteratively growing the tree's depth, the total cost including routing and final attention grows sublinearly in sequence length, resulting in overall subquadratic (but superlinear) scaling for attention.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [RecIS: Unifying Sparse and Dense Computation for Efficient Recommendation Training](https://arxiv.org/abs/2610.41457)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《RecIS: Unifying Sparse and Dense Computation for Efficient Recommendation Training》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Compared with PICASSO and TorchRec, RecIS reaches up to $2.62\times$ and $1.15\times$ their throughput, respectively, while reducing step latency by up to 61.5\% and 12.9\%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [GPUSparse: Fast and Exact Learned Sparse Retrieval on a GPU-Resident Inverted Index](https://arxiv.org/abs/2606.26441)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《GPUSparse: Fast and Exact Learned Sparse Retrieval on a GPU-Resident Inverted Index》在 arXiv cs.DC 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，GPUSparse is 5.6x faster than one core and 2.8x slower than a 32-core socket.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：5.6x、2.8x、3.0x。
- [Flide: Accelerating Decision Inference with Exact State Forking](https://arxiv.org/abs/2610.42148v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Flide: Accelerating Decision Inference with Exact State Forking》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，By unifying physical execution throughput with mathematical exactness, Flide establishes a principled foundation for scalable, latency-critical decision intelligence in agent systems.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [ACCT: Asymmetric Cross-LLM Context Transfer](https://arxiv.org/abs/2610.42116v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《ACCT: Asymmetric Cross-LLM Context Transfer》在 arXiv API 这一方向上的推进。强调异构硬件协同推理。从实验上看，Experiments show that ACCT matches or exceeds the target model's original inference performance even when reducing the KV cache size by 75%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：75%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

