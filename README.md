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

- 日期: 2026-10-20
- 今日新论文: 15
- 今日新权威来源更新: 2
- 本周精选论文: 25
- 本周精选权威来源更新: 11
- 日报: `papers/2026-10-20.md`
- 周报: `digests/weekly-2026-10-20.md`

## 今日最值得看

- [A Hybrid GPU and Processing-Near-Memory Architecture with Shared DRAM for Efficient Prefill-Decode Disaggregation](https://arxiv.org/abs/2610.26131v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《A Hybrid GPU and Processing-Near-Memory Architecture with Shared DRAM for Efficient Prefill-Decode Disaggregation》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Evaluations on server-scale LLMs demonstrate that DuoPD achieves up to 2.23x higher end-to-end throughput than conventional PD-disaggregation.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：2.23x。
- [RouterWorld: Scaling Conversational AI with Latency-Aware LLM Routing](https://arxiv.org/abs/2610.26511v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《RouterWorld: Scaling Conversational AI with Latency-Aware LLM Routing》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，However, existing LLM routing benchmarks assume full observability of all candidate model outcomes, under-emphasize latency as a first-class metric, and fragment evaluation across heterogeneous protocols misaligned with real-world settings.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [SARP: An On-SSD Index for KVCache with Fast Prefix Matching and Recovery](https://arxiv.org/abs/2610.26849v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《SARP: An On-SSD Index for KVCache with Fast Prefix Matching and Recovery》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across four multi-turn chat and agentic workloads, SARP recovers 8.0x to 77.5x faster than the in-memory index baselines and delivers 1.15x to 66.6x the request throughput of the on-SSD index baselines, while reusing only 0.0030% to 0.029% fewer tokens than exact prefix matching.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：8.0x、77.5x、1.15x。
- [AgentLens: Framework-Aware Characterization and Resource Control for Heterogeneous LLM Agents](https://arxiv.org/abs/2610.25231v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《AgentLens: Framework-Aware Characterization and Resource Control for Heterogeneous LLM Agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，In trace-driven replay across three co-location pairs at a memory budget of 90% of aggregate peak demand, AgentLens keeps the protected worker's P95 allocation latency at 5.7-7.1 ms, improving on static allocation by 2.1-2.6x.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：90%、7.1 ms、2.6x。
- [Which Model for Which Role? Cost-Efficient Pareto Recommendation for LLM Agentic Workflows](https://arxiv.org/abs/2610.26676v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《Which Model for Which Role? Cost-Efficient Pareto Recommendation for LLM Agentic Workflows》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across the eight benchmarks, CC-Gittins recovers a substantial fraction of the true Pareto frontier at roughly 10% of the exhaustive-evaluation cost, and recovers most of the frontier with few false positives by 30%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：10%、30%。
- [LIRQuant: An Efficient Locally Isolated Rotation Quantization Method for Large Language Models](https://arxiv.org/abs/2610.25675v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《LIRQuant: An Efficient Locally Isolated Rotation Quantization Method for Large Language Models》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Meanwhile, LIRQuant calibrates LLaMA-3-8B in only 25 minutes with 20.3 GB peak GPU memory, achieving the fastest calibration and the lowest memory footprint among recent learnable-rotation methods, and its fused inference kernels deliver up to $2.3\times$ prefill speedup and $3.5\times$ memory saving over FP16.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：20.3 GB。
- [Peer Pressure: Execution-Verified Co-Evolution of Attacker and Defender Populations for Code Security](https://arxiv.org/abs/2610.24896v1)
  - 主题: Coding agent routing, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Coding agent routing、Cost-efficient LLM inference，核心内容是《Peer Pressure: Execution-Verified Co-Evolution of Attacker and Defender Populations for Code Security》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Under a judge distinct from its training oracle it cuts attack success from 36.0% to 4.6%, against WildGuard's 8.9%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：36.0%、4.6%、8.9%。
- [Autonomous intelligence for mining productivity: a multi-agent AI approach to operational value creation](https://arxiv.org/abs/2610.26369v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《Autonomous intelligence for mining productivity: a multi-agent AI approach to operational value creation》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，It provides a critical review of agentic evaluation along six orthogonal dimensions and identifies the industrial blind spot of current benchmarks.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [System X: An LLM Decision Model That Replies from Its Own KV Cache](https://arxiv.org/abs/2610.25456v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、LLM routing，核心内容是《System X: An LLM Decision Model That Replies from Its Own KV Cache》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Adding dialogue, industry and complaint data (System X+) improves support-task results but lowers IFEval accuracy from 55.5% to 45.0%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：55.5%、45.0%、55.0%。
- [gKSM: GPU Memory Deduplication at Driver Layer for Serverless LLM Inference](https://arxiv.org/abs/2610.25219v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《gKSM: GPU Memory Deduplication at Driver Layer for Serverless LLM Inference》在 arXiv API 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Experiments show that gKSM reduces GPU memory usage by 59.8% while maintaining high throughput compared to ServerlessLLM.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：59.8%、2.15X。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

