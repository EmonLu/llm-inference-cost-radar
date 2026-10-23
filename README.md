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

- 日期: 2026-10-23
- 今日新论文: 15
- 今日新权威来源更新: 2
- 本周精选论文: 25
- 本周精选权威来源更新: 8
- 日报: `papers/2026-10-23.md`
- 周报: `digests/weekly-2026-10-23.md`

## 今日最值得看

- [Specter: Fast MoE Inference via Quantization-Enabled Multi-Step Speculative Offloading](https://arxiv.org/abs/2511.14102)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Specter: Fast MoE Inference via Quantization-Enabled Multi-Step Speculative Offloading》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Under single-request inference, Specter achieves an average 1.50x (up to 1.88x) speedup in time per output token (TPOT) over the state-of-the-art system.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.50x、1.88x。
- [Gandalf: Flash Shall Not Die! Increasing Flash Storage Lifetime for KV Cache Offloading in LLM Serving](https://arxiv.org/abs/2610.30791)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Gandalf: Flash Shall Not Die! Increasing Flash Storage Lifetime for KV Cache Offloading in LLM Serving》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Our evaluation shows that Gandalf extends the SSD lifetime by 7.3X on average, while having negligible impact on cache hit rate across multiple workload traces and wide range of hardware capacity.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：7.3X。
- [SWE-VERIFIER: Selective Verification for Cost-Efficient Coding Agents](https://arxiv.org/abs/2610.30284)
  - 主题: Coding agent routing, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Coding agent routing、Cost-efficient LLM inference，核心内容是《SWE-VERIFIER: Selective Verification for Cost-Efficient Coding Agents》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across both models, SWE-Verifier verifies fewer than 4% of steps and achieves comparable or higher resolution than the trajectory and all-step baselines at substantially lower cost.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：4%、75.47%、77.20%。
- [IQuest-Q1: Advancing Foundation Capabilities for Agentic CLI Systems](https://arxiv.org/abs/2610.30949)
  - 主题: Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Coding agent routing、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《IQuest-Q1: Advancing Foundation Capabilities for Agentic CLI Systems》在 arXiv cs.CL 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，arXiv:2610.30949v1 Announce Type: new Abstract: We present IQuest-Q1, a sparse Mixture-of-Experts (MoE) agentic foundation model with 320B total parameters (15B activated).
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [MoEZip: Routing-Aware KV Cache Compression for Sparse Mixture-of-Experts LLMs](https://arxiv.org/abs/2610.30206)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《MoEZip: Routing-Aware KV Cache Compression for Sparse Mixture-of-Experts LLMs》在 arXiv cs.LG 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，Experiments show that MoEZip achieves robust performance under aggressive cache compression on various benchmarks.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [RIFT: KV Cache Compression for Draft Models with Complementary Compressibility Training](https://arxiv.org/abs/2610.31098)
  - 主题: Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference，核心内容是《RIFT: KV Cache Compression for Draft Models with Complementary Compressibility Training》在 arXiv cs.CL 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，Combined with compressibility training, RIFT enables Qwen3.5-4B, drafting for Qwen3.5-122B, to retain over 98% of its full-cache acceptance length on 32K-token inputs, 4K-token outputs, and an 8K-token KV cache budget.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：98%。
- [Evaluating the Applicability of LLM Inference Optimizations on Apple Silicon](https://arxiv.org/abs/2610.31479)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Evaluating the Applicability of LLM Inference Optimizations on Apple Silicon》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Under the common benchmark, all evaluated speculative decoding methods reduce throughput on Apple, despite reported 2-6 times gains on server GPUs.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [PAUSE: Search-Free Steering of Coding Agents Before Their First Source-Code Edit](https://arxiv.org/abs/2610.29870)
  - 主题: Coding agent routing
  - 中文解读: 这项工作主要关注Coding agent routing，核心内容是《PAUSE: Search-Free Steering of Coding Agents Before Their First Source-Code Edit》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，With Qwen3-coder as Executor and GPT-5.6 Sol as Planner, online steering improves resolution by 16.8% on Verified in OpenHands and by 14.7% on Multilingual in SWE-agent.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：5.6 S、16.8%、14.7%。
- [WeGR: Towards Unified Generative Retrieval via Behavior-aware Tokenization and Preference Alignment](https://arxiv.org/abs/2610.16979)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《WeGR: Towards Unified Generative Retrieval via Behavior-aware Tokenization and Preference Alignment》在 arXiv cs.AI 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Moreover, a six-week online A/B test on a large-scale e-commerce search platform achieves relative gains of 2.539% in orders, 1.508% in CTR, and 1.381% in CVR, while reducing CPU and GPU usage by 25.5% and 26.1%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：2.539%、1.508%、1.381%。
- [uGDS: A User-Space Development Kit for High-Performance GPU Direct Storage](https://arxiv.org/abs/2610.30868)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《uGDS: A User-Space Development Kit for High-Performance GPU Direct Storage》在 arXiv cs.DC 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Evaluated on an A100 with a Samsung 990 PRO, uGDS achieves up to 12.12x GDS's batch-read bandwidth and 30.69x its batch-write bandwidth (8- and 4-KiB requests, batch size 128), and reduces 4-KiB synchronous write latency by 84.1% with two threads.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：12.12x、30.69x、84.1%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

