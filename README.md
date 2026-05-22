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

- 日期: 2026-05-22
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 3
- 日报: `papers/2026-05-22.md`
- 周报: `digests/weekly-2026-05-22.md`

## 今日最值得看

- [CacheClip: Accelerating RAG with Effective KV Cache Reuse](https://arxiv.org/abs/2510.10129)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《CacheClip: Accelerating RAG with Effective KV Cache Reuse》在 arXiv cs.LG 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Experiments show CacheClip retains up to 85.2% and 91.1% of full-attention performance on NIAH and LongBench, outperforming CacheBlend and APE by 16.1 and 12.8 points on NIAH, and by 4.5 and 4.2 points on LongBench (with recomp% = 20%).
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：85.2%、91.1%、20%。
- [SpaceMoE: Realizing Distributed Mixture-of-Experts Inference over Space Networks](https://arxiv.org/abs/2605.00515)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《SpaceMoE: Realizing Distributed Mixture-of-Experts Inference over Space Networks》在 arXiv cs.DC 这一方向上的推进。强调异构硬件协同推理。从实验上看，Experiments over a thousand-satellite constellation show that SpaceMoE achieves at least a threefold latency reduction compared with conventional random and ablation-based placement strategies.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [InnerQ: Hardware-Aware Tuning-Free Quantization of KV Cache for Large Language Models](https://arxiv.org/abs/2602.23200)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《InnerQ: Hardware-Aware Tuning-Free Quantization of KV Cache for Large Language Models》在 arXiv cs.CL 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Beyond reducing latency, experiments on Llama and Mistral models show that InnerQ also improves few-shot evaluation scores relative to prior KV cache quantization methods.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [AutoMCU: Feasibility-First MCU Neural Network Customization via LLM-based Multi-Agent Systems](https://arxiv.org/abs/2605.21560v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《AutoMCU: Feasibility-First MCU Neural Network Customization via LLM-based Multi-Agent Systems》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experiments on CIFAR-10 and CIFAR-100 under strict MCU constraints show that AutoMCU achieves competitive accuracy while reducing customization time to about 1--2 hours, compared with hundreds of GPU hours for representative MCU-oriented HW-NAS baselines.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [WarmServe: Enabling One-for-Many GPU Prewarming for Multi-LLM Serving](https://arxiv.org/abs/2512.09472)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《WarmServe: Enabling One-for-Many GPU Prewarming for Multi-LLM Serving》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Evaluation on real-world datasets shows that WarmServe reduces tail TTFT by up to 50.8$\times$ compared to the state-of-the-art autoscaling-based system, while supporting up to 2.5$\times$ higher request throughput than the GPU-sharing system.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [AgentCo-op: Retrieval-Based Synthesis of Interoperable Multi-Agent Workflows](https://arxiv.org/abs/2605.20425)
  - 主题: Agent systems and multi-agent efficiency
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency，核心内容是《AgentCo-op: Retrieval-Based Synthesis of Interoperable Multi-Agent Workflows》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On six coding, math, and question-answering benchmarks, AgentCo-op achieves the best result on four benchmarks and the best average score under a unified backbone setting, while consistently reducing per-task cost relative to multi-agent baselines.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [MASFactory: A Graph-centric Framework for Orchestrating LLM-Based Multi-Agent Systems with Vibe Graphing](https://arxiv.org/abs/2603.06007)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《MASFactory: A Graph-centric Framework for Orchestrating LLM-Based Multi-Agent Systems with Vibe Graphing》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，We evaluate MASFactory on seven public benchmarks, validating both reproduction consistency for representative MAS methods and the effectiveness of Vibe Graphing.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [LiteCoOp: Lightweight Multi-LLM Shared-Tree Reasoning for Model-Serving Compiler Optimizations](https://arxiv.org/abs/2602.01935)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《LiteCoOp: Lightweight Multi-LLM Shared-Tree Reasoning for Model-Serving Compiler Optimizations》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，This eight-model config reduces total compilation time by 1.95x (1.74x), reduces API cost by 4.47x (4.32x), and invokes the largest model for only 23.1% (23.9%) of total calls while demonstrating collaboration scalability.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.95x、1.74x、4.47x。
- [Maestro: Reinforcement Learning to Orchestrate Hierarchical Model-Skill Ensembles](https://arxiv.org/abs/2605.22177v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Maestro: Reinforcement Learning to Orchestrate Hierarchical Model-Skill Ensembles》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，With only a 4B orchestrator, Maestro achieves an average accuracy of 70.1%, surpassing both GPT-5 (69.3%) and Gemini-2.5-Pro (68.7%).
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：70.1%、69.3%、68.7%。
- [LIDSA: Cognitive Arbitration for Signal-Free Autonomous Intersection Management](https://arxiv.org/abs/2605.12321)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《LIDSA: Cognitive Arbitration for Signal-Free Autonomous Intersection Management》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Results show that LIDSA reduces mean control delay by up to 89.1% and maintains Level of Service C while all non-LLM baselines degrade to Level of Service F.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：89.1%、48.8%、86.2%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

