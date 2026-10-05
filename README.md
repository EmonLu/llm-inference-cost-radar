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

- 日期: 2026-10-05
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 2
- 日报: `papers/2026-10-05.md`
- 周报: `digests/weekly-2026-10-05.md`

## 今日最值得看

- [ORACLE: Agentic AI Orchestrator Routing Via Adaptive Verifier Calibration Feedback](https://arxiv.org/abs/2607.22465)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《ORACLE: Agentic AI Orchestrator Routing Via Adaptive Verifier Calibration Feedback》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Extensive evaluation on SWE-bench, tau2-bench, and Terminal-Bench 2.0 shows that ORACLE improves the accuracy-cost frontier by up to 7 percentage points over state-of-the-art routing baselines, while ORACLE with DISC improves program throughput by up to 1.8x.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：2.0 s、1.8x。
- [EdgeAgent: Orchestrating On-Device LLM inference for End-User Multi-Agent Systems on CPU-GPU Unified Memory Architectures](https://arxiv.org/abs/2610.03394)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《EdgeAgent: Orchestrating On-Device LLM inference for End-User Multi-Agent Systems on CPU-GPU Unified Memory Architectures》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Extensive evaluations on an Apple M4 SoC demonstrate that the UMA-aware execution alone contributes a 1.29x speedup over batched speculative decoding.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：4 S、1.29x、1.77x。
- [ServeTwin: A Benchmark-Validated Simulator for Distributed LLM Architecture Exploration](https://arxiv.org/abs/2610.02732)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《ServeTwin: A Benchmark-Validated Simulator for Distributed LLM Architecture Exploration》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Against real deployments, it reproduces InferenceX's steady-state throughput-interactivity frontier with a 3.6% mean error and predicts LMBenchmark's multi-turn performance with a 9.9% error while tracking KV-cache evolution.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：3.6%、9.9%。
- [Dynamic Expert Pruning for Multi-Agent Systems](https://arxiv.org/abs/2610.02951v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Dynamic Expert Pruning for Multi-Agent Systems》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across diverse tasks and roles, model scales, and MoE architectures, DEP achieves better overall accuracy than static pruning and merging baselines, and generalizes to workflows unseen in training without retraining.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [AFORE: Attention-FFN Disaggregation with Overlapped Reconfiguration of Experts](https://arxiv.org/abs/2610.03203)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《AFORE: Attention-FFN Disaggregation with Overlapped Reconfiguration of Experts》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Evaluation on a 110B-parameter MoE model across four dynamic workloads shows that AFORE improves output throughput by 10.1-17.6% and reduces P95 inter-token latency by 7.1-9.5% compared with the strongest competing baseline.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：17.6%、9.5%、29.8%。
- [Hardware-Native Joint Sparse-Quantization for Trillion-Scale Mixture-of-Experts](https://arxiv.org/abs/2610.02241)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Hardware-Native Joint Sparse-Quantization for Trillion-Scale Mixture-of-Experts》在 arXiv cs.LG 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Across MoE models ranging from 30 billion to one trillion parameters, our framework improves state-of-the-art joint sparse-quantization accuracy by up to 4.35 percentage points while preserving 96.09% of the original model's performance.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：96.09%。
- [Coda: Exploiting Admission Flexibility for Coding-Agent Serving](https://arxiv.org/abs/2610.03088)
  - 主题: Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Coding agent routing、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Coda: Exploiting Admission Flexibility for Coding-Agent Serving》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across the single-worker and multi-worker experiments, Coda improves output-token and SLO-compliant throughput by 20.3% and 70.5% on average, with peak gains of 29.3% and 140.2%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：20.3%、70.5%、29.3%。
- [MaskCoFT: Masked Co-Adaptive Fine-Tuning for Memory-Efficient MoE Inference](https://arxiv.org/abs/2609.34077)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《MaskCoFT: Masked Co-Adaptive Fine-Tuning for Memory-Efficient MoE Inference》在 arXiv cs.LG 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，In real offloading system serving, it lowers the time per output token by up to 16.4% and 5.5%, respectively.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：16.4%、5.5%、23.7%。
- [VenusRL: A Fully Disaggregated Agentic RL System with Priority Scheduling and Scalable Interaction](https://arxiv.org/abs/2610.03286)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《VenusRL: A Fully Disaggregated Agentic RL System with Priority Scheduling and Scalable Interaction》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across representative agentic RL workloads, VenusRL achieves up to 4.24x end-to-end training speedup over state-of-the-art baselines and reduces environment cost by up to 89%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：4.24x、89%。
- [GenomeOcean Anywhere: Private WebGPU Inference for Genome MoEs](https://arxiv.org/abs/2609.35882)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《GenomeOcean Anywhere: Private WebGPU Inference for Genome MoEs》在 arXiv cs.LG 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，We first show that plaintext expert inputs are not private: a probe recovers the token from a single vector at every depth, and one worker can identify the source genome from 300 unordered tokens with 92% accuracy.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：92%、0.74%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

