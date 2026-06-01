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

- 日期: 2026-06-01
- 今日新论文: 15
- 今日新权威来源更新: 1
- 本周精选论文: 25
- 本周精选权威来源更新: 9
- 日报: `papers/2026-06-01.md`
- 周报: `digests/weekly-2026-06-01.md`

## 今日最值得看

- [Mellum2 Technical Report](https://arxiv.org/abs/2605.31268v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《Mellum2 Technical Report》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across code generation, math and reasoning, tool use, knowledge, and safety benchmarks, Mellum 2 is competitive with open-weight baselines in the 4B-14B range while running at the per-token compute of a 2.5B dense model.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [PithTrain: A Compact and Agent-Native MoE Training System](https://arxiv.org/abs/2605.31463v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《PithTrain: A Compact and Agent-Native MoE Training System》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Our evaluation shows PithTrain matches the throughput of production frameworks, and on ATE-Bench, PithTrain enables higher agent-task efficiency, with up to 62% fewer Agent Turns and 64% less Active GPU Time.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：62%、64%。
- [Deterministic Inference across Tensor Parallel Sizes That Eliminates Training-Inference Mismatch](https://arxiv.org/abs/2511.17826)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Deterministic Inference across Tensor Parallel Sizes That Eliminates Training-Inference Mismatch》在 arXiv cs.CL 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，We identify and analyze the root causes of TP-induced inconsistency and propose Tree-Based Invariant Kernels (TBIK), a set of TP-invariant matrix multiplication and reduction primitives that guarantee bit-wise identical results regardless of TP size.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [ParisKV: Fast and Drift-Robust KV-Cache Retrieval for Long-Context LLMs](https://arxiv.org/abs/2602.07721)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《ParisKV: Fast and Drift-Robust KV-Cache Retrieval for Long-Context LLMs》在 arXiv cs.CL 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，ParisKV matches or outperforms full attention quality on long-input and long-generation benchmarks.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [HetCCL: Enabling Collective Communication For Mixed-Vendor Heterogeneous Clusters](https://arxiv.org/abs/2605.31000)
  - 主题: Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference，核心内容是《HetCCL: Enabling Collective Communication For Mixed-Vendor Heterogeneous Clusters》在 arXiv cs.LG 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Our evaluation shows that HetCCL achieves 17-19x higher bandwidth than Gloo in heterogeneous communications, and speeds up end-to-end training by up to 16.9% in the per-step-time.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：19x、16.9%。
- [Eigenvectors of Experts are Training-free Non-collapsing Routers](https://arxiv.org/abs/2605.30992v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Eigenvectors of Experts are Training-free Non-collapsing Routers》在 arXiv API 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，Extensive experiments across diverse language and vision tasks, under both clean and corrupt data settings, demonstrate the strong generalization and robustness of SSMoE.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Memory-Bound but Not Bandwidth-Limited: The Physical AI Inference Gap in Batch-1 LLM Decode](https://arxiv.org/abs/2605.30571)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Memory-Bound but Not Bandwidth-Limited: The Physical AI Inference Gap in Batch-1 LLM Decode》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On H100 at ctx=2048, CUDA Graphs improves decode latency by 1.259x across N=10 fresh sessions, with a 95 percent bootstrap confidence interval of 1.253 to 1.267.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.259x、4x、59.36 ms。
- [A Virtual Processor brings back the Free Lunch](https://arxiv.org/abs/2605.30507)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《A Virtual Processor brings back the Free Lunch》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The current VP primarily targets low-latency strong scaling on local heterogeneous hardware, covering workloads from small, latency-sensitive array operations to large data-parallel computations.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [CoMem: Context Management with A Decoupled Long-Context Model](https://arxiv.org/abs/2605.30842)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《CoMem: Context Management with A Decoupled Long-Context Model》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Our extensive experimental results on SWE-Bench-Verified show that CoMem provides 1.4x latency improvements upon vanilla long-context solutions while preserving most of the performance.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.4x。
- [Graph-Conditioned Mixture of Graph Neural Network Experts for Traffic Forecasting](https://arxiv.org/abs/2605.30486)
  - 主题: Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference、LLM routing，核心内容是《Graph-Conditioned Mixture of Graph Neural Network Experts for Traffic Forecasting》在 arXiv cs.LG 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，Across four standard benchmarks (PEMS04, PEMS07, METR-LA, and PEMS-BAY), GC-MoE improves MAE over a zero-parameter ensemble baseline, with competitive RMSE and MAPE, while training only ~17K parameters on top of 1.5M frozen expert weights.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

