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

- 日期: 2026-10-09
- 今日新论文: 15
- 今日新权威来源更新: 1
- 本周精选论文: 25
- 本周精选权威来源更新: 5
- 日报: `papers/2026-10-09.md`
- 周报: `digests/weekly-2026-10-09.md`

## 今日最值得看

- [RaReCache: Bridging the Gap in Cross-Model KV Cache Reuse via Rank disagreement-based Selective Recomputation](https://arxiv.org/abs/2610.11358v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《RaReCache: Bridging the Gap in Cross-Model KV Cache Reuse via Rank disagreement-based Selective Recomputation》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across two model families and five benchmarks, on a 23x parameter gap (Qwen3-0.6B to 14B) recomputing just 30% of positions retains 95-99% of the target accuracy, whereas on a 8.8x gap (Llama3-8B to 70B), recomputing 40% retains 96.5% of the target accuracy.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：23x、30%、99%。
- [SPIN: Shadow Predictive Indexer for Sparse Attention](https://arxiv.org/abs/2610.09025)
  - 主题: Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference，核心内容是《SPIN: Shadow Predictive Indexer for Sparse Attention》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，In end-to-end vLLM serving, SPIN improves output throughput by up to 14.9% and reduces median inter-token latency by up to 13.2%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：14.9%、13.2%、40%。
- [Mooncake: A KVCache-centric Disaggregated Architecture for LLM Serving](https://arxiv.org/abs/2407.00079)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Mooncake: A KVCache-centric Disaggregated Architecture for LLM Serving》在 arXiv cs.DC 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Compared to the baseline method, Mooncake can achieve up to a 525% increase in throughput in certain simulated scenarios while adhering to SLOs.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：525%、75%。
- [Zepp: Accelerating Distributed MoE Serving under Relaxed Balance Constraints](https://arxiv.org/abs/2610.11158)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Zepp: Accelerating Distributed MoE Serving under Relaxed Balance Constraints》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，We implement Zepp and evaluate it against 7 state-of-the-art MoE serving systems, achieving up to 6.68$\times$ MoE layer speedup and a geometric mean speedup of 1.86$\times$ over the fastest competing baseline.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：7 s。
- [Compile the Table: Query-Calibrated Operator Compression for Tabular In-Context Learning](https://arxiv.org/abs/2610.11784)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Compile the Table: Query-Calibrated Operator Compression for Tabular In-Context Learning》在 arXiv cs.LG 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Compressing 8,192 in-context examples to 512 memory slots yields a 10.5x cache compression ratio; excluding one-time compilation, in a single-core CPU online-serving comparison over 1,000 queries, QCOC is up to 508x faster than dynamic retrieval baselines and 1.98x faster than full-context inference.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：10.5x、508x、1.98x。
- [ReCodeAgent: A Multi-agent Workflow for Language-Agnostic Translation and Validation of Large-Scale Repositories](https://arxiv.org/abs/2604.07341)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing，核心内容是《ReCodeAgent: A Multi-agent Workflow for Language-Agnostic Translation and Validation of Large-Scale Repositories》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Our results demonstrate that ReCodeAgent consistently outperforms prior techniques on translation correctness, improving test pass rate by 60.8% on ground-truth tests, with an average cost of $15.3.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：60.8%、40.4%、28%。
- [TokenRouter: Efficient Serving System for Token-Level LLM Routing](https://arxiv.org/abs/2610.12242v1)
  - 主题: Cost-efficient LLM inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、LLM routing，核心内容是《TokenRouter: Efficient Serving System for Token-Level LLM Routing》在 arXiv API 这一方向上的推进。聚焦大模型路由/小模型分流，直接相关。从实验上看，Across diverse routing algorithms, workloads, and model pairs, TokenRouter achieves 2.01-64.15x higher decoding throughput than existing systems, substantially advancing the serving efficiency of token-level LLM routing.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：64.15x。
- [RouterInterp: Understanding Superposed Specialisation in Mixture of Experts Routing](https://arxiv.org/abs/2610.11775)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《RouterInterp: Understanding Superposed Specialisation in Mixture of Experts Routing》在 arXiv cs.CL 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，On gpt-oss-20b, RouterInterp explains expert routing with ${\sim}65\%$ higher detection accuracy than prior token statistics based methods.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Cost-Aware Mixture-of-Experts Coordination for Model Markets](https://arxiv.org/abs/2610.11908)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Cost-Aware Mixture-of-Experts Coordination for Model Markets》在 arXiv cs.LG 这一方向上的推进。强调异构硬件协同推理。从实验上看，Experiments over five random seeds on fifteen tabular and image benchmarks use independently trained and frozen neural and tree-based experts together with latency-derived execution costs.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Humanize: Judgement Engineering for Agentic Coding](https://arxiv.org/abs/2610.08900v2)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing，核心内容是《Humanize: Judgement Engineering for Agentic Coding》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Agentic coding makes code generation cheap, but reliable completion remains difficult: the agent that writes the code is a weak judge of whether it is done.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

