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

- 日期: 2026-07-08
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 2
- 日报: `papers/2026-07-08.md`
- 周报: `digests/weekly-2026-07-08.md`

## 今日最值得看

- [Nemotron-Labs-3-Puzzle-75B-A9B: Compressing Hybrid MoE LLMs](https://arxiv.org/abs/2607.04371v2)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Nemotron-Labs-3-Puzzle-75B-A9B: Compressing Hybrid MoE LLMs》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，In interactive serving workloads on a single 8xB200 node, Puzzle-75B-A9B achieves approximately 2x higher server throughput than Nemotron-3-Super at matched user throughput constraints.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：8x、2x。
- [Think Before You Grid-Search: Floor-First Triage for LLM Serving](https://arxiv.org/abs/2607.05876v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Think Before You Grid-Search: Floor-First Triage for LLM Serving》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The floors show TP16 decoding is KV-capacity-limited to ~70 concurrent 8K requests; sparse attention removes the KV-bandwidth term but not the capacity wall; an EP16+DP-attention layout accepts slightly worse same-batch weight traffic for an order-of-magnitude higher capacity wall (~644) -- while single-stream latency favors TP by 2.4x.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：2.4x。
- [Is Your NPU Ready for LLMs? Dissecting the Hidden Efficiency Bottlenecks in Mobile LLM Inference](https://arxiv.org/abs/2607.05475v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Is Your NPU Ready for LLMs? Dissecting the Hidden Efficiency Bottlenecks in Mobile LLM Inference》在 arXiv API 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，We estimate that this configuration could reduce energy consumption by up to 54.8% on the NPU backend across three datasets.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：54.8%、40%。
- [Agents That Teach: Towards Designing Incidental Learning Back into AI-Assisted Software Development](https://arxiv.org/abs/2607.06101v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing，核心内容是《Agents That Teach: Towards Designing Incidental Learning Back into AI-Assisted Software Development》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，While these gains are real, they come at the cost of incidental learning.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Quantize the Target, Quantize the Drafter: Efficient Inference with Qwen3.5-4B](https://arxiv.org/abs/2607.04244v2)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Quantize the Target, Quantize the Drafter: Efficient Inference with Qwen3.5-4B》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Because the drafter is invoked at every speculative decoding step, we further reduce its overhead with quantization and sliding-window attention, preserving draft-token acceptance while improving long-context decoding latency.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [UBEP: Re-architecting Expert Parallelism Communication Library for Production Superpods](https://arxiv.org/abs/2607.06202v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《UBEP: Re-architecting Expert Parallelism Communication Library for Production Superpods》在 arXiv API 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，Through large scale experiments, UBEP reduces All-to-All latency by up to 52.4% and MoE inference Time Per Output Token (TPOT) by up to 11.1%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：52.4%、11.1%。
- [RuBench: A Repository-Level Agentic Coding Benchmark with Natively Authored Russian Task Specifications](https://arxiv.org/abs/2607.06411v1)
  - 主题: Coding agent routing
  - 中文解读: 这项工作主要关注Coding agent routing，核心内容是《RuBench: A Repository-Level Agentic Coding Benchmark with Natively Authored Russian Task Specifications》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The best configuration resolves 78.7% of tasks; at N=25 only the gaps to the weakest model are statistically resolvable, which we state explicitly.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：78.7%、20%。
- [Online Linear Programming for Multi-Objective Routing in LLM Serving](https://arxiv.org/abs/2607.03948)
  - 主题: Cost-efficient LLM inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、LLM routing，核心内容是《Online Linear Programming for Multi-Objective Routing in LLM Serving》在 arXiv cs.LG 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，We integrate our router into the Vidur simulator and demonstrate substantial improvements over standard baselines across multiple SLO regimes, including end-to-end latency, time-to-first-token, throughput, and tail performance.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [KARA: Efficient Reasoning LLM Serving via Sliding-Window KV Cache Compression](https://arxiv.org/abs/2607.01237)
  - 主题: Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference，核心内容是《KARA: Efficient Reasoning LLM Serving via Sliding-Window KV Cache Compression》在 arXiv cs.CL 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，Furthermore, we adapt Kara to PagedAttention and develop KvLLM, an inference framework built upon vLLM, which reduces KV cache memory usage and effectively improves output throughput.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Optimal-Agent-Selection: State-Aware Routing Framework for Efficient Multi-Agent Collaboration](https://arxiv.org/abs/2511.02200)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference、LLM routing，核心内容是《Optimal-Agent-Selection: State-Aware Routing Framework for Efficient Multi-Agent Collaboration》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experiments on challenging collaborative reasoning benchmarks demonstrate that our method achieves state-of-the-art performance, achieving up to 23.8% improvement over baselines and reducing data collection overhead by up to 90.1% compared to exhaustive search.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：23.8%、90.1%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

