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

- 日期: 2026-05-23
- 今日新论文: 10
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 3
- 日报: `papers/2026-05-23.md`
- 周报: `digests/weekly-2026-05-23.md`

## 今日最值得看

- [Runtime-Certified Bounded-Error Quantized Attention](https://arxiv.org/abs/2605.20868v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Runtime-Certified Bounded-Error Quantized Attention》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，KV cache quantization reduces the memory cost of long-context LLM inference, but introduces approximation error that is typically validated only empirically.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [MOSS: Self-Evolution through Source-Level Rewriting in Autonomous Agent Systems](https://arxiv.org/abs/2605.22794v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、LLM routing，核心内容是《MOSS: Self-Evolution through Source-Level Rewriting in Autonomous Agent Systems》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Candidates are verified by replaying the batch against the candidate image in ephemeral trial workers, then promoted via user-consent-gated, in-place container swap with health-probe-gated rollback.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Compiling Agentic Workflows into LLM Weights: Near-Frontier Quality at Two Orders of Magnitude Less Cost](https://arxiv.org/abs/2605.22502v1)
  - 主题: Agent systems and multi-agent efficiency, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、LLM routing，核心内容是《Compiling Agentic Workflows into LLM Weights: Near-Frontier Quality at Two Orders of Magnitude Less Cost》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Recent work has shown this architecture is dominated for procedural tasks by simply providing the procedure in a frontier model's system prompt [Dennis et al., 2026a], at the cost of consuming the context window, requiring a frontier model for every conversation, and exposing proprietary procedures to third-party providers.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [F-TIS: Harnessing Diverse Models in Collaborative GRPO](https://arxiv.org/abs/2605.22537v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《F-TIS: Harnessing Diverse Models in Collaborative GRPO》在 arXiv API 这一方向上的推进。强调异构硬件协同推理。从实验上看，Furthermore, we observe in some setups better generalization on out-of-distribution tasks than on-policy training, increasing model's performance by up to 12\%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [PulseCol: Periodically Refreshed Column-Sparse Attention for Accelerating Diffusion Language Models](https://arxiv.org/abs/2605.20813v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《PulseCol: Periodically Refreshed Column-Sparse Attention for Accelerating Diffusion Language Models》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Experiments show that PulseCol achieves higher sparsity and greater practical speedup than prior sparse attention methods for dLLMs, while maintaining model quality.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [ArborKV: Structure-Aware KV Cache Management for Scaling Tree-based LLM Reasoning](https://arxiv.org/abs/2605.22106v1)
  - 主题: Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference，核心内容是《ArborKV: Structure-Aware KV Cache Management for Scaling Tree-based LLM Reasoning》在 arXiv API 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，Experiments on ToT-style reasoning benchmarks show that ArborKV achieves up to ~4x peak KV-memory reduction while preserving near-full-retention accuracy, enabling larger search configurations under fixed device budgets that would otherwise run out of memory.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：4x。
- [FruitEnsemble: MLLM-Guided Arbitration for Heterogeneous ensemble in Fine-Grained Fruit Recognition](https://arxiv.org/abs/2605.20892v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《FruitEnsemble: MLLM-Guided Arbitration for Heterogeneous ensemble in Fine-Grained Fruit Recognition》在 arXiv API 这一方向上的推进。强调异构硬件协同推理。从实验上看，Extensive experiments demonstrate that FruitEnsemble achieves a classification accuracy of 70.49\% and outperforms existing state-of-the-art models.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [IdleSpec: Exploiting Idle Time via Speculative Planning for LLM Agents](https://arxiv.org/abs/2605.22154v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《IdleSpec: Exploiting Idle Time via Speculative Planning for LLM Agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Furthermore, for MLE-Bench, which involves substantial delay from code executions, IdleSpec achieves performance gains of up to 9.1% on the Any Medal rate, highlighting its generalizability to long-horizon tasks.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：9.1%、55.6%、5.1%。
- [Diagnosis Is Not Prescription: Linguistic Co-Adaptation Explains Patching Hazards in LLM Pipelines](https://arxiv.org/abs/2605.21958v1)
  - 主题: Agent systems and multi-agent efficiency, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、LLM routing，核心内容是《Diagnosis Is Not Prescription: Linguistic Co-Adaptation Explains Patching Hazards in LLM Pipelines》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，We operationalize this via a per-agent co-adaptation measure, derived from diagnosis alone, and show it is consistently associated with patching harm across agent families: higher co-adaptation co-occurs with harm, lower with safety.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Agent JIT Compilation for Latency-Optimizing Web Agent Planning and Scheduling](https://arxiv.org/abs/2605.21470v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Agent JIT Compilation for Latency-Optimizing Web Agent Planning and Scheduling》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Our approach comprises three components: (1) JIT-Planner, which generates multiple code plans, validates each against tool specifications, and selects the minimum-cost candidate; (2) JIT-Scheduler, which explores parallelization strategies via Monte Carlo cost estimation from learned latency distributions; and (3) an invariant-enforcing tool protocol specifying precondition and postcondition state requirements that reduce the rate of generating plans with incorrect tool use.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

