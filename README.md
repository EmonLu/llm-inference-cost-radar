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

- 日期: 2026-08-01
- 今日新论文: 15
- 今日新权威来源更新: 1
- 本周精选论文: 25
- 本周精选权威来源更新: 6
- 日报: `papers/2026-08-01.md`
- 周报: `digests/weekly-2026-08-01.md`

## 今日最值得看

- [Agentic Method for Deterministic Validation of Legacy Code Migration](https://arxiv.org/abs/2607.28271v1)
  - 主题: Coding agent routing, Cost-efficient LLM inference, LLM routing
  - 中文解读: 这项工作主要关注Coding agent routing、Cost-efficient LLM inference、LLM routing，核心内容是《Agentic Method for Deterministic Validation of Legacy Code Migration》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across three COBOL-Java case studies, spanning two open-source programs and one internal production-like COBOL program and ranging from 430 to 4,114 source lines, Locksmith consistently improved coverage beyond input-search plateaus, reaching nearly complete coverage on the two open-source programs and 91.90% branch coverage on the internal production-like COBOL program.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：114 s、91.90%。
- [MANTA: Multi-Agent Network Topology Adaptation for Self-Evolving Multi-Agent Systems](https://arxiv.org/abs/2607.28527v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《MANTA: Multi-Agent Network Topology Adaptation for Self-Evolving Multi-Agent Systems》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，We evaluate MANTA against representative single-agent and multi-agent baselines on five benchmarks spanning information seeking, tool use, planning, workflow execution, and mathematical reasoning.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [An Empirical Study of Coordination Mode as the First-Class Citizen in From-Scratch Multi-Agent Coding](https://arxiv.org/abs/2607.27877v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《An Empirical Study of Coordination Mode as the First-Class Citizen in From-Scratch Multi-Agent Coding》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Multi-agent vibe coding promises to accelerate software development, yet existing benchmarks rely on synthetic environments that ignore practical time and monetary costs, conflate reasoning with communication, and reward only superficial completion.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Route by Kinematics, Act by Observation: Kinematics-Supervised Expert Routing in MoE-Augmented VLA](https://arxiv.org/abs/2607.26807v1)
  - 主题: Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference、LLM routing，核心内容是《Route by Kinematics, Act by Observation: Kinematics-Supervised Expert Routing in MoE-Augmented VLA》在 arXiv API 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，Extensive experiments demonstrate KinRT's superiority over both dense and MoE-featured VLAs by more than 23.26% on RoboTwin benchmark and 20.27% on our introduced DIYRobot platform.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：23.26%、20.27%。
- [Agent Harness Distillation: Inference-Time Harness Extraction and Exploitation in Autonomous Multi-Agent Systems](https://arxiv.org/abs/2607.28147v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《Agent Harness Distillation: Inference-Time Harness Extraction and Exploitation in Autonomous Multi-Agent Systems》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experiments on real-world AMAS across multiple backbone LLMs demonstrate the effectiveness of AHD and reveal substantial IP leakage risks.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [MIND: Lightweight and Effective Memory Injection Defense for LLM Agents via Intent-Aware Information Bottleneck](https://arxiv.org/abs/2607.28103v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《MIND: Lightweight and Effective Memory Injection Defense for LLM Agents via Intent-Aware Information Bottleneck》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Notably, on ReAct-StrategyQA, MIND reduces mean ASR-r and ASR-a by 55.4% and 55.3%, respectively, while matching the undefended agent in average accuracy and latency.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：55.4%、55.3%。
- [Emission-Forecasting-Based Spatial-Temporal Carbon Response: A Multi-Agent Attention-Enhanced Deep Learning Framework](https://arxiv.org/abs/2607.26560v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Emission-Forecasting-Based Spatial-Temporal Carbon Response: A Multi-Agent Attention-Enhanced Deep Learning Framework》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The results demonstrate that under a one-hour reduction in carbon scheduling latency, the proposed model and methodology can achieve over 30% emission reduction.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：30%。
- [Scaling LLM-Driven Multi-Agent Systems: Design Principles and Architectural Scalability Analysis](https://arxiv.org/abs/2607.27942v1)
  - 主题: Agent systems and multi-agent efficiency
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency，核心内容是《Scaling LLM-Driven Multi-Agent Systems: Design Principles and Architectural Scalability Analysis》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Our findings show that scaling yields measurable accuracy improvements with approximately linear cost growth, but only when the underlying LLM exceeds a minimum capability threshold.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [From Understanding to Action: Feedback-Grounded Policy Discovery for Generative Recommendation](https://arxiv.org/abs/2607.27789v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《From Understanding to Action: Feedback-Grounded Policy Discovery for Generative Recommendation》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experiments on public benchmarks show consistent improvements over baselines, while large-scale online A/B tests achieve gains of 4.506% in Revenue and 4.621% in ADVV.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：4.506%、4.621%。
- [Back from the Future: Key-Value Cache Management by Counter-Causal Surprise](https://arxiv.org/abs/2607.27600v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Back from the Future: Key-Value Cache Management by Counter-Causal Surprise》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，To further reduce cost, we additionally propose a fast single-layer approximation that restricts the counter-causal pass to the last transformer layer, achieving a significant speedup per refresh cycle at marginal accuracy cost.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

