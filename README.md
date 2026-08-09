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

- 日期: 2026-08-09
- 今日新论文: 12
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 4
- 日报: `papers/2026-08-09.md`
- 周报: `digests/weekly-2026-08-09.md`

## 今日最值得看

- [The Vulnerability With No CVE: Managing Persistent Gaps Between Mandate and Authority in AI Coding Agents](https://arxiv.org/abs/2608.05884)
  - 主题: Coding agent routing, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Coding agent routing、Cost-efficient LLM inference，核心内容是《The Vulnerability With No CVE: Managing Persistent Gaps Between Mandate and Authority in AI Coding Agents》在 arXiv cs.CL 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，We then provide a field vignette, a thresholded definition, six recurring APV patterns, a vulnerability lifecycle, a minimum record, a control-and-closure matrix, tooling implications, and a testable research agenda.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [HomoEnsNER: Does Language Alignment Outperform Architectural Complexity in Gujarati Named Entity Recognition?](https://arxiv.org/abs/2608.03105)
  - 主题: Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference，核心内容是《HomoEnsNER: Does Language Alignment Outperform Architectural Complexity in Gujarati Named Entity Recognition?》在 arXiv cs.CL 这一方向上的推进。强调异构硬件协同推理。从实验上看，This study asks whether, for a low-resource, morphologically rich language like Gujarati, a homogeneous ensemble of a single monolingual encoder outperforms such architectural diversity.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [AgentExecutor: Partial Code Execution via Agentic Context Generation](https://arxiv.org/abs/2608.05959v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《AgentExecutor: Partial Code Execution via Agentic Context Generation》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The results show that AgentExecutor achieves up to 94% and 90% code coverage, outperforming the state-of-the-art approach Treefix by 19.9% and 13.8%, respectively.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：94%、90%、19.9%。
- [CodeGrep: An RL-Trained Retrieval Agent for LLM Coding Agents](https://arxiv.org/abs/2608.05886v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing，核心内容是《CodeGrep: An RL-Trained Retrieval Agent for LLM Coding Agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On all 500 SWE-Bench Verified instances, CodeGrep preserves resolve rate while substantially improving efficiency: 27.0% versus 25.8% for the no-retrieval baseline, with 15% fewer rounds and 19% fewer tokens on resolved instances.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：500 S、27.0%、25.8%。
- [A-SR: Self-Evolving Agentic LLMs for Symbolic Regression via Hierarchical Coordination](https://arxiv.org/abs/2608.04872)
  - 主题: Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference、LLM routing，核心内容是《A-SR: Self-Evolving Agentic LLMs for Symbolic Regression via Hierarchical Coordination》在 arXiv cs.CL 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Averaged over the four LSR-Synth scientific domains in LLM-SRBench, A-SR improves Acc@0.01 over baselines from 25.79% to 48.30% with Llama3.1-8B, while A-SR-LoRA improves the corresponding Qwen3-4B result from 24.58% to 38.29%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：25.79%、48.30%、24.58%。
- [M$^3$Prune: Hierarchical Collaborative Pruning for Efficient Multi-Modal Multi-Agent Retrieval-Augmented Generation](https://arxiv.org/abs/2608.05967v1)
  - 主题: Agent systems and multi-agent efficiency
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency，核心内容是《M$^3$Prune: Hierarchical Collaborative Pruning for Efficient Multi-Modal Multi-Agent Retrieval-Augmented Generation》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Extensive experiments on both general-domain and domain-specific mRAG benchmarks show that M3Prune consistently outperforms single-agent and strong multi-agent mRAG systems while signifi- cantly improving token efficiency.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [PolyAlign: Conditional Human-Distribution Alignment](https://arxiv.org/abs/2606.13227)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《PolyAlign: Conditional Human-Distribution Alignment》在 arXiv cs.CL 这一方向上的推进。强调异构硬件协同推理。从实验上看，Across a bilingual evaluation suite covering English and Chinese single- and multi-turn settings, PolyAlign improves conditional naturalness and distributional faithfulness while preserving competitive task utility.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [From Economic Agents to Agentic Economies: A Systems Blueprint for Economic World Models](https://arxiv.org/abs/2608.06020v1)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《From Economic Agents to Agentic Economies: A Systems Blueprint for Economic World Models》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，A systematic literature survey across these levels reveals that existing work remains concentrated in lower-level agent and simulation environments, while systems with self-evolving agents, endogenous institutions, persistent empirical alignment, and validated economic mechanisms remain rare.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [TensorCast: The Missing Tensor Management Layer in Large Language Model Infrastructure](https://arxiv.org/abs/2608.06007v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、LLM routing，核心内容是《TensorCast: The Missing Tensor Management Layer in Large Language Model Infrastructure》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，A programmable policy implemented with TensorCast improves median TTFT by up to 93.2% under highly concurrent multi-turn agent workloads.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：93.2%。
- [DreamGuard: Efficient Runtime Guardrail for LLM Agents via Risk-Aware World Model](https://arxiv.org/abs/2608.05695v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《DreamGuard: Efficient Runtime Guardrail for LLM Agents via Risk-Aware World Model》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experiments across four benchmarks and an online guardrail evaluation show that DreamGuard outperforms generic, reactive, and proactive guardrail baselines, achieves the best safety-utility trade-off among evaluated guardrails, and maintains an average end-to-end latency of 25 ms per call.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：25 ms。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

