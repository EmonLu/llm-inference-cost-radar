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

- 日期: 2026-07-03
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 1
- 日报: `papers/2026-07-03.md`
- 周报: `digests/weekly-2026-07-03.md`

## 今日最值得看

- [ELDR: Expert-Locality-Aware Decode Routing for PD-Disaggregated MoE Serving](https://arxiv.org/abs/2607.00466)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《ELDR: Expert-Locality-Aware Decode Routing for PD-Disaggregated MoE Serving》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Implemented in vLLM and evaluated on deployments of up to 40 GPUs, ELDR reduces median TPOT by 5.9-13.9% over the strongest of four load-balancing baselines across three MoE models and two workloads, with model outputs unchanged.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：13.9%。
- [Lynx: Progressive Speculative Quantization for accelerating KV Transfer in Long-Context Inference](https://arxiv.org/abs/2607.01831)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Lynx: Progressive Speculative Quantization for accelerating KV Transfer in Long-Context Inference》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Recent KV quantization techniques reduce data volume and alleviate this bottleneck, but existing schemes fail to achieve both low network-exposed latency and high inference accuracy.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Towards Load-Aware Prefill Deflection for Disaggregated LLM Serving](https://arxiv.org/abs/2607.02043)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Towards Load-Aware Prefill Deflection for Disaggregated LLM Serving》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Implemented on vLLM and evaluated on production-style traces with DeepSeek-V2-Lite, our approach reduces P95 TTFT by upto 81% and raises SLO attainment by upto 79% over state-of-the-art disaggregated schedulers, at sub-millisecond per-request routing cost.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：81%、79%、23%。
- [HYPIC: Accelerating Hybrid-Attention LLM Serving with Position-Independent Caching](https://arxiv.org/abs/2607.01299)
  - 主题: Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference，核心内容是《HYPIC: Accelerating Hybrid-Attention LLM Serving with Position-Independent Caching》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Evaluated across four hybrid-attention models and five workloads, Hypic reduces time-to-first-token (TTFT) by 2.45x on average and improves peak throughput by up to 2.0x over existing systems, while staying within 3.3 points of full-recompute accuracy.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：2.45x、2.0x。
- [OmniPilot: An Uncertainty-Aware LLM Inference Advisor for Heterogeneous GPU Clusters](https://arxiv.org/abs/2607.01579)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《OmniPilot: An Uncertainty-Aware LLM Inference Advisor for Heterogeneous GPU Clusters》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，In evaluations across 460 benchmark runs on A100, H100, and H200 hardware across four precisions, OmniPilot predicts aggregate throughput with a 6.2\% mean absolute percentage error (MAPE) and a log-space $R^2=0.92$.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Kara: Efficient Reasoning LLM Serving via Sliding-Window KV Cache Compression](https://arxiv.org/abs/2607.01237)
  - 主题: Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference，核心内容是《Kara: Efficient Reasoning LLM Serving via Sliding-Window KV Cache Compression》在 arXiv cs.CL 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，Furthermore, we adapt Kara to PagedAttention and develop KvLLM, an inference framework built upon vLLM, which reduces KV cache memory usage and effectively improves output throughput.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Mixture-of-Parallelisms: Towards Memory-Efficient Training Stack for Mixture-of-Experts Models](https://arxiv.org/abs/2607.01844)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Mixture-of-Parallelisms: Towards Memory-Efficient Training Stack for Mixture-of-Experts Models》在 arXiv cs.DC 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，In our experiments, MoP delivers 4.7x--8.2x higher per-GPU throughput than a strongly-tuned FSDP2 baseline (with the gap widening at larger scale) and sustains training at context lengths up to 1M tokens, where the baseline runs out of memory beyond 64--128K.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：4.7x、8.2x、8x。
- [Clinically Structured Rank-Gated LoRA for Cross-Benchmark Medical Question Answering](https://arxiv.org/abs/2606.31432)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Clinically Structured Rank-Gated LoRA for Cross-Benchmark Medical Question Answering》在 arXiv cs.CL 这一方向上的推进。强调异构硬件协同推理。从实验上看，It improves over MoELoRA by 0.89 percentage points while using 28.1% fewer trainable parameters; a paired, benchmark-stratified bootstrap over final predictions gives a 95% confidence interval of [0.42, 1.37] for this macro-average gain.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：28.1%、95%、69.31%。
- [Hardware-Enforced Semantic Coordination for Safety-Critical Real-Time Autonomous Systems](https://arxiv.org/abs/2607.02376v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Hardware-Enforced Semantic Coordination for Safety-Critical Real-Time Autonomous Systems》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Software-mediated coordination presents fundamental limitations in domains where bounded latency, deterministic coordination, and enforceable safety guarantees are essential.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [GF-DiT: Scheduling Parallelism for Diffusion Transformer Serving](https://arxiv.org/abs/2606.13501)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《GF-DiT: Scheduling Parallelism for Diffusion Transformer Serving》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Compared with fixed-pipeline execution with static parallelism, GF-DiT improves throughput by up to 6.01$\times$, reduces mean latency by up to 95%, lowers SLO violation rates by up to 90%, and reduces communication-group setup overhead from 778 ms to approximately 60 $\mu$s.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：95%、90%、778 ms。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

