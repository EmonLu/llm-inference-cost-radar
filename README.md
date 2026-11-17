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

- 日期: 2026-11-17
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 8
- 日报: `papers/2026-11-17.md`
- 周报: `digests/weekly-2026-11-17.md`

## 今日最值得看

- [Disaggregated LLM Inference in Space: A Communication Feasibility Study](https://arxiv.org/abs/2611.20893v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Disaggregated LLM Inference in Space: A Communication Feasibility Study》在 arXiv API 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，Orbital data centers could enable large-scale AI inference, but efficiently serving a frontier language model to many users may require several compute satellites to cooperate over optical links.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [IA-MoE: An Intensity-Aware Mixture of Experts for DNN Inference](https://arxiv.org/abs/2611.19669v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《IA-MoE: An Intensity-Aware Mixture of Experts for DNN Inference》在 arXiv API 这一方向上的推进。强调异构硬件协同推理。从实验上看，Experimental results demonstrate that IA-MoE outperforms baseline methods regarding weighted normalized metrics for end-to-end latency and energy consumption.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Multi-LLM Agentic AI at the Edge: Joint Agent Scheduling and Resource Allocation](https://arxiv.org/abs/2611.20915v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Multi-LLM Agentic AI at the Edge: Joint Agent Scheduling and Resource Allocation》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Simulation results show that the proposed resource allocation scheme can reduce system energy consumption compared with other benchmarks, while experiments on a multi-LLM agentic AI system based on Qwen and Llama demonstrate improved task execution success rates.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [CECAR: Cache & Expert Co-Aware Routing Accelerates On-Device Inference of MoE LLMs](https://arxiv.org/abs/2611.20119v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《CECAR: Cache & Expert Co-Aware Routing Accelerates On-Device Inference of MoE LLMs》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，On the Qwen3-30B-A3B model, CECAR achieves 12.5 tokens/s on a consumer-grade GPU with only 16 GB of VRAM, where non-resident experts are fetched from SSD, delivering a 4.5x speedup over conventional MoE inference and exceeding the decode speed of baselines that keep the entire model fully resident in DRAM.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：12.5 tokens/s、16 GB、4.5x。
- [UIAnchor: Anchoring UI Perception and Action Execution for Reliable Service-Composed Mobile Task Automation with GUI Agents](https://arxiv.org/abs/2611.20753v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《UIAnchor: Anchoring UI Perception and Action Execution for Reliable Service-Composed Mobile Task Automation with GUI Agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On the hardest practical tier, L4 tasks (20-30 steps, multi-app, targets < 100 x 100 px, ~5 mm on typical phones), UIAnchor improves success by 31.5% over GPT-4o and 16.6% over Mobile-Agent-v3.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：30 s、100 x、31.5%。
- [Accelerate Bench: Evaluating Agents for Application-Level Program Optimization](https://arxiv.org/abs/2611.20882v1)
  - 主题: Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Coding agent routing、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Accelerate Bench: Evaluating Agents for Application-Level Program Optimization》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Controlled replays show why coordination across an application matters: identical source code runs between 0.29x and 2.12x depending only on build and runtime settings, and one code change is worth 1.01x or 6.4x depending on another.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：0.29x、2.12x、1.01x。
- [GainCtrl: Predicting Remaining Gains for Efficient LLM Agent Execution](https://arxiv.org/abs/2611.20736v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《GainCtrl: Predicting Remaining Gains for Efficient LLM Agent Execution》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，This raises the question of when to stop an attempt to reduce execution cost while preserving task-level Best-of-N quality.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Nemotron 3.5 Bolt E4B 4GB: An Open and Efficient Small Language Model for Fast Conversational Agents](https://arxiv.org/abs/2611.20771v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《Nemotron 3.5 Bolt E4B 4GB: An Open and Efficient Small Language Model for Fast Conversational Agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experiments on 21 benchmarks show that Nemotron 3.5 Bolt E4B 4GB achieves the highest average accuracy while generating the fewest output tokens in both reasoning and non-reasoning modes, compared with Gemma-4-E4B-it and Qwen3.5-4B.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：4GB。
- [KaleidoKV: Rearranging Evidence for Efficient KV Cache Reuse in Offline RAG Inference](https://arxiv.org/abs/2611.19253v1)
  - 主题: Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference，核心内容是《KaleidoKV: Rearranging Evidence for Efficient KV Cache Reuse in Offline RAG Inference》在 arXiv API 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，Experiments on four QA workloads and four LLMs show that KaleidoKV achieves the highest throughput and lowest mean time to first token in all 16 settings, with approximately 1.24-1.75x the throughput of the strongest baseline, including planning time.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：16 s、1.75x、0.5%。
- [When the Cheapest Feasible Router Fails: Auditing Deployment Commitments in Cost-Aware LLM Routing](https://arxiv.org/abs/2611.20417v1)
  - 主题: Cost-efficient LLM inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、LLM routing，核心内容是《When the Cheapest Feasible Router Fails: Auditing Deployment Commitments in Cost-Aware LLM Routing》在 arXiv API 这一方向上的推进。聚焦大模型路由/小模型分流，直接相关。从实验上看，Its practical policywise variant (MARC-P) reduces observed conditional failure to 0.73% at 85.79% deployment, with higher serving cost; fixed-margin and formal risk-control procedures provide competitive alternatives.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：0.73%、85.79%、91.82%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

