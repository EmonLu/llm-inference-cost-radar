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

- 日期: 2026-11-13
- 今日新论文: 15
- 今日新权威来源更新: 5
- 本周精选论文: 25
- 本周精选权威来源更新: 7
- 日报: `papers/2026-11-13.md`
- 周报: `digests/weekly-2026-11-13.md`

## 今日最值得看

- [Tideway: Phase-Aware Tiered Memory Management for MoE Inference on Consumer Devices](https://arxiv.org/abs/2611.14848v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Tideway: Phase-Aware Tiered Memory Management for MoE Inference on Consumer Devices》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On average, TIDEWAY achieves speedups of 1.97x in end-to-end latency and 2.40x in Time-to-First-Token (TTFT), along with 1.61x higher decode throughput against the fastest baseline.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.97x、2.40x、1.61x。
- [Broadcast, Don't Replicate: Eliminating Weight HBM in Datacenter LLM Serving](https://arxiv.org/abs/2611.17097v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Broadcast, Don't Replicate: Eliminating Weight HBM in Datacenter LLM Serving》在 arXiv API 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，Evaluated at a datacenter scale of 80,000 accelerators, OBM eliminates petabytes of HBM while being competitive or better in throughput and energy per token than an HBM-based system.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Alloy: A Multi-Material Physics Engine for Robot Learning](https://arxiv.org/abs/2611.16312v1)
  - 主题: Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Coding agent routing、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Alloy: A Multi-Material Physics Engine for Robot Learning》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，In a cold test, agents that had never seen Alloy installed a pre-release from the package index and trained policies for walking, cable handling and pouring on a single GPU.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [MULTILOOP: Evolving Multi-Agent Harnesses for Complex Information-Seeking Tasks](https://arxiv.org/abs/2611.15754v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing，核心内容是《MULTILOOP: Evolving Multi-Agent Harnesses for Complex Information-Seeking Tasks》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，With only 10 training samples, the evolved harness improves accuracy by 4.6% over the base harness and by 3.2% over the best single-agent system.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：4.6%、3.2%。
- [DecArena: Evaluating Large-Scale Decentralized Multi-Agent Collaboration](https://arxiv.org/abs/2611.15521v1)
  - 主题: Agent systems and multi-agent efficiency, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、LLM routing，核心内容是《DecArena: Evaluating Large-Scale Decentralized Multi-Agent Collaboration》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Results show that GraphHarness substantially improves task success (+48.5) and produces higher quality collaboration (+30.6), while using fewer costs (+34.0) than baselines.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Metal Sandbox: Isolated Execution and Command Scheduling for GPU Coding Agents on Apple Silicon](https://arxiv.org/abs/2611.17294v1)
  - 主题: Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Coding agent routing、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Metal Sandbox: Isolated Execution and Command Scheduling for GPU Coding Agents on Apple Silicon》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Replaying these measured traces under dynamic scheduling reduces mean tool waiting by 18.8% and batch elapsed time by 22.3%, assuming unchanged phase durations.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：18.8%、22.3%。
- [Reducing Batch Makespan for LLM Agent Workloads through Inference-Environment Coordination](https://arxiv.org/abs/2611.16661v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Reducing Batch Makespan for LLM Agent Workloads through Inference-Environment Coordination》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Live evaluations with Ling-3.0-Flash and Ling-3.1-Flash on the BFCL, SWE-bench Multilingual, WideSearch, and MCP-Atlas benchmarks demonstrate makespan reductions of 10.4% to 65.0%, while evaluation scores remain aligned.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：10.4%、65.0%。
- [Contain, Conform, Compare (Extended Version): A Red-Teamed Evaluation Kit for Small Coding Agents and the Full Record of Its Experiments](https://arxiv.org/abs/2611.16485v1)
  - 主题: Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Coding agent routing、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Contain, Conform, Compare (Extended Version): A Red-Teamed Evaluation Kit for Small Coding Agents and the Full Record of Its Experiments》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The unchanged baseline, run again on the same 128 tasks, moved by 1.17 points, and 65% of these tasks were solved in none of eight runs.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：65%、95%。
- [Auriga: Harness-Governed LLM Agents for Effective Throughput Optimization in Execute-Order-Validate Permissioned Blockchains](https://arxiv.org/abs/2611.14945v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Auriga: Harness-Governed LLM Agents for Effective Throughput Optimization in Execute-Order-Validate Permissioned Blockchains》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across three benchmarks and conflict rates up to 70%, Auriga improves effective throughput by up to 6.0 times over default Fabric and 2.0 times over the strongest baseline.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：70%。
- [Where LLM Agents Get Stuck Debugging Databases: Access More Than Reasoning](https://arxiv.org/abs/2611.17304v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing，核心内容是《Where LLM Agents Get Stuck Debugging Databases: Access More Than Reasoning》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，In every incident whose root cause depended on runtime concurrency, the agent announced a cause, shipped a fix, and later walked it back, and each wrong guess cost a deploy-and-observe cycle.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

