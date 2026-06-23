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

- 日期: 2026-06-23
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 3
- 日报: `papers/2026-06-23.md`
- 周报: `digests/weekly-2026-06-23.md`

## 今日最值得看

- [ASAP: A Disaggregated and Asynchronous Inference System for MoE Prefill](https://arxiv.org/abs/2606.22541v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《ASAP: A Disaggregated and Asynchronous Inference System for MoE Prefill》在 arXiv API 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，We implement and evaluate ASAP on CloudMatrix384 super-nodes, demonstrating that it improves SLO-compliant prefill throughput by 90% compared to state-of-the-art synchronous serving solutions.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：384 s、90%。
- [RLM-Cascade: Response-Level Speculative Decoding for Cost-Efficient LLM API Serving](https://arxiv.org/abs/2606.22840v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《RLM-Cascade: Response-Level Speculative Decoding for Cost-Efficient LLM API Serving》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On a real-world agentic coding workload (Claude Code), RLM-Cascade achieves a draft-use rate of 88.8% across 125 production requests, reducing API cost by 45.8% relative to a direct Opus baseline.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：88.8%、45.8%、026 ms。
- [Concordia: JIT-Compiled Persistent-Kernel Checkpointing for Fault-Tolerant LLM Inference](https://arxiv.org/abs/2606.23521v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Concordia: JIT-Compiled Persistent-Kernel Checkpointing for Fault-Tolerant LLM Inference》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The persistent kernel consumes a lock-free ring buffer of compute, checkpoint, append-log, and recovery tasks, so the same always-on executor triggers dirty-page detection, stages deltas, and appends committed records to a CPU-visible log in CXL memory or host DRAM.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Does the Same Token Mean the Same State? MoE Routing as Signal for Reasoning Control](https://arxiv.org/abs/2606.22798v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Does the Same Token Mean the Same State? MoE Routing as Signal for Reasoning Control》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Its value is the interface: the same selector gives direct pass@1 on code, where exact-string voting is ill-defined, and the same routing-density principle, re-anchored to the agentic boundary, improves best-of-16 patch selection on SWE-bench Verified over random, where patches have no answer string to vote on.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Hypothesis-Driven Skill Optimization for LLM Agents](https://arxiv.org/abs/2606.22330v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Hypothesis-Driven Skill Optimization for LLM Agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Under 20% randomly flipped success/failure feedback during skill discovery and validation, HDSO preserves a +7.1-point gain for Qwen3-8B.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：20%。
- [SCENIC: Semantic-Conditioned Edge-Aware Neural Framework for Structured IoT Command Generation](https://arxiv.org/abs/2606.22296v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《SCENIC: Semantic-Conditioned Edge-Aware Neural Framework for Structured IoT Command Generation》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，TensorRT profiling of the NVIDIA 2:4 sparse encoder export further shows up to 1.8x encoder-component speedup, indicating that the selected encoder-decoder deployment path can retain structured command accuracy under edge-oriented compression while hardware acceleration evidence remains component-level.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：4 s、1.8x、91.0%。
- [Agent-as-a-Router: Agentic Model Routing for Coding Tasks](https://arxiv.org/abs/2606.22902v1)
  - 主题: Agent systems and multi-agent efficiency, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、LLM routing，核心内容是《Agent-as-a-Router: Agentic Model Routing for Coding Tasks》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，However, we identify the performance bottleneck for these routers as information deficit: simply augmenting a vanilla LLM router with performance statistics at the task-dimension level yields a 15.3% relative gain, surpassing a heuristic router built on the same dimension-level priors.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：15.3%。
- [From RAN Control to Agentic Intelligence: Architecture and Vision for Energy Efficient AI-RAN](https://arxiv.org/abs/2606.21955v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《From RAN Control to Agentic Intelligence: Architecture and Vision for Energy Efficient AI-RAN》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Through representative AI-for-RAN and AI-on-RAN use cases, we show how such coordination can improve resource efficiency and reduce operational energy consumption, paving the way toward sustainable 6G networks.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Revelio: Cost-Efficient Agentic Memory Safety Vulnerability Detection For Repository-Scale Codebases](https://arxiv.org/abs/2606.22263v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《Revelio: Cost-Efficient Agentic Memory Safety Vulnerability Detection For Repository-Scale Codebases》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On benchmarks, Revelio outperformed frontier coding agents across diverse backbone models at comparable token costs.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [StickyInvoc: Rethinking Task Models for High-throughput Workflows in the LLM Era](https://arxiv.org/abs/2606.22175v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《StickyInvoc: Rethinking Task Models for High-throughput Workflows in the LLM Era》在 arXiv API 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Our evaluation shows that when rewritten in the StickyInvoc paradigm, a claim verification workflow consisting of 150k inferences achieves a 3.6x speedup on a stable testbed with 20 GPUs, and completes in just 784 seconds by incrementally scaling out to 186 otherwise idle GPUs.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：3.6x、784 s。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

