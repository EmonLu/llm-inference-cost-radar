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

- 日期: 2026-06-15
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 4
- 日报: `papers/2026-06-15.md`
- 周报: `digests/weekly-2026-06-15.md`

## 今日最值得看

- [ProServe: Unified Multi-Priority Request Scheduling for LLM Serving](https://arxiv.org/abs/2512.12928)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《ProServe: Unified Multi-Priority Request Scheduling for LLM Serving》在 arXiv cs.DC 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，Extensive evaluation on four open-source and one industrial dataset shows that ProServe outperforms state-of-the-art baselines, improving system gain by up to 35% and SLO attainment by up to 52%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：35%、52%。
- [Efficient On-Device Diffusion LLM Inference with Mobile NPU](https://arxiv.org/abs/2606.13740)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Efficient On-Device Diffusion LLM Inference with Mobile NPU》在 arXiv cs.LG 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，llada.cpp reduces LLaDA-8B generation latency by 17x-42x over the CPU baseline with prefix KV cache reuse, while preserving generation quality.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：17x、42x。
- [When Should Agent Trust Be Conditional? Characterizing and Attacking Skill-Conditional Reputation in Agent Swarms](https://arxiv.org/abs/2606.14200v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《When Should Agent Trust Be Conditional? Characterizing and Attacking Skill-Conditional Reputation in Agent Swarms》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On a public benchmark of 14 genuinely heterogeneous AppWorld agents, real pools land inside the beneficial regime--a small but genuine gain, with the per-skill best agent genuinely changing across skills.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Orchestra-o1: Omnimodal Agent Orchestration](https://arxiv.org/abs/2606.13707)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《Orchestra-o1: Omnimodal Agent Orchestration》在 arXiv cs.CL 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，This scalable design allows agent systems to effectively tackle complex real-world tasks involving heterogeneous information sources, surpassing the second-best approach by 10.3% accuracy on the OmniGAIA benchmark.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：10.3%。
- [Expert-Driven Survival Machines: Improving Stratification and Interpretability in Multiple Clinical Cohorts](https://arxiv.org/abs/2606.14608)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Expert-Driven Survival Machines: Improving Stratification and Interpretability in Multiple Clinical Cohorts》在 arXiv cs.LG 这一方向上的推进。强调异构硬件协同推理。从实验上看，The proposed method demonstrates improved predictive performance and leads to interpretable results in survival analysis.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Exact Linear Attention](https://arxiv.org/abs/2605.18848)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Exact Linear Attention》在 arXiv cs.LG 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Experimental results demonstrate that ELA achieves up to 6x faster decoding speed and 75% reduction in KV cache memory usage compared to full attention, while maintaining comparable or superior training performance.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：6x、75%、4.3x。
- [LoMC: Localized Multidirectional Correction for Refusal Suppression in Routed Foundation Models](https://arxiv.org/abs/2606.13709)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《LoMC: Localized Multidirectional Correction for Refusal Suppression in Routed Foundation Models》在 arXiv cs.LG 这一方向上的推进。强调异构硬件协同推理。从实验上看，Experiments on text-only and multimodal safety benchmarks across four routed backbones show that LoMC substantially improves non-refusal target-response behavior while maintaining general capability under a compact intervention footprint.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Fast Autoregressive Video Diffusion and World Models with Temporal Cache Compression and Sparse Attention](https://arxiv.org/abs/2602.01801)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Fast Autoregressive Video Diffusion and World Models with Temporal Cache Compression and Sparse Attention》在 arXiv cs.AI 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Experiments demonstrate up to x5 - x10 end-to-end speedups while preserving near-identical visual quality and, crucially, maintaining stable throughput and nearly constant peak GPU memory usage over long rollouts, where prior methods progressively slow down and suffer from increasing memory usage.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Towards Direct Latent-Space Synthesis for Parallel Branches in LLM-Agent Workflows](https://arxiv.org/abs/2606.14672v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《Towards Direct Latent-Space Synthesis for Parallel Branches in LLM-Agent Workflows》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，It also reduces time-to-first-token by 2.5x-11x, suggesting that direct cache-based synthesis is a promising interface for more native and efficient synthesis over parallel agent branches.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：2.5x、11x。
- [When Errors Become Narratives: A Longitudinal Taxonomy of Silent Failures in a Production LLM Agent Runtime](https://arxiv.org/abs/2606.14589)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《When Errors Become Narratives: A Longitudinal Taxonomy of Silent Failures in a Production LLM Agent Runtime》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Three findings: about 70% of silent failures were caught by human user-view observation, not tests or audits; a retrospective audit of 15 incidents found 0% ex-ante prevention but 87% regression blocking -- audits are regression engines, not prediction engines; incident latency (13 hours to 60 days) tracks failure mechanism, not code complexity -- the longest-lived failures lived in the seams between components, where no test runs.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：70%、0%、87%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

