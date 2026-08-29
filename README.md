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

- 日期: 2026-08-29
- 今日新论文: 15
- 今日新权威来源更新: 1
- 本周精选论文: 25
- 本周精选权威来源更新: 2
- 日报: `papers/2026-08-29.md`
- 周报: `digests/weekly-2026-08-29.md`

## 今日最值得看

- [ScaleSense: Cost-Intelligent Scaling Framework via Learned Resource Estimation in Alibaba AnalyticDB](https://arxiv.org/abs/2608.07945)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《ScaleSense: Cost-Intelligent Scaling Framework via Learned Resource Estimation in Alibaba AnalyticDB》在 arXiv cs.AI 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，By achieving a 76.7% relative improvement in optimal resource configuration selection over the best baseline, this approach addresses the critical performance-cost trade-off while maintaining low-overhead inference latency, confirming its practical performance in production deployments.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：76.7%、5.22x。
- [AgentFold: Closed-Loop Agentic Search for Protein Folding Model Design](https://arxiv.org/abs/2608.26747)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《AgentFold: Closed-Loop Agentic Search for Protein Folding Model Design》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Under a matched computational budget, AgentFold improves the best lDDT by 7.5% over independent Codex proposals and outperforms a random-search control.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：7.5%。
- [Heaviside Continuity of Rolling Coefficients for Eliminating Epistemic Entropy in Large Language Models](https://arxiv.org/abs/2607.04562)
  - 主题: Coding agent routing, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Coding agent routing、Cost-efficient LLM inference，核心内容是《Heaviside Continuity of Rolling Coefficients for Eliminating Epistemic Entropy in Large Language Models》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On capable proposers, the gate reduces the false-completion rate (FCR) from 4--7% to 0% while remaining latency-competitive and, in some settings, faster than the unwrapped model.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：7%、0%。
- [Code World Model: Coding Agent as World Brain](https://arxiv.org/abs/2608.25927v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《Code World Model: Coding Agent as World Brain》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，These results demonstrate the potential of combining code for persistent world evolution with video models for flexible visual realization, providing a new path toward open-ended world models.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [SkillShield: Prompt-Space Security Skills for LLM Coding Agents](https://arxiv.org/abs/2608.25817v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、LLM routing，核心内容是《SkillShield: Prompt-Space Security Skills for LLM Coding Agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across six large language models on RedCode, the default all-classes skill reduces malware-generation severity from 3.37 to 0.58 and achieves a 43.6% execution attack success rate, comparable to Llama Guard 3's 42.7% without its separate 8B classifier.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：43.6%、42.7%、36.2%。
- [Naive Prompt Optimization: Rethinking the Need for Complex Prompt Search](https://arxiv.org/abs/2608.27266)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《Naive Prompt Optimization: Rethinking the Need for Complex Prompt Search》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，arXiv:2608.27266v1 Announce Type: new Abstract: Efficiently improving autonomous agents across diverse tasks is central to accelerating recursive self-improvement (RSI) in agentic AI, with prompt optimization emerging as a promising approach capable of delivering performance gains comparable to those achieved by fine-tuning model weights, while reducing computational costs in both optimization and serving.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [LoopMoE: Unifying Iterative Computation with Mixture-of-Experts for Language Modeling](https://arxiv.org/abs/2606.04438)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《LoopMoE: Unifying Iterative Computation with Mixture-of-Experts for Language Modeling》在 arXiv cs.AI 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，Across nine downstream benchmarks, LoopMoE's average improvement over its matched vanilla MoE increases from over 1 point at the 3B scale to approximately 3 points at the 9B scale.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [When Does Latent Communication Pay? A Causal Audit of Relayed KV Caches in Multi-Agent LLMs](https://arxiv.org/abs/2608.04893)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《When Does Latent Communication Pay? A Causal Audit of Relayed KV Caches in Multi-Agent LLMs》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Where it does, the battery reads ceiling: 100% against 23-25% for answer-irrelevant relays on the primary backbone, a contrast replicated across three families, five checkpoints, and a prose document-QA surface.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：100%、25%。
- [MLLM-Routed Heterogeneous Ensembles for Robust Cross-Dataset Image Classification](https://arxiv.org/abs/2608.13463)
  - 主题: Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference、LLM routing，核心内容是《MLLM-Routed Heterogeneous Ensembles for Robust Cross-Dataset Image Classification》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Empirical evaluations illuminate the distinct capabilities and vulnerabilities of each architecture across disparate visual domains.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [GRAIN: Bridging Name and Narrative Shifts in Real-World Graph Reasoning through Invariance-Rewarded Agentic RL](https://arxiv.org/abs/2608.27142v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《GRAIN: Bridging Name and Narrative Shifts in Real-World Graph Reasoning through Invariance-Rewarded Agentic RL》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，GRAIN outperforms multi-agent baselines by 16.45\% in accuracy with approximately 24\% lower latency.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

