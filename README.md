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

- 日期: 2026-08-27
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 3
- 日报: `papers/2026-08-27.md`
- 周报: `digests/weekly-2026-08-27.md`

## 今日最值得看

- [Minima-KV: Retention-Preserving KV Cache Compression with Mixed-Format Paged Attention](https://arxiv.org/abs/2608.23834)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Minima-KV: Retention-Preserving KV Cache Compression with Mixed-Format Paged Attention》在 arXiv cs.AI 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，A separate single-pair direct-decode canary with two 59,008-token requests measures 3.625x active-KV compression and 0.9821x throughput relative to its control, routes all 16 full-attention layers without fallback, and retains no dense shadow.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：3.625x、0.9821x、3.50x。
- [Simthesizer: An Agent-Driven Simulation Framework for LLM Serving Systems](https://arxiv.org/abs/2608.24650v2)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《Simthesizer: An Agent-Driven Simulation Framework for LLM Serving Systems》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Under the same coding agent and harnesses, extensions built on Simthesizer follow a vLLM-based real system with 2.51% average throughput error, versus 6.03% for extensions built on existing simulators.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：2.51%、6.03%、284.96x。
- [MAPLE: MoE Adaptive Plug-and-play Layer-wise Expert allocation](https://arxiv.org/abs/2608.15299)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《MAPLE: MoE Adaptive Plug-and-play Layer-wise Expert allocation》在 arXiv cs.AI 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，These accuracy gains translate into measured deployment efficiency: implementing MAPLE in SGLang reduces single-GPU end-to-end serving latency by 32.2% and improves throughput by 47.4%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：32.2%、47.4%、75%。
- [TOPAS: Workflow-Aware Prefix-State Scheduling for Multi-Agent LLM Serving](https://arxiv.org/abs/2608.25523v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《TOPAS: Workflow-Aware Prefix-State Scheduling for Multi-Agent LLM Serving》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Compared with the best performing baseline for each workload and metric, TOPAS reduces the mean/p99 JCT by up to 39.8%/49.4% on the synthetic workloads, while lowering mean JCT by 9.8% on MetaGPT-SOP and mean/p99 JCT by 22.0%/26.6% on MetaGPT-TL.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：39.8%、49.4%、9.8%。
- [A Heterogeneous Mixture of Experts Framework for Interpretable Machine Learning](https://arxiv.org/abs/2608.24195v1)
  - 主题: Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference，核心内容是《A Heterogeneous Mixture of Experts Framework for Interpretable Machine Learning》在 arXiv API 这一方向上的推进。强调异构硬件协同推理。从实验上看，Experiments on a diverse collection of synthetic and real-world benchmark datasets demonstrate that the proposed framework adaptively specializes experts according to local data geometry, yielding interpretable expert assignments while achieving predictive performance competitive with homogeneous MoDT and Random Forests.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [More GPUs or a Smaller Cache? Tensor Parallelism versus KV Compression for Memory-Bound LLM Serving](https://arxiv.org/abs/2608.23962)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《More GPUs or a Smaller Cache? Tensor Parallelism versus KV Compression for Memory-Bound LLM Serving》在 arXiv cs.AI 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Tensor parallelism is the only lever that improves latency (compression makes per-token latency worse, by 8 to 93%, through batching contention), while compression is the only lever that multiplies capacity per dollar (16.5x, against 1.21x for an eightfold spend on GPUs).
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：93%、16.5x、1.21x。
- [Scorpio: Serving Right Requests at the Right Time for Heterogeneous SLOs in LLM Inference](https://arxiv.org/abs/2505.23022)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Scorpio: Serving Right Requests at the Right Time for Heterogeneous SLOs in LLM Inference》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Evaluations demonstrate that Scorpio improves system goodput by up to 14.4x and SLO adherence by up to 46.5% under high load compared to state-of-the-art baselines.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：14.4x、46.5%。
- [Design-to-Plan: A Large Language Model-Based Multi-Agent Framework for Manufacturing Process Planning from 3D CAD Models and 2D Engineering Drawings](https://arxiv.org/abs/2608.24039v1)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《Design-to-Plan: A Large Language Model-Based Multi-Agent Framework for Manufacturing Process Planning from 3D CAD Models and 2D Engineering Drawings》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The parallel architecture achieves 100% success across downstream agents, Tool F1 scores of 95.9%-97.6%, 90% source detection accuracy in conflict analysis, and a 60%-68% reduction in token usage for key planning tasks.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：100%、1 s、95.9%。
- [psRL: Efficient Training for Agentic AI via Training-Time Prefix Sharing](https://arxiv.org/abs/2608.25683)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《psRL: Efficient Training for Agentic AI via Training-Time Prefix Sharing》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Evaluations using production traces demonstrate that psRL outperforms existing systems by up to 5.2x in throughput.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：5.2x。
- [The Handoff Tax: Continuing Non-Native Trajectories in LLM Agents](https://arxiv.org/abs/2608.24358v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《The Handoff Tax: Continuing Non-Native Trajectories in LLM Agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Interestingly, the preferred interface also reverses with direction: reducing LC-model trajectory information improves escalation quality, whereas removing the HC-model trajectory reduces downshift quality.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

