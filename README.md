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

- 日期: 2026-06-02
- 今日新论文: 15
- 今日新权威来源更新: 1
- 本周精选论文: 25
- 本周精选权威来源更新: 9
- 日报: `papers/2026-06-02.md`
- 周报: `digests/weekly-2026-06-02.md`

## 今日最值得看

- [Idleness is Relative: Exploiting Tool-Call Idle Windows for Offloading in Agentic Systems with MORI](https://arxiv.org/abs/2606.00866v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《Idleness is Relative: Exploiting Tool-Call Idle Windows for Offloading in Agentic Systems with MORI》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Evaluated on real coding agent workloads collected from Claude Code across four GPU and model pairs, MORI delivers 20--71% higher throughput and 18--43% lower TTFT than the best baseline with offloading.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：71%、43%。
- [Observation, Not Prediction: Conversation-Level Disaggregated Scheduling for Agentic Serving](https://arxiv.org/abs/2606.01839)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Observation, Not Prediction: Conversation-Level Disaggregated Scheduling for Agentic Serving》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Against a per-turn prediction baseline, ConServe reduces p95 time-to-first-effective-token (the latency of a conversation's first user-visible output) by 51.08% and improves energy efficiency by 7.51% while preserving last-turn TBT and SLOs; mapping the two phases onto heterogeneous GPU tiers adds a further 22.75% in energy efficiency.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：51.08%、7.51%、22.75%。
- [Skill-Based Mixture-of-Experts: Adaptive Routing for Heterogeneous Reasoning via Inferred Skills](https://arxiv.org/abs/2503.05641)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference、LLM routing，核心内容是《Skill-Based Mixture-of-Experts: Adaptive Routing for Heterogeneous Reasoning via Inferred Skills》在 arXiv cs.CL 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across diverse benchmarks (MMLU-Pro, GPQA, AIME, and MedMCQA), Skill-MoE achieves an average absolute improvement of 8.15% over the best baseline.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：8.15%。
- [DuetServe: Harmonizing Prefill and Decode for LLM Serving via Adaptive GPU Multiplexing](https://arxiv.org/abs/2511.04791)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《DuetServe: Harmonizing Prefill and Decode for LLM Serving via Adaptive GPU Multiplexing》在 arXiv cs.LG 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Evaluations show that DuetServe improves total throughput by up to 1.3x while maintaining low generation latency compared to state-of-the-art frameworks.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.3x。
- [SparseX: Efficient Segment-Level KV Cache Sharing for Interleaved LLM Serving](https://arxiv.org/abs/2606.01751v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《SparseX: Efficient Segment-Level KV Cache Sharing for Interleaved LLM Serving》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，In long-context LLM serving, the prefill stage often dominates time-to-first-token and computational cost.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Lodestar: An Online-Learning LLM Inference Router](https://arxiv.org/abs/2606.00946)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Lodestar: An Online-Learning LLM Inference Router》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，With continuous online adaptation to changing workloads and infrastructure conditions, Lodestar achieves 1.41x lower average TTFT and 1.47x lower P99 TTFT on average (up to 2.15x/1.86x on homogeneous and 4.38x/4.42x on heterogeneous clusters) compared to a state-of-the-art prefix cache and load-aware heuristic, and learns these efficient routing strategies within about 5 minutes, based on experiments in a public cloud GPU cluster.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.41x、1.47x、2.15x。
- [BitsMoE: Efficient Spectral Energy-Guided Bit Allocation for MoE LLM Quantization](https://arxiv.org/abs/2606.00079)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《BitsMoE: Efficient Spectral Energy-Guided Bit Allocation for MoE LLM Quantization》在 arXiv cs.LG 这一方向上的推进。强调异构硬件协同推理。从实验上看，Experiments across multiple MoE LLMs show that BitsMoE substantially reduces downstream task accuracy degradation in ultra-low-bit regimes.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [MAVEN-T: Reinforced Heterogeneous Distillation for Real-Time Multi-Agent Trajectory Prediction](https://arxiv.org/abs/2604.10169)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《MAVEN-T: Reinforced Heterogeneous Distillation for Real-Time Multi-Agent Trajectory Prediction》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experiments on NGSIM, HighD, MoCAD, Argoverse~2, and the Waymo Open Motion Dataset evaluate accuracy, efficiency, generalization, robustness, and closed-loop safety.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [ViBE: Co-Optimizing Workload Skew and Hardware Variability for MoE Serving](https://arxiv.org/abs/2606.00735)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《ViBE: Co-Optimizing Workload Skew and Hardware Variability for MoE Serving》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Results show that ViBE consistently reduces execution-time imbalance and improves SLO attainment by 14%, while lowering P90 TTFT by up to 45%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：14%、45%。
- [HyperParallel-MoE: Multi-Core Interleaved Scheduling for Fast MoE Training on Ascend NPUs](https://arxiv.org/abs/2605.23764)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《HyperParallel-MoE: Multi-Core Interleaved Scheduling for Fast MoE Training on Ascend NPUs》在 arXiv cs.DC 这一方向上的推进。强调异构硬件协同推理。从实验上看，Across multiple expert-parallel configurations, HyperParallel-MoE reduces Dispatch-to-Combine MoE-FFN latency by up to 1.58x, demonstrating that tile-level heterogeneous scheduling can substantially improve MoE training efficiency on modern NPUs.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.58x。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

