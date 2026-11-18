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

- 日期: 2026-11-18
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 6
- 日报: `papers/2026-11-18.md`
- 周报: `digests/weekly-2026-11-18.md`

## 今日最值得看

- [HyCoInfer: Cloud-Edge Collaborative Inference for Large Language Models on Heterogeneous GPU-FPGA Architectures](https://arxiv.org/abs/2611.22086v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《HyCoInfer: Cloud-Edge Collaborative Inference for Large Language Models on Heterogeneous GPU-FPGA Architectures》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，At 500 Mbps, HyCoInfer delivers up to 4.11 times the request goodput of cloud-only vLLM and reduces mean end-to-end latency by up to 61.1%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：500 Mb、61.1%。
- [JigSLO: Solving the Resource Puzzle for Efficient Multi-LLM Serving](https://arxiv.org/abs/2509.06261)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《JigSLO: Solving the Resource Puzzle for Efficient Multi-LLM Serving》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Guided by these predictions, its placement algorithm jointly selects each instance's tensor parallelism, compute share, and batch configuration, pairing complementary memory-access patterns to maximize throughput within each model's latency targets.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [LaFlash: Capacity-Driven Acceleration for Coding Agent Workflows via QLC-HBF](https://arxiv.org/abs/2611.22746v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《LaFlash: Capacity-Driven Acceleration for Coding Agent Workflows via QLC-HBF》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On end-to-end coding agent workloads, LaFlash achieves 7.04$\times$ higher throughput and 10.96$\times$ higher energy efficiency over SLC-HBF with batch expansion, and 2.36$\times$ higher throughput over QLC-HBF with CDA.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [TeleChat to Xing4: Advancing Frontier Agentic Models on Domestic Chips and Frameworks](https://arxiv.org/abs/2611.22115v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《TeleChat to Xing4: Advancing Frontier Agentic Models on Domestic Chips and Frameworks》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，CPU affinity and core isolation further reduce host scheduling interference.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [XM-Sparse: High-Throughput Sparse-Attention LLM Serving over Scale-up Memory Pools](https://arxiv.org/abs/2611.22280)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《XM-Sparse: High-Throughput Sparse-Attention LLM Serving over Scale-up Memory Pools》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，We have implemented XM-Sparse atop SGLang, and our experiments on DeepSeek-V3.2 and GLM-5.3 with an emulated scale-up memory pool show that XM-Sparse delivers up to 4.98$\times$ and 4.52$\times$ higher decode throughput than PCIe-based ECHO and HiSparse, respectively, and up to 1.34$\times$ over a naive integration on the same platform, across 16K-1M contexts.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Communicate the Change: Efficient Expert Parallelism via Activation Compression](https://arxiv.org/abs/2611.22215)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Communicate the Change: Efficient Expert Parallelism via Activation Compression》在 arXiv cs.DC 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，EchoMoE reduces inter-node communication volume by 58% and improves throughput by 22.6%, while preserving average performance within 3.8 percentage points across 18 benchmarks.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：58%、22.6%、2.38x。
- [IA-MoE: An Intensity-Aware Mixture of Experts for DNN Inference](https://arxiv.org/abs/2611.19669)
  - 主题: Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference，核心内容是《IA-MoE: An Intensity-Aware Mixture of Experts for DNN Inference》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Training on the remaining request time after each decision removes this myopia and reduces the mean delay by 12-56% on congested workloads.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：56%、27%。
- [Localized LoRA-MoE: Mixture of Low-Rank Experts With Adaptive Routing](https://arxiv.org/abs/2607.05114)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Localized LoRA-MoE: Mixture of Low-Rank Experts With Adaptive Routing》在 arXiv cs.CL 这一方向上的推进。强调异构硬件协同推理。从实验上看，When fine-tuning a language model on six interleaved GLUE tasks, task-conditioned routing at a fixed adapter budget outperforms LoRA and static localized adapters, matching per-task adapters with 6x budgets.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：6x。
- [SLED: Sensor SLicing from Edge to Datacenter](https://arxiv.org/abs/2611.21937v1)
  - 主题: Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Coding agent routing、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《SLED: Sensor SLicing from Edge to Datacenter》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Scaling evaluations on the two RAN stacks show that throughput remains within 0.9% and 1.4% of expected allocations even as the number of sensor slices increases.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：0.9%、1.4%。
- [EmbedGym: Letting Coding Agents Develop and Debug Embedded Firmware Without Physical Hardware](https://arxiv.org/abs/2611.21845v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing，核心内容是《EmbedGym: Letting Coding Agents Develop and Debug Embedded Firmware Without Physical Hardware》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Our results also show that an agent with EmbedGym outperforms prior embedded agent frameworks, and lightweight models with EmbedGym match frontier models without it at 30-70x lower cost.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：70x、99.7%、19.9%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

