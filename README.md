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

- 日期: 2026-08-15
- 今日新论文: 15
- 今日新权威来源更新: 1
- 本周精选论文: 25
- 本周精选权威来源更新: 6
- 日报: `papers/2026-08-15.md`
- 周报: `digests/weekly-2026-08-15.md`

## 今日最值得看

- [Multi-Agent Scheduling with LLM-Assisted Contract Net Negotiation for Stream Processing in Mobile Edge Computing](https://arxiv.org/abs/2608.12371)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Multi-Agent Scheduling with LLM-Assisted Contract Net Negotiation for Stream Processing in Mobile Edge Computing》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Under the evaluated configurations, MAS-DecStream reduces latency violations to 3\%, eliminates resource overcommitment, reaches a conflict-resolution rate of 0.91 with 20 agents, and improves utility by up to 22\% over the multi-round rule-based baseline.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Dual-Flow Transformers: Decoupling the Primary Prefill Path from Additional Decode Computation](https://arxiv.org/abs/2608.12385)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Dual-Flow Transformers: Decoupling the Primary Prefill Path from Additional Decode Computation》在 arXiv cs.AI 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，These experiments expose a prefill-decode-quality trade-off and demonstrate the potential of phase-specific expert allocation.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [TEMPO: Makespan-Aware Expert-Parallel Load Balancing Across Memory- and Compute-Bound Regimes](https://arxiv.org/abs/2608.13057)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《TEMPO: Makespan-Aware Expert-Parallel Load Balancing Across Memory- and Compute-Bound Regimes》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，End-to-end on Testbed~B, Qwen3-235B (inside the win region) gains $4$--$6\%$ throughput and cuts p99 latency by ${\sim}15.6\%$; DeepSeek-V3 (outside, communication-dominated) shows only mechanism cost.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [FlashDrive: Flash Vision-Language-Action Inference for Autonomous Driving](https://arxiv.org/abs/2608.12932)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《FlashDrive: Flash Vision-Language-Action Inference for Autonomous Driving》在 arXiv cs.AI 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Applied to Alpamayo 1.5-10B with W4A8 quantization, FlashDrive reduces end-to-end latency from 717ms to 151ms (4.7x) while leaving accuracy essentially unchanged: minADE6@6.4s shifts by only 0.08m, minADE1 improves, and closed-loop collision and off-road rates improve in simulation.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：717ms、151ms、4.7x。
- [Natural Language Processing: A Comprehensive Practical Guide from Tokenisation to RLHF](https://arxiv.org/abs/2605.03799)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《Natural Language Processing: A Comprehensive Practical Guide from Tokenisation to RLHF》在 arXiv cs.CL 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，All experiments are conducted on a single evolving corpus, and the work advocates open weight models over commercial APIs, with special attention to the Hugging Face ecosystem.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [MergeOver: Post-Training Token Merging for Recursive Vision Transformers](https://arxiv.org/abs/2608.13141)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《MergeOver: Post-Training Token Merging for Recursive Vision Transformers》在 arXiv cs.LG 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，On the GPU, it reduces peak activation memory by 37.3% and 38.4% at batch sizes 1 and 16, while throughput decreases by 21.7% at batch size 1 but increases by 21.7% at batch size 16.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：37.3%、38.4%、21.7%。
- [When Does Trace-Driven Evaluation Mislead MoE Expert Caching? Replay Semantics, Workload Contamination, and Operating Regimes](https://arxiv.org/abs/2608.07911)
  - 主题: Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference，核心内容是《When Does Trace-Driven Evaluation Mislead MoE Expert Caching? Replay Semantics, Workload Contamination, and Operating Regimes》在 arXiv cs.LG 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，A causal next-use predictor, used as an eviction rule, recovers -11.4% of the gap; it picks an optimal victim 3.4% of the time, against 2.4% for a random resident block and 20.6-22.1% for LRU and LFRU.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：11.4%、3.4%、2.4%。
- [Heterogeneity-Aware Belief Synchronization for Semantic Communication in AI-Native 6G Networks](https://arxiv.org/abs/2608.13394)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Heterogeneity-Aware Belief Synchronization for Semantic Communication in AI-Native 6G Networks》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，By exchanging compact belief updates through a latent translation model only when necessary, the framework preserves privacy, reduces synchronization cost, and minimizes local knowledge drift.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Moral Hazard in Multi-Agent Language Models](https://arxiv.org/abs/2607.23982)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《Moral Hazard in Multi-Agent Language Models》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Their effects are heterogeneous: SmolLM3-3B and OLMo-7B show the clearest mechanism-consistent, weight-level gains, whereas GEPA sometimes raises team success while reducing or eliminating costly queries.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Learning Latency-Aware Orchestration for Multi-Agent Systems](https://arxiv.org/abs/2601.10560)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《Learning Latency-Aware Orchestration for Multi-Agent Systems》在 arXiv cs.CL 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experiments on four benchmarks show that LAMaS achieves the best latency among evaluated learning-based MAS baselines, reducing end-to-end latency by over 50% while maintaining competitive or better accuracy.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：50%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

