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

- 日期: 2026-10-18
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 10
- 日报: `papers/2026-10-18.md`
- 周报: `digests/weekly-2026-10-18.md`

## 今日最值得看

- [OPRD: On-Policy Reminder Distillation for Long-Horizon Coding Agents](https://arxiv.org/abs/2610.21496v1)
  - 主题: Coding agent routing, Cost-efficient LLM inference, LLM routing
  - 中文解读: 这项工作主要关注Coding agent routing、Cost-efficient LLM inference、LLM routing，核心内容是《OPRD: On-Policy Reminder Distillation for Long-Horizon Coding Agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Under the same diagnostic protocol, it reduces the aggregate error-event count from 446 to 222, a 50.2% reduction.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：50.2%。
- [Trajectory-Level Speculation with Semantic Verification for Tool-Using Agents](https://arxiv.org/abs/2610.21463v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《Trajectory-Level Speculation with Semantic Verification for Tool-Using Agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On $τ^2$-Bench, SpecAgent comes within one point of the strong model's success rate while roughly halving memory traffic and wall time, and on AutomationBench and VitaBench it recovers 44-75% of the quality gap while lowering both.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：75%。
- [Augment the Cache, Replace the Activation: A 2x2 Study of Internal-State Sharing](https://arxiv.org/abs/2610.22026v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《Augment the Cache, Replace the Activation: A 2x2 Study of Internal-State Sharing》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Every agent pair that must communicate needs its own transfer bridge, and every agent added to a system needs a new bridge fitted against each previous agent.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Jev-LiteMAS: Separating Decisions from Generation in Multi-Agent Workflows](https://arxiv.org/abs/2610.21411v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、LLM routing，核心内容是《Jev-LiteMAS: Separating Decisions from Generation in Multi-Agent Workflows》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across four benchmarks and two backbones, Jev-LiteMAS reduces generative-LLM tokens by 12.7-54.6% over LAS, maintaining accuracy within 1.34 percentage points and lowering latency in seven of eight settings.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：54.6%、43.5%。
- [Learning to Steer LLM Agents and Multi-Agent Systems](https://arxiv.org/abs/2610.22316v1)
  - 主题: Agent systems and multi-agent efficiency
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency，核心内容是《Learning to Steer LLM Agents and Multi-Agent Systems》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experiments on information-seeking search tasks show that the steering agent provides effective supervision for both single-agent and multi-agent systems, improving their performance and efficiency.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Bias Control and Injection for Multi-Agent Aggregation](https://arxiv.org/abs/2610.21290v1)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《Bias Control and Injection for Multi-Agent Aggregation》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Overall, our framework achieves higher average accuracy and better token efficiency than competing non-oracle aggregation methods across three mathematical reasoning benchmarks and four heterogeneous LLM combinations.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Decentralized LLM Workflows via Sequential Auctions](https://arxiv.org/abs/2610.22201v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Decentralized LLM Workflows via Sequential Auctions》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across a diverse set of domains, we demonstrate that imperfect competition successfully sustains necessary agent profit margins while maintaining high task success rates at low costs.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [The Role of Agentic Instruction Categories for Code Generation: A Study of Five Python Libraries](https://arxiv.org/abs/2610.21421v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing，核心内容是《The Role of Agentic Instruction Categories for Code Generation: A Study of Five Python Libraries》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，No Gemma 4 variant passed all tests, whereas 12.99% of GPT-5.4 variants did.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：12.99%。
- [X-RIC: An Agentic RAN-Intelligent Controller Benchmark for Enhancing Reinforcement Learning](https://arxiv.org/abs/2610.22269v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《X-RIC: An Agentic RAN-Intelligent Controller Benchmark for Enhancing Reinforcement Learning》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，X-RIC achieves 89% operational cost reduction while maintaining SLA compliance, converging 75% faster with 50% fewer training steps and 46% lower variance.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：89%、75%、50%。
- [Training Reasoning Models to Generate Diverse Scientific Ideas](https://arxiv.org/abs/2610.22324v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing，核心内容是《Training Reasoning Models to Generate Diverse Scientific Ideas》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，When a coding agent runs proof-of-concept experiments on the ideas, our model's success@k is comparable to Claude Opus 4.8's, so we see that the added diversity does not cost any executability.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

