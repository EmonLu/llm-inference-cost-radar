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

- 日期: 2026-07-14
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 1
- 日报: `papers/2026-07-14.md`
- 周报: `digests/weekly-2026-07-14.md`

## 今日最值得看

- [Automated Tensor Scheduling for Hybrid CPU-GPU LLM Inference on Consumer Devices](https://arxiv.org/abs/2607.10183v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Automated Tensor Scheduling for Hybrid CPU-GPU LLM Inference on Consumer Devices》在 arXiv API 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Compared with existing systems, ATSInfer improves prefill throughput by up to 1.94$\times$ and decode throughput by up to 3.29$\times$, while also increasing GPU utilization and making more effective use of PCIe bandwidth.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [[AAFLOW+] Stateful Operator Abstraction with Zero-Copy Distributed KV Cache Orchestration for Multi-Agent Workflows](https://arxiv.org/abs/2607.10987v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《[AAFLOW+] Stateful Operator Abstraction with Zero-Copy Distributed KV Cache Orchestration for Multi-Agent Workflows》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，AAFLOW+ reduces TTFT by up to 50.2x, achieves up to 7.63x reduced multi-agent compute cost at 16-agent scale, reduces KV memory by 1.72-6.10x, and increases throughput by more than 7.74x, based on an analytical cost model parameterized by empirical hardware microbenchmarks.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：50.2x、7.63x、6.10x。
- [MemDecay: Region-Aware KV Cache Eviction for Efficient LLM Agent Inference](https://arxiv.org/abs/2607.10582v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《MemDecay: Region-Aware KV Cache Eviction for Efficient LLM Agent Inference》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Accumulated-attention retention performs better on unpinned content, however, and ablations identify attention-score normalization as the main limitation of the current formulation.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [UMoE:Unlocking Every Expert in Domain-Specific Training](https://arxiv.org/abs/2607.11444v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《UMoE:Unlocking Every Expert in Domain-Specific Training》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Analysis reveals that the direct-SFT model allocates substantial routed-expert compute to a low-saliency subset that can be removed post hoc with little average degradation; UMoE turns this redundant capacity into useful domain capacity and achieves lower training loss, with gains spanning all difficulty levels in downstream evaluation.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [HCRMap: Pressure-Aware Hot-Expert Residency Mapping for 3.5D MoE Chiplet Inference](https://arxiv.org/abs/2607.11586v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《HCRMap: Pressure-Aware Hot-Expert Residency Mapping for 3.5D MoE Chiplet Inference》在 arXiv API 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，Experimental results show that HCRMap reduces end-to-end latency by 43.6% and 43.0% over Hydra in the prefill and decode stages, respectively; by 34.5% and 33.1% over MoEntwine; and by 46.7% and 46.0% over PIMoE.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：43.6%、43.0%、34.5%。
- [WebDesignIter: Co-Evolving Design Knowledge for Repository-Level Front-End Code Generation](https://arxiv.org/abs/2607.10621v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing，核心内容是《WebDesignIter: Co-Evolving Design Knowledge for Repository-Level Front-End Code Generation》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，More importantly, WebDesignIter outperforms every general-purpose coding agent Claude Code, OpenHands, SWE-Agent, Codex CLI on every model configuration, posting the highest Pass@1 and Pass@2 while consuming 2530 fewer input tokens.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [FlashAccel: Leveraging High-Bandwidth Flash for High-Throughput LLM Inference](https://arxiv.org/abs/2607.10186v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《FlashAccel: Leveraging High-Bandwidth Flash for High-Throughput LLM Inference》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Experimental results demonstrate that integrating six HBF stacks into the GPU enables FlashAccel to deliver an average improvement of 2.54$\times$ and 1.93$\times$ in throughput per GPU and energy efficiency over the HBM-only GPU under 100ms latency constraint, respectively.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：100ms。
- [Heterogeneous Agent Cohorts for Safe Open-Ended Exploration with Runtime Constraint Memory](https://arxiv.org/abs/2607.11226v1)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《Heterogeneous Agent Cohorts for Safe Open-Ended Exploration with Runtime Constraint Memory》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，In a spatial-semantic sandbox (N=20 runs, p<0.01), our cohort reaches remote targets where debate fails, the Validator prevents all executed breaches, and Scars reduce token consumption by 15.1% by avoiding redundant validator checks.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：15.1%、55.9%。
- [Agentic Routing: The Harness-Native Data Flywheel](https://arxiv.org/abs/2607.11399v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、LLM routing，核心内容是《Agentic Routing: The Harness-Native Data Flywheel》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The report studies singleton and multi-model routing on agentic benchmarks including DRACO and PinchBench, and argues that agentic routing is not merely cost control, but a data engine for agent-native training.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Prompt Generation Technical Report](https://arxiv.org/abs/2607.11326v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Prompt Generation Technical Report》在 arXiv API 这一方向上的推进。强调异构硬件协同推理。从实验上看，PG has been deployed on Taobao Search with statistically significant online A/B uplifts of +0.47% in transaction count and +0.51% in GMV, and has been applied across multiple Taobao search and recommendation teams as the iteration framework for generative retrieval.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：0.47%、0.51%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

