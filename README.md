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

- 日期: 2026-08-18
- 今日新论文: 15
- 今日新权威来源更新: 1
- 本周精选论文: 25
- 本周精选权威来源更新: 4
- 日报: `papers/2026-08-18.md`
- 周报: `digests/weekly-2026-08-18.md`

## 今日最值得看

- [From LLM Inference to Agentic Workloads: Characterization and Implications for Serving Systems](https://arxiv.org/abs/2608.15127v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《From LLM Inference to Agentic Workloads: Characterization and Implications for Serving Systems》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Four design explorations demonstrate that these findings are actionable: task-aware serving reduces latency by 29--40%, communication-aware placement by up to 4.5x, state offloading reduces memory usage by 4.6x, and tool-result caching removes 35.2% of redundant search calls and saves 19.3% of aggregate search latency.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：40%、4.5x、4.6x。
- [Every Expert Counts: ExactMoE for Memory-Efficient W4A16 Inference](https://arxiv.org/abs/2608.15383v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Every Expert Counts: ExactMoE for Memory-Efficient W4A16 Inference》在 arXiv API 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，On OLMoE-1B-7B-0924-Instruct, evaluated on a single NVIDIA L4, a 16-slot configuration reduces peak reserved GPU memory from 14.168 to 1.836 GiB (87.04%) while retaining 81.85% of BF16 decode throughput.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.836 GiB、87.04%、81.85%。
- [P-PAS: Prefill-Pressure Adaptive Scheduling for Long-Context LLM Serving](https://arxiv.org/abs/2608.15171v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《P-PAS: Prefill-Pressure Adaptive Scheduling for Long-Context LLM Serving》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Larger token budgets can reduce latency under low scheduling pressure, while smaller budgets become preferable under higher pressure.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [RLCascadeRouter: Quality-Estimator-Free Cascade Routing via Reinforcement Learning](https://arxiv.org/abs/2608.15817v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《RLCascadeRouter: Quality-Estimator-Free Cascade Routing via Reinforcement Learning》在 arXiv API 这一方向上的推进。强调异构硬件协同推理。从实验上看，Evaluated across ten LLMRouterBench benchmarks with thirteen LLMs, RLCascadeRouter outperforms strong baselines and achieves superior performance-cost trade-offs.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Depth-Aware Sensitivity Analysis of Mixture-of-Experts Models via Magnitude-Based Expert Masking](https://arxiv.org/abs/2608.13565)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Depth-Aware Sensitivity Analysis of Mixture-of-Experts Models via Magnitude-Based Expert Masking》在 arXiv cs.AI 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，On a later 500-prompt held-out validation slice, the narrow very-late policy (layers 35-39 @ 50%) achieves the strongest quality/masked-expert tradeoff among tested candidates, retaining 419/500 Good+Similar outputs while masking only 640 of 10,240 total experts.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：50%、30%。
- [TEMPO: Makespan-Aware Expert-Parallel Load Balancing Across Memory- and Compute-Bound Regimes](https://arxiv.org/abs/2608.13057)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《TEMPO: Makespan-Aware Expert-Parallel Load Balancing Across Memory- and Compute-Bound Regimes》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，End-to-end on Testbed B, Qwen3-235B (inside the win region) gains $4$--$6\%$ throughput and cuts p99 latency by $\sim 15.6\%$; DeepSeek-V3 (outside, communication-dominated) shows only mechanism cost.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [FlashQuant: Sparse-Dense Fusion for Memory-Efficient Outlier-Aware LLM Inference](https://arxiv.org/abs/2608.15531v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《FlashQuant: Sparse-Dense Fusion for Memory-Efficient Outlier-Aware LLM Inference》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Experiments show that FlashQuant reduces outlier-processing overhead, achieving $2.74\times - 4.18\times$ speedup over cuBLAS BF16 and up to $1.53\times$ speedup over the strongest unfused outlier-aware baseline.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [S2-MoE: Enabling Efficient Self-Speculative Decoding for Mixture-of-Experts on Edge Devices](https://arxiv.org/abs/2608.15018v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《S2-MoE: Enabling Efficient Self-Speculative Decoding for Mixture-of-Experts on Edge Devices》在 arXiv API 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，Implemented in llama.cpp, S2-MoE achieves up to 5.3x speedup (about 2.0x on average) over standard autoregressive de?coding across diverse MoE models and datasets on edge devices.Code is available at https://github.com/angerybob/S2-MoE.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：5.3x、2.0x。
- [LOCAL: Enabling Learning On-device Contiguously for Agent LLMs](https://arxiv.org/abs/2608.15241v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《LOCAL: Enabling Learning On-device Contiguously for Agent LLMs》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On a single 24 GB GPU with 7B-class models, LOCAL lowers foreground queue-wait p95 by 3.1x over FIFO, lowers p95 time-to-first-token (TTFT) by 1.55x versus non-preemptible training, cuts post-publish first-hit prefill p99 by 25.6% and cross-agent TTFT p99 by 21.9%, and keeps background learning progressing under tight KV budgets.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：24 GB、3.1x、1.55x。
- [Collective Communication for Distributed LLM Systems: Planning, Runtime Adaptation, and Computation Coordination](https://arxiv.org/abs/2608.15118v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Collective Communication for Distributed LLM Systems: Planning, Runtime Adaptation, and Computation Coordination》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，In modern LLM training and serving clusters, heterogeneous GPU interconnects, multi-NIC networking, mixed parallelism strategies, low-latency inference requests, and high-throughput training pipelines have motivated increasingly diverse ways to plan, execute, and overlap collective communication.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

