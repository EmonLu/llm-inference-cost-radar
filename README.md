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

- 日期: 2026-08-10
- 今日新论文: 7
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 4
- 日报: `papers/2026-08-10.md`
- 周报: `digests/weekly-2026-08-10.md`

## 今日最值得看

- [Rethinking Unified Memory for NPU-PIM Systems: Dual-View Memory for Dynamic Inference of LLM](https://arxiv.org/abs/2608.06989v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Rethinking Unified Memory for NPU-PIM Systems: Dual-View Memory for Dynamic Inference of LLM》在 arXiv API 这一方向上的推进。强调异构硬件协同推理。从实验上看，Our evaluation across LLMs shows that PFM improves end-to-end throughput by up to 2.32$\times$, demonstrating its effectiveness and broad applicability as a unified memory management solution for NPU-PIM systems.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [LLMRouter: Unified Infrastructure for Developing, Evaluating, and Deploying LLM Routers](https://arxiv.org/abs/2608.06867v1)
  - 主题: Cost-efficient LLM inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、LLM routing，核心内容是《LLMRouter: Unified Infrastructure for Developing, Evaluating, and Deploying LLM Routers》在 arXiv API 这一方向上的推进。聚焦大模型路由/小模型分流，直接相关。从实验上看，Our empirical study shows that learned routers outperform the strongest fixed-model baseline by 14.6% relatively, lightweight routers become more competitive under tight cost constraints, and user-conditioned routing consistently improves personalization.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：14.6%。
- [Autonomy-of-Heads: Data-Free Sparse Attention from Frozen Query-Key Geometry](https://arxiv.org/abs/2608.06849v1)
  - 主题: Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference，核心内容是《Autonomy-of-Heads: Data-Free Sparse Attention from Frozen Query-Key Geometry》在 arXiv API 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，We conducted extensive experiments across models demonstrating that at 50\% sparsity, AoH retains 96.5\% of Full Attention performance on average while reducing prefill and decode latency by up to 41.4\% and 66.0\%, respectively, and KV-cache memory by 50.0\% at 256K tokens.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Does Splitting a Triage Decision Across Agents Hide Bias or Help Catch It? A Multi-Agent Simulation Study of LLM-Based Resource Allocation Under Audit Capacity Constraints](https://arxiv.org/abs/2608.06949v1)
  - 主题: Agent systems and multi-agent efficiency
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency，核心内容是《Does Splitting a Triage Decision Across Agents Hide Bias or Help Catch It? A Multi-Agent Simulation Study of LLM-Based Resource Allocation Under Audit Capacity Constraints》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，A follow-up experiment shows that reordering the audit queue by estimated risk, rather than first-come-first-served, recovers most of the lost coverage under the same capacity constraint (65.6% to 91.7%, p = 0.028).
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：65.6%、91.7%、100.0%。
- [CubicQuant: Parametric Non-Uniform Codebooks for High-Throughput LLM Inference with 1-8-Bit Weights](https://arxiv.org/abs/2608.06763v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《CubicQuant: Parametric Non-Uniform Codebooks for High-Throughput LLM Inference with 1-8-Bit Weights》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Relative to the best enumerated four-bit finite floating-point format, the reductions were 3.90%, 9.44%, and 6.27%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：3.90%、9.44%、6.27%。
- [PsychoAgent: An Affect-Sensitive Cognitive Architecture for Conflict-Aware Memory in LLM Agents](https://arxiv.org/abs/2608.07438v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《PsychoAgent: An Affect-Sensitive Cognitive Architecture for Conflict-Aware Memory in LLM Agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，0.500 and 0.667), with a small semantic-similarity cost.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Every Cache Entry Earns Its Place: Global Allocation of Resolution and Coverage for KV Cache Compression](https://arxiv.org/abs/2608.07001v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Every Cache Entry Earns Its Place: Global Allocation of Resolution and Coverage for KV Cache Compression》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Systematic experiments across diverse long-context tasks and compression ratios show that GraceKV ranks first in 24 of 32 settings and remains robust up to 128-fold compression.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：32 s。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

