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

- 日期: 2026-09-30
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 1
- 日报: `papers/2026-09-30.md`
- 周报: `digests/weekly-2026-09-30.md`

## 今日最值得看

- [Mira: Memory-Efficient MoE Inference Using Adaptive Caching and Predictive Expert Staging](https://arxiv.org/abs/2609.38090v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Mira: Memory-Efficient MoE Inference Using Adaptive Caching and Predictive Expert Staging》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Compared against state-of-the-art baselines, Mira achieves a 5.71x speedup in average throughput on a memory-constrained GPU.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：5.71x、11.71x。
- [Federation of Experts: Communication Efficient Distributed Inference for Large Language Models](https://arxiv.org/abs/2605.06206)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Federation of Experts: Communication Efficient Distributed Inference for Large Language Models》在 arXiv cs.LG 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，An implementation of FoE finds that on LongBench, FoE significantly improves inference throughput and latency in both single-node and multi-node settings, reducing end-to-end prefill latency by up to 5.88x, TTFT by 3.66x, and TPOT by 1.53x.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：5.88x、3.66x、1.53x。
- [LLM Serving Optimization with Variable Prefill and Decode Lengths](https://arxiv.org/abs/2508.06133)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《LLM Serving Optimization with Variable Prefill and Decode Lengths》在 arXiv cs.LG 这一方向上的推进。强调异构硬件协同推理。从实验上看，Experiments on public conversational and long-document summarization workloads show that F-metric-based scheduling substantially reduces latency relative to standard baselines and remains close to the LP relaxation lower bound on tractable instances.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Efficient Agentic LLM Serving over SSD-based Sparse KV Storage](https://arxiv.org/abs/2609.36938v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Efficient Agentic LLM Serving over SSD-based Sparse KV Storage》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across three models and three agentic traces, Janus outperforms existing works by up to 1.57-3.69 times (1.22-1.85 times on average) in terms of the time to first token latency, while maintaining decode efficiency.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [The Hitchhiker's Guide to Agentic AI: From Foundations to Systems](https://arxiv.org/abs/2606.24937)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《The Hitchhiker's Guide to Agentic AI: From Foundations to Systems》在 arXiv cs.CL 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The book concludes with agent development frameworks, agentic UI design, evaluation methodology (non-deterministic evaluation, reasoning collapse, LLM-as-Judge), production deployment, and the regulatory environment (EU AI Act, California SB 942) as an engineering requirement.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Decode-Branch Transformers: Decoupling the Primary Prefill Path from Additional Decode Computation](https://arxiv.org/abs/2608.12385)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Decode-Branch Transformers: Decoupling the Primary Prefill Path from Additional Decode Computation》在 arXiv cs.AI 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，Grouped decode reuses loaded weight tiles and the primary KV cache across both paths, so the added arithmetic does not proportionally increase dominant memory traffic or decode latency.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [GenomeOcean Anywhere: Private WebGPU Inference for Genome MoEs](https://arxiv.org/abs/2609.35882)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《GenomeOcean Anywhere: Private WebGPU Inference for Genome MoEs》在 arXiv cs.LG 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，We first show that plaintext expert inputs are not private: a probe recovers the token from a single vector at every depth, and one worker can identify the source genome from 300 unordered tokens with 92% accuracy.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：92%、0.74%。
- [CipherGenome: Homomorphic Inference for Genomic Mixture-of-Experts](https://arxiv.org/abs/2609.35883)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《CipherGenome: Homomorphic Inference for Genomic Mixture-of-Experts》在 arXiv cs.LG 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，A reusable public hint cuts end-to-end latency by 3.54 times, wire compression reduces traffic 6.8 times, per-layer padding reduces routing leakage from 54.9% to 8.9% accuracy, and HE-compatible int4 experts remain non-inferior to their plaintext counterparts.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：54.9%、8.9%、99.8%。
- [DScale: Scaling Block-Diffusion Speculative Decoding with Adaptive Verification](https://arxiv.org/abs/2609.37532v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《DScale: Scaling Block-Diffusion Speculative Decoding with Adaptive Verification》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Geometric-mean throughput gains across these configurations are respectively 43.9% and 48.8% over DFlash, 22.2% and 37.7% over DSpark, and 24.4% and 32.0% over Domino, with lower request latency.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：43.9%、48.8%、22.2%。
- [XBridge: Entity-Grounded Latent Bridge for Heterogeneous LLM Communication](https://arxiv.org/abs/2608.11676)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《XBridge: Entity-Grounded Latent Bridge for Heterogeneous LLM Communication》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across three model families (Llama, Qwen, and Mistral), seven benchmarks, and both communication directions, XBRIDGE outperforms text-based communication on all seven tasks for each model pair while achieving 11x lower latency, and in a same-architecture setting it also exceeds a KV-sharing baseline on six of seven tasks.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：11x、3.8%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

