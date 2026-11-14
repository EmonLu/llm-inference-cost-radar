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

- 日期: 2026-11-14
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 7
- 日报: `papers/2026-11-14.md`
- 周报: `digests/weekly-2026-11-14.md`

## 今日最值得看

- [Lara Mini Base: Language Diversity as a Resource, Not a Trade-off](https://arxiv.org/abs/2611.16956)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Lara Mini Base: Language Diversity as a Resource, Not a Trade-off》在 arXiv cs.AI 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，arXiv:2611.16956v1 Announce Type: cross Abstract: General-purpose language models are trained mostly on English: over open models we review, at most, non-English pretraining data makes up only a 12% share.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：12%。
- [DrugCoding: A Scientific Programming Agent for Drug Discovery](https://arxiv.org/abs/2611.13651)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、LLM routing，核心内容是《DrugCoding: A Scientific Programming Agent for Drug Discovery》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experimental results demonstrate that DrugCoding achieves an average session-level Pass@1 of 97.35% on the full benchmark, outperforming the strongest baseline, Codex, by 9.24%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：97.35%、9.24%、97.92%。
- [VideoEditor-MoE: Scaling Complex Video Editing with Mixture of Experts](https://arxiv.org/abs/2611.03043)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《VideoEditor-MoE: Scaling Complex Video Editing with Mixture of Experts》在 arXiv cs.AI 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，Meeting these demands through dense model scaling substantially increases computational cost.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [HeMeR: Heterogeneous Memory Reconciliation for Embodied Agents via Structured KV Reuse](https://arxiv.org/abs/2611.16487)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《HeMeR: Heterogeneous Memory Reconciliation for Embodied Agents via Structured KV Reuse》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，In the real-world setting, HeMeR achieves 83.20% task success and reduces per-step inference time from 2.94 to 1.87 seconds compared with MemRL, while preserving compatible KV states as task progress updates the memory context.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：83.20%、1.87 s。
- [Beyond the Trial-and-Error Loop: Hybrid Projection and Automated Tuning for Distributed Training](https://arxiv.org/abs/2610.19423)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Beyond the Trial-and-Error Loop: Hybrid Projection and Automated Tuning for Distributed Training》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，In a Mixtral 8x22B case study, the Primus Tuning Agent discovers a configuration delivering +27% throughput over the published 4-node BF16 reference at the same scale, in under 30 minutes of single-node exploration.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：8x、27%。
- [OSCAR: Offline Spectral Covariance-Aware Rotation for 2-bit KV Cache Quantization](https://arxiv.org/abs/2605.17757)
  - 主题: Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference，核心内容是《OSCAR: Offline Spectral Covariance-Aware Rotation for 2-bit KV Cache Quantization》在 arXiv cs.AI 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，On RULER-NIAH up to 128K tokens, OSCAR substantially outperforms QuaRot-style INT2 across context lengths.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Synthesizing Human Trajectory Anomalies: An LLM-Driven Framework with Map-Constrained Routing and Sensor Noise Simulation](https://arxiv.org/abs/2606.10314)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference、LLM routing，核心内容是《Synthesizing Human Trajectory Anomalies: An LLM-Driven Framework with Map-Constrained Routing and Sensor Noise Simulation》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Furthermore, collecting large-scale mobility data is hindered by strict privacy regulations and acquisition costs.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Open Challenges and Opportunities in Human-Agent Systems](https://arxiv.org/abs/2611.14846)
  - 主题: Agent systems and multi-agent efficiency
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency，核心内容是《Open Challenges and Opportunities in Human-Agent Systems》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，arXiv:2611.14846v1 Announce Type: new Abstract: Agentic AI systems increasingly undertake extended tasks and act on people's behalf, making human-agent interaction central to their effectiveness.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Toward Agentic Retrieval-Augmented Generation for Enterprise Retail Workflows over Heterogeneous Data Sources](https://arxiv.org/abs/2610.25096)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Toward Agentic Retrieval-Augmented Generation for Enterprise Retail Workflows over Heterogeneous Data Sources》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，RetailRAG consistently outperforms existing agentic RAG baselines across all evaluation axes, serving as a strong reference system for assessing LLM agents on retail workflows.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [TraceKV: Policy-Preserving Low-Rank KV Cache Compression for Reasoning Vision-Language Models](https://arxiv.org/abs/2611.15569)
  - 主题: Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference，核心内容是《TraceKV: Policy-Preserving Low-Rank KV Cache Compression for Reasoning Vision-Language Models》在 arXiv cs.AI 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，Experiments across multiple VLMs and visual reasoning benchmarks demonstrate superior accuracy--memory trade-offs, achieving near-lossless reasoning accuracy with 5.64$\times$ KV cache compression when combined with quantization.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

