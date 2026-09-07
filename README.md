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

- 日期: 2026-09-07
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 2
- 日报: `papers/2026-09-07.md`
- 周报: `digests/weekly-2026-09-07.md`

## 今日最值得看

- [How to Speculate about Uncertainty in Agentic Coding? A Draft-Model Gate Method](https://arxiv.org/abs/2609.05274v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《How to Speculate about Uncertainty in Agentic Coding? A Draft-Model Gate Method》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，To show the signal is actionable, we instantiate one such policy, a pre-execution veto gate, on software engineering agents Qwen3-Coder-480B and closed-source Claude 3.5 Sonnet, cutting execution error rate by 6-8 percentage points and token cost by 14-19% in deployment, transferring to out-of-distribution benchmarks without retraining, and generalizing across agent models.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：3.5 S、19%。
- [Cost-Aware Hierarchical Multi-Agent Ransomware Detection and Family Attribution](https://arxiv.org/abs/2609.04820v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Cost-Aware Hierarchical Multi-Agent Ransomware Detection and Family Attribution》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The complete HMAS achieved 96.57% accuracy, 0.96 F1-score and 0.99 ROC-AUC for binary detection.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：96.57%、43.97%。
- [RefactorPlatform: An Open-Source Harness for Controlled Evaluation of Repository-Scale Refactoring Agents](https://arxiv.org/abs/2609.04898v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、LLM routing，核心内容是《RefactorPlatform: An Open-Source Harness for Controlled Evaluation of Repository-Scale Refactoring Agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Demonstrating the platform on 100 multi-file RefactorBench tasks across four model families, we illustrate the analyses it supports: AST-aware chunking outperforms naive token-window chunking by 25-30% across prompt modes, whereas naive retrieval falls below the retrieval-free baseline; a lean retrieval-augmented single agent (86%) beats the sub-agent configuration we evaluated (66%) on matched tasks with no task passing under delegation that fails under retrieval; and retrieval's accuracy gains absorb its token overhead, leaving cost per successful refactoring unchanged.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：30%、86%、66%。
- [$\tau^\tau$-Bench: An Environment for End-To-End, Realistic Agent Construction](https://arxiv.org/abs/2609.04611)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《$\tau^\tau$-Bench: An Environment for End-To-End, Realistic Agent Construction》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across 53 tasks spanning four domains, the strongest configuration, Claude Opus 5 under Claude Code, passes just 23.9% of evaluation simulations.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：23.9%、82.2%。
- [Training-Free Halving of Activated Experts in Fine-Grained Mixture-of-Experts Models](https://arxiv.org/abs/2609.04575)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Training-Free Halving of Activated Experts in Fine-Grained Mixture-of-Experts Models》在 arXiv cs.LG 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，We further find that perplexity and downstream accuracy favor different $k_2$, cautioning against selecting MoE compression settings using unlabeled text alone.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Testing Interchangeability in LLM Agent Teams](https://arxiv.org/abs/2609.05279v1)
  - 主题: Agent systems and multi-agent efficiency
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency，核心内容是《Testing Interchangeability in LLM Agent Teams》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Against a placebo that reproduces the disruption of a roster change without changing who occupies the seat, a swap costs little in task score but raises the communication a team spends per unit of progress by 16 to 63 percent, and in Hanabi a swapped agent is more expensive than an inexperienced one, consistent with interference from conventions learned with its former partner.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Same Request, Different Answer: Quantization Amplifies Cache-Induced Divergence in LLM Serving](https://arxiv.org/abs/2609.04748)
  - 主题: Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference，核心内容是《Same Request, Different Answer: Quantization Amplifies Cache-Induced Divergence in LLM Serving》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Repeated cache-enabled runs did diverge, and three experiments locate the cause: a single server-level prompt-cache setting moves run-to-run divergence by 37.5 percentage points, execution order acts only while that setting is active, and restoring cache state makes the cached and recompute paths each reproduce on 40 of 40 items while still differing from each other on 14.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Diffusion Language Models for Mobile Edge Agentic AI: Foundations, Applications, and Challenges](https://arxiv.org/abs/2609.04778v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《Diffusion Language Models for Mobile Edge Agentic AI: Foundations, Applications, and Challenges》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，This survey reviews DLM foundations and analyzes their suitability for edge settings under latency, memory, energy, bandwidth, privacy, and reliability constraints.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Design Docs Are All You Need: An AI-native Machine-Learning Performance Tool](https://arxiv.org/abs/2609.05364v1)
  - 主题: Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Coding agent routing、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Design Docs Are All You Need: An AI-native Machine-Learning Performance Tool》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Two ingredients make regeneration reliable: (i) a design-doc style built around step-by-step worked examples that act as in-context demonstrations for the generating agents, and (ii) a minimal, recursively defined operator IR with symbolic (SymPy) cost expressions, a fast analytical roll-up mode for large sweeps, and a slow modulo-scheduling mode for fine-grained schedule studies.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Large Language Models for HVAC Operations in Building Energy Systems: A Critical Review of Methods, Applications, and Deployment Readiness](https://arxiv.org/abs/2609.05314v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Large Language Models for HVAC Operations in Building Energy Systems: A Critical Review of Methods, Applications, and Deployment Readiness》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Future work should prioritise field-validated benchmarks, orchestration evaluation under operational constraints, and LLM-MPC/RL architectures with bounded latency and verifiable safety properties.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

