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

- 日期: 2026-08-12
- 今日新论文: 15
- 今日新权威来源更新: 1
- 本周精选论文: 25
- 本周精选权威来源更新: 6
- 日报: `papers/2026-08-12.md`
- 周报: `digests/weekly-2026-08-12.md`

## 今日最值得看

- [RotaryQuant: Fitting 120B MoE Models on Consumer Hardware via Fused Compressed-Space Attention](https://arxiv.org/abs/2608.08081)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《RotaryQuant: Fitting 120B MoE Models on Consumer Hardware via Fused Compressed-Space Attention》在 arXiv cs.LG 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，The combined system fits Gemma 4-26B-A4B and Qwen3-30B-A3B within a 16\,GB budget and Nemotron-H 120B within 32\,GB, running interactively at 9--19 tok/s with near-zero perplexity degradation ($\Delta$PPL $\leq +0.0012$) and 100\% retrieval accuracy at 32K context.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [FlashRT: Agent Harness for Guiding Agents to Deploy Real-Time Multimodal Applications](https://arxiv.org/abs/2607.18171)
  - 主题: Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Coding agent routing、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《FlashRT: Agent Harness for Guiding Agents to Deploy Real-Time Multimodal Applications》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On AMD MI355X GPUs, FlashRT matches the peak latency reduction while increasing peak throughput improvement to 3.6x, demonstrating that agent-driven optimization can be more scalable on platforms with less mature expert optimization.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：355X、3.6x、70x。
- [Optimizing CUDA like a Human: Micro-Profiling Tools as Expert Surrogates for LLM-Based GPU Kernel Optimization](https://arxiv.org/abs/2606.26453)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Heterogeneous MoE inference，核心内容是《Optimizing CUDA like a Human: Micro-Profiling Tools as Expert Surrogates for LLM-Based GPU Kernel Optimization》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Ablation studies demonstrate that each design component independently and significantly improves optimization quality: micro-profiling tools (p < 0.0001 vs raw metrics), MCTS search (26% higher geometric mean vs greedy, p = 0.004), and proactive tool orchestration (23% improvement, p = 0.035).
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：26%、23%、2.42x。
- [MoE-Prism: Disentangling Monolithic Experts for Elastic MoE Services via Model-System Co-Designs](https://arxiv.org/abs/2510.19366)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《MoE-Prism: Disentangling Monolithic Experts for Elastic MoE Services via Model-System Co-Designs》在 arXiv cs.CL 这一方向上的推进。强调异构硬件协同推理。从实验上看，\textsc{MoE-Prism} expands the number of available routing operating points by $4\times$, improves offline inference throughput by up to 33.9\%, and reduces online serving TTFT under heterogeneous workloads.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Dynamic Coalition Formation and Communication Pricing in Skill-Based Agentic AI Systems](https://arxiv.org/abs/2608.07532)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Dynamic Coalition Formation and Communication Pricing in Skill-Based Agentic AI Systems》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，In synthetic experiments, greedy routing achieves $99.5%$ of brute-force-optimal utility while activating $1.96$ of $8$ agents on average, compared with $38.8%$ for full broadcast.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：99.5%、38.8%、66%。
- [Scheduling Mixed RL Rollouts Beyond Prefix Locality](https://arxiv.org/abs/2608.11152v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Scheduling Mixed RL Rollouts Beyond Prefix Locality》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，In rollout-only ablations on Step3.7 and Qwen3.6-35B-A3B, MISA-T improves rollout throughput over a sweep-tuned cache-aware vLLM Router by 53.3% and 43.6%, respectively, while maintaining high prefix-cache hit rates.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：53.3%、43.6%、35.6%。
- [El Agente Gr\'afico: A Semantic Execution Runtime for Scientific Agents](https://arxiv.org/abs/2602.17902)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Heterogeneous MoE inference，核心内容是《El Agente Gr\'afico: A Semantic Execution Runtime for Scientific Agents》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Using the same top-level LLM and task-specific rubrics on six university-level quantum chemistry exercises, El Agente Gr\'afico improved performance while reducing model cost by approximately 80% and wall-clock time by more than fourfold relative to our previous multi-agent architecture.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：80%。
- [Alignment Collapse Under KV Cache Quantization: Diagnosis and Mitigation](https://arxiv.org/abs/2606.09864)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Alignment Collapse Under KV Cache Quantization: Diagnosis and Mitigation》在 arXiv cs.LG 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Across eleven instruction-tuned models (3.8B-72B) and five benchmarks (1,894 prompts), we find that low-bit quantization can silently destroy safety alignment: Mistral-7B loses 15.2% of its refusals at only 1.03x perplexity, and no universal safe bit-width exists, with sharp model-specific phase transitions invisible to standard metrics.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：15.2%、1.03x、97%。
- [MammoMix: Leveraging Mixture of Experts for Robust Mammogram Breast Detection](https://arxiv.org/abs/2608.10437v1)
  - 主题: Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference，核心内容是《MammoMix: Leveraging Mixture of Experts for Robust Mammogram Breast Detection》在 arXiv API 这一方向上的推进。强调异构硬件协同推理。从实验上看，Results show that MammoMix outperforms baseline detectors in both average precision and reliability, particularly on datasets with greater variability.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [FlashBoot: Sub-Second Weight Loading for Large Models at Rack Scale](https://arxiv.org/abs/2608.08482)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《FlashBoot: Sub-Second Weight Loading for Large Models at Rack Scale》在 arXiv cs.DC 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，In experiments on NVL72 with DeepSeek-V4-Pro and DeepSeek-V4-Flash, FlashClone maps remote weight memory in ~10 ms (versus 10-110 s for NCCL) and sustains >=700 GB/s per clone.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：10 ms、110 s、700 GB。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

