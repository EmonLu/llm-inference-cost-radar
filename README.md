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

- 日期: 2026-05-25
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 2
- 日报: `papers/2026-05-25.md`
- 周报: `digests/weekly-2026-05-25.md`

## 今日最值得看

- [AlignedServe: Orchestrating Prefix-aware Batching to Build a High-throughput and Computing-efficient LLM Serving System](https://arxiv.org/abs/2605.23389)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《AlignedServe: Orchestrating Prefix-aware Batching to Build a High-throughput and Computing-efficient LLM Serving System》在 arXiv cs.DC 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Experiments on synthetic and application workloads show that AlignedServe improves decoding throughput by up to 1.98 times and reduces latency by up to 7.4 times over state-of-the-art systems.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [ZipMoE: Efficient On-Device MoE Serving via Lossless Compression and Cache-Affinity Scheduling](https://arxiv.org/abs/2601.21198)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《ZipMoE: Efficient On-Device MoE Serving via Lossless Compression and Cache-Affinity Scheduling》在 arXiv cs.DC 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，Our evaluation reveals that ZipMoE achieves up to $72.77\%$ inference latency reduction and up to $6.76\times$ higher throughput than the state-of-the-art systems.Our code is available at: https://github.com/npnothard/ZipMoE-ICML26.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Fast-dDrive: Efficient Block-Diffusion VLM for Autonomous Driving](https://arxiv.org/abs/2605.23163)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Fast-dDrive: Efficient Block-Diffusion VLM for Autonomous Driving》在 arXiv cs.CL 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On the WOD-E2E test set, Fast-dDrive achieves SOTA ADE@3s and ADE@5s, alongside the highest RFS among diffusion-based VLAs; on nuScenes, it reduces average L2 error to $0.32$m (a $22\%$ improvement).
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：3s、5s。
- [HyperParallel-MoE: Multi-Core Interleaved Scheduling for Fast MoE Training on Ascend NPUs](https://arxiv.org/abs/2605.23764)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《HyperParallel-MoE: Multi-Core Interleaved Scheduling for Fast MoE Training on Ascend NPUs》在 arXiv cs.DC 这一方向上的推进。强调异构硬件协同推理。从实验上看，Across multiple expert-parallel configurations, HyperParallel-MoE reduces Dispatch-to-Combine MoE-FFN latency by up to 1.58x, demonstrating that tile-level heterogeneous scheduling can substantially improve MoE training efficiency on modern NPUs.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.58x。
- [TwinRouterBench: Fast Static and Live Dynamic Evaluation for Realistic Agentic LLM Routing](https://arxiv.org/abs/2605.18859)
  - 主题: Coding agent routing, LLM routing
  - 中文解读: 这项工作主要关注Coding agent routing、LLM routing，核心内容是《TwinRouterBench: Fast Static and Live Dynamic Evaluation for Realistic Agentic LLM Routing》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Routing each call to the cheapest sufficient model can cut costs without sacrificing quality, yet existing router benchmarks evaluate routers only on one-shot prompts.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Parallel Context Compaction for Long-Horizon LLM Agent Serving](https://arxiv.org/abs/2605.23296v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Parallel Context Compaction for Long-Horizon LLM Agent Serving》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，At matched compaction decode volume, it reduces end-to-end wall time and improves compaction throughput over the sequential baseline.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [ObjectCache: Layerwise Object-Storage Retrieval for KV Cache Reuse](https://arxiv.org/abs/2605.22850)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《ObjectCache: Layerwise Object-Storage Retrieval for KV Cache Reuse》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Under shared bandwidth caps, our scheduler reduces added TTFT by 1.2--1.8x compared with equal bandwidth sharing.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.8x。
- [Hybrid Edge-HPC Systems for Low-Latency Data-Driven Inference](https://arxiv.org/abs/2605.20532)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Hybrid Edge-HPC Systems for Low-Latency Data-Driven Inference》在 arXiv cs.DC 这一方向上的推进。强调异构硬件协同推理。从实验上看，Our evaluation characterizes end-to-end system behavior under realistic constraints, quantifying simulation latency, training cost, inference throughput, and the impact of delayed model updates on prediction accuracy.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [GEMQ: Global Expert-Level Mixed-Precision Quantization for MoE LLMs](https://arxiv.org/abs/2605.23078)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《GEMQ: Global Expert-Level Mixed-Precision Quantization for MoE LLMs》在 arXiv cs.CL 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，Experiments demonstrate that GEMQ significantly reduces memory and accelerates inference with minimal accuracy degradation.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [ModeSwitch-LLM: A Lightweight Phase-Aware Controller for Cross-Mode LLM Inference on a Single GPU](https://arxiv.org/abs/2605.23057)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《ModeSwitch-LLM: A Lightweight Phase-Aware Controller for Cross-Mode LLM Inference on a Single GPU》在 arXiv cs.CL 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，On deployment-style synthetic workloads, the online controller achieves a 2.10x mean latency speedup over FP16 and a 0.48x mean energy ratio, corresponding to 51.7% lower energy per token.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：2.10x、0.48x、51.7%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

