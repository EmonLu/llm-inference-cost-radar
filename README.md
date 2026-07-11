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

- 日期: 2026-07-11
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 2
- 日报: `papers/2026-07-11.md`
- 周报: `digests/weekly-2026-07-11.md`

## 今日最值得看

- [What to Keep, What to Forget: A Rate--Distortion View of Memory Compaction in LLMs and Agents](https://arxiv.org/abs/2607.08032v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《What to Keep, What to Forget: A Rate--Distortion View of Memory Compaction in LLMs and Agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，We turn both observations into a benchmark proposal, a small reference experiment, and a set of compaction-aware design principles, and we map the open problems.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [PolyWorkBench: Benchmarking Multilingual Long-Horizon LLM Agents](https://arxiv.org/abs/2607.06008)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《PolyWorkBench: Benchmarking Multilingual Long-Horizon LLM Agents》在 arXiv cs.CL 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，However, most existing benchmarks implicitly assume a monolingual setting, where the entire execution process, including reasoning, tool invocation, and output generation, is conducted within a single language.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Collate: Collaborative Neural Network Learning for Latency-Critical Edge Systems](https://arxiv.org/abs/2607.08013)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Collate: Collaborative Neural Network Learning for Latency-Critical Edge Systems》在 arXiv cs.DC 这一方向上的推进。强调异构硬件协同推理。从实验上看，Extensive experiments indicate that, compared to state-of-the-art methods and under a latency constraint, our extended models can improve the accuracy by 1.96% on average, and our shrunk models can also obtain a 3.09% accuracy improvement on average, with almost no extra training overhead.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.96%、3.09%。
- [Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents](https://arxiv.org/abs/2607.08448v1)
  - 主题: Coding agent routing, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Coding agent routing、Cost-efficient LLM inference，核心内容是《Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across perturbed tabletop, household kitchen, and clean-to-randomized bimanual manipulation, Harness VLA improves over the strongest relevant baselines by 38.6 and 25.4 percentage points on LIBERO-Pro and RoboCasa365, respectively, and reaches 58.4% on RoboTwin C2R.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：58.4%。
- [Single-Rollout Asynchronous Optimization for Agentic Reinforcement Learning](https://arxiv.org/abs/2607.07508v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《Single-Rollout Asynchronous Optimization for Agentic Reinforcement Learning》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，SAO is able to train stably for one thousand steps and consistently outperform GRPO and its variants on agentic coding and reasoning benchmarks, such as SWE-Bench Verified, BeyondAIME, and IMOAnswerBench.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [PolyUQuest: Verifiable Structure-Aware Web RAG over Heterogeneous Graphs](https://arxiv.org/abs/2607.08269)
  - 主题: Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference、LLM routing，核心内容是《PolyUQuest: Verifiable Structure-Aware Web RAG over Heterogeneous Graphs》在 arXiv cs.AI 这一方向上的推进。强调异构硬件协同推理。从实验上看，PolyUQuest outperforms existing RAG systems in answer correctness, coverage, and faithfulness, while consuming significantly fewer LLM tokens per query.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Image classification via a quantum-inspired strategy involving a mixture of experts](https://arxiv.org/abs/2607.07754)
  - 主题: Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference，核心内容是《Image classification via a quantum-inspired strategy involving a mixture of experts》在 arXiv cs.LG 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Using MNIST and Fashion-MNIST datasets as benchmarks, we demonstrate that the joint expert analysis outperforms the individual expert one, as well as reduces the failure rate of image class prediction by around a factor of two.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [TTHE: Test-Time Harness Evolution](https://arxiv.org/abs/2607.08124)
  - 主题: Agent systems and multi-agent efficiency
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency，核心内容是《TTHE: Test-Time Harness Evolution》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，These results recast test-time adaptation for LLM agents as evolution over executable control programs and identify execution-derived proxy reliability as a central challenge for robust unsupervised agent improvement.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Multi-Agent Robotic Control with Onboard Vision-Language Models](https://arxiv.org/abs/2607.07403v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《Multi-Agent Robotic Control with Onboard Vision-Language Models》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Results demonstrate that a fully onboard MAS architecture is a viable, cost-efficient alternative to cloud-dependent deployments, with strong potential for real-world transfer.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [MetaHGNIE: Meta-Path Induced Hypergraph Contrastive Learning in Heterogeneous Knowledge Graphs](https://arxiv.org/abs/2512.12477)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《MetaHGNIE: Meta-Path Induced Hypergraph Contrastive Learning in Heterogeneous Knowledge Graphs》在 arXiv cs.LG 这一方向上的推进。强调异构硬件协同推理。从实验上看，Extensive experiments on multiple benchmark datasets demonstrate that DualHNIE outperforms state-of-the-art methods, validating the effectiveness of explicit high-order modeling and disentangled dual-channel representation learning for heterogeneous knowledge graphs.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

