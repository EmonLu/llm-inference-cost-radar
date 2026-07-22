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

- 日期: 2026-07-22
- 今日新论文: 15
- 今日新权威来源更新: 1
- 本周精选论文: 25
- 本周精选权威来源更新: 2
- 日报: `papers/2026-07-22.md`
- 周报: `digests/weekly-2026-07-22.md`

## 今日最值得看

- [ExpertPlex: A High-Goodput Disaggregated Serving System for MoE LLMs with Adaptive Persistent Kernels](https://arxiv.org/abs/2607.18002)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《ExpertPlex: A High-Goodput Disaggregated Serving System for MoE LLMs with Adaptive Persistent Kernels》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Experiments serving MiniMax-M2.7 and GLM-5.1-FP8 show that ExpertPlex improves goodput by up to 2.01$\times$ over instance-level prefill-decode disaggregation and 1.66$\times$ over prefill-decode colocation.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：8 s。
- [FlowBlock: Wavefront-Parallel Decoding for Self-Correcting Diffusion Language Models](https://arxiv.org/abs/2607.17652)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《FlowBlock: Wavefront-Parallel Decoding for Self-Correcting Diffusion Language Models》在 arXiv cs.AI 这一方向上的推进。强调异构硬件协同推理。从实验上看，Across different benchmarks, \flowblock{} improves tokens per second (TPS) over LLaDA-2.1 and LLaDA-2.0, two serial block-wise dLLMs, by up to 2.95$\times$ and 4.01$\times$, while reducing latency by up to 53.6\% and 77.1\%, respectively.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [AirMoE: Statistic-Augmented Over-the-Air MoE for Collaborative Intelligence](https://arxiv.org/abs/2607.16562)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《AirMoE: Statistic-Augmented Over-the-Air MoE for Collaborative Intelligence》在 arXiv cs.DC 这一方向上的推进。强调异构硬件协同推理。从实验上看，Taking semantic segmentation task as an example, extensive experiments demonstrate that AirMoE outperforms MoE baselines and single-model competitors.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [A Multi-Agent System for 5G Throughput Prediction in Multi-Operator Urban Environments](https://arxiv.org/abs/2607.16930)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《A Multi-Agent System for 5G Throughput Prediction in Multi-Operator Urban Environments》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The system demonstrates high operational efficiency, with rapid micro-agent training times, low inference latencies, and agentic routing overhead of 0.004 to 0.126 ms.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：0.126 ms。
- [It Takes a MAESTRO To Prune Bad Experts](https://arxiv.org/abs/2607.08601)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《It Takes a MAESTRO To Prune Bad Experts》在 arXiv cs.CL 这一方向上的推进。强调异构硬件协同推理。从实验上看，Evaluated across five diverse domains including Safety, Bias, and Ethics, MAESTRO outperforms state-of-the-art baselines by up to 10.61% in average performance retention under a strict 50% compression regime, while exhibiting substantially lower cross-task variance, indicating that global, routing-congruent pruning produces models that generalize more consistently across heterogeneous tasks.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：10.61%、50%。
- [RELIC: Revealed Principles for Learning Interpretable Composable Skills in Multi-Agent Planning](https://arxiv.org/abs/2607.16745)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《RELIC: Revealed Principles for Learning Interpretable Composable Skills in Multi-Agent Planning》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，arXiv:2607.16745v1 Announce Type: new Abstract: Multi-agent planning becomes substantially harder when agents must improve specialized decision-making skills while keeping their internal implementations private.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Empowering On-Device Model Adaptation with an Edge AI Inference Accelerator](https://arxiv.org/abs/2607.18101)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Empowering On-Device Model Adaptation with an Edge AI Inference Accelerator》在 arXiv cs.LG 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Across multiple architectures and datasets, this pipeline achieves up to 15.4x faster wall-clock training time compared to a Raspberry Pi 5 CPU baseline, offers competitive throughput in favorable settings, and consistently reduces energy per sample.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：15.4x。
- [SkillRouter: Skill Routing for LLM Agents at Scale](https://arxiv.org/abs/2603.22455)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、LLM routing，核心内容是《SkillRouter: Skill Routing for LLM Agents at Scale》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Skillrouter achieves 74.0% Hit@1 on our benchmark -- the strongest average top-1 routing performance among the baselines we evaluate -- while using 13$\times$ fewer parameters and running 5.8$\times$ faster than the strongest base pipeline.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：74.0%。
- [LongStraw: Long-Context RL Beyond 2M Tokens under a Fixed GPU Budget](https://arxiv.org/abs/2607.14952)
  - 主题: Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference，核心内容是《LongStraw: Long-Context RL Beyond 2M Tokens under a Fixed GPU Budget》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On eight H20 GPUs, Qwen completes exact-attention response-only GRPO at 2,097,152 positions for G=2 and G=8; a 4,456,448-position prefix supports eight G=8 cycles (64 replays) at 83.894 GB per rank.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：83.894 GB。
- [TraceDev: A Traceability-Driven Multi-agent Framework for Requirement-to-Code Development](https://arxiv.org/abs/2607.18886v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Heterogeneous MoE inference，核心内容是《TraceDev: A Traceability-Driven Multi-agent Framework for Requirement-to-Code Development》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On the ETOUR dataset, TraceDev achieves a success rate of 53.63\%, outperforming baseline approaches by up to 186.63\%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

