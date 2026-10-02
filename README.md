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

- 日期: 2026-10-02
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 1
- 日报: `papers/2026-10-02.md`
- 周报: `digests/weekly-2026-10-02.md`

## 今日最值得看

- [RapidMoE: Exploiting Cross-Asymmetry via Adaptive Residual Offloading for Large-Scale MoE Inference](https://arxiv.org/abs/2610.01265)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《RapidMoE: Exploiting Cross-Asymmetry via Adaptive Residual Offloading for Large-Scale MoE Inference》在 arXiv cs.DC 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Experimental results show that RapidMoE achieves up to 3.5x speedup in decoding and 2.1x speedup in prefill compared to state-of-the-art (SOTA) offloading systems.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：3.5x、2.1x。
- [MoE-CORE: Coordinated Expert Offloading and Residency for Memory-Constrained MoE Inference](https://arxiv.org/abs/2610.01950v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《MoE-CORE: Coordinated Expert Offloading and Residency for Memory-Constrained MoE Inference》在 arXiv API 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，Under an 84-GB NPU-memory cap, the best measured DeepSeek GSM8K configuration achieves a TPOT of 21.5 ms with approximate expert substitution and multi-token prediction (MTP) at depth 2.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：21.5 ms、44.8 ms、1269.1 ms。
- [MOMAT: Mixture of Multiple Atlases for Low-Power Jailbreak Defense of Quantized LLMs](https://arxiv.org/abs/2610.01058)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《MOMAT: Mixture of Multiple Atlases for Low-Power Jailbreak Defense of Quantized LLMs》在 arXiv cs.AI 这一方向上的推进。强调异构硬件协同推理。从实验上看，MOMAT's CiM-based retrieval accelerates a 100-query batch from 15,052.44 ms to 3,207.21 ns (a $4.69 \times 10^6\times$ speedup) and reduces energy from $8.1 \times 10^7$ $\mu$J to 3.32 $\mu$J, yielding an approximately $2.5 \times 10^5\times$ energy reduction over DRAM-based (Raspberry Pi) baselines.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：052.44 ms。
- [Nalar: Workflow-Aware Management of Agentic Applications](https://arxiv.org/abs/2601.05109)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Nalar: Workflow-Aware Management of Agentic Applications》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across three agentic workloads, Nalar reduces tail latency by 34-74% and achieves up to 3.38x speedups.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：74%、3.38x。
- [Raw-Routed Mixture of Adapters: A Causal Intervention for Routing Collapse in Time Series Foundation Models](https://arxiv.org/abs/2609.39445)
  - 主题: Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference、LLM routing，核心内容是《Raw-Routed Mixture of Adapters: A Causal Intervention for Routing Collapse in Time Series Foundation Models》在 arXiv cs.LG 这一方向上的推进。强调异构硬件协同推理。从实验上看，Frozen RR-MoA also beats full fine-tuning by 12-79% (the Frozen Paradox); two architecturally distinct variants confirm the principle generalizes beyond this specific router.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：79%。
- [Denoising Surface: Modeling and Predicting Inference Cost for Diffusion LLM Serving](https://arxiv.org/abs/2610.00499v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Denoising Surface: Modeling and Predicting Inference Cost for Diffusion LLM Serving》在 arXiv API 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，In \textit{real-world} serving experiments, DWS reduces cost-prediction error by up to $2.50\times$ over scalar-based predictors, while the DWS-guided shortest-job-first scheduler reduces end-to-end latency by up to $1.92\times$ for online chatbots.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [TierKV: Long-Context On-Device LLMs via Predictive Multi-Tier KV Caching](https://arxiv.org/abs/2609.21172)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《TierKV: Long-Context On-Device LLMs via Predictive Multi-Tier KV Caching》在 arXiv cs.LG 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，Across eight text, vision, and audio models on three mobile SoCs, TierKV improves prefill throughput by up to 17.6x over existing mobile LLM frameworks, reduces RAM-resident KV cache by 12.5-34%, thereby enabling substantially longer contexts under the same memory budget, while incurring only minor accuracy degradation.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：17.6x、34%。
- [Spatial Strategies, Not Actions: Vector-Quantized Geodesics as Tools for LLM-Driven Agents](https://arxiv.org/abs/2610.00613v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《Spatial Strategies, Not Actions: Vector-Quantized Geodesics as Tools for LLM-Driven Agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Pairing the geometry-derived tool library with an agent-centered zoom tool and a collision detection tool lets a fast, non-reasoning configuration match the goal-reaching rate of a much more costly chain-of-thought version, while cutting the cost of a decision from minutes to seconds.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [GPU-Initiated Communication: Dissecting Down to the Bone](https://arxiv.org/abs/2610.01380)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《GPU-Initiated Communication: Dissecting Down to the Bone》在 arXiv cs.DC 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Reaching the 260 M msg/s ceiling of our InfiniBand platform requires doorbell batching and queue parallelism, and both have resource costs: communication code can reduce GPU block residency even when unused, and all-to-all traffic loses 59% of its NIC message rate at about 3,000 active connections.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：59%。
- [RouteRec: Behavior-Guided Sparse Routing for Sequential Recommendation](https://arxiv.org/abs/2609.39007)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《RouteRec: Behavior-Guided Sparse Routing for Sequential Recommendation》在 arXiv cs.LG 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，Across six public datasets and 18 dataset-metric combinations, RouteRec ranks first in 12 and second in three, yielding the best overall average rank of 1.61 compared with 4.11 for the next-best baseline.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

