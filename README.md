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

- 日期: 2026-10-12
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 5
- 日报: `papers/2026-10-12.md`
- 周报: `digests/weekly-2026-10-12.md`

## 今日最值得看

- [P-PAS: Prefill-Pressure Adaptive Scheduling for Long-Context LLM Serving](https://arxiv.org/abs/2608.15171)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《P-PAS: Prefill-Pressure Adaptive Scheduling for Long-Context LLM Serving》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On mixed-shape workloads using Qwen3.8-27B and Nemotron-3.5-Lightning-30B-A3B, P-PAS+ reduces mean end-to-end latency by 3.0--3.1% relative to the best tested static token budget.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：3.1%、91.2%、88.5%。
- [Taking Tokenization off the Host for Agentic LLM Serving](https://arxiv.org/abs/2610.13325v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Taking Tokenization off the Host for Agentic LLM Serving》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On TokTier's own single-request benchmark, it is 2.6-3.9x faster than gigatoken and up to 18.1x faster than TokTier.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：3.9x、18.1x、2.5x。
- [Democratizing MoE inference on commodity GPUs with CoMoE](https://arxiv.org/abs/2610.09424)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Democratizing MoE inference on commodity GPUs with CoMoE》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Evaluation on RTX 5090 GPUs shows that CoMoE improves inference throughput by up to 1.46x, approaching the performance of NVLink-capable A800 GPUs at only 23.4% of the hardware cost.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.46x、23.4%。
- [Zepp: Accelerating Distributed MoE Serving under Relaxed Balance Constraints](https://arxiv.org/abs/2610.11158)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Zepp: Accelerating Distributed MoE Serving under Relaxed Balance Constraints》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，We implement Zepp and evaluate it against 7 state-of-the-art MoE serving systems, achieving up to 6.68$\times$ MoE layer speedup and a geometric mean speedup of 1.86$\times$ over the fastest competing baseline.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：7 s。
- [STAPLE: Static Sparse Upcycling of Pretrained Checkpoints via Embedding Modules](https://arxiv.org/abs/2610.12599)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《STAPLE: Static Sparse Upcycling of Pretrained Checkpoints via Embedding Modules》在 arXiv cs.LG 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，STAPLE also outperforms static sparse baselines such as STEM and an Engram-style model, and achieves a higher average score than an MoE upcycling baseline while decoding 2x faster with less than half its GPU model memory and measured GPU energy per token in our throughput-oriented decoding evaluation.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：2x、1.5%、3%。
- [S$^3$R: Fast and Faithful RL Rollouts via Self-Sparse Speculative Decoding](https://arxiv.org/abs/2610.13202)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《S$^3$R: Fast and Faithful RL Rollouts via Self-Sparse Speculative Decoding》在 arXiv cs.CL 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，Under S$^3$R, we characterize speedup conditions and the costs of drafting and verification.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [DuoRate: Two-Rate Per-Expert Precision Allocation for Mixture-of-Experts Serving](https://arxiv.org/abs/2610.13328)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《DuoRate: Two-Rate Per-Expert Precision Allocation for Mixture-of-Experts Serving》在 arXiv cs.LG 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，Against controls in its own format, the allocation alone is worth 0.07-0.11 bpw of read rate.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Adaptive DHiSparse: Speculative Decoding over a Load-Adaptive KV Hierarchy](https://arxiv.org/abs/2610.13708)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Adaptive DHiSparse: Speculative Decoding over a Load-Adaptive KV Hierarchy》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，In a load step, optional residency reduces host fetches from 14.2% to 1.4% of selected rows at low load and releases memory under pressure.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：14.2%、1.4%。
- [Can escalation channels redirect reward hacking toward defect disclosure?](https://arxiv.org/abs/2608.29460)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、LLM routing，核心内容是《Can escalation channels redirect reward hacking toward defect disclosure?》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across 8 frontier models spanning 5 families, the combined intervention reduces reward hacking from 23.6% to 5.3% (mixed-effects logistic OR = 9.2, 95% CI 5.0--16.8, $p < 10^{-12}$) with no detectable cost or performance overhead, eliminating it entirely for 6 of 8 models.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：23.6%、5.3%、95%。
- [Agentic Peer-to-Peer Networks: From Content Distribution to Capability and Action Sharing](https://arxiv.org/abs/2603.03753)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Agentic Peer-to-Peer Networks: From Content Distribution to Capability and Action Sharing》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Results from a proxy-level discrete-event simulation suggest improved workflow success under poisoning and drift with modest control-plane overhead.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

