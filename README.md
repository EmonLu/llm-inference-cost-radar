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

- 日期: 2026-08-28
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 2
- 日报: `papers/2026-08-28.md`
- 周报: `digests/weekly-2026-08-28.md`

## 今日最值得看

- [VPP: Virtual Pipeline Parallelism for Efficient Chunked Prefill in Long-Context LLM Inference](https://arxiv.org/abs/2608.26523)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《VPP: Virtual Pipeline Parallelism for Efficient Chunked Prefill in Long-Context LLM Inference》在 arXiv cs.DC 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，VPP improves throughput by up to 13.1% over DCPP on long sequences and 6.7% on mixed workloads, while preserving performance on short sequences.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：13.1%、6.7%、6.4%。
- [Characterizing CPU-Induced Slowdowns in Multi-GPU LLM Inference](https://arxiv.org/abs/2603.22774)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Characterizing CPU-Induced Slowdowns in Multi-GPU LLM Inference》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Under moderate serving load, we observe that CPU-starved configurations frequently time out, while providing adequate CPU resources restores responsiveness and reduces time-to-first-token (TTFT) latency by 1.47-7.11x across configurations, all without requiring additional GPUs.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：7.11x。
- [MM-Spectrum: Multimodal Multi-spectral Molecular Structural Elucidation with a Stable MoE Framework](https://arxiv.org/abs/2608.27286v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《MM-Spectrum: Multimodal Multi-spectral Molecular Structural Elucidation with a Stable MoE Framework》在 arXiv API 这一方向上的推进。强调异构硬件协同推理。从实验上看，Across full-modality, bimodal, and missing-modality settings on molecular structural elucidation, MM-Spectrum achieves consistent and substantial improvements, supported by ablation studies and interpretability analyses.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [A Few Pages of Markdown: Committed AI Configuration and Lower Quality Cost after Coding-Agent Adoption](https://arxiv.org/abs/2608.25241v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing，核心内容是《A Few Pages of Markdown: Committed AI Configuration and Lower Quality Cost after Coding-Agent Adoption》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Re-estimating an existing agent-adoption panel within each stratum, agents accelerate development regardless of maturity (28-38% more commits), but quality diverges: among agent-first repositories, where the contrast is identified, those without committed AI configuration show roughly twice the increase in cognitive complexity (+53% versus +27%) and 1.7x the increase in static-analysis warnings.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：38%、53%、27%。
- [AsymSpec: Context-Asymmetric Speculative Decoding for Agentic LLMs](https://arxiv.org/abs/2608.26004v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《AsymSpec: Context-Asymmetric Speculative Decoding for Agentic LLMs》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Evaluated across four agentic capabilities and two end-to-end agent benchmarks, AsymSpec reaches $\approx 90\%$ of full-context accuracy on average, delivering $1.3$--$1.7\times$ throughput speedups at $0.2$--$0.3\times$ the compute cost on isolated text capabilities.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Tunable Tool-Call Rates in LLM Agents via Representation Steering](https://arxiv.org/abs/2608.25198v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Tunable Tool-Call Rates in LLM Agents via Representation Steering》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，With live tool execution, a single sweep of the steering traces a cost/accuracy Pareto frontier and nearly doubles open-domain QA accuracy ($0.29 \!
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [CRAM: Centroid-Routing and Adaptive MoE for Multimodal Continual Instruction Tuning](https://arxiv.org/abs/2606.02502)
  - 主题: Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference、LLM routing，核心内容是《CRAM: Centroid-Routing and Adaptive MoE for Multimodal Continual Instruction Tuning》在 arXiv cs.CL 这一方向上的推进。强调异构硬件协同推理。从实验上看，Extensive experiments across diverse benchmarks demonstrate its superiority over existing methods.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Routed Graph Handoff: Adaptive Format Selection for Multi-Agent LLM Delegation](https://arxiv.org/abs/2608.25277v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、LLM routing，核心内容是《Routed Graph Handoff: Adaptive Format Selection for Multi-Agent LLM Delegation》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Replacing these with structured graphs reduces cost but fails on tasks requiring adaptive reasoning.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Meta-Learning Where to Allocate Experts: Task-Conditioned Layer-Wise Compression for MoEs](https://arxiv.org/abs/2608.26650)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Meta-Learning Where to Allocate Experts: Task-Conditioned Layer-Wise Compression for MoEs》在 arXiv cs.CL 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，Relative to fixed k=6, a conservative setting activates 3.61 experts on average (40% fewer) and achieves comparable MMLU accuracy (0.489 vs.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：40%、62%。
- [A Unified Framework for Fair and Personalized Decentralized Learning under Communication Constraints](https://arxiv.org/abs/2608.26493)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《A Unified Framework for Fair and Personalized Decentralized Learning under Communication Constraints》在 arXiv cs.LG 这一方向上的推进。强调异构硬件协同推理。从实验上看，Experiments on CIFAR-10 and the real heterogeneous MUSMET EEG dataset demonstrate that DMFL-SQ substantially reduces communication while maintaining predictive performance and improving fairness across clients.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

