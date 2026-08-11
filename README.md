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

- 日期: 2026-08-11
- 今日新论文: 15
- 今日新权威来源更新: 2
- 本周精选论文: 25
- 本周精选权威来源更新: 6
- 日报: `papers/2026-08-11.md`
- 周报: `digests/weekly-2026-08-11.md`

## 今日最值得看

- [OmniInfer: System-Wide Acceleration Techniques for Optimizing LLM Serving Throughput and Latency](https://arxiv.org/abs/2511.22481)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《OmniInfer: System-Wide Acceleration Techniques for Optimizing LLM Serving Throughput and Latency》在 arXiv cs.DC 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，Built atop vLLM, OmniInfer delivers system-wide performance gains through adaptive resource disaggregation, efficient sparsity exploitation, and global coordination across prefill and decode phases.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Topology-Aware Data Movement for Disaggregated GPU Inference](https://arxiv.org/abs/2607.28633)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Topology-Aware Data Movement for Disaggregated GPU Inference》在 arXiv cs.LG 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，We present analytical bandwidth models, component implementations, and projected analysis across three architectures showing 3 to 18x transfer latency reduction over uniform RDMA.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：18x、6x、86x。
- [OasisKV: Scaling In-Decode KV Cache Beyond HBM with Lookahead Sparse Prefetching](https://arxiv.org/abs/2608.08097v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《OasisKV: Scaling In-Decode KV Cache Beyond HBM with Lookahead Sparse Prefetching》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，This lets OasisKV turn sparsity into throughput gain: $1.69\times$ over dense vLLM on the reasoning workload at 0.1 points of accuracy loss, and up to $2.1\times$ on multi-GPU long-context serving.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Predictive Multi-Tier Memory Management for KV Cache in Large-Scale GPU Inference](https://arxiv.org/abs/2604.26968)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Predictive Multi-Tier Memory Management for KV Cache in Large-Scale GPU Inference》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Analytical projections combining validated component behavior with published hardware specifications indicate TTFT reductions of 1.4x to 2.1x, throughput improvements of 1.7x to 2.9x, and 47% cost reduction relative to published baselines; these cluster-scale projections are analytical and carry no error bars.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.4x、2.1x、1.7x。
- [TokTier: Exact Stateful CPU+GPU Tokenization for Agentic LLM Serving](https://arxiv.org/abs/2607.29678)
  - 主题: Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Coding agent routing、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《TokTier: Exact Stateful CPU+GPU Tokenization for Agentic LLM Serving》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，With vLLM, median TTFT drops 16-34% and P99 TTFT 23% under recorded bursts.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：34%、23%、0.87 ms。
- [Cascade: Exploiting SLO-Aware latency budget for fair and high goodput LLM inference serving](https://arxiv.org/abs/2608.06557)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Cascade: Exploiting SLO-Aware latency budget for fair and high goodput LLM inference serving》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On production traces across three large language models, Cascade improves goodput by up to2.4x and reduces SLO violations by 40% relative to the default vLLM first-come, first-served scheduler.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：2.4x、40%。
- [CHIME: A Case for Efficient Long-Context Attention-FC Disaggregated Inference with DIMM-PIM](https://arxiv.org/abs/2504.17584)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《CHIME: A Case for Efficient Long-Context Attention-FC Disaggregated Inference with DIMM-PIM》在 arXiv cs.LG 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Evaluations show CHIME achieves up to 5.15$\times$ speedup over state-of-the-art HBM-PIM solutions.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Motif 3: Technical Report](https://arxiv.org/abs/2608.09119v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Motif 3: Technical Report》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across a broad evaluation suite, Motif 3 demonstrates competitive performance against leading open weight models, including strong results on long-horizon agentic tasks, mathematical reasoning, scientific knowledge, and hallucination-sensitive evaluation.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Can Coding Agents Solve Repository-Level Issues with Rendered Code? An Exploratory Study of Visual Representations](https://arxiv.org/abs/2608.09268v1)
  - 主题: Coding agent routing, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Coding agent routing、Cost-efficient LLM inference，核心内容是《Can Coding Agents Solve Repository-Level Issues with Rendered Code? An Exploratory Study of Visual Representations》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Rendered code consistently reduces prompt-token cost, but the savings do not increase linearly with the nominal visual compression ratio.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [LLMVisor: A Real-Time Latency Attribution Model for Multi-Tenant LLM Serving](https://arxiv.org/abs/2608.08382v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《LLMVisor: A Real-Time Latency Attribution Model for Multi-Tenant LLM Serving》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Compared to a token-count baseline, LLMVisor attains near-perfect R-squared and reduces relative error by up to 2.5x and 3.3x at p90 and p99, respectively, for prefill, and by up to 3.5x and 4.4x for decode, despite batching variability and sequence divergence.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：2.5x、3.3x、3.5x。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

