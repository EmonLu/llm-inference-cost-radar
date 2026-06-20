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

- 日期: 2026-06-20
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 4
- 日报: `papers/2026-06-20.md`
- 周报: `digests/weekly-2026-06-20.md`

## 今日最值得看

- [RouteJudge: An Open Platform for Reproducible and Preference-Aware LLM Routing](https://arxiv.org/abs/2606.18774v1)
  - 主题: Cost-efficient LLM inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、LLM routing，核心内容是《RouteJudge: An Open Platform for Reproducible and Preference-Aware LLM Routing》在 arXiv API 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，Each evaluation record stores the query, routing decisions, model responses, preference labels, cost, latency, and task metadata, enabling preference-aware, cost-aware, and task-conditioned analysis of LLM routers.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [ReMP: Low-Downtime Runtime Model-Parallelism Reconfiguration for LLM Serving](https://arxiv.org/abs/2606.18741v1)
  - 主题: Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference，核心内容是《ReMP: Low-Downtime Runtime Model-Parallelism Reconfiguration for LLM Serving》在 arXiv API 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，Moreover, ReMP significantly outperforms fixed configurations under dynamic workloads, delivering superior performance in terms of TTFT, TPOT, and output throughput.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：7 s。
- [AgentFinVQA: A Deployable Multi-Agent Pipeline for Auditable Financial Chart QA](https://arxiv.org/abs/2606.19782)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、LLM routing，核心内容是《AgentFinVQA: A Deployable Multi-Agent Pipeline for Auditable Financial Chart QA》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On FinMME, AgentFinVQA improves $+7.68$ pp over a primary-backbone matched zero-shot baseline with a proprietary backbone (Gemini-3 Flash; 71.24% vs.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：71.24%、55.6%。
- [Cost-Optimal LLM Routing with Limited User Feedback under User Satisfaction Guarantees](https://arxiv.org/abs/2606.19376)
  - 主题: Cost-efficient LLM inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、LLM routing，核心内容是《Cost-Optimal LLM Routing with Limited User Feedback under User Satisfaction Guarantees》在 arXiv cs.AI 这一方向上的推进。聚焦大模型路由/小模型分流，直接相关。从实验上看，Experiments across a wide range of LLM benchmarks show that SLARouter satisfies SLA constraints without the need for per-benchmark tuning, reducing operating cost by up to 2.2x over existing baselines.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：2.2x。
- [ViCoStream: Streaming VideoLLMs Can Run Beyond 100 FPS with Stage-Wise Coordinated Inference](https://arxiv.org/abs/2606.19849v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《ViCoStream: Streaming VideoLLMs Can Run Beyond 100 FPS with Stage-Wise Coordinated Inference》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Experiments with Qwen2.5-VL-3B/7B-Instruct across multiple streaming benchmarks show that ViCoStream achieves 134 FPS video throughput and less than 50 ms TTFT on a single A100 GPU while maintaining accuracy close to full-history baselines.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：50 ms。
- [Autonomous Event-Driven Multi-Agent Orchestration for Enterprise AI at Scale](https://arxiv.org/abs/2606.20058)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《Autonomous Event-Driven Multi-Agent Orchestration for Enterprise AI at Scale》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The Task Manager reduces high-priority queue latency by 14-75% and improves related-event correctness by over 20 percentage points at enterprise scale.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：75%。
- [Where to Place the Query? Unveiling and Mitigating Positional Bias in In-Context Learning for Diffusion LLMs via Decoding Dynamics](https://arxiv.org/abs/2606.19349)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Where to Place the Query? Unveiling and Mitigating Positional Bias in In-Context Learning for Diffusion LLMs via Decoding Dynamics》在 arXiv cs.AI 这一方向上的推进。强调异构硬件协同推理。从实验上看，arXiv:2606.19349v1 Announce Type: cross Abstract: While In-Context Learning (ICL) is extensively studied in Autoregressive (AR) LLMs, its mechanism within Diffusion Large Language Models (dLLMs) remains largely unexplored.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Dual-Agent Framework for Cross-Model Verified Translation of Natural-Language Protocols into Robotic Laboratory Platform](https://arxiv.org/abs/2606.20120v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Dual-Agent Framework for Cross-Model Verified Translation of Natural-Language Protocols into Robotic Laboratory Platform》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The accuracy-latency trade-off is further verified by comparing the rule-based mapping of the proposed framework with LLM end-to-end direct mapping.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [DynAMO:Dynamic Asset Management Orchestration via Topological Multi-Agent Scheduling](https://arxiv.org/abs/2606.19382)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《DynAMO:Dynamic Asset Management Orchestration via Topological Multi-Agent Scheduling》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，After instrumenting external tool calls with realistic latencies, a latency decomposition shows that LLM reasoning and orchestration still account for more than 90% of execution time, identifying model inference as the primary system bottleneck.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：90%、1.6x、1.8x。
- [ScaleWoB: Guiding GUI Agents with Coding Agents via Large-Scale Environmental Synthesis](https://arxiv.org/abs/2605.25160)
  - 主题: Coding agent routing
  - 中文解读: 这项工作主要关注Coding agent routing，核心内容是《ScaleWoB: Guiding GUI Agents with Coding Agents via Large-Scale Environmental Synthesis》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experiment results on five state-of-the-art mobile GUI agents reveal substantial headroom -- the average success rate is only 27.92\%, dropping to 17.82\% on long-horizon subset -- while humans reach 92.08\%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

