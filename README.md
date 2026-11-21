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

- 日期: 2026-11-21
- 今日新论文: 15
- 今日新权威来源更新: 1
- 本周精选论文: 25
- 本周精选权威来源更新: 2
- 日报: `papers/2026-11-21.md`
- 周报: `digests/weekly-2026-11-21.md`

## 今日最值得看

- [Learning to Coordinate: LLM-Guided Workflow Evolution for Token-Efficient Red Teaming](https://arxiv.org/abs/2611.24221v1)
  - 主题: Agent systems and multi-agent efficiency, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、LLM routing，核心内容是《Learning to Coordinate: LLM-Guided Workflow Evolution for Token-Efficient Red Teaming》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across the six executor-target configurations, L2C improves ASR over EvoSynth by 1.4 to 4.5 percentage points while reducing mean online tokens by 35.6% to 37.3%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：35.6%、37.3%。
- [RoCoKV: Accelerating LLM Inference Serving through Uncertainty and Redundancy Aware KV Cache Compression](https://arxiv.org/abs/2611.25433v1)
  - 主题: Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference，核心内容是《RoCoKV: Accelerating LLM Inference Serving through Uncertainty and Redundancy Aware KV Cache Compression》在 arXiv API 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，For DeepSeek-R1-Distill-Llama-8B in vLLM, RoCoKV achieves a 1.27X speedup and 38% higher throughput on AIME25, the most challenging evaluated reasoning benchmark, and a 1.43X speedup and 45% higher throughput on the long synthetic benchmark, compared with Full-KV.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.27X、38%、1.43X。
- [Berth: SLO-Preserving GPU Sharing Without New Preemption](https://arxiv.org/abs/2611.25091v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Berth: SLO-Preserving GPU Sharing Without New Preemption》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Across 31 scenario points with MLPerf SLOs and 13 baselines, Berth meets SLOs within a few percentage points of running alone, above every baseline, with 2.7-3.5x the best-effort throughput of the strongest ones; beside LLM serving, it meets per-token targets for nearly every request while training keeps running.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：31 s、3.5x。
- [The American Medical Directory Panel: Comparing AI-Assisted and LLM Transcription with Manual Data Entry at Scale](https://arxiv.org/abs/2611.25218v1)
  - 主题: Coding agent routing, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Coding agent routing、Heterogeneous MoE inference，核心内容是《The American Medical Directory Panel: Comparing AI-Assisted and LLM Transcription with Manual Data Entry at Scale》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，As the manual transcription's own error rate is unknown, these rates measure agreement rather than accuracy.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [The FrontierOR Challenge: Agentic Algorithm Design for Operations Research](https://arxiv.org/abs/2611.26171v1)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference、LLM routing，核心内容是《The FrontierOR Challenge: Agentic Algorithm Design for Operations Research》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Large language model (LLM) agents now write, test and improve code, but whether they can design algorithms that scale to realistic instances is open: in the FrontierOR benchmark's one-shot evaluation, the strongest model matches Gurobi, with an objective within 1% of Gurobi's and no slower, on only 39% of the large instances.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1%、39%。
- [Verified Netlist-to-RTL Recovery with LLM Agents](https://arxiv.org/abs/2611.25324v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《Verified Netlist-to-RTL Recovery with LLM Agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Per-run recovery across models rises from 5% to 74%, at a median cost below one dollar with a low-cost model.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：5%、74%。
- [Cost-Aware Agentic Feature Optimization System for Fleet-Scale Ranking Models](https://arxiv.org/abs/2611.26531v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《Cost-Aware Agentic Feature Optimization System for Fleet-Scale Ranking Models》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across production models, the system improves normalized entropy by 0.31% on average within each model's budget, and the trimming step cuts pipeline cost by 2.3% with no regression beyond measurement noise.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：0.31%、2.3%、0.20%。
- [Forget Freely, Grep Later: Lossless, Index-Free Memory for Long-Horizon LLM Agents](https://arxiv.org/abs/2611.25123v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《Forget Freely, Grep Later: Lossless, Index-Free Memory for Long-Horizon LLM Agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，GrepMem achieves 95-97% accuracy on ContextBench, versus at most 21% for lossy baselines, and outperforms SUPO's summarization by 8.8 percentage points on BCP-Multi.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：97%、21%。
- [BlockJack: Cross-Tenant Redirection Fault Attacks on Paged KV Cache Address Translation in LLM Serving](https://arxiv.org/abs/2611.25945v1)
  - 主题: Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference，核心内容是《BlockJack: Cross-Tenant Redirection Fault Attacks on Paged KV Cache Address Translation in LLM Serving》在 arXiv API 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，On a 248-scene medical benchmark, the integrity attack causes up to 41.1% of responses to recommend less urgent care, while still appearing consistent with the victim's question.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：41.1%。
- [Held While Waiting: What LLM Agent Sessions Reserve on Serverless and Agent Runtimes](https://arxiv.org/abs/2611.26480v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Held While Waiting: What LLM Agent Sessions Reserve on Serverless and Agent Runtimes》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，But it reserves a separate environment, a virtual machine with its own memory, for every conversation, and keeps it reserved until the conversation is closed.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：33 s。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

