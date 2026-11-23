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

- 日期: 2026-11-23
- 今日新论文: 15
- 今日新权威来源更新: 1
- 本周精选论文: 25
- 本周精选权威来源更新: 3
- 日报: `papers/2026-11-23.md`
- 周报: `digests/weekly-2026-11-23.md`

## 今日最值得看

- [Mosaic: Efficient CPU-GPU Coordinated Block-Sparse Attention](https://arxiv.org/abs/2605.07719)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Mosaic: Efficient CPU-GPU Coordinated Block-Sparse Attention》在 arXiv cs.LG 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Across 2 models, 3 benchmarks, and 40 tasks, Mosaic preserves near-FULL quality while achieving a better overall quality--efficiency tradeoff than the evaluated baselines.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Agentic Coding in the Wild: Characterizing GitHub Copilot Traces at Production Scale](https://arxiv.org/abs/2608.00101)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《Agentic Coding in the Wild: Characterizing GitHub Copilot Traces at Production Scale》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，We demonstrate two use cases: (1) a harness-side LLM API keep-alive policy that preserves provider-side context KV cache, reducing token costs by 14.9% on turn boundaries; and (2) a serving-side KV cache residency policy that uses predicted idle time to guide DRAM offloading, reducing time to first token (TTFT) by 3-33% compared with LRU during a one-week evaluation with GitHub Copilot traces.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：14.9%、33%、89%。
- [IsoMoE: Placement-Invariant Hybrid CPU-GPU MoE Inference with Lossless 12-bit Experts](https://arxiv.org/abs/2611.27604v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《IsoMoE: Placement-Invariant Hybrid CPU-GPU MoE Inference with Lossless 12-bit Experts》在 arXiv API 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Experimental results on three MoE models show that IsoMoE produces bitwise identical outputs across different expert placements.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Weave: Routing-Adaptive Runtime Warp Scheduling for MoE Megakernels](https://arxiv.org/abs/2611.27765)
  - 主题: Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference、LLM routing，核心内容是《Weave: Routing-Adaptive Runtime Warp Scheduling for MoE Megakernels》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Across all evaluated platforms, Weave outperforms the strongest baselines: under EP8 over DeepGEMM-MegaMoE, it speeds up the MoE layer by 1.30x geomean and up to 1.97x on SM103, and by 1.24x geomean and up to 1.72x on SM90; under EP16 on CDNA3, it beats the fastest official RCCL+AITER baseline by 1.44x geomean (up to 2.87x; 1.67x over vLLM).
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.30x、1.97x、1.24x。
- [FOREST: Coordinating Tree-based HBF, RRAM, and HBM for Efficient Speculative LLM Inference](https://arxiv.org/abs/2611.27701v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《FOREST: Coordinating Tree-based HBF, RRAM, and HBM for Efficient Speculative LLM Inference》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Evaluated across six SD configurations spanning 32B-405B target models, FOREST achieves up to 5.5x end-to-end speedup, 11.46x higher decode throughput, and 16.5x higher decode energy efficiency over NVIDIA A800 GPU-based SD baselines.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：5.5x、11.46x、16.5x。
- [ScrapMem: A Bio-Inspired Framework for On-Device Personalized Agent Memory via Optical Forgetting](https://arxiv.org/abs/2605.03804)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《ScrapMem: A Bio-Inspired Framework for On-Device Personalized Agent Memory via Optical Forgetting》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Optical Forgetting reduces the persistent memory footprint by up to 93.0% relative to the raw corpus while retaining over 90% of No-Forget performance.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：93.0%、90%、51.0%。
- [Contexture: Runtime Context Eviction for High-Throughput Agent Serving](https://arxiv.org/abs/2611.26980)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Contexture: Runtime Context Eviction for High-Throughput Agent Serving》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across two models, two harnesses, and two benchmarks, Contexture improves throughput under SLO by 20-73% over the best of no eviction, harness compaction, AgentDiet, and Continuum, and by 7-63% over observation masking in five of eight configurations, and reduces GPU energy per completed session by up to 11%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：73%、63%、11%。
- [MemOnce: A Scalable Memory Architecture for Large Language Models](https://arxiv.org/abs/2611.27973v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《MemOnce: A Scalable Memory Architecture for Large Language Models》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，In particular, adapting Qwen3.5-4B with MemOnce reduces memory state cache by 1313$\times$ and prefill latency by 6.9$\times$ at 1M context, and improves throughput by 3.5$\times$ and overall memory performance by +5.77%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：5.77%。
- [QuantStream3D: Geometry-Aligned Low-Bit KV Cache Quantization for Streaming Visual Geometry Transformers](https://arxiv.org/abs/2611.27901v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《QuantStream3D: Geometry-Aligned Low-Bit KV Cache Quantization for Streaming Visual Geometry Transformers》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Our optimized StreamVGGT backend achieves $5.05\times$ physical KV compression and 23.1% lower latency at batch size one.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：23.1%、57.4%、69.7%。
- [Flying over The Uncertain Nature (FORTUNE): Intelligent and Humanistic 3D Path Planning for Low-Altitude Collaboration](https://arxiv.org/abs/2608.03408)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Flying over The Uncertain Nature (FORTUNE): Intelligent and Humanistic 3D Path Planning for Low-Altitude Collaboration》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experiments on real-world traffic and synthetic datasets show FORTUNE consistently outperforms state-of-the-art benchmarks, validating effectiveness, scalability, and practical applicability in dynamic low-altitude systems.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

