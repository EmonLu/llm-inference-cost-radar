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

- 日期: 2026-08-20
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 3
- 日报: `papers/2026-08-20.md`
- 周报: `digests/weekly-2026-08-20.md`

## 今日最值得看

- [LEGO-RL: Harness-Native Reinforcement Learning for Coding Agents](https://arxiv.org/abs/2608.17393)
  - 主题: Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Coding agent routing、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《LEGO-RL: Harness-Native Reinforcement Learning for Coding Agents》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，LEGO-RL improves Qwen3.5-35B-A3B across OpenHands SDK (64.0% to 70.4%), Claude Code (62.4% to 68.2%), and OpenCode (57.2% to 66.6%) on SWE-bench Verified, while maintaining a rollout-training probability correlation above 0.99.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：64.0%、70.4%、62.4%。
- [EvoTS-Agent: A Self-Evolving LLM Agent for Financial Time Series Change Point Detection](https://arxiv.org/abs/2608.17933)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《EvoTS-Agent: A Self-Evolving LLM Agent for Financial Time Series Change Point Detection》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experiments across four benchmark datasets demonstrate that EvoTS-Agent consistently outperforms existing LLM-based agents while maintaining a 100\% execution success rate across all evaluated backbone LLMs.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Agent Lightning v1.0: Towards Harnessed Agentic RL](https://arxiv.org/abs/2608.17528)
  - 主题: Coding agent routing, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Coding agent routing、Heterogeneous MoE inference，核心内容是《Agent Lightning v1.0: Towards Harnessed Agentic RL》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Using only 6K training examples and modest compute, RL improves Qwen3.5-9B on SWE-bench Verified from 41.8% to 56.4%, a 14.6-point absolute gain.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：41.8%、56.4%。
- [Co-RL: Unsupervised Reasoning Emerges from Diverse Cohort in Multi-agent RL](https://arxiv.org/abs/2608.17253)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《Co-RL: Unsupervised Reasoning Emerges from Diverse Cohort in Multi-agent RL》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Concretely, Co-RL yields average gains of 3.0-8.6% across seven text-only benchmarks for LLMs and 2.3-7.2% across four multimodal benchmarks for VLMs.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：8.6%、7.2%。
- [Mixture-of-Expert Blocks Contain Strong Hallucination Detection Signals](https://arxiv.org/abs/2608.17687)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Mixture-of-Expert Blocks Contain Strong Hallucination Detection Signals》在 arXiv cs.LG 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，Our results show that InnerExpert outperforms existing methods across five datasets and two MoE architectures, achieving up to 0.91 answer-level and 0.76 token-level AUROC, while requiring only a single forward pass.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Belayer: Efficient Fault Tolerance for LLM Agentic RL Training](https://arxiv.org/abs/2608.14635)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Belayer: Efficient Fault Tolerance for LLM Agentic RL Training》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Empirical results show low measured overhead during failure-free training, a worker-recovery-time reduction of up to 42 times faster compared with a full engine cold start, and 1.5 to 3.5 times faster recovery from environment failures.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [TiMi: Empower Time Series Transformers with Multimodal Mixture of Experts](https://arxiv.org/abs/2602.21693)
  - 主题: Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference，核心内容是《TiMi: Empower Time Series Transformers with Multimodal Mixture of Experts》在 arXiv cs.LG 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，Experimentally, our proposed TiMi demonstrates consistent state-of-the-art performance on sixteen real-world multimodal forecasting benchmarks, outperforming advanced baselines while offering both strong adaptability and interpretability.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [DominoTree: Conditional Tree-Structured Drafting with Domino for Speculative Decoding](https://arxiv.org/abs/2607.08642)
  - 主题: Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference，核心内容是《DominoTree: Conditional Tree-Structured Drafting with Domino for Speculative Decoding》在 arXiv cs.CL 这一方向上的推进。关注在线 serving 系统优化，适合成本控制。从实验上看，Where the round is verify-dominated, throughput follows: up to 7.3x over AR on Qwen3-8B, beating the released Domino decoder at its CUDA-graph best at every temperature, and inside SGLang winning single-request throughput by +12% over Domino on Qwen3-8B.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：7.3x、12%、36%。
- [Beyond the Trace: Coupling an Interpretable Reasoning-State Readout to Native MoE Routing](https://arxiv.org/abs/2608.17638)
  - 主题: Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference、LLM routing，核心内容是《Beyond the Trace: Coupling an Interpretable Reasoning-State Readout to Native MoE Routing》在 arXiv cs.AI 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，The result is R64, a low-overhead proxy: its median per-axis correlation with J64 is 0.69 to 0.86 across three models and two families, and on gpt-oss-20b it preserves 95 to 100% of J64's predictive gain.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：100%。
- [Token Optimization and Context Window Management in Multi-Agent AI Workflows](https://arxiv.org/abs/2608.17188)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《Token Optimization and Context Window Management in Multi-Agent AI Workflows》在 arXiv cs.CL 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，In production they cut measured cold-load latency to 61-116 seconds (six timed runs) from an operational baseline of roughly 3.5-10.5 minutes, with an estimated 60-70% token reduction.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：116 s、70%、50 s。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

