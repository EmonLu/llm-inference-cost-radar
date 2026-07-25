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

- 日期: 2026-07-25
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 5
- 日报: `papers/2026-07-25.md`
- 周报: `digests/weekly-2026-07-25.md`

## 今日最值得看

- [Efficient and Privacy Aware Edge Cloud Collaborative Inference for Large Language Models](https://arxiv.org/abs/2607.13093)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Efficient and Privacy Aware Edge Cloud Collaborative Inference for Large Language Models》在 arXiv cs.AI 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Evaluations demonstrate that the framework reduces per-token latency by up to 46.1\% and downlink payloads by up to 67.4\% over baseline split inference, retaining comparable performance to full cloud inference.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Windowed-MTP: Removing the Full-Context Draft-KV Tax at Million-Token Context](https://arxiv.org/abs/2607.21535)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Windowed-MTP: Removing the Full-Context Draft-KV Tax at Million-Token Context》在 arXiv cs.CL 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Finally, the unread draft KV -- 7.7-11% of total KV at 1M -- is reclaimed via a compact ring buffer at no acceptance or quality cost.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：11%、28%、44%。
- [AINTMA: Agentic AI Architecture for Autonomous Test Management with Generative Intelligence, Secure Cloud Communication and Adaptive Quality Analytics](https://arxiv.org/abs/2607.20452)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《AINTMA: Agentic AI Architecture for Autonomous Test Management with Generative Intelligence, Secure Cloud Communication and Adaptive Quality Analytics》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Evaluation across 12 heterogeneous software projects over 18 months demonstrates: 88.4% test prioritization accuracy (APFD, vs.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：88.4%、51.2%、82.1%。
- [Overcoming the Communication-Performance Tradeoff in LLM Pretraining](https://arxiv.org/abs/2508.15706)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Overcoming the Communication-Performance Tradeoff in LLM Pretraining》在 arXiv cs.LG 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，In this work, we introduce SparseLoCo, a communication-efficient training algorithm for LLMs that can effectively leverage Top-k sparsification and 2-bit quantization to reach extreme sparsity in the communicated pseudo-gradient, as high as 97-99%, while achieving lower final loss than dense DiLoCo.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：99%。
- [VibeVoice-ASR-BitNet Technical Report](https://arxiv.org/abs/2607.21075)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《VibeVoice-ASR-BitNet Technical Report》在 arXiv cs.CL 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，VibeVoice-ASR-BitNet is 1.6-2.3x faster than Whisper.cpp at comparable model sizes (~1.6 GB), with only modest accuracy degradation compared to the FP16 baseline.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：2.3x、1.6 GB。
- [From Scalars to Time Series: Rethinking Implicit Neural Representations for Time-Varying Volumetric Data](https://arxiv.org/abs/2607.20970)
  - 主题: Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference，核心内容是《From Scalars to Time Series: Rethinking Implicit Neural Representations for Time-Varying Volumetric Data》在 arXiv cs.AI 这一方向上的推进。强调异构硬件协同推理。从实验上看，We demonstrate that this representation is compatible with a range of existing INR architectures and consistently improves reconstruction quality, while significantly reducing training cost.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [InferenceBench: A Benchmark for Open-Ended LLM Inference Optimization by AI Agents](https://arxiv.org/abs/2607.20468)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《InferenceBench: A Benchmark for Open-Ended LLM Inference Optimization by AI Agents》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Three optimization scenarios isolate distinct bottlenecks of inference (prefill latency, decode latency, and concurrent request throughput) and a fourth balances all three at the same time.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Explainable Belief Harmonization under Dynamic Epistemic Partitions](https://arxiv.org/abs/2607.21210)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Explainable Belief Harmonization under Dynamic Epistemic Partitions》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Evaluation across 100 randomly generated topology changes confirms complete violation detection and explanation coverage.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [HERMES: Heterogeneous Edge-Relational Multi-Head Embedded SSM Attention for Traffic Conflict Prediction at Signalized Intersections](https://arxiv.org/abs/2607.20505)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《HERMES: Heterogeneous Edge-Relational Multi-Head Embedded SSM Attention for Traffic Conflict Prediction at Signalized Intersections》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，At a 5% false-alarm rate, it detected 95.7% of conflict sequences, outperforming the strongest Transformer baseline and XGBoost.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：5%、95.7%。
- [A Three-Phase Foundation Model for Tax-Aware Personalized Portfolio Management](https://arxiv.org/abs/2606.30997)
  - 主题: Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference、LLM routing，核心内容是《A Three-Phase Foundation Model for Tax-Aware Personalized Portfolio Management》在 arXiv cs.AI 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，Phase 2 fine-tunes a MoE (Mixture of Experts) portfolio actor critic with PPO under an objective-conditioned reward that simultaneously serves six distinct investment goals sampled per episode: short-term alpha, short-term gain, long-term gain, capital preservation, tax-loss harvesting, and long-term-gains-only.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

