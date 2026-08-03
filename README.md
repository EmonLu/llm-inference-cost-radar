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

- 日期: 2026-08-03
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 5
- 日报: `papers/2026-08-03.md`
- 周报: `digests/weekly-2026-08-03.md`

## 今日最值得看

- [TokTier: Exact Stateful Tokenization for Agentic LLM Serving](https://arxiv.org/abs/2607.29678)
  - 主题: Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Coding agent routing、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《TokTier: Exact Stateful Tokenization for Agentic LLM Serving》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，With vLLM, median time to first token drops 16-34% and P99 drops 23% under recorded bursts.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：34%、23%、94.1%。
- [Topology-Aware Data Movement for Disaggregated GPU Inference](https://arxiv.org/abs/2607.28633)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Topology-Aware Data Movement for Disaggregated GPU Inference》在 arXiv cs.LG 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，We present analytical bandwidth models, component implementations, and projected analysis across three architectures showing 3 to 18x transfer latency reduction over uniform RDMA.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：18x、6x、86x。
- [Mixture-of-Translators: Translating KV Caches Across Heterogeneous Large Language Models](https://arxiv.org/abs/2607.28979)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Mixture-of-Translators: Translating KV Caches Across Heterogeneous Large Language Models》在 arXiv cs.CL 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across homogeneous and heterogeneous translations among Qwen2.5, GPT-2, and OPT models, MoT preserves downstream QA performance, including Qwen2.5-7B-scale translation with 51.0% average closed-set QA accuracy and 0.43 average extractive QA F1.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：51.0%、96.3%。
- [MoPET: Parameter-Efficient Mixture-of-Experts for Unified Medical Image Classification](https://arxiv.org/abs/2607.29462)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《MoPET: Parameter-Efficient Mixture-of-Experts for Unified Medical Image Classification》在 arXiv cs.LG 这一方向上的推进。强调异构硬件协同推理。从实验上看，Through selected evaluations on the MedMNIST benchmark, we first establish that PEFT outperforms full network updates, improving average accuracy from 86.50% to 88.97%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：86.50%、88.97%、81.58%。
- [Rethinking AI Cloud Infrastructure for Agentic Serving Systems with the Aries Experimentation Framework](https://arxiv.org/abs/2607.29069)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Rethinking AI Cloud Infrastructure for Agentic Serving Systems with the Aries Experimentation Framework》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，We use Aries to conduct reproducible experiments on open agent harnesses and benchmarks.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [MOSAIC: Masked Outsourcing of Secure AI Computations](https://arxiv.org/abs/2607.29221)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《MOSAIC: Masked Outsourcing of Secure AI Computations》在 arXiv cs.AI 这一方向上的推进。强调异构硬件协同推理。从实验上看，Its security reduces to the decisional LWE and LPN assumptions.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Studying quantization trade-offs for efficient inference deployment in machine translation](https://arxiv.org/abs/2607.29397v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Studying quantization trade-offs for efficient inference deployment in machine translation》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Quantization is a common approach to reduce the memory footprint and improve inference efficiency, yet its impact on latency and throughput is rarely evaluated under controlled, orchestration-level workloads.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [DeltaServe: Host-Agnostic Co-Serving of Inference and Fine-Tuning for LLMs](https://arxiv.org/abs/2607.28848)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《DeltaServe: Host-Agnostic Co-Serving of Inference and Fine-Tuning for LLMs》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，It also achieves 39% higher fine-tuning throughput than a baseline running vLLM+torchtune, using no additional hardware and maintaining full SLO compliance.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：39%、2.9x、100%。
- [MerchantBench: Benchmarking LLM Agents for Long-Term Coherence in E-Commerce Operations](https://arxiv.org/abs/2607.28956)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《MerchantBench: Benchmarking LLM Agents for Long-Term Coherence in E-Commerce Operations》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，arXiv:2607.28956v1 Announce Type: new Abstract: Large language model agents are increasingly evaluated as autonomous tool users, yet most benchmarks focus on bounded tasks with immediate success criteria.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [SLIM: Saturation-Aware Lightweight Performance Modeling for LLM Serving](https://arxiv.org/abs/2607.29575)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《SLIM: Saturation-Aware Lightweight Performance Modeling for LLM Serving》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Building on this analysis, we present the Batching Configuration Advisor (BCA), which selects the highest-throughput batching configuration satisfying a target latency constraint and identifies up to 55 GB of GPU memory allocation that can be avoided for the evaluated OPT models with minimal throughput loss.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：55 GB。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

