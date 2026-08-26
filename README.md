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

- 日期: 2026-08-26
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 4
- 日报: `papers/2026-08-26.md`
- 周报: `digests/weekly-2026-08-26.md`

## 今日最值得看

- [SAEM: Stage-Aware Expert Management for Memory-Efficient MoE Inference in Chain-of-Thought Reasoning](https://arxiv.org/abs/2608.21614)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《SAEM: Stage-Aware Expert Management for Memory-Efficient MoE Inference in Chain-of-Thought Reasoning》在 arXiv cs.DC 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，On mathematical and scientific reasoning workloads, SAEM achieves an average 1.33x throughput improvement over the strongest state-of-the-art caching and offloading baselines under constrained GPU memory, rising to 1.54x when calibration data matches the workload, demonstrating the effectiveness of stage-aware, locality-driven MoE inference for CoT reasoning.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.33x、1.54x。
- [When KV Meets Embeddings: Dynamic GPU Memory Allocation for Accelerating Generative Recommender Serving](https://arxiv.org/abs/2605.04450)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《When KV Meets Embeddings: Dynamic GPU Memory Allocation for Accelerating Generative Recommender Serving》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Evaluations on three production-scale datasets over a 32-node A100 cluster show that RACER reduces P99 latency by 24-38\% over the best static policy and achieves 93.5-99.6\% SLO satisfaction across Steady, Trend, and Burst workloads, significantly outperforming state-of-the-art baselines without sacrificing throughput.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [PowerSlider: Exploiting Phase Asymmetry for LLM Serving under Demand Response](https://arxiv.org/abs/2608.21719)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《PowerSlider: Exploiting Phase Asymmetry for LLM Serving under Demand Response》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，\sys{} does so with a new Flex SLO contract that turns bounded user slack into an optimization constraint, prefill--think--answer disaggregation exposing per-stage frequency and KV control, and a Karush--Kuhn--Tucker (KKT) online solver re-solving within 7.7 ms of every cap change, backed by a consolidated fail-safe that power-gates drained instances when DVFS bottoms out on static power.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：7.7 ms。
- [GraniKV: Asymmetric Granularity KV-Cache Paging for Multi-Agent Systems with Long Shared Prefix](https://arxiv.org/abs/2608.15584)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《GraniKV: Asymmetric Granularity KV-Cache Paging for Multi-Agent Systems with Long Shared Prefix》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The gain decomposes: cascade attention integration contributes the majority at saturation; the asymmetric storage layer adds $1.05$--$1.15\times$ end-to-end while being what makes the batched-GEMM prefix backend possible at all.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [MAVEN-T: Reinforced Heterogeneous Distillation for Real-Time Multi-Agent Trajectory Prediction](https://arxiv.org/abs/2604.10169)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《MAVEN-T: Reinforced Heterogeneous Distillation for Real-Time Multi-Agent Trajectory Prediction》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experiments on NGSIM, HighD, MoCAD, Argoverse~2, and the Waymo Open Motion Dataset evaluate accuracy, efficiency, generalization, robustness, and closed-loop safety.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [SchemaRouter: Field-Aware Tool Routing for Efficient Heterogeneous Agentic RAG](https://arxiv.org/abs/2608.21375)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《SchemaRouter: Field-Aware Tool Routing for Efficient Heterogeneous Agentic RAG》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，It uses 227 retrieved-context tokens versus 2,066 for fetch-everything and achieves 2.7x lower end-to-end latency than prompt-all.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：2.7x。
- [E2LLM: Towards Efficient LLM Serving in Heterogeneous Edge/Fog Environments](https://arxiv.org/abs/2606.03770)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《E2LLM: Towards Efficient LLM Serving in Heterogeneous Edge/Fog Environments》在 arXiv cs.DC 这一方向上的推进。强调异构硬件协同推理。从实验上看，Compared to the Splitwise baseline, E2LLM reduces average waiting time by over 50% under high-demand conditions
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：50%。
- [KVBoost: Chunk-Level Key-Value Cache Reuse with Deviation-Guided Recomputation for Efficient Large Language Model Inference](https://arxiv.org/abs/2608.21362)
  - 主题: Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference，核心内容是《KVBoost: Chunk-Level Key-Value Cache Reuse with Deviation-Guided Recomputation for Efficient Large Language Model Inference》在 arXiv cs.DC 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，Evaluated on Qwen/Qwen2.5-3B over 1,000 bug-localization samples, KVBoost achieves a 4.49x reduction in time-to-first-token (142.4 ms vs.\ 639.1 ms) and outperforms prefix caching by 16%, with no loss in accuracy (99.2% vs.\ 99.1%).
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：4.49x、142.4 ms、639.1 ms。
- [Disagree to Explore, Agree to Commit: Routing-Guided Test-Time Scaling for Software Agents](https://arxiv.org/abs/2608.22191)
  - 主题: Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Coding agent routing、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Disagree to Explore, Agree to Commit: Routing-Guided Test-Time Scaling for Software Agents》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Risa's routing arbitration raises the macro-average resolved rate from 44.9% under uniform sampling to 48.2% on the gpt-oss family, matching text consensus without answer-string matching, and it transfers to Qwen3.6, where it improves on uniform choice and matches text consensus on the full 500-task benchmark.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：44.9%、48.2%。
- [WnW: Waxing-and-Waning KV Cache for Long-Form Speech LLMs](https://arxiv.org/abs/2608.22704)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《WnW: Waxing-and-Waning KV Cache for Long-Form Speech LLMs》在 arXiv cs.CL 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，On LibriSpeech-Long with two 3B backbones (Voxtral-mini-3b and Qwen2.5-Omni-3B), WnW preserves near-Full-Cache accuracy while keeping only 20% of audio tokens on GPU, where prefill-only baselines fail to terminate.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：20%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

