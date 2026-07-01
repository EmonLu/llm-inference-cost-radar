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

- 日期: 2026-07-01
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 2
- 日报: `papers/2026-07-01.md`
- 周报: `digests/weekly-2026-07-01.md`

## 今日最值得看

- [Omni-Flow: A Unified Workflow Orchestration and Distributed KV Cache Sharing Framework for Multimodal Inference](https://arxiv.org/abs/2606.31093)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Omni-Flow: A Unified Workflow Orchestration and Distributed KV Cache Sharing Framework for Multimodal Inference》在 arXiv cs.DC 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，arXiv:2606.31093v1 Announce Type: new Abstract: As large language model (LLM) inference evolves from text-only to multimodal paradigms, inference systems face three challenges: (1) flexible orchestration of multimodal workflows, where heterogeneous computing units exhibit complex dependencies and concurrent control; (2) efficient transmission of massive intermediate data across processes and nodes, with tensors flowing at high speed among heterogeneous roles; and (3) efficient sharing of KV caches and model weights across roles to eliminate redundant GPU memory.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [TraceLab: Characterizing Coding Agent Workloads for LLM Serving](https://arxiv.org/abs/2606.30560)
  - 主题: Coding agent routing, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Coding agent routing、Cost-efficient LLM inference，核心内容是《TraceLab: Characterizing Coding Agent Workloads for LLM Serving》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，These findings point to concrete opportunities for optimizing serving, including lower-overhead tool calling, append-length-aware prefill, semantic-aware tool-latency prediction, and improved KV-cache management around human-paced gaps.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [SeKV: Resolution-Adaptive KV Cache with Hierarchical Semantic Memory for Long-Context LLM Inference](https://arxiv.org/abs/2606.31145v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《SeKV: Resolution-Adaptive KV Cache with Hierarchical Semantic Memory for Long-Context LLM Inference》在 arXiv API 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Across four benchmarks, SeKV improves over the strongest semantic compression baseline by 5.9% on average while reducing GPU memory by 53.3% versus full KV caching at 128K context.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：5.9%、53.3%、0.05%。
- [ComplianceGate: Classifier-Gated Multi-Tier LLM Routing for Inference in Regulated Industries](https://arxiv.org/abs/2606.31163v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《ComplianceGate: Classifier-Gated Multi-Tier LLM Routing for Inference in Regulated Industries》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Our evaluation on 600 queries demonstrates 39% median latency reduction, 33-52% cost savings depending on query distribution, and generation throughput of 122-200 tokens/second versus 50-64 for the baseline.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：39%、52%、200 tokens/s。
- [Demystifying the Design Space and Best Practices for Heterogeneous LLM Inference and Serving](https://arxiv.org/abs/2606.29708v2)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Demystifying the Design Space and Best Practices for Heterogeneous LLM Inference and Serving》在 arXiv API 这一方向上的推进。强调异构硬件协同推理。从实验上看，Heterogeneous prefill-decode (PD) inference is now in production: prefill on cost-efficient or supply-available accelerators, decode on bandwidth-strong ones, and KV state crossing mixed interconnects in mixed numerical formats.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [KV-RM: Regularizing KV-Cache Movement for Static-Graph LLM Serving](https://arxiv.org/abs/2605.09735)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《KV-RM: Regularizing KV-Cache Movement for Static-Graph LLM Serving》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，On a 2-GPU NVIDIA A100 node, KV-RM improves mixed-length decoding throughput and tail latency relative to a static-graph baseline, reduces reserved KV memory across workload families, and removes severe burst-time latency spikes under production-trace replay.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Clinically Structured Rank-Gated LoRA for Cross-Benchmark Medical Question Answering](https://arxiv.org/abs/2606.31432)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Clinically Structured Rank-Gated LoRA for Cross-Benchmark Medical Question Answering》在 arXiv cs.CL 这一方向上的推进。强调异构硬件协同推理。从实验上看，It improves over MoELoRA by 0.89 percentage points while using 28.1% fewer trainable parameters; a paired, benchmark-stratified bootstrap over final predictions gives a 95% confidence interval of [0.42, 1.37] for this macro-average gain.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：28.1%、95%、69.31%。
- [Think in English, Answer in Korean: Efficient Adaptation of Multilingual Tool-Using Agents](https://arxiv.org/abs/2606.31648)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《Think in English, Answer in Korean: Efficient Adaptation of Multilingual Tool-Using Agents》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，These results provide a practical recipe and failure-mode analysis for adapting post-trained multilingual models to verifiable agentic workflows under memory-constrained deployment.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：2S。
- [LLM-Aided Joint Secrecy Precoding and Trajectory for RSMA-Based Heterogeneous UAV Networks](https://arxiv.org/abs/2507.17188)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《LLM-Aided Joint Secrecy Precoding and Trajectory for RSMA-Based Heterogeneous UAV Networks》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The formulated problem is highly non-convex due to the coupling among UAV trajectories, RSMA transmission variables, and secrecy constraints.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [When LLMs Develop Languages: Symbolic Communication for Efficient Multi-Agent Reasoning](https://arxiv.org/abs/2606.29354v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、LLM routing，核心内容是《When LLMs Develop Languages: Symbolic Communication for Efficient Multi-Agent Reasoning》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across challenging benchmarks, CLSR reduces latency-oriented generated token completion by $3\sim 6\times$ compared to standard CoT while maintaining accuracy.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

