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

- 日期: 2026-11-26
- 今日新论文: 15
- 今日新权威来源更新: 1
- 本周精选论文: 25
- 本周精选权威来源更新: 5
- 日报: `papers/2026-11-26.md`
- 周报: `digests/weekly-2026-11-26.md`

## 今日最值得看

- [MixMoMo: Accelerating Extra--Large MoE Inference with Mixed--Precision GPU--NPU Execution on Mobile Devices](https://arxiv.org/abs/2611.33981v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《MixMoMo: Accelerating Extra--Large MoE Inference with Mixed--Precision GPU--NPU Execution on Mobile Devices》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across three MoE models and five benchmarks on two mobile platforms, MixMoMo achieves average decoding speedups of 3.72x over uniform Q4_0 and 1.53x over the strongest mixed-precision MoE baseline.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：3.72x、1.53x。
- [SparDA: Sparse Decoupled Attention for Efficient Long-Context LLM Inference](https://arxiv.org/abs/2606.04511)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《SparDA: Sparse Decoupled Attention for Efficient Long-Context LLM Inference》在 arXiv cs.CL 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，On the evaluated 8B models, SparDA adds <0.5% parameters and trains only the Forecast projections using attention-derived supervision from the frozen backbone.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：0.5%。
- [VibeServe: Can AI Agents Build Bespoke LLM Serving Systems?](https://arxiv.org/abs/2605.06068)
  - 主题: Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Coding agent routing、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《VibeServe: Can AI Agents Build Bespoke LLM Serving Systems?》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，In standard serving settings, VibeServe matches vLLM and SGLang on Llama-3.1-8B, and delivers 2.3x the goodput of a tuned SGLang for a 397B MoE model on four AMD MI300As.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：2.3x。
- [RankCast: Phase-Aware Rank Balancing in MoE Serving](https://arxiv.org/abs/2611.33542v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《RankCast: Phase-Aware Rank Balancing in MoE Serving》在 arXiv API 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，On Qwen3-235B-A22B with EP=8 and Qwen3.5-397B-A17B with EP=16, RankCast removes over 75% of the busiest rank's excess prefill load, improves prefill input throughput by up to 19%, and reduces decode time per output token by up to 10%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：75%、19%、10%。
- [Latent-in-the-Middle: On the Security of Cross-Model Latent Communication in Multi-Agent Systems](https://arxiv.org/abs/2611.34278v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Latent-in-the-Middle: On the Security of Cross-Model Latent Communication in Multi-Agent Systems》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On the other hand, for jailbreak attacks, transfer alone raises attack success by up to 24.6 pp within a model family and zero-shot attacks by up to 69.2 pp, whereas white-box optimization through the mapper boosts the attack success rate to 92.5%, against 37.5% for ordinary GCG on the same target.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：92.5%、37.5%、0.4%。
- [Ostinato: Low-Latency CPU-GPU MoE Inference for Local Agents](https://arxiv.org/abs/2611.11533)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Ostinato: Low-Latency CPU-GPU MoE Inference for Local Agents》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Short tool turns touch more experts than consumer GPUs can hold, yet direct roughly 85% of DeepSeek-V4-Flash's routes to a static GPU pool while leaving 3.3-5.5 tokens per cold expert.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：85%、335 GB、2.19x。
- [MobileMoE: Scaling On-Device Mixture of Experts](https://arxiv.org/abs/2605.27358)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《MobileMoE: Scaling On-Device Mixture of Experts》在 arXiv cs.AI 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，Across 14 benchmarks, MobileMoE matches or exceeds leading on-device dense LLMs with 2-4$\times$ fewer inference FLOPs, and matches or surpasses the state-of-the-art MoE OLMoE-1B-7B with up to 60% fewer parameters.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：60%。
- [FlashProve-Next: Verifiable Inference for Production LLM APIs](https://arxiv.org/abs/2611.33741v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《FlashProve-Next: Verifiable Inference for Production LLM APIs》在 arXiv API 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Rust fpn-verify checks 8 MiB FPN2 Relation 2 proofs in 10.1 ms on CPU.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：8 MiB、10.1 ms。
- [InterQ-RL: Interaction-Aware Correction of Execution Mismatch in Quantized Agentic RL](https://arxiv.org/abs/2610.35303)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《InterQ-RL: Interaction-Aware Correction of Execution Mismatch in Quantized Agentic RL》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Quantized rollout reduces these costs, but its low-precision executor also serves as the behavior policy and can induce execution mismatch with the learner.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [When Are Parallel Subagents Effective for Coding? An Empirical Study on Repository Construction](https://arxiv.org/abs/2611.33893v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing，核心内容是《When Are Parallel Subagents Effective for Coding? An Empirical Study on Repository Construction》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On randomly drawn tasks, parallel subagents raise hidden-test pass rates by only about 1 to 5 percentage points at up to 3.8x the cost of a single agent.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：3.8x。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

