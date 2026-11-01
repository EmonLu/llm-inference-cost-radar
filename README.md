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

- 日期: 2026-11-01
- 今日新论文: 10
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 2
- 日报: `papers/2026-11-01.md`
- 周报: `digests/weekly-2026-11-01.md`

## 今日最值得看

- [The Price of a Chance in Artificial Societies](https://arxiv.org/abs/2610.40259v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《The Price of a Chance in Artificial Societies》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Further broadening reward coverage yields additional savings but reduces selection quality.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [EpiAgent: Epistemic Self-Play for LLM Agents](https://arxiv.org/abs/2610.40227v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《EpiAgent: Epistemic Self-Play for LLM Agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Empirical results across both mixed and competitive scenarios show that EpiAgent consistently outperforms prompting-based and RL-based baselines.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Don't Lose the Thread: Empowering Long-Horizon LLM Agents with Cognitive Resource Self-Allocation](https://arxiv.org/abs/2610.40350v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《Don't Lose the Thread: Empowering Long-Horizon LLM Agents with Cognitive Resource Self-Allocation》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On the GAIA benchmark, CORAL with an 8B model achieves 42.8% average accuracy, with particularly strong gains on the most challenging long-horizon tasks (Level 2 and Level 3).
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：42.8%。
- [Heterogeneous Co-Evolution Learning for Tool-Efficient Search Agents with Zero Labels](https://arxiv.org/abs/2610.39682v1)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《Heterogeneous Co-Evolution Learning for Tool-Efficient Search Agents with Zero Labels》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experiments on seven general-domain and multi-hop question answering benchmarks demonstrate that \textsc{ZEST-Search} consistently improves search-agent performance while achieving higher tool efficiency without labeled search-training data or expert search trajectories.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Judging Before Propagation: Task-Graph Contextual Integrity for Multi-Agent Privacy](https://arxiv.org/abs/2610.39532v1)
  - 主题: Agent systems and multi-agent efficiency
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency，核心内容是《Judging Before Propagation: Task-Graph Contextual Integrity for Multi-Agent Privacy》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，In our primary experimental configuration, TG-CI reduces the mean unauthorized disclosure count by 85.8-94.1% relative to the Local-History CI baseline, while retaining 93.6-96.1% of the baseline's task accuracy, with the two enforcement policies providing complementary privacy--cost--utility trade-offs.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：94.1%、96.1%。
- [TextSeal2: Distortion-Free LLM Watermarking with Copula Mixing and Memoryless Races](https://arxiv.org/abs/2610.40613v1)
  - 主题: Cost-efficient LLM inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、LLM routing，核心内容是《TextSeal2: Distortion-Free LLM Watermarking with Copula Mixing and Memoryless Races》在 arXiv API 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，It also preserves output diversity and adds no measurable inference latency.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [TokWatt: an open, boundary-annotated database of AI inference energy, from chat answers to agents](https://arxiv.org/abs/2610.39846v1)
  - 主题: Coding agent routing
  - 中文解读: 这项工作主要关注Coding agent routing，核心内容是《TokWatt: an open, boundary-annotated database of AI inference energy, from chat answers to agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Five independent estimates for default production chat systems agree within a factor of 1.8, and the reference values shift by at most 12% under alternative harmonization parameters.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：12%。
- [LLM Agent-Based Design of RISC-V CPUs with FPGA-in-the-Loop Evaluation](https://arxiv.org/abs/2610.39570v1)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《LLM Agent-Based Design of RISC-V CPUs with FPGA-in-the-Loop Evaluation》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，For the same CPU candidate running 8,000 CoreMark iterations, FPGA evaluation, including implementation, was 9.6x faster than single-threaded RTL simulation.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：9.6x。
- [On the Fundamental Limits of Prefill-Based Decoding Length Prediction](https://arxiv.org/abs/2610.40541v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《On the Fundamental Limits of Prefill-Based Decoding Length Prediction》在 arXiv API 这一方向上的推进。它重点讨论系统效率、成本控制或推理路径优化带来的实际价值。从实验上看，We show that current benchmarks conflate predictor quality with task hardness: when the target model, dataset, or sampling configuration changes, reported accuracy collapses even though the predictor is unchanged.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Raincheck: Deferred Multimodal Prefill for Efficient Multi-Turn MLLM Inference](https://arxiv.org/abs/2610.39562v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Raincheck: Deferred Multimodal Prefill for Efficient Multi-Turn MLLM Inference》在 arXiv API 这一方向上的推进。它重点讨论系统效率、成本控制或推理路径优化带来的实际价值。从实验上看，On MultiVerse, the SGLang implementation reduces mean first-turn TTFT by up to 24.1% relative to full prefill, with less than 0.5% increase in mean time per output token (TPOT).
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：24.1%、0.5%、30%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

