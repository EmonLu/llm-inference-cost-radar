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

- 日期: 2026-06-10
- 今日新论文: 15
- 今日新权威来源更新: 1
- 本周精选论文: 25
- 本周精选权威来源更新: 4
- 日报: `papers/2026-06-10.md`
- 周报: `digests/weekly-2026-06-10.md`

## 今日最值得看

- [Achieving Cloud-Grade SLOs for Local Mixture-of-Experts Inference through CPU-GPU Hybrid Design](https://arxiv.org/abs/2606.10493v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Achieving Cloud-Grade SLOs for Local Mixture-of-Experts Inference through CPU-GPU Hybrid Design》在 arXiv API 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，We present a CPU-GPU hybrid system that achieves cloud-level SLOs on dual-socket commodity CPUs and consumer GPUs by (1) stream-loading prefill (SLP), boosting prefill throughput to 1,200 tokens/s and enabling 32K prompts within 30 seconds; (2) distributed SLP (DSLP) with SmallEP expert parallelism, reaching 1,800 tokens/s and 45K prompts in 30 seconds on two RTX 5090s; (3) intra-node prefill-decode disaggregation with zero-copy shared weights and a dual-batch attention-MoE overlap scheme, sustaining concurrency with under 15 percent latency increase and 50 percent throughput gains; (4) an AVX-512-optimized FP8 GEMV kernel, enabling native CPU FP8 inference while delivering 4-5x lower CPU latency; and (5) fine-grained CPU parallelism that attains 28 tokens/s on INT4 DeepSeek-V3 and 21.5 tokens/s on intact FP8 V3.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：200 tokens/s、30 s、800 tokens/s。
- [AGENTSERVESIM: A Hardware-aware Simulator for Multi-Turn LLM Agent Serving](https://arxiv.org/abs/2606.09613v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《AGENTSERVESIM: A Hardware-aware Simulator for Multi-Turn LLM Agent Serving》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across real serving deployments and hardware configurations, AGENTSERVESIM reproduces real-system behavior within 6% error across key performance metrics while running entirely on commodity CPUs.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：6%。
- [FAME: Forecastability-Aware Mixture of Experts for Heterogeneous Time Series Forecasting](https://arxiv.org/abs/2606.08896v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《FAME: Forecastability-Aware Mixture of Experts for Heterogeneous Time Series Forecasting》在 arXiv API 这一方向上的推进。强调异构硬件协同推理。从实验上看，The deployed component produces demand forecasts, while inventory-oriented gains are estimated by an offline replay simulator under a fixed replenishment policy rather than by online intervention.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Kwai Keye-VL-2.0 Technical Report](https://arxiv.org/abs/2606.10651v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Kwai Keye-VL-2.0 Technical Report》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Extensive evaluations across video understanding, temporal grounding, reasoning, STEM, and agent benchmarks demonstrate that Keye-VL-2.0-30B-A3B achieves state-of-the-art performance among models of similar scale, particularly excelling in fine-grained temporal localization on TimeLens and long-video comprehension on Video-MME-v2 and LongVideoBench.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Game-Theoretic Multi-Agent Control for Robust Contextual Reasoning in LLMs](https://arxiv.org/abs/2606.10322v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Game-Theoretic Multi-Agent Control for Robust Contextual Reasoning in LLMs》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Empirical evaluation over 500 interaction turns under an adaptive adversarial threat model shows that contextual drift remains bounded in 99.6% of turns, with recovery required in only 0.4%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：99.6%、0.4%、98%。
- [Alignment Collapse Under KV Cache Quantization: Diagnosis and Mitigation](https://arxiv.org/abs/2606.09864)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Alignment Collapse Under KV Cache Quantization: Diagnosis and Mitigation》在 arXiv cs.LG 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Across eleven instruction-tuned models (3.8B-72B) and five benchmarks (1,894 prompts), we find that low-bit quantization can silently destroy safety alignment: Mistral-7B loses 15.2% of its refusals at only 1.03x perplexity, and no universal safe bit-width exists, with sharp model-specific phase transitions invisible to standard metrics.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：15.2%、1.03x、97%。
- [Isolation-aware Scheduling Framework for DNN-based End-to-End Autonomous Driving System on Tile-based Accelerators](https://arxiv.org/abs/2606.10303)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Isolation-aware Scheduling Framework for DNN-based End-to-End Autonomous Driving System on Tile-based Accelerators》在 arXiv cs.DC 这一方向上的推进。强调异构硬件协同推理。从实验上看，On an industry- and academia- derived ADS benchmark, ADS-Tile uses up to 32% fewer tiles than the work-conserving baseline in deadline-critical settings and cuts reallocation-induced wasted processing capacity from 17%-44% to below 1.2%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：32%、17%、44%。
- [Projecting the Emerging Mindset of SWE Agent by Launching a Wild Code Understanding Journey](https://arxiv.org/abs/2606.08500v1)
  - 主题: Coding agent routing, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Coding agent routing、Cost-efficient LLM inference，核心内容是《Projecting the Emerging Mindset of SWE Agent by Launching a Wild Code Understanding Journey》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The results expose differences in efficiency, trajectory diversity, epistemic grounding, and the limits of intervention, while providing a methodological foundation for observing SWE agent behavior in real codebases.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [LLM-Aided Joint Secrecy Precoding and Trajectory for RSMA-Based Heterogeneous UAV Networks](https://arxiv.org/abs/2507.17188)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《LLM-Aided Joint Secrecy Precoding and Trajectory for RSMA-Based Heterogeneous UAV Networks》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The inner layer uses a semidefinite relaxation (SDR)-based S2DC algorithm combining penalty functions and difference-of-convex (D.C.) programming to solve the secrecy precoding problem with fixed UAV positions.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Semantic Multi-Agent Intrusion Detection for IoT:Zero-Day and Adversarial Threats with Risk-Aware Reasoning](https://arxiv.org/abs/2606.10323v1)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《Semantic Multi-Agent Intrusion Detection for IoT:Zero-Day and Adversarial Threats with Risk-Aware Reasoning》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Extensive experiments across multiple real-world IoT datasets demonstrate that the proposed system achieves 95.9% overall detection accuracy, reduces false-positive rates to 6.8%, improves zero-day detection to 87.9%, and maintains computational efficiency suitable for edge deployment.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：95.9%、6.8%、87.9%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

