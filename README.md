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

- 日期: 2026-10-01
- 今日新论文: 15
- 今日新权威来源更新: 1
- 本周精选论文: 25
- 本周精选权威来源更新: 1
- 日报: `papers/2026-10-01.md`
- 周报: `digests/weekly-2026-10-01.md`

## 今日最值得看

- [ORACLE: Agentic AI Orchestrator Routing Via Adaptive Verifier Calibration Feedback](https://arxiv.org/abs/2607.22465)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《ORACLE: Agentic AI Orchestrator Routing Via Adaptive Verifier Calibration Feedback》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Extensive evaluation on SWE-bench, tau2-bench, and Terminal-Bench 2.0 shows that ORACLE improves the accuracy-cost frontier by up to 7 percentage points over state-of-the-art routing baselines, while ORACLE with DISC improves program throughput by up to 1.8x.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：2.0 s、1.8x。
- [Higher-order pruning of experts in mixture-of-experts language models](https://arxiv.org/abs/2609.18916)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《Higher-order pruning of experts in mixture-of-experts language models》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，At 50% pruning, HOPE outperforms all baselines and achieves an average rank of 1.58 out of 5 methods (versus 2.42 for the next-best method, REAP), with gains of up to +6.1% on agentic coding.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：50%、6.1%。
- [Characterizing High Bandwidth Flash for LLM Serving](https://arxiv.org/abs/2609.39131)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Characterizing High Bandwidth Flash for LLM Serving》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across the evaluated workloads, the fastest HBF-augmented systems reduce completion time by 36.1-87.0% relative to HBM-only systems.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：87.0%、55.8%。
- [Cascadia: A Control-Plane-Free Alternative to Hyperconverged AI Infrastructure](https://arxiv.org/abs/2609.38697)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Cascadia: A Control-Plane-Free Alternative to Hyperconverged AI Infrastructure》在 arXiv cs.DC 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，A three-node Phi-3.5-mini NPU testbed delivered 3.10x the response throughput of its one-node configuration under ten concurrent requests; a separate four-node deployment recorded 4.06x the throughput of direct single-node serving.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：3.10x、4.06x。
- [Efficient Expert-Parallel Communication on PCIe-Connected Consumer GPUs](https://arxiv.org/abs/2609.40093v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Efficient Expert-Parallel Communication on PCIe-Connected Consumer GPUs》在 arXiv API 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Experiments on two PCIe systems equipped with RTX 4090 and RTX 5090 GPUs show that ThunderEP achieves average speedups of 2.00$\times$ and 1.53$\times$ over NCCL for dispatch and combine, respectively, and up to 1.66$\times$ end-to-end speedup over state-of-the-art MoE inference frameworks.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [SparseEngine: Sparse-First Inference Engine](https://arxiv.org/abs/2609.39068v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《SparseEngine: Sparse-First Inference Engine》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，While maintaining method quality, SparseEngine delivers over 10x higher throughput with KV eviction, over 2.5x faster decoding at matched concurrency than vLLM, and over 2x end-to-end speedup on agent benchmarks.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：10x、2.5x、2x。
- [DAMP: Decay-Aware Mixed-Precision Recurrent-State Quantization](https://arxiv.org/abs/2608.27513)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《DAMP: Decay-Aware Mixed-Precision Recurrent-State Quantization》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，In SGLang, DAMP reduces recurrent-state storage by 69.1%, accelerates the recurrent-state update kernel by up to 2.59x , and lowers full-model time per output token by up to 19.0%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：69.1%、2.59x、19.0%。
- [PANDA: A Decentralized Architecture with Flexible Orchestration for Scalable, Fault-Tolerant Multi-Agent Systems](https://arxiv.org/abs/2609.38482v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《PANDA: A Decentralized Architecture with Flexible Orchestration for Scalable, Fault-Tolerant Multi-Agent Systems》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，We evaluate PANDA on the HotPotQA benchmark, demonstrating that it scales to thousands of agents, assembles teams in milliseconds, matches state-of-the-art accuracy at up to 8x the efficiency, and sustains 100% task completion under faults where existing systems fail.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：8x、100%。
- [Prefill-Free Cross-Family KV Cache Transfer for Heterogeneous Multi-Agent LLMs](https://arxiv.org/abs/2609.32259)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Prefill-Free Cross-Family KV Cache Transfer for Heterogeneous Multi-Agent LLMs》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across six transfer directions, HeteroFold achieves the best cache-transfer performance on all four long-context benchmarks and most short-context settings.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [MoEless: Efficient MoE LLM Serving with Serverless Experts](https://arxiv.org/abs/2603.06350)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《MoEless: Efficient MoE LLM Serving with Serverless Experts》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Experiments with open-source MoE models and real-world workloads show that MoEless reduces inference latency by 43% and inference cost by 84% compared to state-of-the-art solutions.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：43%、84%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

