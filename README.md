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

- 日期: 2026-09-15
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 2
- 日报: `papers/2026-09-15.md`
- 周报: `digests/weekly-2026-09-15.md`

## 今日最值得看

- [Dynamic HBM Repartitioning for Multi-Turn MoE Serving](https://arxiv.org/abs/2609.13537)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Dynamic HBM Repartitioning for Multi-Turn MoE Serving》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across five replays of a recorded 2,103-turn SWE-bench agent workload, VAMP with a 15% maximum expert-offloading ratio reduces time-to-first-token (TTFT) p90 from 26.1 s to 1.10 s (23.6 times) and increases request throughput by 20.7% relative to unmodified vLLM, while increasing time per output token (TPOT) by 31.1%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：15%、26.1 s、1.10 s。
- [PDD: Unleashing Economical and Flexible Heterogeneous LLM Inference via Cross-Datacenter Prefill-Decode Disaggregation](https://arxiv.org/abs/2609.13161)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《PDD: Unleashing Economical and Flexible Heterogeneous LLM Inference via Cross-Datacenter Prefill-Decode Disaggregation》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Compared to the intra-DC homogeneous PD baseline, PDD's cross-datacenter mapping of compute-intensive H100s and memory-bandwidth-optimized H200s achieves a Benefit-Cost Ratio (BCR) up to 37.5% higher in SLA-compliant goodput.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：100s、200s、37.5%。
- [OpWeave: Flexible Operator Disaggregation for Heterogeneous LLM Serving](https://arxiv.org/abs/2609.14237)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《OpWeave: Flexible Operator Disaggregation for Heterogeneous LLM Serving》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，In our evaluation, OpWeave reduces serving cost by up to $1.78\times$ on homogeneous and $1.89\times$ on heterogeneous GPU clusters relative to the best feasible baseline, while meeting latency SLOs.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [MAPS: Memory-Aware Predictive Scheduling Framework for Large Language Model Serving](https://arxiv.org/abs/2609.15359)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《MAPS: Memory-Aware Predictive Scheduling Framework for Large Language Model Serving》在 arXiv cs.AI 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，Extensive experiments on two real-world workloads and two LLMs show that MAPS significantly outperforms three state-of-the-art systems, reducing average end-to-end latency by 42.6 and tail latency by up to 84.8.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [BigMoMo: Efficient Inference of Large-Scale MoE with Speculative Decoding on Mobile Devices](https://arxiv.org/abs/2609.14643)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《BigMoMo: Efficient Inference of Large-Scale MoE with Speculative Decoding on Mobile Devices》在 arXiv cs.DC 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，Across four MoE models and five benchmarks on two mobile platforms, \textsc{BigMoMo} achieves mean decoding speedups of $4.83\times$ over on-demand autoregressive offloading and $1.82\times$ over the best speculative MoE baseline, supporting MoE models up to 30B parameter.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Flattening Every Memory Peak in Long-Context Mixture-of-Experts Training](https://arxiv.org/abs/2609.14306)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Flattening Every Memory Peak in Long-Context Mixture-of-Experts Training》在 arXiv cs.DC 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，In matched component tests, they cut the MoE dispatch peak by up to $59.3\%$ without losing throughput, the vocabulary projection peak by $86.6\%$, and the offloaded optimizer step by $2.05\times$ faster.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [OrchSLM: Probing the Dynamics of Small Language Model Orchestration](https://arxiv.org/abs/2609.13470)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《OrchSLM: Probing the Dynamics of Small Language Model Orchestration》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，arXiv:2609.13470v1 Announce Type: new Abstract: Although large language models (LLMs) have demonstrated remarkable capabilities, their reliance on cloud-scale infrastructure poses fundamental challenges for deployment in agentic pipelines, including latency, privacy, connectivity, and substantial computational cost.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [STHMoE: Hypergraph-Enhanced Heterogeneous Dependency Coordination for LLM-Based Urban Traffic Data Forecasting](https://arxiv.org/abs/2609.15172)
  - 主题: Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference、LLM routing，核心内容是《STHMoE: Hypergraph-Enhanced Heterogeneous Dependency Coordination for LLM-Based Urban Traffic Data Forecasting》在 arXiv cs.AI 这一方向上的推进。强调异构硬件协同推理。从实验上看，Experiments on 10 real-world traffic benchmarks show that STHMoE achieves competitive performance against temporal, spatio-temporal graph, and LLM-based baselines.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [DeepSeek-V4-Flash on AMD gfx90a: Correctness Recovery and Inference Performance Engineering](https://arxiv.org/abs/2609.15627)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《DeepSeek-V4-Flash on AMD gfx90a: Correctness Recovery and Inference Performance Engineering》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，On four MI250 GCDs, TP4/EP1 native autoregressive decode reaches approximately 74.5 tok/s, while a 4,604-token prompt reaches 2.061-2.062 s TTFT, or approximately 2,234 input tok/s.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：2.062 s。
- [SMetric: Rethink LLM Scheduling for Serving Agents with Balanced Session-centric Scheduling](https://arxiv.org/abs/2607.08565)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《SMetric: Rethink LLM Scheduling for Serving Agents with Balanced Session-centric Scheduling》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Evaluated on real-world traces, SMetric improves the peak TPS by 9-15% under prefill-decode colocation with a provisioned global tier and the peak prefill TPS by 9% under disaggregation over state-of-the-art schedulers, also with lower latency.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：15%、9%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

