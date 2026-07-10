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

- 日期: 2026-07-10
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 2
- 日报: `papers/2026-07-10.md`
- 周报: `digests/weekly-2026-07-10.md`

## 今日最值得看

- [Tessera: Unlocking Heterogeneous GPUs through Kernel-Granularity Disaggregation](https://arxiv.org/abs/2604.10180)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Tessera: Unlocking Heterogeneous GPUs through Kernel-Granularity Disaggregation》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Extensive evaluations across five heterogeneous GPUs and four model architectures, scaling up to 16 GPUs, show that Tessera improves serving throughput and cost efficiency by up to 2.3x and 1.6x, respectively, compared to existing disaggregation methods, while generalizing to model architectures where prior approaches do not apply.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：2.3x、1.6x。
- [It Takes a MAESTRO To Prune Bad Experts](https://arxiv.org/abs/2607.08601v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《It Takes a MAESTRO To Prune Bad Experts》在 arXiv API 这一方向上的推进。强调异构硬件协同推理。从实验上看，Evaluated across five diverse domains including Safety, Bias, and Ethics, MAESTRO outperforms state-of-the-art baselines by up to 10.61% in average performance retention under a strict 50% compression regime, while exhibiting substantially lower cross-task variance, indicating that global, routing-congruent pruning produces models that generalize more consistently across heterogeneous tasks.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：10.61%、50%。
- [Does Mixture-of-Experts Actually Help Inference on Consumer and Edge Hardware? An Empirical Study](https://arxiv.org/abs/2606.21428)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Does Mixture-of-Experts Actually Help Inference on Consumer and Edge Hardware? An Empirical Study》在 arXiv cs.AI 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，We benchmark OLMoE-1B-7B (1.3 B active of 6.9 B total) against three dense baselines on an Apple M2 Pro and an NVIDIA Jetson Orin Nano 8 GB through llama$.$cpp, measuring throughput, memory, and on-device energy.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：8 GB、9%。
- [SMetric: Rethink LLM Scheduling for Serving Agents with Balanced Session-centric Scheduling](https://arxiv.org/abs/2607.08565)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《SMetric: Rethink LLM Scheduling for Serving Agents with Balanced Session-centric Scheduling》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，SMETRIC improves cluster TPS by 10-16% under prefill-decode colocation with a global store and prefill TPS by 2-34% under disaggregation over state-of-the-art schedulers, also with a better per-token latency.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：16%、34%、80%。
- [MORES: Mobile Reasoning-as-a-Service via Distributed LLM Inference-Time Scaling](https://arxiv.org/abs/2607.08116v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《MORES: Mobile Reasoning-as-a-Service via Distributed LLM Inference-Time Scaling》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experimental results show that the proposed method achieves an approximately 18% improvement in system throughput over the baseline Soft Actor-Critic (SAC) algorithm.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：18%。
- [Towards Efficient Large Language Model Serving: A Survey on System-Aware KV Cache Optimization](https://arxiv.org/abs/2607.08057v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Towards Efficient Large Language Model Serving: A Survey on System-Aware KV Cache Optimization》在 arXiv API 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，Despite the rapid advancements of large language models (LLMs), LLM serving systems remain memory-intensive and costly.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Tool-Making and Self-Evolving LLM Agents in Low-Latency Systems](https://arxiv.org/abs/2607.08010v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Tool-Making and Self-Evolving LLM Agents in Low-Latency Systems》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，In production, tool calls reduce p50 latency by 42%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：42%、62%。
- [Agentic AI and Retrieval-Augmented Models in Straight-Through Underwriting](https://arxiv.org/abs/2607.07858)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《Agentic AI and Retrieval-Augmented Models in Straight-Through Underwriting》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The agentic system performs best overall, with the largest gains in multi-step and missing-information scenarios, where structured retrieval and reflection help the model avoid unsupported straight-through decisions.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Autonomous heterogeneous catalyst discovery with a self-evolving multi-agent digital twin](https://arxiv.org/abs/2606.05050)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《Autonomous heterogeneous catalyst discovery with a self-evolving multi-agent digital twin》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Two innovations address the hardest steps: UniMech finds dominant pathways for novel materials at over $10^3\times$ lower cost than exhaustive enumeration by fusing agent-guided proposals with energy-cached graph search, and a memory-augmented reinforcement loop raises barrier-calculation success from 41% to 84% across 600 catalytic surfaces.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：41%、84%、100%。
- [Multi-Agent Firewall Architecture for Privacy Protection of Sensitive Data in Interactions with Language Models](https://arxiv.org/abs/2607.08282v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Multi-Agent Firewall Architecture for Privacy Protection of Sensitive Data in Interactions with Language Models》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Evaluation results demonstrate it achieves F1 scores of up to 94.93% on optimal configurations.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1 s、94.93%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

