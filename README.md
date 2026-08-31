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

- 日期: 2026-08-31
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 1
- 日报: `papers/2026-08-31.md`
- 周报: `digests/weekly-2026-08-31.md`

## 今日最值得看

- [Training Communication-Efficient Mixture-of-Experts Language Models with Layer Re-Configuration](https://arxiv.org/abs/2608.28511v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Training Communication-Efficient Mixture-of-Experts Language Models with Layer Re-Configuration》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Across a scaling ladder from 2B to 31.5B total parameters, under matched total and activated parameters, CE-MoE models consistently reduce training cost while matching validation loss and downstream benchmarks with full-MoE baselines.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [ContextPilot: Teaching Agents for Proactive Context Management via Fine-grained RL](https://arxiv.org/abs/2608.28476)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《ContextPilot: Teaching Agents for Proactive Context Management via Fine-grained RL》在 arXiv cs.CL 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experiments on long-context QA and deep search tasks show that ContextPilot achieves stronger performance with a more compact working context, consistently outperforming existing baselines across various base models and benchmarks.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Characterization of Request and Token Energy Costs for LLM Inference Workloads on GPU Platforms](https://arxiv.org/abs/2608.28044v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Characterization of Request and Token Energy Costs for LLM Inference Workloads on GPU Platforms》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Batching also reduces token energy, but the gain is context-bounded: at 10 output tokens, the batch-16 to batch-1 gain falls from 6.31x at context-512 to 1.17x at context-4K.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：6.31x、1.17x。
- [Transformer-Based Autonomous Driving Models and Deployment-Oriented Compression: A Survey](https://arxiv.org/abs/2304.10891)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《Transformer-Based Autonomous Driving Models and Deployment-Oriented Compression: A Survey》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，At the same time, their deployment in real vehicles remains difficult because high-capacity attention-based architectures impose substantial latency, memory, and energy overhead.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [DAMP: Decay-Aware Mixed-Precision Recurrent-State Quantization](https://arxiv.org/abs/2608.27513)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《DAMP: Decay-Aware Mixed-Precision Recurrent-State Quantization》在 arXiv cs.LG 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，DAMP reduces recurrent-state storage by 69.1%, accelerates the recurrent-state update kernel by up to 2.01x, and lowers full-model TPOT by up to 10.9%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：69.1%、2.01x、10.9%。
- [CRAM: Centroid-Routing and Adaptive MoE for Multimodal Continual Instruction Tuning](https://arxiv.org/abs/2606.02502)
  - 主题: Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference、LLM routing，核心内容是《CRAM: Centroid-Routing and Adaptive MoE for Multimodal Continual Instruction Tuning》在 arXiv cs.CL 这一方向上的推进。强调异构硬件协同推理。从实验上看，Extensive experiments across diverse benchmarks demonstrate its superiority over existing methods.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [HARTS: Efficient Agentic Reinforcement Learning for Hybrid-Attention Models over Arbitrary Rollout Trees](https://arxiv.org/abs/2608.28158)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《HARTS: Efficient Agentic Reinforcement Learning for Hybrid-Attention Models over Arbitrary Rollout Trees》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，To our knowledge, HARTS is the first system to demonstrate arbitrary-rollout-tree prefix-sharing speedups on a real hybrid-attention model.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [FedEHR-Agents: Federated Agentic Optimization for Automated EHR Modeling](https://arxiv.org/abs/2608.27856)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《FedEHR-Agents: Federated Agentic Optimization for Automated EHR Modeling》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Extensive experiments on real-world multi-hospital EHR benchmarks demonstrate that FedEHR-Agents consistently outperforms local and federated baselines across diverse clinical prediction tasks and remains robust across different federation scales and LLM backbones.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Parser States Already Know: Structure-Conditioned KV Persistence for Structured Generation](https://arxiv.org/abs/2608.28276v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Parser States Already Know: Structure-Conditioned KV Persistence for Structured Generation》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，In end-to-end serving, PASK achieves up to 2.2x higher throughput and 3.3x lower TPOT, while using 0.53x the peak GPU memory of Full KV.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：2.2x、3.3x、0.53x。
- [Mixture of Multicenter Experts in Multimodal AI for Debiased Radiotherapy Target Delineation](https://arxiv.org/abs/2410.00046)
  - 主题: Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference，核心内容是《Mixture of Multicenter Experts in Multimodal AI for Debiased Radiotherapy Target Delineation》在 arXiv cs.LG 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，With few-shot training that combines imaging and clinical notes from each center, the model outperformed baselines, particularly in settings with high inter-center variability or limited data availability.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

