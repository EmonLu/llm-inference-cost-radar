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

- 日期: 2026-06-13
- 今日新论文: 15
- 今日新权威来源更新: 1
- 本周精选论文: 25
- 本周精选权威来源更新: 4
- 日报: `papers/2026-06-13.md`
- 周报: `digests/weekly-2026-06-13.md`

## 今日最值得看

- [The End of Code Review: Coding Agents Supersede Human Inspection](https://arxiv.org/abs/2606.13175v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《The End of Code Review: Coding Agents Supersede Human Inspection》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Our argument rests on two claims: every stated goal of code review can be served by agents at lower cost and higher throughput; the naive integration in which agents write code and humans remain the mandatory reviewers is a dead end because it neither provides meaningful assurance nor scales with AI-assisted throughput.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Functional Cache Grafting: Robust and Rapid Code-Policy Synthesis for Embodied Agents](https://arxiv.org/abs/2606.13097v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《Functional Cache Grafting: Robust and Rapid Code-Policy Synthesis for Embodied Agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，By eliminating redundant prefill computation, this approach reduces generation latency, while reusing validated control structures improves robustness over prompt-level caching methods RAGCache, achieving 18.31% higher task success rate and 2.3x faster policy synthesis.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：18.31%、2.3x。
- [Reward Modeling for Multi-Agent Orchestration](https://arxiv.org/abs/2606.13598v1)
  - 主题: Agent systems and multi-agent efficiency
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency，核心内容是《Reward Modeling for Multi-Agent Orchestration》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，OrchRM improves training efficiency by up to 10x in token usage while improving MAS test-time scaling performance by up to 8% in accuracy.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：10x、8%。
- [Breaking Entropy Bounds: Accelerating RL Training via MTP with Rejection Sampling](https://arxiv.org/abs/2606.12370v1)
  - 主题: Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference，核心内容是《Breaking Entropy Bounds: Accelerating RL Training via MTP with Rejection Sampling》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experimental results show our method achieves up to 1.8x end-to-end acceleration in async RL training of Qwen3.5, Qwen3.6, and Qwen3.7 models.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.8x、10%、95%。
- [VIA-SD: Verification via Intra-Model Routing for Speculative Decoding](https://arxiv.org/abs/2606.12243v1)
  - 主题: Cost-efficient LLM inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、LLM routing，核心内容是《VIA-SD: Verification via Intra-Model Routing for Speculative Decoding》在 arXiv API 这一方向上的推进。直接讨论模型选择或路由策略，与你的主线高度一致。从实验上看，Across four representative tasks and multiple model families, VIA-SD reduces rejection rates by 0.10-0.22 and delivers 10-20% speedups over strong SD baselines, while achieving 2.5-3x acceleration over non-drafting decoding.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：20%、3x。
- [Multi-Bitwidth Quantization for LLMs Using Additive Codebooks](https://arxiv.org/abs/2606.12876v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Multi-Bitwidth Quantization for LLMs Using Additive Codebooks》在 arXiv API 这一方向上的推进。强调异构硬件协同推理。从实验上看，This approach significantly reduces storage and memory overhead by allowing a single checkpoint to serve multiple bitwidths, while maintaining competitive perplexity and accuracy across major architectures, such as Qwen, LLaMA, Gemma, and Mistral.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Agents All the Way Down; A Methodology for Building Custom AI Agents from Substrate to Production](https://arxiv.org/abs/2606.11869v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing，核心内容是《Agents All the Way Down; A Methodology for Building Custom AI Agents from Substrate to Production》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Custom AI agents areagents that live inside their own application, talk to their own data and tools, enforce their own security boundaries, and carry their own brand and audit trail.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [DynamicPTQ: Mitigating Activation Quantization Collapse via Residual-Stream Dynamics](https://arxiv.org/abs/2606.12487v1)
  - 主题: Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference，核心内容是《DynamicPTQ: Mitigating Activation Quantization Collapse via Residual-Stream Dynamics》在 arXiv API 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，Experiments on LLaMA-2 and LLaMA-3 show that DynamicPTQ consistently improves perplexity and zero-shot QA performance under W4A4KV4 quantization, while achieving 1.05 to 1.07 times throughput improvement with modest memory overhead.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：3 s。
- [Understanding the Rejection of Fixes Generated by Agentic Pull Requests -- Insights from the AIDev Dataset](https://arxiv.org/abs/2606.13468v1)
  - 主题: Coding agent routing
  - 中文解读: 这项工作主要关注Coding agent routing，核心内容是《Understanding the Rejection of Fixes Generated by Agentic Pull Requests -- Insights from the AIDev Dataset》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Our results shed light on the importance of better guiding the model at these levels: (1) proposing hints about the approach to follow for fixing an issue, (2) outlining constraints or limitations regarding the approaches that should not be taken, and (3) instructing the agent on how to validate the implementation through CI pipelines and without introducing a breaking change.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [PROJECTMEM: A Local-First, Event-Sourced Memory and Judgment Layer for AI Coding Agents](https://arxiv.org/abs/2606.12329v1)
  - 主题: Coding agent routing
  - 中文解读: 这项工作主要关注Coding agent routing，核心内容是《PROJECTMEM: A Local-First, Event-Sourced Memory and Judgment Layer for AI Coding Agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，We frame this as Memory-as-Governance: memory that does not merely answer the agent but acts on its next action.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

