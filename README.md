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

- 日期: 2026-05-20
- 今日新论文: 15
- 今日新权威来源更新: 1
- 本周精选论文: 25
- 本周精选权威来源更新: 5
- 日报: `papers/2026-05-20.md`
- 周报: `digests/weekly-2026-05-20.md`

## 今日最值得看

- [Towards Multi-Model LLM Schedulers: Empirical Insights into Offloading and Preemption](https://arxiv.org/abs/2605.19593)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Towards Multi-Model LLM Schedulers: Empirical Insights into Offloading and Preemption》在 arXiv cs.DC 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，We show that offloading leads to strongly non-linear and model-dependent degradation in decode throughput, with smaller models exhibiting sharper sensitivity to reduced GPU residency.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [SuperInfer: SLO-Aware Rotary Scheduling and Memory Management for LLM Inference on Superchips](https://arxiv.org/abs/2601.20309)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《SuperInfer: SLO-Aware Rotary Scheduling and Memory Management for LLM Inference on Superchips》在 arXiv cs.DC 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Evaluations on GH200 using various models and datasets show that SuperInfer improves TTFT SLO attainment rates by up to 74.7% while maintaining comparable TBT and throughput compared to state-of-the-art systems, demonstrating that SLO-aware scheduling and memory co-design unlocks the full potential of Superchips for responsive LLM serving.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：74.7%。
- [PiKV: KV Cache Management System for Mixture of Experts](https://arxiv.org/abs/2508.06526)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《PiKV: KV Cache Management System for Mixture of Experts》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，To further reduce memory usage, PiKV integrates \textit{PiKV Compression} modules the caching pipeline for acceleration.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [CoX-MoE: Coalesced Expert Execution for High-Throughput MoE Inference with AMX-Enabled CPU-GPU Co-Execution](https://arxiv.org/abs/2605.17889)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《CoX-MoE: Coalesced Expert Execution for High-Throughput MoE Inference with AMX-Enabled CPU-GPU Co-Execution》在 arXiv cs.LG 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Compared to state-of-the-art frameworks, CoX-MoE delivers significant gains, achieving up to 7.1x and 2.4x higher throughput than FlexGen and MoE-Lightning, respectively.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：7.1x、2.4x。
- [TIDE: Efficient and Lossless MoE Diffusion LLM Inference with I/O-aware Expert Offload](https://arxiv.org/abs/2605.20179)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《TIDE: Efficient and Lossless MoE Diffusion LLM Inference with I/O-aware Expert Offload》在 arXiv cs.CL 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，In a single GPU-CPU system, we demonstrate that TIDE achieves up to 1.4$\times$ and 1.5$\times$ throughput improvements over prior baselines on LLaDA2.0-mini and LLaDA2.0-flash models, respectively.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [A novel YOLO26-MoE optimized by an LLM agent for insulator fault detection considering UAV images](https://arxiv.org/abs/2605.19595)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《A novel YOLO26-MoE optimized by an LLM agent for insulator fault detection considering UAV images》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The proposed model achieved 0.9900 mAP@0.5 and 0.9515 mAP@0.5:0.95, outperforming the latest YOLO versions.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Phase-Aware Mixture of Experts for Agentic Reinforcement Learning](https://arxiv.org/abs/2602.17038)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference、LLM routing，核心内容是《Phase-Aware Mixture of Experts for Agentic Reinforcement Learning》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experimental results demonstrate the effectiveness of our proposed PA-MoE.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [GEM: GPU-Variability-Aware Expert to GPU Mapping for MoE Systems](https://arxiv.org/abs/2605.19945)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《GEM: GPU-Variability-Aware Expert to GPU Mapping for MoE Systems》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Our experiments show that GEM improves end-to-end latency by 7.9% on average and by up to 16.5% compared to the baseline.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：7.9%、16.5%。
- [Understanding Inference Scaling for LLMs: Bottlenecks, Trade-offs, and Performance Principles](https://arxiv.org/abs/2605.19775)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Understanding Inference Scaling for LLMs: Bottlenecks, Trade-offs, and Performance Principles》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Tensor parallelism unlocks stranded memory and delivers sublinear gains near the 32B crossover.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [TwinRouterBench: Fast Static and Live Dynamic Evaluation for Realistic Agentic LLM Routing](https://arxiv.org/abs/2605.18859)
  - 主题: Coding agent routing, LLM routing
  - 中文解读: 这项工作主要关注Coding agent routing、LLM routing，核心内容是《TwinRouterBench: Fast Static and Live Dynamic Evaluation for Realistic Agentic LLM Routing》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Routing each call to the cheapest sufficient model can cut costs without sacrificing quality, yet existing router benchmarks evaluate routers only on one-shot prompts.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

