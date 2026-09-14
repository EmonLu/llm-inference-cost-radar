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

- 日期: 2026-09-14
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 5
- 日报: `papers/2026-09-14.md`
- 周报: `digests/weekly-2026-09-14.md`

## 今日最值得看

- [Dynamic Expert Quantization for Scalable Mixture-of-Experts Inference](https://arxiv.org/abs/2511.15015)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Dynamic Expert Quantization for Scalable Mixture-of-Experts Inference》在 arXiv cs.LG 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Across Qwen3-MoE-30B/80B and six benchmarks, DynaExq improves accuracy over static PTQ on Qwen3-80B (73.09% to 77.57%) under comparable device-memory budgets and achieves up to 2.73x higher throughput than offloading/prefetch baselines at batch size 32.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：73.09%、77.57%、2.73x。
- [UltraQuant: 4-bit KV Caching for Context-Heavy Agents](https://arxiv.org/abs/2606.20474)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《UltraQuant: 4-bit KV Caching for Context-Heavy Agents》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On an adaptive-SLO replay of production Claude Code traces, UltraQuant sustains 2.71x (MiniMax-M2.5) and 4.38x (Qwen3-235B) the qualified-request throughput of the BF16 baseline, matching or exceeding hardware FP8 KV while using half the KV bytes.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：2.71x、4.38x。
- [Behavior Quotient Learning for Low-Rank Adaptation of LLM Agents](https://arxiv.org/abs/2609.12896)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Behavior Quotient Learning for Low-Rank Adaptation of LLM Agents》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experiments on AppWorld and BrowseComp-Plus compare BQ-LoRA with standard LoRA and recent low-rank adaptation methods, while separate ablations evaluate the complementary contributions of both components.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [DeepStack: Facilitating Co-Design Exploration of 3D DRAM-Stacked Accelerators for Distributed LLM Inference](https://arxiv.org/abs/2604.04750)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《DeepStack: Facilitating Co-Design Exploration of 3D DRAM-Stacked Accelerators for Distributed LLM Inference》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，A search-space ablation shows that restricted DSE baselines can miss up to 9.5x modeled throughput.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：9.5x、000x。
- [Quality-Constrained Routing over a Fixed Pool of Quantized Mixture-of-Experts Instances](https://arxiv.org/abs/2609.12550)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Quality-Constrained Routing over a Fixed Pool of Quantized Mixture-of-Experts Instances》在 arXiv cs.LG 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，Under the same population and $\tau=0.1513$, FWP allocation reaches a $1.284\times$ offline model-based multiplier versus $1.253\times$ for request-agnostic mixing and $1.000\times$ for static W4, an incremental $2.5\%$ relative FWP gain.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [NS-Copilot: An LLM-Driven Agent System for Autonomous Neuroscience Analysis](https://arxiv.org/abs/2609.01971)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《NS-Copilot: An LLM-Driven Agent System for Autonomous Neuroscience Analysis》在 arXiv cs.CL 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，We evaluate NS-Copilot on neuroscience benchmarks spanning Alzheimer's disease, Parkinson's disease, and working memory spike decoding.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Efficient Vision-Language-Action Management and Serving for Robot Factories](https://arxiv.org/abs/2609.12075)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Efficient Vision-Language-Action Management and Serving for Robot Factories》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，In a large-scale experiment of serving 8 different models on a 4-GPU server, Robion can serve up to 64 robots within 98% SLO attainment.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：98%。
- [HoliBench: A Cross-Platform Benchmarking and Deployment Toolkit for Foundation Models in CPS-IoT Applications](https://arxiv.org/abs/2609.12412)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《HoliBench: A Cross-Platform Benchmarking and Deployment Toolkit for Foundation Models in CPS-IoT Applications》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，In a multi-model CPS deployment, standalone profiles predict combined-pipeline latency and power within 1.2% and 2.5%, enabling deployment exploration without exhaustively profiling every pipeline configuration.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.2%、2.5%。
- [A Dynamic Vertical Scaling Strategy for Distributed Stream Processing Applications in Edge Computing](https://arxiv.org/abs/2609.12975)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《A Dynamic Vertical Scaling Strategy for Distributed Stream Processing Applications in Edge Computing》在 arXiv cs.DC 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，In EdgeStreamPy simulation experiments with two application profiles, two workloads, and ten paired placements per combination, the selected policies preserved throughput, obtained mean violation rates from 0.03% to 0.30%, below VRebalance in every scenario, and used less CPU in three of four combinations.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：0.03%、0.30%。
- [Attention Quantization for Tabular Foundation Models](https://arxiv.org/abs/2609.13031)
  - 主题: Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference，核心内容是《Attention Quantization for Tabular Foundation Models》在 arXiv cs.LG 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，Our Triton kernel achieves a speedup up to 1.7x over regular 16-bit kernels, and we show that on TabPFN-v3 and TabICLv2 there is no relevant accuracy loss across TabArena and BeyondArena.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.7x。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

