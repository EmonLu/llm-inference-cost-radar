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

- 日期: 2026-07-05
- 今日新论文: 5
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 2
- 日报: `papers/2026-07-05.md`
- 周报: `digests/weekly-2026-07-05.md`

## 今日最值得看

- [ContextSniper: AntTrail's Token-Efficient Code Memory for Repository-Level Program Repair](https://arxiv.org/abs/2607.01916v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《ContextSniper: AntTrail's Token-Efficient Code Memory for Repository-Level Program Repair》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，ContextSniper reduces total token use by 51.5% and logged cost by 36.4% for OpenClaw, and reduces total token use by 38.9% and estimated cost by 27.3% for Claude Code.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：51.5%、36.4%、38.9%。
- [Reasoning effort, not tool access, buys first-try reliability in agentic code generation: an observational study](https://arxiv.org/abs/2607.02436v1)
  - 主题: Coding agent routing, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Coding agent routing、Cost-efficient LLM inference，核心内容是《Reasoning effort, not tool access, buys first-try reliability in agentic code generation: an observational study》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Capability tier dominated: frontier models clustered near the ceiling while a low cost local model fell to 24 to 37 points.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [TestEvo-Bench: An Executable and Live Benchmark for Test and Code Co-Evolution](https://arxiv.org/abs/2607.02469v1)
  - 主题: Coding agent routing
  - 中文解读: 这项工作主要关注Coding agent routing，核心内容是《TestEvo-Bench: An Executable and Live Benchmark for Test and Code Co-Evolution》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Results show that they achieve up to 77.5% success rate on test generation and 74.6% on test update.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：77.5%、74.6%。
- [PACE: A Proxy for Agentic Capability Evaluation](https://arxiv.org/abs/2607.02032v1)
  - 主题: Agent systems and multi-agent efficiency, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、LLM routing，核心内容是《PACE: A Proxy for Agentic Capability Evaluation》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experiments across 14 models, 4 agentic benchmarks, and 19 non-agentic benchmarks show that PACE-Bench predicts agentic scores with leave-one-out cross-validation (LOOCV) mean absolute error (MAE) under 4%, Spearman correlation above 0.80, and pairwise model-ranking accuracy around 85%, all at much less than 1% of the full agentic evaluation cost.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：4%、85%、1%。
- [SkillCoach: Self-Evolving Rubrics for Evaluating and Enhancing Agentic Skill-Use](https://arxiv.org/abs/2607.01874v1)
  - 主题: Agent systems and multi-agent efficiency
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency，核心内容是《SkillCoach: Self-Evolving Rubrics for Evaluating and Enhancing Agentic Skill-Use》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experiments show that evolved rubrics substantially improve evaluation quality, expose failures hidden by final accuracy, and provide stronger supervision signals than outcome-only filtering for enhancing agentic skill-use.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

