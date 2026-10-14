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

- 日期: 2026-10-14
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 3
- 日报: `papers/2026-10-14.md`
- 周报: `digests/weekly-2026-10-14.md`

## 今日最值得看

- [FORGE: Procedural Weight Generation for Sparse MoE Inference](https://arxiv.org/abs/2610.16890v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《FORGE: Procedural Weight Generation for Sparse MoE Inference》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，With 30% of the MoE FFN layers replaced across five Sparse MoE models, we estimate 1.3-2.8x higher system throughput at matched GPU count and 1.10-1.15x lower per-user decode latency at short context.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：30%、2.8x、1.15x。
- [Think Before You Speak: Enabling Training-Free Latent Communication Between Language Models](https://arxiv.org/abs/2610.16165v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Think Before You Speak: Enabling Training-Free Latent Communication Between Language Models》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，We systematically analyze CacheFuse across four reasoning and knowledge benchmarks and demonstrate up to 8.6 percentage points higher accuracy compared to single-model baselines and up to 12.2x TTFT speedup compared to text-based communication in multi-model inference.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：12.2x。
- [An Optical KV Cache Network for Disaggregated LLM Serving](https://arxiv.org/abs/2610.18444v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《An Optical KV Cache Network for Disaggregated LLM Serving》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，In simulations of GPU clusters on real serving traces with measured prefill times on H100 GPUs, this optical KV cache network matches 400G packet fabrics with adaptive routing at 0.55 to 0.78 times the cost of a 2:1 fabric and tolerates the 50 ms reconfiguration delay of a 384-port mechanical OCS.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：50 ms。
- [Scaling Inference-Time Compute with Teams of Coding Agents](https://arxiv.org/abs/2610.17471v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《Scaling Inference-Time Compute with Teams of Coding Agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Second, cheap models pay off as planners but not as implementers: a strong lead with cheap planners recovers 47.5% of the reward gain of an all-strong team for only 13.9% of its additional cost, whereas cheap implementers lower reward.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：47.5%、13.9%、70%。
- [DuoDiscover: Scaling Autonomous Discovery Beyond the Evaluation Bottleneck](https://arxiv.org/abs/2610.17184v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《DuoDiscover: Scaling Autonomous Discovery Beyond the Evaluation Bottleneck》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，We demonstrate DuoDiscover on two repository-level benchmarks and four GPU and TPU kernel suites covering hundreds of kernels.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [MLAfication: Efficiently Enabling High-Fidelity MLA for Modern LLMs](https://arxiv.org/abs/2610.17202v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《MLAfication: Efficiently Enabling High-Fidelity MLA for Modern LLMs》在 arXiv API 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，On Qwen3-30B-A3B, MLAfication delivers up to $5.35\times$ the serving throughput of BF16 GQA and, combined with 4-bit KV quantization, reduces the KV-cache footprint by $94.73\%$.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [ATTUNE: Agentic Throughput Tuning for LLM Training](https://arxiv.org/abs/2610.17528v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《ATTUNE: Agentic Throughput Tuning for LLM Training》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On four held-out models at 64-128 GPUs, ATTUNE raises mean throughput over the strongest public recipe run on our stack by 6.7% on Llama-3.1-405B (best campaign 11.9%) and 33.9% on GLM-4.5 (54.7%), whose public recipe was written for H100.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：6.7%、11.9%、33.9%。
- [SpecFit: Not All Draft Tokens Cost the Same in Offloaded MoE Inference](https://arxiv.org/abs/2610.15417v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《SpecFit: Not All Draft Tokens Cost the Same in Offloaded MoE Inference》在 arXiv API 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，On CNN/DailyMail summarization and a GSM8K subset with Qwen3-30B-A3B, SpecFit decodes 21.6% and 7.0% faster than EAGLE-3 with the same expert cache and 1.97x and 1.72x as fast as vanilla EAGLE-3.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：21.6%、7.0%、1.97x。
- [MultiAlloc: Budget-Aware Precision Allocation for KV Cache Quantization](https://arxiv.org/abs/2610.18642v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《MultiAlloc: Budget-Aware Precision Allocation for KV Cache Quantization》在 arXiv API 这一方向上的推进。强调异构硬件协同推理。从实验上看，Extensive experiments on reasoning and long-context benchmarks demonstrate that MultiAlloc consistently improves over layer-wise, token-wise, and recent multi-granularity KV cache quantization methods under matched memory budgets across diverse models, including Mistral, Llama, DeepSeek-Qwen, and QwQ.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [FastEEP: Fast Intra-Instance Elastic Scaling for Expert-Parallel MoE Serving](https://arxiv.org/abs/2610.18451v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《FastEEP: Fast Intra-Instance Elastic Scaling for Expert-Parallel MoE Serving》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Our evaluation shows that FastEEP achieves 4.5x--11.7x faster scaling than the existing vLLM-based approach across different models, enabling efficient, fine-grained scaling of MoE serving.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：4.5x、11.7x。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

