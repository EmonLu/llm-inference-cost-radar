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

- 日期: 2026-05-19
- 今日新论文: 15
- 今日新权威来源更新: 2
- 本周精选论文: 25
- 本周精选权威来源更新: 4
- 日报: `papers/2026-05-19.md`
- 周报: `digests/weekly-2026-05-19.md`

## 今日最值得看

- [HexAGenT: Efficient Agentic LLM Serving via Workflow- and Heterogeneity-Aware Scheduling](https://arxiv.org/abs/2605.16637)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《HexAGenT: Efficient Agentic LLM Serving via Workflow- and Heterogeneity-Aware Scheduling》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across representative agentic workloads and heterogeneous A100/H100/H200 clusters, HexAGenT reduces the SLO scale required for timely workflow completion by an average of 20.1% at 95% attainment and 33.0% at 99% attainment, with maximum reductions of 45.0% and 80.5%, respectively.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：20.1%、95%、33.0%。
- [KVDrive: A Holistic Multi-Tier KV Cache Management System for Long-Context LLM Inference](https://arxiv.org/abs/2605.18071)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《KVDrive: A Holistic Multi-Tier KV Cache Management System for Long-Context LLM Inference》在 arXiv cs.CL 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，The system achieves up to 1.74x higher throughput compared to state-of-the-art works while preserving accuracy.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.74x。
- [CoX-MoE: Coalesced Expert Execution for High-Throughput MoE Inference with AMX-Enabled CPU-GPU Co-Execution](https://arxiv.org/abs/2605.17889)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《CoX-MoE: Coalesced Expert Execution for High-Throughput MoE Inference with AMX-Enabled CPU-GPU Co-Execution》在 arXiv cs.LG 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Compared to state-of-the-art frameworks, CoX-MoE delivers significant gains, achieving up to 7.1x and 2.4x higher throughput than FlexGen and MoE-Lightning, respectively.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：7.1x、2.4x。
- [TriAxialKV: Toward Extreme Low-Precision KV-Cache Quantization for Agentic Inference Tasks](https://arxiv.org/abs/2605.17170)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《TriAxialKV: Toward Extreme Low-Precision KV-Cache Quantization for Agentic Inference Tasks》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，When using Qwen3-VL-32B-Thinking as a computer-use agent operating the OSWorld, TriAxialKV matches the accuracy of SGLang with BF16 KV cache while supporting 4.5$\times$ KV cache size and achieving 30% higher end-to-end throughput, when running on real GPU systems.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：30%。
- [VeriCache: Turning Lossy KV Cache into Lossless LLM Inference](https://arxiv.org/abs/2605.17613)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《VeriCache: Turning Lossy KV Cache into Lossless LLM Inference》在 arXiv cs.LG 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Experimental results show that VeriCache achieves up to 4X higher throughput than full-KV inference while producing identical outputs.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：4X。
- [Stream2LLM: Overlap Context Streaming and Prefill for Reduced Time-to-First-Token (TTFT)](https://arxiv.org/abs/2604.16395)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Stream2LLM: Overlap Context Streaming and Prefill for Reduced Time-to-First-Token (TTFT)》在 arXiv cs.AI 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Our evaluation demonstrates that streaming architecture delivers up to 11x TTFT improvements, with cost-aware scheduling providing critical benefits under memory pressure, all while maintaining throughput parity with non-streaming baselines.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：11x。
- [OxyGen: Unified KV Cache Management for VLA Inference under Multi-Task Parallelism](https://arxiv.org/abs/2603.14371)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《OxyGen: Unified KV Cache Management for VLA Inference under Multi-Task Parallelism》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，OxyGen achieves up to 3.7$\times$ speedup over isolated execution, delivering over 200 tokens/s language throughput and 70 Hz action frequency simultaneously without degrading action quality, and we further validate the gains on a real humanoid robot with on-board Jetson AGX Thor.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：200 tokens/s。
- [HyDRA: Hybrid Dynamic Routing Architecture for Heterogeneous LLM Pools](https://arxiv.org/abs/2605.17106)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《HyDRA: Hybrid Dynamic Routing Architecture for Heterogeneous LLM Pools》在 arXiv cs.CL 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，74.2% resolution) at 12.9% cost savings; iso-quality matches Sonnet at 54.1% cost savings, a 6x improvement over our prior in-house binary router at 9.1%; aggressive pushes savings to 72.5% for a 3.2-point quality trade.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：74.2%、12.9%、54.1%。
- [OSCAR: Offline Spectral Covariance-Aware Rotation for 2-bit KV Cache Quantization](https://arxiv.org/abs/2605.17757)
  - 主题: Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference，核心内容是《OSCAR: Offline Spectral Covariance-Aware Rotation for 2-bit KV Cache Quantization》在 arXiv cs.DC 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，System-wise, OSCAR reduces KV-cache memory by approximately 8x, improves throughput by up to 7x at large batch sizes under the same memory budget, and accelerates batch-size-1 decoding by up to 3x over BF16 due to reduced memory bandwidth overhead.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：8x、7x、3x。
- [Learning Transferable Topology Priors for Multi-Agent LLM Collaboration Across Domains](https://arxiv.org/abs/2605.17359)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Learning Transferable Topology Priors for Multi-Agent LLM Collaboration Across Domains》在 arXiv cs.CL 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experiments on multi-domain reasoning benchmarks show that TopoPrior consistently improves several heterogeneous topology-evolution backbones while reducing online inference-time token usage, with only modest additional trainable parameters.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

