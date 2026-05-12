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

- 日期: 2026-05-12
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 4
- 日报: `papers/2026-05-12.md`
- 周报: `digests/weekly-2026-05-12.md`

## 今日最值得看

- [SplitZip: Ultra Fast Lossless KV Compression for Disaggregated LLM Serving](https://arxiv.org/abs/2605.01708)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《SplitZip: Ultra Fast Lossless KV Compression for Disaggregated LLM Serving》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，End-to-end transfer experiments show up to $1.32\times$ speedup for BF16 KV cache transfer, $1.30\times$ speedup for TTFT, and $1.23\times$ increase on Request Throughput.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Continuum: Efficient and Robust Multi-Turn LLM Agent Scheduling with KV Cache Time-to-Live](https://arxiv.org/abs/2511.02230)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Continuum: Efficient and Robust Multi-Turn LLM Agent Scheduling with KV Cache Time-to-Live》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Evaluations on real-world agents (SWE-Bench, BFCL, OpenHand) with Llama-3.1 8B/70B, Gemma-3 12B, and GLM-4.5 355B shows that Continuum improves the average job completion times by over 8x while improving throughput.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：8x。
- [Agentic AI-Driven UAV Network Deployment: An LLM-Enhanced Exact Potential Game Approach](https://arxiv.org/abs/2603.07456)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Agentic AI-Driven UAV Network Deployment: An LLM-Enhanced Exact Potential Game Approach》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Simulation results demonstrate that the proposed framework consistently outperforms baseline methods in terms of energy consumption, end-to-end latency, and system throughput.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [TileQ: Efficient Low-Rank Quantization of Mixture-of-Experts with 2D Tiling](https://arxiv.org/abs/2605.09281)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《TileQ: Efficient Low-Rank Quantization of Mixture-of-Experts with 2D Tiling》在 arXiv cs.LG 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，Experiments show that \textsc{TileQ} cuts down additional memory usage up to 10$\times$ and reduces inference latency to $\sim$5\% while preserving state-of-the-art accuracy.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Agent-X: Full Pipeline Acceleration of On-device AI Agents](https://arxiv.org/abs/2605.10380v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《Agent-X: Full Pipeline Acceleration of On-device AI Agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On representative agentic workloads, Agent-X achieves a 1.61x end-to-end speedup in real systems with no accuracy loss and can be seamlessly integrated into existing on-device AI agents.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.61x。
- [SPECTRE: Hybrid Ordinary-Parallel Speculative Serving for Resource-Efficient LLM Inference](https://arxiv.org/abs/2605.08151)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《SPECTRE: Hybrid Ordinary-Parallel Speculative Serving for Resource-Efficient LLM Inference》在 arXiv cs.DC 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，Results show that SPECTRE consistently improves large-model serving throughput while causing only minor interference to the native workloads of tail-model services.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Surviving Partial Rank Failures in Wide Expert-Parallel MoE Inference](https://arxiv.org/abs/2605.10670)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Surviving Partial Rank Failures in Wide Expert-Parallel MoE Inference》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，The results show that explicit mutable membership preserves the steady-state fast path, staying within 4.4% of a fixed-membership DeepEP baseline under static serving, while turning a local rank fault from whole-instance downtime into two bounded interruptions.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：4.4%、11s、8s。
- [Elastic MoE: Unlocking the Inference-Time Scalability of Mixture-of-Experts](https://arxiv.org/abs/2509.21892)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Elastic MoE: Unlocking the Inference-Time Scalability of Mixture-of-Experts》在 arXiv cs.CL 这一方向上的推进。强调异构硬件协同推理。从实验上看，Extensive experiments across four MoE architectures (7B--21B) and nine benchmarks show that EMoE significantly expands the effective scaling range to 2-3$\times$ the training-time $k$, while also achieving higher peak performance.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Understand and Accelerate Memory Processing Pipeline for Disaggregated LLM Inference](https://arxiv.org/abs/2603.29002)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Understand and Accelerate Memory Processing Pipeline for Disaggregated LLM Inference》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Through systematic profiling, we identify a 22%-97% memory processing overhead in LLM inference and strong heterogeneity in its computational characteristics.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：22%、97%。
- [GELATO: Generative Entropy- and Lyapunov-based Adaptive Token Offloading for Device-Edge Speculative LLM Inference](https://arxiv.org/abs/2605.10124)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《GELATO: Generative Entropy- and Lyapunov-based Adaptive Token Offloading for Device-Edge Speculative LLM Inference》在 arXiv cs.DC 这一方向上的推进。涉及 KV/参数/专家的卸载策略，可节约显存或成本。从实验上看，Extensive evaluations demonstrate that GELATO achieves a globally optimal tradeoff, outperforming state-of-the-art distributed SD architectures by 64.98% in token throughput and reducing energy consumption by 47.47% under resource-constrained environments, while preserving LLM decoding quality.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：64.98%、47.47%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

