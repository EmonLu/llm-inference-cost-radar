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

- 日期: 2026-07-13
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 1
- 日报: `papers/2026-07-13.md`
- 周报: `digests/weekly-2026-07-13.md`

## 今日最值得看

- [STEEL: Sparsity-Aware Fused Attention for Energy-Efficient Long-Sequence Inference on AMD's XDNA NPU](https://arxiv.org/abs/2607.09385v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《STEEL: Sparsity-Aware Fused Attention for Energy-Efficient Long-Sequence Inference on AMD's XDNA NPU》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experimental results show that STEEL reduces energy consumption by an average of 9.17x and 1.75x relative to CPU and GPU baselines, respectively.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：9.17x、1.75x、9.6x。
- [BlockServe: Block-Grained Continuous Batching for High-Throughput Diffusion LLM Serving](https://arxiv.org/abs/2607.08930)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《BlockServe: Block-Grained Continuous Batching for High-Throughput Diffusion LLM Serving》在 arXiv cs.LG 这一方向上的推进。强调异构硬件协同推理。从实验上看，On Dream and LLaDA across five benchmarks, BlockServe achieves 1.9--10.6$\times$ throughput over Fast-dLLM with comparable generation quality, establishing block-grained scheduling as a foundation for high-throughput offline dLLM inference.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Director: Accelerating Distributed MoE Serving via Online Proactive Expert Placement](https://arxiv.org/abs/2607.08782)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Director: Accelerating Distributed MoE Serving via Online Proactive Expert Placement》在 arXiv cs.LG 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Finally, we implement a prototype and demonstrate, through extensive experiments, a reduction in end-to-end latency of $11\sim55\%$ for popular MoE models (e.g., Mistral, DeepSeek and Qwen) compared to existing work.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Sticky Routing: Training MoE Models for Memory-Efficient Inference](https://arxiv.org/abs/2607.08780)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Sticky Routing: Training MoE Models for Memory-Efficient Inference》在 arXiv cs.CL 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，Experiments on small-scale MoE language models show that StickyMoE reduces the expert switch rate by up to 60% with less than 4% perplexity degradation, Pareto-dominating post-hoc fine-tuning on the quality-locality frontier.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：60%、4%。
- [The Serialized Bridge: Understanding and Recovering LLM Serving Performance under Blackwell GPU Confidential Computing](https://arxiv.org/abs/2606.23969)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《The Serialized Bridge: Understanding and Recovering LLM Serving Performance under Blackwell GPU Confidential Computing》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Yet LLM serving under Intel TDX plus GPU-CC still loses 13-27% of throughput, and KV-cache restore latency can more than double.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：27%、131%、34x。
- [KV-PRM: Efficient Process Reward Modeling via KV-Cache Transfer for Multi-Agent Test-Time Scaling](https://arxiv.org/abs/2607.09153v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《KV-PRM: Efficient Process Reward Modeling via KV-Cache Transfer for Multi-Agent Test-Time Scaling》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Empirically, across the MATH, GSM8K, and AIME benchmarks, KV-PRM matches or strictly outperforms text-PRMs under various TTS methods such as Beam Search, MCTS, and Weighted Voting, with up to a 5,000x reduction in scoring FLOPs, a 37x reduction in latency, and a 34x reduction in per-sequence memory footprint compared to text-based PRMs.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：000x、37x、34x。
- [Leveraging Multi-Agent System (MAS) and Fine-Tuned Small Language Models (SLMs) for Automated Telecom Network Troubleshooting](https://arxiv.org/abs/2511.00651)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《Leveraging Multi-Agent System (MAS) and Fine-Tuned Small Language Models (SLMs) for Automated Telecom Network Troubleshooting》在 arXiv cs.CL 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experimental results demonstrate that the proposed framework significantly accelerates troubleshooting automation across both Radio Access Network (RAN) and Core network domains.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Heterogeneous Information-Bottleneck Coordination Graphs for Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2605.17393)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Heterogeneous Information-Bottleneck Coordination Graphs for Multi-Agent Reinforcement Learning》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，arXiv:2605.17393v2 Announce Type: replace-cross Abstract: Coordination graphs are a central abstraction in cooperative multi-agent reinforcement learning (MARL), yet existing sparse-graph learners lack a theoretically grounded mechanism to decide which edges should exist and how much information each edge should carry.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [AnchorMoE: Interpretable Time Series Classification via Anchor-Routed MoE](https://arxiv.org/abs/2606.03631)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《AnchorMoE: Interpretable Time Series Classification via Anchor-Routed MoE》在 arXiv cs.LG 这一方向上的推进。强调异构硬件协同推理。从实验上看，Extensive experiments on real-world and synthetic benchmarks demonstrate that AnchorMoE achieves highly competitive classification performance while faithfully grounding its decisions in the raw time series.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Jet-Long: Efficient Long-Context Extension with Dynamic Bifocal RoPE](https://arxiv.org/abs/2607.07740)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《Jet-Long: Efficient Long-Context Extension with Dynamic Bifocal RoPE》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On Qwen3-1.7B/4B/8B up to 128K context, Jet-Long leads RULER by $+4.79$/$+2.18$/$+2.03$ pp over the strongest baseline at 1.7B/4B/8B, achieves the best overall accuracy on HELMET-RAG (a benchmark identified by HELMET as the most efficient predictor of downstream long-context performance) and attains the lowest PG-19 perplexity.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

