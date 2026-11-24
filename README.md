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

- 日期: 2026-11-24
- 今日新论文: 15
- 今日新权威来源更新: 1
- 本周精选论文: 25
- 本周精选权威来源更新: 4
- 日报: `papers/2026-11-24.md`
- 周报: `digests/weekly-2026-11-24.md`

## 今日最值得看

- [ANOR: Scaling Sparse Attention with a GPU-PNM Computing Hierarchy](https://arxiv.org/abs/2611.30417v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《ANOR: Scaling Sparse Attention with a GPU-PNM Computing Hierarchy》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across two models and three long-context agentic workloads, ANOR improves decode throughput by 2.3x over HiSparse and 2.0x over a PNM baseline on average.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：2.3x、2.0x。
- [LiveLoRA: Exact KV Cache Migration Across LoRA Updates for LLM Agents](https://arxiv.org/abs/2611.31105v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《LiveLoRA: Exact KV Cache Migration Across LoRA Updates for LLM Agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Serving benchmarks show approximately 4.8% decoding overhead relative to native cached decoding.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：4.8%。
- [EdgeALM: An Efficient and Unified Edge Accelerator for Large Audio Language Models via Full-Stack Hardware-Software Co-Design and Agent-Driven Recursive Optimization](https://arxiv.org/abs/2611.30216v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《EdgeALM: An Efficient and Unified Edge Accelerator for Large Audio Language Models via Full-Stack Hardware-Software Co-Design and Agent-Driven Recursive Optimization》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，It achieves high-throughput audio-to-text inference at up to 169.5 tokens/s and sustains real-time streaming audio-to-audio inference, with 94% bandwidth utilization and 26 W power consumption on average.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：169.5 tokens/s、94%。
- [When Does Decomposition Help? Empirical Study on Workload-Architecture Affinity in LLM Inference Serving](https://arxiv.org/abs/2611.29104v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《When Does Decomposition Help? Empirical Study on Workload-Architecture Affinity in LLM Inference Serving》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Pipeline parallelism reduces 32K time to first token by 58-59% at non-stress rates, while hybrid pipeline-based disaggregation achieves the best 32K end-to-end latency at 0.4 requests/s.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：59%、40GB。
- [NoeVera: Can Knowledge Guide Experiments and Experiments Refine Knowledge?](https://arxiv.org/abs/2611.29255v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《NoeVera: Can Knowledge Guide Experiments and Experiments Refine Knowledge?》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，In configuration search over four serving scenarios, NoeVera comes within 5% of the optimum in a median of 6-7 simulator calls, versus 9 for Bayesian optimization and 15 for a knowledge-free agent with the same tools; on A100 GPUs, its representative configurations deliver ~1.30x vLLM-default throughput and meet every scenario's latency objective.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：5%、7 s、1.30x。
- [Who Is Prompt-Injecting Coding Agents? An Empirical Study of Hidden AI-Directed Text on GitHub](https://arxiv.org/abs/2611.28763v1)
  - 主题: Coding agent routing, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Coding agent routing、Heterogeneous MoE inference，核心内容是《Who Is Prompt-Injecting Coding Agents? An Empirical Study of Hidden AI-Directed Text on GitHub》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Replayed offline against five models we tested, the attacks succeed against one small, fast model in 19% of cases, and against none once HTML comments are stripped.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：19%。
- [CGSpec: Consistency-Guided Speculative Decoding with Overlap-Aware Verification Scheduling for Edge-Cloud Inference](https://arxiv.org/abs/2611.30455v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《CGSpec: Consistency-Guided Speculative Decoding with Overlap-Aware Verification Scheduling for Edge-Cloud Inference》在 arXiv API 这一方向上的推进。强调异构硬件协同推理。从实验上看，Compared with current SOTA methods, it improves system throughput by 12.2\% and 10.2\%, and mean client throughput by 14.0\% and 33.0\%, respectively.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Analytical Modeling and Optimal GPU Provisioning for Disaggregated LLM Inference](https://arxiv.org/abs/2611.28760v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Analytical Modeling and Optimal GPU Provisioning for Disaggregated LLM Inference》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，We evaluate our scheme over H100 (NVL8) and GB300 (NVL72) using vLLM inference serving and show throughput, predicted and measured latency, showing near-perfect theoretical-to-measured values over leading LLMs (Llama and Qwen)
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Gossamer: A Utility-Driven Architecture for Constant-Budget KV Cache Compression in Reasoning LLMs](https://arxiv.org/abs/2611.29497v1)
  - 主题: Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference，核心内容是《Gossamer: A Utility-Driven Architecture for Constant-Budget KV Cache Compression in Reasoning LLMs》在 arXiv API 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，Through cross-domain co-design, we fuse cosine-similarity estimation directly into the attention computation, exploiting idle compute cycles to perform similarity evaluation without latency or bandwidth cost.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [AI-Assisted Auto-formalization for Trustworthy Scientific Computing: Case Studies and Lessons Learned](https://arxiv.org/abs/2611.31033v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《AI-Assisted Auto-formalization for Trustworthy Scientific Computing: Case Studies and Lessons Learned》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Our results characterize both the practical value and the current limitations of AI-assisted formalization for trustworthy scientific computing.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

