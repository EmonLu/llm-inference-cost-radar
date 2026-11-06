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

- 日期: 2026-11-06
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 2
- 日报: `papers/2026-11-06.md`
- 周报: `digests/weekly-2026-11-06.md`

## 今日最值得看

- [AgentServe: Algorithm-System Co-Design for Efficient Agentic AI Serving on a Consumer-Grade GPU](https://arxiv.org/abs/2603.10342)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《AgentServe: Algorithm-System Co-Design for Efficient Agentic AI Serving on a Consumer-Grade GPU》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Evaluation results show that AgentServe significantly improves latency stability while sustaining competitive throughput, achieving up to 2.8x TTFT improvement and 2.7x TPOT improvement over state-of-the-art baselines across different settings.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：2.8x、2.7x。
- [FlashOffloading: Low-Latency KV Cache Offloading for Long-Context LLM Serving](https://arxiv.org/abs/2611.07542v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《FlashOffloading: Low-Latency KV Cache Offloading for Long-Context LLM Serving》在 arXiv API 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，In experiments deploying GLM-5.2 with multi-token prediction (MTP3) speculative decoding on an Ascend910C prefill--decode (PD)-disaggregated platform, FlashOffloading improves prefill throughput by up to 1.38\(\times\) and decode throughput by up to 1.91\(\times\) under a 30 ms TPOT constraint.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：30 ms。
- [FastAFD: When Does Attention-FFN Disaggregation Pay on Rack-Scale NVLink?](https://arxiv.org/abs/2611.07149)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《FastAFD: When Does Attention-FFN Disaggregation Pay on Rack-Scale NVLink?》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Experiments show that AFD has a throughput advantage of up to 1.17x over wide EP on Qwen3 and 1.16x on Qwen3.5, and matches it on MiniMax-M2.5.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.17x、1.16x、8%。
- [Twig: Parallel and Memory-Efficient Tree Speculative Decoding for Hybrid-Attention LLMs](https://arxiv.org/abs/2608.01651)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Twig: Parallel and Memory-Efficient Tree Speculative Decoding for Hybrid-Attention LLMs》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Under online agent workloads, Twig reduces TTFT and TPOT by up to $67.6\%$ and $49.9\%$, respectively, over the strongest tree-speculative baseline.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [SeKV: Resolution-Adaptive KV Cache with Hierarchical Semantic Memory for Long-Context LLM Inference](https://arxiv.org/abs/2606.31145)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《SeKV: Resolution-Adaptive KV Cache with Hierarchical Semantic Memory for Long-Context LLM Inference》在 arXiv cs.CL 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Across five backbones and four benchmarks at a 10% GPU-resident KV budget, SeKV outperforms every method that fixes resolution at prefill, improving over the strongest semantic baseline by 2.9 points (5.5% relative).
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：10%、5.5%、0.1%。
- [Alignment Collapse Under KV Cache Quantization: Diagnosis and Mitigation](https://arxiv.org/abs/2606.09864)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Alignment Collapse Under KV Cache Quantization: Diagnosis and Mitigation》在 arXiv cs.LG 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Across eleven instruction-tuned models (3.8B-72B) and five benchmarks (1,894 prompts), we find that low-bit quantization can silently destroy safety alignment: Mistral-7B loses 15.2% of its refusals at only 1.03x perplexity, and no universal safe bit-width exists, with sharp model-specific phase transitions invisible to standard metrics.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：15.2%、1.03x、97%。
- [The Physical Cost of Context: Quality-Constrained Resource Accounting for Coding Agents](https://arxiv.org/abs/2610.34763)
  - 主题: Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Coding agent routing、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《The Physical Cost of Context: Quality-Constrained Resource Accounting for Coding Agents》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，In a separate 900-cell study, Eager cuts model calls by 35.7% and the GPU-energy proxy by 33.2% against on-demand search (Grep); Compact saves nothing further.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：35.7%、33.2%、8.3%。
- [Server-Side Sparse Assignment for Federated Mixture-of-Experts](https://arxiv.org/abs/2611.07093)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Server-Side Sparse Assignment for Federated Mixture-of-Experts》在 arXiv cs.LG 这一方向上的推进。强调异构硬件协同推理。从实验上看，Experiments using a CNN-based MoE on CIFAR-100 show that $S^3$-MoE recovers task-dependent client--expert preferences and reduces conflicts caused by correlated expert selection across clients.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：100 s。
- [Octopus: One Brain, Many Branches for Latent-KV Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2611.06956)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Octopus: One Brain, Many Branches for Latent-KV Multi-Agent Reinforcement Learning》在 arXiv cs.CL 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Trained end-to-end with GRPO on Qwen3.5-4B over a sparse BM25 corpus, Octopus reaches $49.6\%$ accuracy on BrowseComp-Plus ($+17.5$ points over single-agent GRPO at 143K context and $+12.5$ points over text-summary multi-agent RL) and $51.2\%$ on OpenResearcher, outperforming dense-retrieval agents up to $250\times$ larger while increasing training throughput $3.3\times$ and cutting peak KV memory $2.8\times$.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [GAAC: Lossless KV Compression for Bandwidth-Efficient LLM Inference on Personal Devices](https://arxiv.org/abs/2610.38210)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《GAAC: Lossless KV Compression for Bandwidth-Efficient LLM Inference on Personal Devices》在 arXiv cs.AI 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，In serving, it reduces resident KV memory by approximately 26% and increases aggregate throughput by 13-29% under comparable KV-memory budgets.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：26%、29%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

