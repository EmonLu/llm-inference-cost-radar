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

- 日期: 2026-08-16
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 6
- 日报: `papers/2026-08-16.md`
- 周报: `digests/weekly-2026-08-16.md`

## 今日最值得看

- [BoardroomAI: Dependency-Aware Human-Steerable Multi-Agent Deliberation through Evolving Decision Graphs](https://arxiv.org/abs/2608.13046)
  - 主题: Agent systems and multi-agent efficiency, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、LLM routing，核心内容是《BoardroomAI: Dependency-Aware Human-Steerable Multi-Agent Deliberation through Evolving Decision Graphs》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，In a 12-case exploratory pilot, selective repair recomputed 62.11% of canonical nodes, preserved all gold-unaffected nodes, and produced valid updated decisions in six cases while abstaining in the remaining six.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：62.11%、14.59%。
- [MLLM-Routed Heterogeneous Ensembles for Robust Cross-Dataset Image Classification](https://arxiv.org/abs/2608.13463)
  - 主题: Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference、LLM routing，核心内容是《MLLM-Routed Heterogeneous Ensembles for Robust Cross-Dataset Image Classification》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Empirical evaluations illuminate the distinct capabilities and vulnerabilities of each architecture across disparate visual domains.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [OpScale: Operator-level Provisioning and Autoscaling for LLM Serving](https://arxiv.org/abs/2608.13499v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《OpScale: Operator-level Provisioning and Autoscaling for LLM Serving》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Evaluated with production traces on up to 40 A100s and 24 GB200s, OpScale attains SLOs with up to 36.3% fewer GPUs and 28% less power, or achieves 44% higher throughput under fixed cost budgets.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：100s、24 GB、200s。
- [Specification-first convergence with an AI coding agent: a case study of dismantling a core architectural invariant across 189 files in a 717k-line codebase with no test oracle and no human code review](https://arxiv.org/abs/2608.12440)
  - 主题: Coding agent routing
  - 中文解读: 这项工作主要关注Coding agent routing，核心内容是《Specification-first convergence with an AI coding agent: a case study of dismantling a core architectural invariant across 189 files in a 717k-line codebase with no test oracle and no human code review》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The protocol: formal specification by the agent, 14 refinement cycles auditing that specification against the source code, atomic implementation, a compile/test feedback loop, then 17 verification cycles auditing the code against the frozen specification.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Where Should Optimizer State Live? Tiered State Allocation for Memory-Efficient Mixture-of-Experts Training](https://arxiv.org/abs/2607.19058)
  - 主题: Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference、LLM routing，核心内容是《Where Should Optimizer State Live? Tiered State Allocation for Memory-Efficient Mixture-of-Experts Training》在 arXiv cs.AI 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，The resulting state occupies 1.29 GB or 2.6% of AdamW's and peak training memory falls from 81.4 GB to 31.3 GB, within the budget of a 40 GB accelerator.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.29 GB、2.6%、81.4 GB。
- [VALG: An Agentic System for ML Theory Research](https://arxiv.org/abs/2608.13060)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《VALG: An Agentic System for ML Theory Research》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，These case studies show how VALG keeps source-scope matches, relaxations, conditional results, and blocked attempts mathematically distinct.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [DomusFM: A Foundation Model for Event-Based Behavioral Monitoring in Smart-Homes](https://arxiv.org/abs/2602.01910)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《DomusFM: A Foundation Model for Event-Based Behavioral Monitoring in Smart-Homes》在 arXiv cs.AI 这一方向上的推进。强调异构硬件协同推理。从实验上看，Through a leave-one-dataset-out evaluation across seven public smart-home datasets, we demonstrate that DomusFM consistently outperforms baselines on three downstream tasks: ADL recognition, next-k event prediction, and unsupervised clustering.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Humans are Missing from AI Coding Agent Research](https://arxiv.org/abs/2608.12355)
  - 主题: Coding agent routing
  - 中文解读: 这项工作主要关注Coding agent routing，核心内容是《Humans are Missing from AI Coding Agent Research》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，arXiv:2608.12355v1 Announce Type: cross Abstract: Recent progress in AI coding agent research has led to rapid improvements in agents' ability to autonomously perform complex software engineering tasks, from editing large codebases to executing long-horizon development workflows.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Error-Aware Reverse Auction Mechanism for Large Language Model Routing](https://arxiv.org/abs/2608.12719)
  - 主题: LLM routing
  - 中文解读: 这项工作主要关注LLM routing，核心内容是《Error-Aware Reverse Auction Mechanism for Large Language Model Routing》在 arXiv cs.AI 这一方向上的推进。直接讨论模型选择或路由策略，与你的主线高度一致。从实验上看，Experiments on simulations and real-world benchmarks show that EA-RAM is robust to the Dual Error and achieves a better cost--performance Pareto frontier than centralized baselines, with additional gains when providers contribute local information, validating its practical effectiveness.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [SPADE: Speculative Decoding for Precise and Low Cost Distributed Edge Cloud Inference](https://arxiv.org/abs/2608.13076v1)
  - 主题: Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference，核心内容是《SPADE: Speculative Decoding for Precise and Low Cost Distributed Edge Cloud Inference》在 arXiv API 这一方向上的推进。通过 speculative decoding 提升吞吐并降低单次推理成本。从实验上看，Experimental results across multiple Natural Language Processing tasks using SpecBench and CNN/Dailymail datasets demonstrate that \our{} reduces the cloud model calls by $76\%$ with zero loss in accuracy as compared to the full model.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

