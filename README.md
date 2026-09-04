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

- 日期: 2026-09-04
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 3
- 日报: `papers/2026-09-04.md`
- 周报: `digests/weekly-2026-09-04.md`

## 今日最值得看

- [Latency-Aware Orchestration for Multi-Agent LLM Workflows on Heterogeneous GPUs](https://arxiv.org/abs/2609.03335)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Latency-Aware Orchestration for Multi-Agent LLM Workflows on Heterogeneous GPUs》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across a workload spanning three workflow scenarios on a heterogeneous GPU pool, our system reduces end-to-end makespan and overall p95 completion latency under burst arrivals by up to 36.8% and 25.9%, respectively, over state-of-the-art workflow schedulers.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：36.8%、25.9%。
- [Iapetus: Content-Aware Hierarchical Scheduling for Collaborative ViT Inference in LEO Satellite Networks](https://arxiv.org/abs/2609.03318)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Iapetus: Content-Aware Hierarchical Scheduling for Collaborative ViT Inference in LEO Satellite Networks》在 arXiv cs.DC 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，A unified objective balances per-task latency, energy, and quality loss against accumulated workload and battery pressures.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Value-Preserving Architectures for Agentic AI Systems](https://arxiv.org/abs/2609.03920)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《Value-Preserving Architectures for Agentic AI Systems》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Although software engineering has traditionally focused on functional correctness, the adoption of LLMs and AI agents into complex socio-technical systems has intensified the need for responsible software engineering and robust value alignment.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Evolving Excellence: Automated Optimization of LLM-based Agents](https://arxiv.org/abs/2512.09108)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《Evolving Excellence: Automated Optimization of LLM-based Agents》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，We evaluate ARTEMIS on four representative agent systems: the \emph{ALE Agent} for competitive programming on AtCoder Heuristic Contest, achieving a \textbf{$13.6\%$ improvement} in acceptance rate; the \emph{Mini-SWE Agent} for code optimization on SWE-Perf, with a statistically significant \textbf{10.1\% performance gain}; and the \emph{CrewAI Agent} for cost and mathematical reasoning on Math Odyssey, achieving a statistically significant \textbf{$36.9\%$ reduction} in the number of tokens required for evaluation.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Para-Pipe: Exploiting Hierarchical Operator Parallelism of ML Computational Graphs on SoCs](https://arxiv.org/abs/2609.04168)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Para-Pipe: Exploiting Hierarchical Operator Parallelism of ML Computational Graphs on SoCs》在 arXiv cs.DC 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，More importantly, throughput-optimized configurations under Para-Pipe on Amlogic SoC show an average energy efficiency improvement of 11.0% over purely pipelined strategies and 23.3% relative to non-pipelined parallel execution.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：11.0%、23.3%。
- [VestigeKV: The NoPE-MLA KV Cache Carries Its Own Eviction Signal in a Vestigial Branch](https://arxiv.org/abs/2609.03949)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《VestigeKV: The NoPE-MLA KV Cache Carries Its Own Eviction Signal in a Vestigial Branch》在 arXiv cs.CL 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，The recall tier -- the standard configuration -- holds 128x at 1.00.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：128x、46.8%。
- [HyGRAIL: Cost-Aware and Evidence-Grounded Scientific Hypothesis Discovery over Knowledge Graphs](https://arxiv.org/abs/2609.02056v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《HyGRAIL: Cost-Aware and Evidence-Grounded Scientific Hypothesis Discovery over Knowledge Graphs》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Meanwhile, GNN triage reduces the LLM call rate by 54.36% on average.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：54.36%。
- [Towards a Statistical Understanding of Mixture-of-Experts](https://arxiv.org/abs/2609.03501)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Towards a Statistical Understanding of Mixture-of-Experts》在 arXiv cs.LG 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，Together, these results provide a unified statistical framework for understanding MoE through input-dependent expert aggregation, in which expert specialization and computational tradeoffs are governed by local predictive structure.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [PPO-STGNN: A Proximal Policy Optimization Approach with Spatio-Temporal Graph Neural Networks for DAG Task Scheduling in Cloud-Edge-End Computing](https://arxiv.org/abs/2609.03503)
  - 主题: Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference，核心内容是《PPO-STGNN: A Proximal Policy Optimization Approach with Spatio-Temporal Graph Neural Networks for DAG Task Scheduling in Cloud-Edge-End Computing》在 arXiv cs.AI 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Experimental results show that PPO-STGNN significantly improves load balancing while maintaining a low completion time, making it suitable for dynamic and heterogeneous cloud-edge- end DAG scheduling scenarios.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [What Matters for Aggressive Decoding-Time KV Eviction? Temporal Aggregation and Ranking Preservation](https://arxiv.org/abs/2609.03515)
  - 主题: Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference，核心内容是《What Matters for Aggressive Decoding-Time KV Eviction? Temporal Aggregation and Ranking Preservation》在 arXiv cs.AI 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，Building on this observation, we introduce InertiaKV, an EMA-based decoding-time eviction method, and InertiaKV-Lazy, its periodic-refresh variant, which yields 1.34-1.46x decode throughput relative to full refresh InertiaKV.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.46x。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

