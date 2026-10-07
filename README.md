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

- 日期: 2026-10-07
- 今日新论文: 15
- 今日新权威来源更新: 1
- 本周精选论文: 25
- 本周精选权威来源更新: 3
- 日报: `papers/2026-10-07.md`
- 周报: `digests/weekly-2026-10-07.md`

## 今日最值得看

- [FluidPD: In-Place Elasticity for SLO-Aware Prefill-Decode Disaggregated LLM Serving](https://arxiv.org/abs/2610.06917)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《FluidPD: In-Place Elasticity for SLO-Aware Prefill-Decode Disaggregated LLM Serving》在 arXiv cs.AI 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，As a result, a configuration that is well provisioned at one time may quickly become mismatched, causing latency SLO violations even when idle capacity exists elsewhere.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Cascadia: Resident 975B MoE Inference on Eleven AI PCs](https://arxiv.org/abs/2610.07219)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Cascadia: Resident 975B MoE Inference on Eleven AI PCs》在 arXiv cs.DC 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，At fifteen streams, median first-token latency is 6.05 s.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：6.05 s、4.5 ms。
- [A Shape-Adaptive Architecture with Disaggregated Quantization for Efficient LLM Serving](https://arxiv.org/abs/2610.07443v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《A Shape-Adaptive Architecture with Disaggregated Quantization for Efficient LLM Serving》在 arXiv API 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，Evaluation with real-world serving traces shows that DynaCore substantially reduces service-level latency over quantization and reconfigurable accelerators, improving TTFT by 3.50x and 2.97x and TPOT by 36.55x and 8.02x, respectively.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：3.50x、2.97x、36.55x。
- [KVCMAS: Efficient KV cache Correction for Shared Context in Multi-Agent Systems](https://arxiv.org/abs/2609.34060)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《KVCMAS: Efficient KV cache Correction for Shared Context in Multi-Agent Systems》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Under controlled serving traces, it provides a 2.0x TTFT speedup over inference without KV cache sharing and reduces peak GPU memory by up to 3.7x relative to a prior KV cache correction method.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：2.0x、3.7x。
- [TRANSIT: Transparent Scale-in for Multi-Node LLM Training](https://arxiv.org/abs/2610.07593)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《TRANSIT: Transparent Scale-in for Multi-Node LLM Training》在 arXiv cs.DC 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Our evaluation shows that TRANSIT can: (a) outperform state-of-the-art framework-managed offloading techniques, achieving up to 68%, 59%, and 42% higher per-GPU throughput than TorchTitan, ZeRO-Offload, and ZeRO-Infinity, respectively, (b) enables training with 50% fewer GPUs while maintaining over 90% of baseline per-GPU throughput, (c) lower per-node network traffic by up to 33%, and (d) improve per-GPU throughput by up to 35% in communication-bound settings.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：68%、59%、42%。
- [AgSpec: Pushing the Limits of Retrieval-Based Speculative Decoding in Coding Agent Pipelines](https://arxiv.org/abs/2610.01108)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《AgSpec: Pushing the Limits of Retrieval-Based Speculative Decoding in Coding Agent Pipelines》在 arXiv cs.CL 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On two repository-level multi-agent coding benchmarks, AgSpec outperforms five retrieval-based drafters and EAGLE-3 in most evaluated settings, raising generation throughput over autoregressive decoding up to 4.37$\times$ at batch size 1 and 4.76$\times$ at batch size 16.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [DySCo: Dynamic Sharding for Collaborative Edge-Cloud LLM Inference with Depth-Synchronized Batching](https://arxiv.org/abs/2610.08268v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《DySCo: Dynamic Sharding for Collaborative Edge-Cloud LLM Inference with Depth-Synchronized Batching》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，At an average concurrency of eight, DSB improves throughput by 275% over FIFO, 48% over exact-match batching, and 79% over round-robin interleaving while reducing mean per-session latency.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：275%、48%、79%。
- [Large Language Model Orchestration under Heterogeneous Preferences via Explicit Persona Inference](https://arxiv.org/abs/2610.07587v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Large Language Model Orchestration under Heterogeneous Preferences via Explicit Persona Inference》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Empirical results on three substrates, ranging from payoffs the preferences fully determine, through payoffs that depend on more than them, to scales where explicit joint inference is infeasible, demonstrate that HARP\textsuperscript{+} is the strongest non-oracle method across the class our theory identifies.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [PReCache: Efficient KV Cache Sharing for Multi-LoRA Agents via Low-Rank Precomputation and Neutral Reconstruction](https://arxiv.org/abs/2609.34054)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《PReCache: Efficient KV Cache Sharing for Multi-LoRA Agents via Low-Rank Precomputation and Neutral Reconstruction》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across multiple models and agent benchmarks, PreLRShared achieves up to a 3.1x TTFT speedup and a 2.3x improvement in per-request throughput over inference without KV cache sharing.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：3.1x、2.3x。
- [WorkflowOps: Learning Agent Collaboration Priors for Multi-Agent Workflow Orchestration](https://arxiv.org/abs/2610.07860v1)
  - 主题: Agent systems and multi-agent efficiency, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、LLM routing，核心内容是《WorkflowOps: Learning Agent Collaboration Priors for Multi-Agent Workflow Orchestration》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experiments on mixed code, math, and question-answering suites show that WorkflowOps improves end-to-end pass rates over recent workflow-construction baselines, with the largest gains on structured, decomposable tasks where past agent handoff patterns transfer.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

