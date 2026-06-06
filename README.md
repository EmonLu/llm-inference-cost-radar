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

- 日期: 2026-06-06
- 今日新论文: 15
- 今日新权威来源更新: 1
- 本周精选论文: 25
- 本周精选权威来源更新: 8
- 日报: `papers/2026-06-06.md`
- 周报: `digests/weekly-2026-06-06.md`

## 今日最值得看

- [RedKnot: Efficient Long-Context LLM Serving with Head-Aware KV Reuse and SegPagedAttention](https://arxiv.org/abs/2606.06256)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《RedKnot: Efficient Long-Context LLM Serving with Head-Aware KV Reuse and SegPagedAttention》在 arXiv cs.AI 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，This head-level decomposition turns the KV cache from a monolithic tensor abstraction into a structured memory object, enabling RedKnot to uniformly support position-independent KV reuse, prefix KV compression, hot/cold KV separation, and distributed KV placement while preserving output fidelity and improving resource efficiency, without requiring model retraining or fine-tuning.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [What Should Agents Say? Action-state Communication for Efficient Multi-Agent Systems](https://arxiv.org/abs/2606.05304v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《What Should Agents Say? Action-state Communication for Efficient Multi-Agent Systems》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The gains extend to production coding harnesses: PACT lifts OpenHands' resolve rate at -10% tokens-per-resolved, and is resolve-neutral on SWE-agent while halving input tokens.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：10%。
- [Do More Agents Help? Controlled and Protocol-Aligned Evaluation of LLM Agent Workflows](https://arxiv.org/abs/2606.05670v1)
  - 主题: Agent systems and multi-agent efficiency
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency，核心内容是《Do More Agents Help? Controlled and Protocol-Aligned Evaluation of LLM Agent Workflows》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On the PAE GAIA snapshot, a Claude-Code-style runtime workflow reaches 66.72% overall and 69.23% on Level 3, more than 20 points above the strongest non-Claude baseline, Jarvis, a fixed MAS.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：66.72%、69.23%。
- [Vortex: Efficient and Programmable Sparse Attention Serving for AI Agents](https://arxiv.org/abs/2606.06453v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Vortex: Efficient and Programmable Sparse Attention Serving for AI Agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Vortex enables rapid prototyping, deployment, and evaluation of sparse attention algorithms, effectively translating their theoretical efficiency gains into real-world throughput improvements.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [LatentSkill: From In-Context Textual Skills to In-Weight Latent Skills for LLM Agents](https://arxiv.org/abs/2606.06087v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《LatentSkill: From In-Context Textual Skills to In-Weight Latent Skills for LLM Agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On ALFWorld and Search-QA, LatentSkill outperforms the corresponding in-context skill baseline while using substantially fewer prefill tokens: it improves ALFWorld success by 21.4 and 13.4 points on the seen and unseen splits with 64.1% fewer prefill tokens, and improves Search-QA exact match by 3.0 points with 72.2% lower skill-token overhead.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：64.1%、72.2%。
- [The Meta-Agent Challenge: Are Current Agents Capable of Autonomous Agent Development?](https://arxiv.org/abs/2606.04455v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing，核心内容是《The Meta-Agent Challenge: Are Current Agents Capable of Autonomous Agent Development?》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，To ensure evaluation integrity, this framework is secured by multi-layer defenses against reward hacking.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [ADK Arena: Evaluating Agent Development Kits via LLM-as-a-Developer](https://arxiv.org/abs/2606.05548v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing，核心内容是《ADK Arena: Evaluating Agent Development Kits via LLM-as-a-Developer》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Evaluating all 51 popular Python ADK frameworks (204 agent--benchmark pairs), we find that: (1)~generation succeeds for 57\% of runs, and its cost varies 5.6$\times$ across frameworks (\$0.6 to \$3.4 per agent), a quantitative proxy for API complexity, though cost alone does not predict success; (2)~no single framework dominates: the best single-benchmark ADK agents resolve up to 80\% of tasks and can even \emph{beat} general-purpose frontier coding agents at a fraction of the cost, yet the median framework resolves only 32\%; (3)~across information-source ablations, genuine framework usage stays within a narrow 28--40\% band (highest with raw source access and still 33\% with no reference material at all), indicating that documentation, source code, and parametric knowledge are largely substitutable rather than any one being a hard bottleneck.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads](https://arxiv.org/abs/2606.06448v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Third, we characterize ten representative systems across two benchmark suites, uncovering how design choices shift cost across the write and read paths.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Microskill Architecture: A Modular Skill-Driven Framework for AI-Native Code Generation](https://arxiv.org/abs/2606.05720v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、LLM routing，核心内容是《Microskill Architecture: A Modular Skill-Driven Framework for AI-Native Code Generation》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，An empirical case study an enterprise content management system with fifteen complex features shows that MicroSkill cuts token consumption by over 90%, nearly doubles first-try compilation success rates, eliminates architectural violations entirely, and enables autonomous extraction and registration of seven new skill capsules via a self-learning mechanism.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：90%。
- [Beyond tokens: a unified framework for latent communication in LLM-based multi-agent systems](https://arxiv.org/abs/2606.05711v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《Beyond tokens: a unified framework for latent communication in LLM-based multi-agent systems》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，We hope that this framework both lowers the barrier to entry for new researchers and provides a vocabulary for comparing future work.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

