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

- 日期: 2026-11-28
- 今日新论文: 9
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 5
- 日报: `papers/2026-11-28.md`
- 周报: `digests/weekly-2026-11-28.md`

## 今日最值得看

- [WebVibe: Multimodal Interactive Website Generation via Reverse Synthesis and Visual Self-Distillation](https://arxiv.org/abs/2611.34292v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、LLM routing，核心内容是《WebVibe: Multimodal Interactive Website Generation via Reverse Synthesis and Visual Self-Distillation》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On the public Vision2Web L2, one-shot InteractiveCoder-9B nearly 3x its base model's functional score (20.2 to 55.2 FS) and matches a 1T-parameter coding agent in a single pass with 111x fewer total parameters and 78x fewer tokens.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：3x、111x、78x。
- [Do We Still Need Reinforcement Learning When We Can Read the World Model?](https://arxiv.org/abs/2611.34656v1)
  - 主题: Coding agent routing
  - 中文解读: 这项工作主要关注Coding agent routing，核心内容是《Do We Still Need Reinforcement Learning When We Can Read the World Model?》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experiments across diverse decision-making benchmarks show that synthesized policies match or outperform conventional RL methods while requiring substantially less experience.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [VibeVideoAgent: Closing the Perceptual Loop for Code-Driven Video Generation](https://arxiv.org/abs/2611.34237v1)
  - 主题: Coding agent routing
  - 中文解读: 这项工作主要关注Coding agent routing，核心内容是《VibeVideoAgent: Closing the Perceptual Loop for Code-Driven Video Generation》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On all 239 VibeVideoBench tasks, with matched agent runtimes and a fixed perception model, VibeVideoAgent improves holistic audiovisual quality (L3) for Claude Opus 5.5 (4.03 -> 4.43, while L2 rubric compliance rises from 98.87% to 99.35%), GPT-6 Astra (4.03 -> 4.27), and Claude Sonnet 5.5 (3.97 -> 4.10), with the largest gains in audio-visual synchronization (up to +0.56).
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：98.87%、99.35%。
- [SemProxy: Semantic 3D Proxies for Controllable Agentic 3D Modeling](https://arxiv.org/abs/2611.34414v1)
  - 主题: Coding agent routing
  - 中文解读: 这项工作主要关注Coding agent routing，核心内容是《SemProxy: Semantic 3D Proxies for Controllable Agentic 3D Modeling》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Coding agents are increasingly capable of generating 3D models, yet enabling users to effectively control the modeling process remains challenging.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Routeability Before Routing: Routeability Audit Protocol (RAP) and RouteabilityBench for Audited LLM Model Selection](https://arxiv.org/abs/2611.34825v1)
  - 主题: LLM routing
  - 中文解读: 这项工作主要关注LLM routing，核心内容是《Routeability Before Routing: Routeability Audit Protocol (RAP) and RouteabilityBench for Audited LLM Model Selection》在 arXiv API 这一方向上的推进。聚焦大模型路由/小模型分流，直接相关。从实验上看，Across four benchmarks and 66 LLMs, generic routing enhancements such as larger embedding sets, dimensionality reduction, selective abstention, clustering, and stronger regressors do not consistently outperform the single best model.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Compact Vision-Language Navigation in Continuous Environmentsvia On-Policy Training and Route-Bearing Output](https://arxiv.org/abs/2611.34561v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Compact Vision-Language Navigation in Continuous Environmentsvia On-Policy Training and Route-Bearing Output》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On-policy correction improves success, while bearing decoding outperforms image-plane waypoint scanning across all evaluated start headings with identical weights.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [One Ocean, Many Tasks: A Data-Grounded Simulation Suite and Benchmark for Marine Robotics](https://arxiv.org/abs/2611.34925v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《One Ocean, Many Tasks: A Data-Grounded Simulation Suite and Benchmark for Marine Robotics》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Simulation is essential for marine robotics, yet existing platforms often trade off between visually realistic worlds, high-throughput experimentation, and ocean-condition realism grounded in real data.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [SOLVE: Sparse, Ordered Keyposes Make LLM Agents Versatile and Efficient Robot Manipulator](https://arxiv.org/abs/2611.34750v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《SOLVE: Sparse, Ordered Keyposes Make LLM Agents Versatile and Efficient Robot Manipulator》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On a real robot, the same agent achieves an 88% success rate (75 of 85 episodes) over 16 challenging zero-shot tasks.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：88%、74.5%、84.5%。
- [PatternMiner: Automated Mathematical Discovery Through LLM-Guided Training and Interpretation of Small Models](https://arxiv.org/abs/2611.33966v1)
  - 主题: Agent systems and multi-agent efficiency, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、LLM routing，核心内容是《PatternMiner: Automated Mathematical Discovery Through LLM-Guided Training and Interpretation of Small Models》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，We describe the results of applying PatternMiner to five well-known positivity problems in algebraic combinatorics.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

