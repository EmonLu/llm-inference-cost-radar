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

- 日期: 2026-11-08
- 今日新论文: 6
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 4
- 日报: `papers/2026-11-08.md`
- 周报: `digests/weekly-2026-11-08.md`

## 今日最值得看

- [An Agent-Driven, Cross-Validated Inverse-Design Pipeline for Dielectric Metasurfaces](https://arxiv.org/abs/2611.08127v1)
  - 主题: Coding agent routing
  - 中文解读: 这项工作主要关注Coding agent routing，核心内容是《An Agent-Driven, Cross-Validated Inverse-Design Pipeline for Dielectric Metasurfaces》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，In the other cases, instead, the obtained RCWA results are confirmed by full-wave simulations.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [SwarmEvolve: Latent Agent Swarms for Evolutionary Discovery and Optimization](https://arxiv.org/abs/2611.08483v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《SwarmEvolve: Latent Agent Swarms for Evolutionary Discovery and Optimization》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On several problems, SwarmEvolve with Qwen3 8B improves on the solutions that AlphaEvolve first found with frontier LLMs.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Benchmarks as Software: Terminal-Bench and the Case for Continuous Benchmarks](https://arxiv.org/abs/2611.08417v1)
  - 主题: Coding agent routing
  - 中文解读: 这项工作主要关注Coding agent routing，核心内容是《Benchmarks as Software: Terminal-Bench and the Case for Continuous Benchmarks》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Our audit identifies issues in roughly 30% of the benchmark, and we release the resulting repairs as Terminal-Bench 2.1.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：30%。
- [PCBRouteAgent: How Close Are LLM Agents to Becoming PCB Routing Engineers?](https://arxiv.org/abs/2611.08175v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、LLM routing，核心内容是《PCBRouteAgent: How Close Are LLM Agents to Becoming PCB Routing Engineers?》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，It achieves clean-pass rates of 100%, 94.9%, 100%, and 40% on D2, D3-A, D3-B, and D3-C, respectively.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：100%、94.9%。
- [Who Should Know What? Empirical Information Design for Multi-Agent LLM Economies](https://arxiv.org/abs/2611.07667v1)
  - 主题: Agent systems and multi-agent efficiency
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency，核心内容是《Who Should Know What? Empirical Information Design for Multi-Agent LLM Economies》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，In trade, revealing exact valuations rather than ordinal preference rankings reduces realized gains for GPT-6 Sol (from 98% to 91% of maximum) yet increases them for Claude Sonnet 5 (from 72% to 86%).
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：6 S、98%、91%。
- [Towards Foundation Decision Models: Drex](https://arxiv.org/abs/2611.07854v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《Towards Foundation Decision Models: Drex》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Max answers a typical request in 183 ms, against about 2.0 s for GPT-6 Sol and 3.5 s for Claude Opus 5.5, and its outputs are stable under option reordering.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：183 ms、2.0 s、6 S。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

