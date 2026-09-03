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

- 日期: 2026-09-03
- 今日新论文: 15
- 今日新权威来源更新: 1
- 本周精选论文: 25
- 本周精选权威来源更新: 3
- 日报: `papers/2026-09-03.md`
- 周报: `digests/weekly-2026-09-03.md`

## 今日最值得看

- [WhiFlash: Accelerating Speculative Decoding with Token-Level Cross-Paradigm Routing](https://arxiv.org/abs/2606.07710)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、LLM routing，核心内容是《WhiFlash: Accelerating Speculative Decoding with Token-Level Cross-Paradigm Routing》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，By capitalising on the complementary strengths of fundamentally distinct drafting architectures, WhiFlash achieves significantly higher acceptance lengths, yielding category-specific throughput gains of up to 69.6% over the state-of-the-art autoregressive EAGLE-3 and 37.3% over the diffusion-based DFlash.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：69.6%、37.3%、7%。
- [Scaling Inference Prefill with High-Radix Photonic Interconnects](https://arxiv.org/abs/2609.01821v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Scaling Inference Prefill with High-Radix Photonic Interconnects》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，We show 2.1--3.2x latency improvements in the stressed high-batch regimes and 2.8--5.8x improvements over baselines in communication-limited configurations.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：3.2x、5.8x、4.5x。
- [PaperCompiler: Faithful Paper-to-Code Generation via Repository-Level Specification Compilation](https://arxiv.org/abs/2609.02272v1)
  - 主题: Coding agent routing, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Coding agent routing、Cost-efficient LLM inference，核心内容是《PaperCompiler: Faithful Paper-to-Code Generation via Repository-Level Specification Compilation》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，PaperCompiler outperforms strong baselines on Paper2CodeBench, achieving a 13.8% relative improvement in reference-based fidelity (from 3.64 to 4.15) and reducing high-severity evaluator critiques (from 13.2% to 6.1%).
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：13.8%、13.2%、6.1%。
- [GMTRouter: Personalized LLM Router over Multi-turn User Interactions](https://arxiv.org/abs/2511.08590)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《GMTRouter: Personalized LLM Router over Multi-turn User Interactions》在 arXiv cs.CL 这一方向上的推进。强调异构硬件协同推理。从实验上看，Extensive experiments demonstrate that GMTRouter outperforms the strongest baselines, achieving up to a 0.108 absolute improvement in accuracy and a 0.124 improvement in AUC.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [ShallowStream: Index Shallow then Answer Deep for Streaming Video Understanding](https://arxiv.org/abs/2609.02780)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《ShallowStream: Index Shallow then Answer Deep for Streaming Video Understanding》在 arXiv cs.CL 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，ShallowStream achieves performance on par with the strongest existing streaming methods, while reducing per-frame prefill latency and 10-second end-to-end latency by up to 52.1x and 11.9x, respectively.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：52.1x、11.9x。
- [NS-Copilot: An LLM-Driven Agent System for Autonomous Neuroscience Analysis](https://arxiv.org/abs/2609.01971)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《NS-Copilot: An LLM-Driven Agent System for Autonomous Neuroscience Analysis》在 arXiv cs.CL 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，We evaluate NS-Copilot on neuroscience benchmarks spanning Alzheimer's disease, Parkinson's disease, and working memory spike decoding.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Jailbreaking Text-to-Image Models Through Cracks: Navigating Heterogeneous Safety Filters via Multi-Agent Debate](https://arxiv.org/abs/2609.01168)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Jailbreaking Text-to-Image Models Through Cracks: Navigating Heterogeneous Safety Filters via Multi-Agent Debate》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Extensive experiments across multiple T2I models, datasets, and safety configurations show that CRACK achieves Attack Success Rates (ASR) of up to 99.63% under composite defenses, while requiring fewer queries than existing methods and maintaining semantic fidelity.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：99.63%。
- [SEAL: Reinforcing Global Safety in Mixture-of-Experts through Shared Expert ALignment](https://arxiv.org/abs/2609.02293)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《SEAL: Reinforcing Global Safety in Mixture-of-Experts through Shared Expert ALignment》在 arXiv cs.LG 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，SEAL reduces attack success rate (ASR) by up to 60\%, at a capability cost of at most 1.4\% on a five-benchmark average.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Can escalation channels redirect reward hacking toward defect disclosure?](https://arxiv.org/abs/2608.29460)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、LLM routing，核心内容是《Can escalation channels redirect reward hacking toward defect disclosure?》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across 8 frontier models spanning 5 families, the combined intervention reduces reward hacking from 23.6% to 5.3% (mixed-effects logistic OR = 9.2, 95% CI 5.0--16.8, $p < 10^{-12}$) with no detectable cost or performance overhead, eliminating it entirely for 6 of 8 models.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：23.6%、5.3%、95%。
- [Agent Flight Recorder: Tamper-Evident Audit Trails with On-Chain Anchoring for Long-Horizon Tool-Using Agents](https://arxiv.org/abs/2609.01931v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《Agent Flight Recorder: Tamper-Evident Audit Trails with On-Chain Anchoring for Long-Horizon Tool-Using Agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The full integrity stack detects edit, delete, reorder, and fork tampering at 100% with zero false positives.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：100%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

