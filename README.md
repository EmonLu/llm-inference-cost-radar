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

- 日期: 2026-10-03
- 今日新论文: 15
- 今日新权威来源更新: 1
- 本周精选论文: 25
- 本周精选权威来源更新: 2
- 日报: `papers/2026-10-03.md`
- 周报: `digests/weekly-2026-10-03.md`

## 今日最值得看

- [Trustworthy Runtime Error Healing in Real-World Repositories: A Benchmark and Guardrail](https://arxiv.org/abs/2609.39086v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing，核心内容是《Trustworthy Runtime Error Healing in Real-World Repositories: A Benchmark and Guardrail》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The best setting resumes execution in 38.11% of instances and passes the target test in 28.68%, showing that existing agents can already heal a meaningful share of real repository-level crashes.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：38.11%、28.68%、68.42%。
- [EfficientRollout: System-Aware Self-Speculative Decoding for RL Rollouts](https://arxiv.org/abs/2606.18967)
  - 主题: Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference，核心内容是《EfficientRollout: System-Aware Self-Speculative Decoding for RL Rollouts》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，EfficientRollout reduces rollout and end-to-end latency by up to 24.2% and 15.6%, respectively, over an accelerated AR rollout baseline, while preserving final model quality.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：24.2%、15.6%。
- [GraphMAS: A Systematic Benchmark of Multi-Agent Coordination for Graph Learning](https://arxiv.org/abs/2609.39777v1)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《GraphMAS: A Systematic Benchmark of Multi-Agent Coordination for Graph Learning》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，We find that heterogeneous graph perspectives are complementary, and that coordinating specialists improves over individual specialists and single-agent graph reasoning, with gains from decomposing reasoning across specialists rather than from broader evidence access alone.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [HakiCC: LLM-Driven Multi-Agent Design and Optimization of Concurrency Control Protocols](https://arxiv.org/abs/2610.00889v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《HakiCC: LLM-Driven Multi-Agent Design and Optimization of Concurrency Control Protocols》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，All ten are conflict-serializable after Stage 1; Stage 2 improves throughput for every protocol, with average gains of +50.6% for TPC-C protocols and +92.2% for AuctionMark protocols.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：50.6%、92.2%。
- [Capture the lifecycle: KV Cache management in ReAct Agents with KVTether](https://arxiv.org/abs/2609.39819v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《Capture the lifecycle: KV Cache management in ReAct Agents with KVTether》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across agent benchmarks and production workloads, KVTether reduces end-to-end request latency by up to 26.3% and 17.4% relative to LMCache and MORI, respectively, and lowers estimated task cost by 40.0% and 33.2% on average.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：26.3%、17.4%、40.0%。
- [Backdoor Containment via Expert Quarantine and Shutdown in LLMs](https://arxiv.org/abs/2610.00663v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Backdoor Containment via Expert Quarantine and Shutdown in LLMs》在 arXiv API 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，Empirically, our methods reduce the attack success rate ASR from 100% to 0-10% on most settings across two tasks, three attacks, and four model families, while downstream utility is often preserved or only modestly affected.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：100%、10%。
- [OverAct: Measuring and Mitigating Proactive Over-Authorization in LLM Tool-Calling Agents](https://arxiv.org/abs/2610.01508v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing，核心内容是《OverAct: Measuring and Mitigating Proactive Over-Authorization in LLM Tool-Calling Agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，SelfAudit reduces privacy-oriented excess by 43% without oracle knowledge.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：43%。
- [Score the Update, Not the Token: Descent-Aligned Routing for Combinatorial LoRA Experts](https://arxiv.org/abs/2610.00493)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Score the Update, Not the Token: Descent-Aligned Routing for Combinatorial LoRA Experts》在 arXiv cs.LG 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，To first order, adding an expert's update to a layer output lowers the loss by the inner product between that update and the negative loss gradient at the output.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Learning When and How to Intervene: A Hindsight-Distilled Sentinel for Coding Agents](https://arxiv.org/abs/2609.39957v1)
  - 主题: Coding agent routing
  - 中文解读: 这项工作主要关注Coding agent routing，核心内容是《Learning When and How to Intervene: A Hindsight-Distilled Sentinel for Coding Agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across SWE-bench Verified Mini and Ask or Assume, HiSentinel consistently improves task completion across Sentinel scales and coding-agent families, with gains of up to 14% and 10%, respectively, while maintaining competitive token consumption.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：14%、10%。
- [Selection-Based Structured Reasoning: Toward Efficient Multimodal Search Agents](https://arxiv.org/abs/2610.01892)
  - 主题: Cost-efficient LLM inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、LLM routing，核心内容是《Selection-Based Structured Reasoning: Toward Efficient Multimodal Search Agents》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，SSR achieves an average success rate competitive with leading search agents of the same scale, while reducing per-turn reasoning latency by over 90% and total per-question model inference latency by 28-54%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：90%、54%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

