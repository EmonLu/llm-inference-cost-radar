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

- 日期: 2026-05-28
- 今日新论文: 15
- 今日新权威来源更新: 2
- 本周精选论文: 25
- 本周精选权威来源更新: 4
- 日报: `papers/2026-05-28.md`
- 周报: `digests/weekly-2026-05-28.md`

## 今日最值得看

- [How Far Can Disaggregation Go? A Design-Space Exploration of Attention-FFN Disaggregation for Efficient MoE LLM Serving](https://arxiv.org/abs/2605.28302)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《How Far Can Disaggregation Go? A Design-Space Exploration of Attention-FFN Disaggregation for Efficient MoE LLM Serving》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，We systematically characterize this trade-off for MoE inference across realistic workloads spanning input/output sequence lengths, prefix-KV reuse, and per-user latency constraints.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [When NPUs Are Not Always Faster: A Stage-Level Analysis of Mobile LLM Inference](https://arxiv.org/abs/2605.27435)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《When NPUs Are Not Always Faster: A Stage-Level Analysis of Mobile LLM Inference》在 arXiv cs.AI 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Our results reveal a counter-intuitive stage-level performance reversal: CPUs outperform NPUs in the compute-intensive Prefill stage (up to 1.6x), while NPUs provide only limited acceleration in the memory-bound Decode stage (1.05-1.2x).
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.6x、1.2x、51%。
- [Nonvolatile Charge-Domain Attention with HZO Ferroelectric Capacitors: A Simulation-Based Device-to-System Evaluation](https://arxiv.org/abs/2605.28208v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Nonvolatile Charge-Domain Attention with HZO Ferroelectric Capacitors: A Simulation-Based Device-to-System Evaluation》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，A workload-level simulator anchored on measured INT4 decode energy delivers 18-35x lower per-served-token energy on RAG and agent loops against a single-user INT4 GPU baseline; against optimized GPU serving (batched vLLM, CPU+NVMe park, power-gate) the robust advantage shrinks to 1.36-4.69x and remains >=41x on parked sessions with multi-hour residency.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：35x、4.69x、41x。
- [VidPrism: Heterogeneous Mixture of Experts for Image-to-Video Transfer](https://arxiv.org/abs/2605.28229)
  - 主题: Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference，核心内容是《VidPrism: Heterogeneous Mixture of Experts for Image-to-Video Transfer》在 arXiv cs.AI 这一方向上的推进。强调异构硬件协同推理。从实验上看，Extensive experiments on various video recognition benchmarks demonstrate that VidPrism achieves state-of-the-art performance and effectively fosters expert specialization.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [The Energy Blind Spot: NVIDIA's Flagship Edge AI Hardware Cannot Support Process-Level Energy Attribution](https://arxiv.org/abs/2605.27599)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《The Energy Blind Spot: NVIDIA's Flagship Edge AI Hardware Cannot Support Process-Level Energy Attribution》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，show that CPU-side processing accounts for up to 90.6% of total latency and 44% of total dynamic energy in agentic workloads.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：90.6%、44%、4.33x。
- [AgensFlow: A Coordination-Policy Substrate for Multi-Agent Systems](https://arxiv.org/abs/2605.27466)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、LLM routing，核心内容是《AgensFlow: A Coordination-Policy Substrate for Multi-Agent Systems》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The evaluation shows three main results: learned routing reaches a higher-quality operating point than a fixed pipeline baseline on coordination-heavy classes; skip:X isolates topology compression as a meaningful part of the substrate; and warm-started policy graphs can reduce exploration cost while preserving plateau quality.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Hurwitz Quaternion Multiplicative Quantization for KV Cache Compression](https://arxiv.org/abs/2605.27646)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Hurwitz Quaternion Multiplicative Quantization for KV Cache Compression》在 arXiv cs.LG 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，The multiplicative composition yields $24S$ effective codewords at $S$ stored parameters; random initialization suffices because left-multiplication is an $S^3$ isometry, so seeded codebooks vary in end-task ppl by $<1.5\%$.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：24S、43 GB、8.5 GB。
- [DIG to Heal: Scaling General-purpose Agent Collaboration via Explainable Dynamic Decision Paths](https://arxiv.org/abs/2603.00309)
  - 主题: Agent systems and multi-agent efficiency
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency，核心内容是《DIG to Heal: Scaling General-purpose Agent Collaboration via Explainable Dynamic Decision Paths》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，While many agentic AI systems reduce complexity through predefined workflows or fixed agent roles, the ideal is to support truly autonomous agents capable of emergent collaboration across many interacting agents.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Routing-Aligned Fine-Tuning for Multilingual Downstream Tasks in Mixture-of-Experts Models](https://arxiv.org/abs/2605.28306)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Routing-Aligned Fine-Tuning for Multilingual Downstream Tasks in Mixture-of-Experts Models》在 arXiv cs.CL 这一方向上的推进。强调异构硬件协同推理。从实验上看，Experiments across three MoE models, three tasks, and six target languages demonstrate that RA-MoE consistently outperforms standard SFT and strong baselines including Routing Steering and RISE, with the ci proportion of a task-language pair serving as a reliable predictor of alignment benefit.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Heterogeneous Parallelism for Multimodal Large Language Model Training](https://arxiv.org/abs/2605.27678)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Heterogeneous Parallelism for Multimodal Large Language Model Training》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Across this sweep, colocated heterogeneity improves TFLOPS/GPU by up to 49.3%, while non-colocated heterogeneity improves aggregate token throughput by up to 13.0% and TFLOPS/GPU by up to 9.6%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：49.3%、13.0%、9.6%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

