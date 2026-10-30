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

- 日期: 2026-10-30
- 今日新论文: 15
- 今日新权威来源更新: 1
- 本周精选论文: 25
- 本周精选权威来源更新: 2
- 日报: `papers/2026-10-30.md`
- 周报: `digests/weekly-2026-10-30.md`

## 今日最值得看

- [PDScope: Breaking the Prefill-Decode Seesaw for Memory-Bound MoE Inference](https://arxiv.org/abs/2610.39216v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《PDScope: Breaking the Prefill-Decode Seesaw for Memory-Bound MoE Inference》在 arXiv API 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，On mainstream MoE models, PDScope achieves 2.5-10.3x higher prefill throughput and 2.1-6.1x higher decode throughput than existing systems, showing that phase-aware co-design unlocks efficient MoE inference under memory constraints and extends naturally to multi-batch settings.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：10.3x、6.1x。
- [DWISE: Denoising Workload-Informed Scheduling Engine](https://arxiv.org/abs/2610.39852v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《DWISE: Denoising Workload-Informed Scheduling Engine》在 arXiv API 这一方向上的推进。强调异构硬件协同推理。从实验上看，Implemented in SGLang and evaluated on five models from three dLLM families under bursty workloads, DWISE reduces mean end-to-end latency over SGLang by 5.4$\times$ on average and up to 14.9$\times$ while preserving task accuracy.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [GAAC: Lossless KV Compression for Bandwidth-Efficient LLM Inference on Personal Devices](https://arxiv.org/abs/2610.38210v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《GAAC: Lossless KV Compression for Bandwidth-Efficient LLM Inference on Personal Devices》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，In serving, it reduces resident KV memory by approximately 26% and increases aggregate throughput by 13-29% under comparable KV-memory budgets.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：26%、29%。
- [FlatCake: A Flat KVCache Storage Architecture for LLM Serving](https://arxiv.org/abs/2610.38355v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《FlatCake: A Flat KVCache Storage Architecture for LLM Serving》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On a production Claude Code trace with DeepSeek-V4-Flash, FlatCake sustains a 94% cache hit rate as load increases (versus 64% for Mooncake), eliminates Mooncake's $6.5\times$--$6.7\times$ SSD read amplification, and reduces peak-load mean TTFT by $1.6\times$ while improving total token throughput by $1.6\times$.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：94%、64%。
- [MAServeBench: Benchmarking Multi-Agent LLM Serving Systems with Hierarchical Collaboration Workloads](https://arxiv.org/abs/2610.40293v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《MAServeBench: Benchmarking Multi-Agent LLM Serving Systems with Hierarchical Collaboration Workloads》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The benchmark code is available at https://github.com/ShengxuanQiu/MAServeBench.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [NORmal: Architecting 3D Ferroelectric NOR Flash as Main Memory -- From Co-Fabricated BEOL Arrays to 200B-Class Multi-Agent LLMs in a Smartphone](https://arxiv.org/abs/2610.40000v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《NORmal: Architecting 3D Ferroelectric NOR Flash as Main Memory -- From Co-Fabricated BEOL Arrays to 200B-Class Multi-Agent LLMs in a Smartphone》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，In serving-level simulation on production agent traces, NORmal is 8.9$\times$--28.0$\times$ faster than UFS offloading, within 0.4% of an unlimited-DRAM ideal, and 2.8$\times$--6.3$\times$ faster than HBF on sessions beyond 256K tokens, with 8.1$\times$--17.8$\times$ less memory energy per token.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：0.4%。
- [DolphinRouting: Cluster-Level Binary Routing for Disaggregated LLM Inference Serving](https://arxiv.org/abs/2610.40292v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《DolphinRouting: Cluster-Level Binary Routing for Disaggregated LLM Inference Serving》在 arXiv API 这一方向上的推进。关注在线 serving 系统优化，适合成本控制。从实验上看，We evaluate DolphinRouting on a real PD-disaggregated cluster using three public benchmarks, a mixed workload, and real data.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [GPU-Resident Speculative Decoding for In-Browser LLM Inference with WebGPU](https://arxiv.org/abs/2610.39761v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《GPU-Resident Speculative Decoding for In-Browser LLM Inference with WebGPU》在 arXiv API 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Optional draft heads raise the peak speedup to 10.2$\times$, while session memory provides additional gains without downloading extra weights.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Selective and Hybrid-State Communication for Latent Multi-Agent Systems](https://arxiv.org/abs/2610.37779v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《Selective and Hybrid-State Communication for Latent Multi-Agent Systems》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across six benchmarks, SelectKV reduces communicated KV positions and logical KV payload by 9.7-9.9%, with accuracy unchanged on two benchmarks, within one percentage point on three, and six points lower on HumanEval+.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：9.9%、80%、2.78x。
- [GAUSS: A Workload-Aware Analytical and Monte-Carlo Simulator for LLM Inference Serving](https://arxiv.org/abs/2610.37989v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《GAUSS: A Workload-Aware Analytical and Monte-Carlo Simulator for LLM Inference Serving》在 arXiv API 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，Large language model (LLM) inference has become an operational workload that fleets must provision, monitor, and bill against latency service-level objectives (SLOs).
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

