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

- 日期: 2026-09-29
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 3
- 日报: `papers/2026-09-29.md`
- 周报: `digests/weekly-2026-09-29.md`

## 今日最值得看

- [SPIMOE: Exploiting Hybrid Sparsity for Reasoning MoE Inference on Heterogeneous PIM Architectures](https://arxiv.org/abs/2609.34612v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《SPIMOE: Exploiting Hybrid Sparsity for Reasoning MoE Inference on Heterogeneous PIM Architectures》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Evaluations show that SPIMOE achieves up to $8.35\times$ end-to-end speedup over an NVIDIA A100 GPU and $3.33\times$ speedup in MoE FFN execution over PIMoE, while preserving reasoning accuracy comparable to full-attention baselines.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [EfficientAgent: What Makes KV Cache Offloading Work for Concurrent Agents?](https://arxiv.org/abs/2609.33762v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《EfficientAgent: What Makes KV Cache Offloading Work for Concurrent Agents?》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On SWE-bench Verified coding agents, a host tier sized to the estimated working set cuts recomputed prompt tokens by 93% and end-to-end time by 39%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：93%、39%、35%。
- [OLED-MoE: Accelerating MoE-Based dLLM Inference via Inter-Iteration Locality-Aware Expert Offloading](https://arxiv.org/abs/2609.33385v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《OLED-MoE: Accelerating MoE-Based dLLM Inference via Inter-Iteration Locality-Aware Expert Offloading》在 arXiv API 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Across diverse dLLM workloads, OLED-MoE reduces time per output token (TPOT) by 1.23x-7.93x and improves expert cache utilization by 1.44x-4.23x over state-of-the-art offloading systems.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.23x、7.93x、1.44x。
- [Beyond the Model: Demystifying Harness Effects in Software Engineering Agents](https://arxiv.org/abs/2609.32459v1)
  - 主题: Coding agent routing, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Coding agent routing、Cost-efficient LLM inference，核心内容是《Beyond the Model: Demystifying Harness Effects in Software Engineering Agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Complex harnesses provide diminishing marginal gains on SWE-style issue repair as model capability improves, but can benefit stronger models on more complex and open-ended repository-level tasks.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Higher-order pruning of experts in mixture-of-experts language models](https://arxiv.org/abs/2609.18916)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《Higher-order pruning of experts in mixture-of-experts language models》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，At 50% pruning, HOPE outperforms all baselines and achieves an average rank of 1.58 out of 5 methods (versus 2.42 for the next-best method, REAP), with gains of up to +6.1% on agentic coding.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：50%、6.1%。
- [RR-Evict: Fine-Grained Prefix Cache Eviction beyond LRU for Agentic LLM Serving](https://arxiv.org/abs/2609.32278v1)
  - 主题: Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Coding agent routing、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《RR-Evict: Fine-Grained Prefix Cache Eviction beyond LRU for Agentic LLM Serving》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Compared with LRU, RR-EVICT reduces P99 TTFT by up to 75.4% and P99 uncached prompt tokens by up to 65.7%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：75.4%、65.7%。
- [The KV Cache Is the New Memory Wall](https://arxiv.org/abs/2609.30854)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《The KV Cache Is the New Memory Wall》在 arXiv cs.LG 这一方向上的推进。强调异构硬件协同推理。从实验上看，For Llama-3-70B in BF16, the 140 GB weight footprint exceeds the 80 GB HBM of a single accelerator, and one 128k-token sequence adds 42 GB of KV cache.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：140 GB、80 GB、42 GB。
- [VarioPath: Workload-Aware All-to-All Communication for PCIe GPU Clusters](https://arxiv.org/abs/2609.34340v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《VarioPath: Workload-Aware All-to-All Communication for PCIe GPU Clusters》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，End-to-end experiments show that VarioPath reduces Qwen3 inference latency by up to 27.2% and Wan2.1 generation latency by 6.1%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：27.2%、6.1%、5.88x。
- [MaskCoFT: Masked Co-Adaptive Fine-Tuning for Memory-Efficient MoE Inference](https://arxiv.org/abs/2609.34077v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《MaskCoFT: Masked Co-Adaptive Fine-Tuning for Memory-Efficient MoE Inference》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，In real offloading system serving, it lowers the time per output token by up to 16.4% and 5.5%, respectively.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：16.4%、5.5%、23.7%。
- [Planner-as-Router: Joint Plan-Time Model Routing for Cost-Efficient Multi-Agent Workflows](https://arxiv.org/abs/2609.32917v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、LLM routing，核心内容是《Planner-as-Router: Joint Plan-Time Model Routing for Cost-Efficient Multi-Agent Workflows》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，It matches a sink-frontier heuristic (frontier model on terminal nodes only) in accuracy at comparable cost and a faithful FrugalGPT cascade at lower cost, and cuts cost 44% against all-frontier routing while giving up 2.9 points of accuracy.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：44%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

