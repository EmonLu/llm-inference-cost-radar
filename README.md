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

- 日期: 2026-11-27
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 4
- 日报: `papers/2026-11-27.md`
- 周报: `digests/weekly-2026-11-27.md`

## 今日最值得看

- [FluidPD: In-Place Elasticity for SLO-Aware Prefill-Decode Disaggregated LLM Serving](https://arxiv.org/abs/2610.06917)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《FluidPD: In-Place Elasticity for SLO-Aware Prefill-Decode Disaggregated LLM Serving》在 arXiv cs.AI 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Real workloads exhibit both short bursts and sustained shifts in the prefill-to-decode demand ratio, so a fixed split can violate latency SLOs while capacity sits idle in the other pool.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Not Every Input Needs Everything: Unifying Expert Gating, Model Cascades, and Agent Orchestration](https://arxiv.org/abs/2611.34112)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、LLM routing，核心内容是《Not Every Input Needs Everything: Unifying Expert Gating, Model Cascades, and Agent Orchestration》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Discrete hard selection accounts for 70%, 83%, and 91% of token-, query-, and task-scale literature respectively, and computational overhead appears as a top operational bottleneck across every layer.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：70%、83%、91%。
- [DFly2: Turbocharging Long-Context Speculative Decoding by Sharing the Target's Sparsity](https://arxiv.org/abs/2611.34776)
  - 主题: Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference，核心内容是《DFly2: Turbocharging Long-Context Speculative Decoding by Sharing the Target's Sparsity》在 arXiv cs.CL 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，At high concurrency on DS-V4.1-Flash, at matched per-user decode speed, its throughput is 62% and 81% higher on two 64K sets.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：62%、81%、3.9%。
- [Partial Routing: Trace-Tuned Delegation for Resource-Efficient Agentic Workflows](https://arxiv.org/abs/2611.33402)
  - 主题: Agent systems and multi-agent efficiency, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、LLM routing，核心内容是《Partial Routing: Trace-Tuned Delegation for Resource-Efficient Agentic Workflows》在 arXiv cs.CL 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，With $\delta = 0.75$, it raises the lead's ViBench score from 70.2 to 78.5 at 19% lower cost, and its Terminal-Bench pass rate from 54% to 61% at similar cost.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：19%、54%、61%。
- [Routing and Cache Retention for Multi-Turn LLM Inference: Theory and Implementation](https://arxiv.org/abs/2611.34584v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《Routing and Cache Retention for Multi-Turn LLM Inference: Theory and Implementation》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，In real GPU cluster experiments serving a 197-billion-parameter mixture-of-experts model on multi-turn software-engineering agent benchmarks (SWE and Terminal-Bench), PARK outperforms all five load-balancing and prefix-aware baselines across contrasting traffic regimes.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [CoordRoute: Coordinated Multi-Model Routing for Maximum Compute-Budget Utility](https://arxiv.org/abs/2611.34161v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《CoordRoute: Coordinated Multi-Model Routing for Maximum Compute-Budget Utility》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，On Azure Conversation and BurstGPT traces, CoordRoute improves total satisfaction by 18.72% over the strongest existing router.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：18.72%。
- [Do We Really Need an LLM for Weight-Space Programming? A Deterministic Forward-Only Paradigm and Its Capability Boundaries](https://arxiv.org/abs/2611.34612)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Do We Really Need an LLM for Weight-Space Programming? A Deterministic Forward-Only Paradigm and Its Capability Boundaries》在 arXiv cs.AI 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，We show that for core structured editing regimes, an LLM optimizer is unnecessary, and introduce Forward Weight-Space Programming (FWSP): a deterministic pipeline combining probing, localization, stratified operators (O1-O4), automatic blind routing (83.3% vs.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：83.3%、84.2%、9.4%。
- [DuoMI: Dual Mutual Information Regularization for Expert Reuse in Looped Transformers](https://arxiv.org/abs/2611.33952)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《DuoMI: Dual Mutual Information Regularization for Expert Reuse in Looped Transformers》在 arXiv cs.AI 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，On a looped OLMoE backbone in which paired adjacent layers share experts, DuoMI improves the average score across $15$ downstream tasks from $50.08\%$ to $51.82\%$, a gain of $1.74$ percentage points over the looped baseline.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [ModelLess: A Serverless System for Multi-Tier LLM Inference on Shared GPUs](https://arxiv.org/abs/2611.32634v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《ModelLess: A Serverless System for Multi-Tier LLM Inference on Shared GPUs》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On one node, a single four-hour run per policy shows that pausing yields 22% more borrower tokens per held GPU sample than abort-and-requeue, with the same median online latency.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：22%、38%。
- [RoboEvo$^2$: Recursive Robot Self-Improvement via Harness-Policy Co-Evolution](https://arxiv.org/abs/2611.34675v1)
  - 主题: Coding agent routing, LLM routing
  - 中文解读: 这项工作主要关注Coding agent routing、LLM routing，核心内容是《RoboEvo$^2$: Recursive Robot Self-Improvement via Harness-Policy Co-Evolution》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Through recursive co-evolution without additional human demonstrations, RoboEvo$^2$ improves standalone success from 11.0% to 84.1% and hybrid success from 30.4% to 90.5% on LIBERO-PRO, with similar gains and reduced agentic costs on RoboTwin C2R.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：11.0%、84.1%、30.4%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

