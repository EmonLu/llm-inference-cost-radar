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

- 日期: 2026-11-05
- 今日新论文: 15
- 今日新权威来源更新: 2
- 本周精选论文: 25
- 本周精选权威来源更新: 2
- 日报: `papers/2026-11-05.md`
- 周报: `digests/weekly-2026-11-05.md`

## 今日最值得看

- [Runway Characters: Serving a 57B Video Diffusion Transformer for Real-Time Conversation](https://arxiv.org/abs/2611.05642)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Runway Characters: Serving a 57B Video Diffusion Transformer for Real-Time Conversation》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Each chunk takes 240 attention calls, each reading a 5,788-slot KV cache in which only 757 tokens are new, and 29% of the original step was whole-cache work repeated in every call.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：29%、99.5%、0.49 s。
- [Beyond Compression Ratio: High-Throughput KV Compression for Disaggregated LLM Serving](https://arxiv.org/abs/2611.04382)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Beyond Compression Ratio: High-Throughput KV Compression for Disaggregated LLM Serving》在 arXiv cs.DC 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，The fused kernel achieves up to 5.9x speedup, while the new lossless backend increases compression throughput from below 90 GB/s to over 500 GB/s.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：5.9x、90 GB、500 GB。
- [HELIX: HEterogeneous LLM Inference with FleXible and Fine-Grained Partitioning](https://arxiv.org/abs/2611.06513v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《HELIX: HEterogeneous LLM Inference with FleXible and Fine-Grained Partitioning》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，At engine initialization, HELIX automatically determines hardware-specific operator placements that minimize execution latency, accounting for profiled execution costs, communication overheads, device capabilities, and memory constraints.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [TokenScale: Timely and Accurate Autoscaling for Disaggregated LLM Serving with Token Velocity](https://arxiv.org/abs/2512.03416)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《TokenScale: Timely and Accurate Autoscaling for Disaggregated LLM Serving with Token Velocity》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Our evaluation on a GPU cluster with production traces shows TokenScale improves SLO attainment from 50-88% to 80-96% and reduces costs by 4-14% over state-of-the-art systems, including DistServe, BlitzScale, and AIBrix.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：88%、96%、14%。
- [vExpert: Virtualizing Expert Storage for Adaptive Load Balancing in Distributed MoE Inference](https://arxiv.org/abs/2611.06057v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《vExpert: Virtualizing Expert Storage for Adaptive Load Balancing in Distributed MoE Inference》在 arXiv API 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，Evaluated on DeepSeek-V3.1 within an 8-node H100 cluster, vExpert improves load balance ratio by up to 55% and achieves 1.2$\times$ end-to-end speedup.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：55%。
- [MASBench: Benchmarking LLM-based Multi-Agent Collaboration under Partial Observability](https://arxiv.org/abs/2610.04672)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《MASBench: Benchmarking LLM-based Multi-Agent Collaboration under Partial Observability》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experiments across diverse LLM backbones and mechanism configurations offer empirical guidance for effective MAS design.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [ServerBench: How can your coding agents design specialized LLM serving systems?](https://arxiv.org/abs/2611.06841v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《ServerBench: How can your coding agents design specialized LLM serving systems?》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Agents experiment against a common objective, dollars per dollar: latency-qualified token value per dollar of GPU cost.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [UniCompress: From Multi-LoRA Experts to One Compact Model for Edge Intelligence](https://arxiv.org/abs/2611.06075)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《UniCompress: From Multi-LoRA Experts to One Compact Model for Edge Intelligence》在 arXiv cs.AI 这一方向上的推进。强调异构硬件协同推理。从实验上看，UniCompress reduces the approximate weight storage from 8.9 GB in BF16 to 2.1 GB in INT2, corresponding to a reduction of approximately 76%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：8.9 GB、2.1 GB、76%。
- [KV-PRM: Efficient Process Reward Modeling via KV-Cache Transfer for Multi-Agent Test-Time Scaling](https://arxiv.org/abs/2607.09153)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《KV-PRM: Efficient Process Reward Modeling via KV-Cache Transfer for Multi-Agent Test-Time Scaling》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Empirically, across the MATH, GSM8K, and AIME benchmarks, KV-PRM matches or strictly outperforms text-PRMs under various TTS methods such as Beam Search, MCTS, and Weighted Voting, with up to a 5,000x reduction in scoring FLOPs, a 37x reduction in latency, and a 34x reduction in per-sequence memory footprint compared to text-based PRMs.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：000x、37x、34x。
- [Shallow Encoding Emits Deep Memories](https://arxiv.org/abs/2611.06084v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《Shallow Encoding Emits Deep Memories》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Trained copies of the deep layers' write paths, which we call emitters, therefore write a prompt's deep memories from the residual stream of a shallower anchor layer, and all prompt tokens but the last run as few as 63% of the layers.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：63%、1.4x。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

