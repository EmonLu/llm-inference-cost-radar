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

- 日期: 2026-10-31
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 2
- 日报: `papers/2026-10-31.md`
- 周报: `digests/weekly-2026-10-31.md`

## 今日最值得看

- [Nemotron 3.5 Super and Lightning: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Models for Agentic AI](https://arxiv.org/abs/2610.38095)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Nemotron 3.5 Super and Lightning: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Models for Agentic AI》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Post-training MTP boosting improves speculative- decoding acceptance length by up to 21.8% under probabilistic draft sampling, while NVFP4 quantization achieves 99.62% median accuracy recovery relative to BF16.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：21.8%、99.62%、51.78%。
- [Rocks, Pebbles and Sand: Modality-aware Scheduling for Multimodal Large Language Model Inference](https://arxiv.org/abs/2603.26498)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Rocks, Pebbles and Sand: Modality-aware Scheduling for Multimodal Large Language Model Inference》在 arXiv cs.AI 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Evaluation across state-of-the-art MLLMs shows that RPS-Serve increases GPU utilization by 65% and reduces TTFT by up to 9.3x, on average across models, compared to disaggregation-based multi-modal systems.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：65%、9.3x。
- [Interpretability Is Not Just a Tax: Sparsity and Diversity Yield Legible and Composable Reward Experts for Personalization](https://arxiv.org/abs/2606.04284)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Interpretability Is Not Just a Tax: Sparsity and Diversity Yield Legible and Composable Reward Experts for Personalization》在 arXiv cs.AI 这一方向上的推进。强调异构硬件协同推理。从实验上看，The resulting configuration, which we call sparse MoE, recovers all underlying semantic categories without domain supervision in a controlled setting, reaching 84.8% expert purity against 60.8% for conventional MoE; on real-world data its experts admit human-interpretable task- and domain-level descriptions aligned with their functional strengths.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：84.8%、60.8%。
- [From Legacy Fortran to Portable Kokkos: An Autonomous Agentic AI Workflow](https://arxiv.org/abs/2509.12443)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《From Legacy Fortran to Portable Kokkos: An Autonomous Agentic AI Workflow》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，dollars, whereas open-weights models such as gpt-oss-120b and Qwen3.5-397B-A17B handled simpler kernels but struggled with complex Kokkos abstractions such as parallel reductions and hierarchical parallelism.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Why Speculative Decoding Works Better Than Predicted on Sparse MoE Models](https://arxiv.org/abs/2610.38981)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Why Speculative Decoding Works Better Than Predicted on Sparse MoE Models》在 arXiv cs.AI 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，For mixture-of-experts (MoE) models, prior work predicts a concave speedup-batch size relationship, with gains peaking at intermediate batch sizes due to expert saturation.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：10 s。
- [LRMoE: Demand-Side Load Re-Calibration for Efficient MoE Training on Memory-Constrained Nodes](https://arxiv.org/abs/2610.37720)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《LRMoE: Demand-Side Load Re-Calibration for Efficient MoE Training on Memory-Constrained Nodes》在 arXiv cs.AI 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Experiments on Qwen3-30B-A3B and GLM4.5-106B-A12B show that LRMoE reduces cumulative MoE-layer training time to fixed-loss targets by 21.2-44.8% relative to SYMI.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：44.8%。
- [The Illusion of Power Capping in LLM Decode: A Phase-Aware Energy Characterisation Across Attention Architectures](https://arxiv.org/abs/2605.11999)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《The Illusion of Power Capping in LLM Decode: A Phase-Aware Energy Characterisation Across Attention Architectures》在 arXiv cs.AI 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Locking the SM clock instead lowers power without slowing memory-bound decode and recovers up to 32% of decode energy at minimal throughput loss.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：32%。
- [S$^2$-MAS: A Society-Scale Multi-Agent Simulation Framework with a 500-Million-Persona Resource](https://arxiv.org/abs/2610.27746)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《S$^2$-MAS: A Society-Scale Multi-Agent Simulation Framework with a 500-Million-Persona Resource》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Trained with SFT + RLCD on 2.93 million examples, YN-mini-MLX achieves 74.55% accuracy and 38.37% question-macro F1 on held-out consumer financial-choice tasks, improving on the training-question majority baseline by 2.78 and 6.21 percentage points.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：74.55%、38.37%、3.42%。
- [INFRAMIND: Infrastructure-Aware Multi-Agent Orchestration](https://arxiv.org/abs/2606.11440)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《INFRAMIND: Infrastructure-Aware Multi-Agent Orchestration》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，With 15 models and Azure timings replayed on the same benchmark and deadline tiers, this fraction rises from 11.6% to 54.8% over MasRouter.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：11.6%、54.8%、300 s。
- [Only Accepted Tokens Count: An Energy Accounting of Speculative Decoding Under Latency Targets](https://arxiv.org/abs/2610.40287)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Only Accepted Tokens Count: An Energy Accounting of Speculative Decoding Under Latency Targets》在 arXiv cs.AI 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Meeting a tighter latency target with speculation then costs additional energy.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

