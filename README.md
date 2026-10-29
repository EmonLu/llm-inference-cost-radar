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

- 日期: 2026-10-29
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 4
- 日报: `papers/2026-10-29.md`
- 周报: `digests/weekly-2026-10-29.md`

## 今日最值得看

- [CRISP: Co-designing Pruning and Scheduling for Efficient MoE Inference on Edge Servers](https://arxiv.org/abs/2610.37442v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《CRISP: Co-designing Pruning and Scheduling for Efficient MoE Inference on Edge Servers》在 arXiv API 这一方向上的推进。强调异构硬件协同推理。从实验上看，Across Mixtral-8x7B and DeepSeek-MoE-16B, CRISP improves throughput by up to $2.1\times$ at the same memory budget while limiting accuracy loss to 3.6\% relative to full-width inference.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：8x。
- [INC-MoE: Overlapping In-Network Collectives and Expert Computation for Expert-Parallel Mixture-of-Experts Inference](https://arxiv.org/abs/2610.36339v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《INC-MoE: Overlapping In-Network Collectives and Expert Computation for Expert-Parallel Mixture-of-Experts Inference》在 arXiv API 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，On OLMoE prefill with four-way expert parallelism, INC-MoE reduces time to first token (TTFT) by up to 33% and increases throughput by up to 50% relative to vLLM's default collective path, while matching its outputs.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：33%、50%。
- [TAO: Tool-Aware Joint Scheduling for LLM-Based Agentic Serving](https://arxiv.org/abs/2610.37230v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《TAO: Tool-Aware Joint Scheduling for LLM-Based Agentic Serving》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across the 12 reported model-workload-concurrency settings, TAO reduces latency by up to 26.8%, reduces mean time to first token (TTFT) by up to 36.3%, and increases decode throughput by up to 29.5% relative to the best evaluated state-of-the-art baseline for each metric.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：26.8%、36.3%、29.5%。
- [Spine: Compiling Subtask Trees into Structured Context for Long-Horizon Coding Agents](https://arxiv.org/abs/2610.37224v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《Spine: Compiling Subtask Trees into Structured Context for Long-Horizon Coding Agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，With GPT-5.6 Sol, compared with native Codex, SpineCodex improves SWE-Milestone Score by 11.8% while reducing total cost by 32.4%, improves the average ProgramBench test-pass rate by 17.3%, and improves Mean@5 on eight of the ten evaluated FrontierSWE tasks.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：5.6 S、11.8%、32.4%。
- [TP-JSCC: Efficient Token Pruning and Joint Source-Channel Coding for LVLMs-based 3D-VQA in Cloud-Edge Collaboration](https://arxiv.org/abs/2610.35489v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《TP-JSCC: Efficient Token Pruning and Joint Source-Channel Coding for LVLMs-based 3D-VQA in Cloud-Edge Collaboration》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Specifically, on ScanQA validation set, the LGS-HTP module could achieve 90% pruning ratio while incurring less than a 1% CIDEr loss.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：90%、1%。
- [Reva: Real-Time Vulnerability Detection through Contextual Probing of Large Language Models](https://arxiv.org/abs/2610.35829v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing，核心内容是《Reva: Real-Time Vulnerability Detection through Contextual Probing of Large Language Models》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On PrimeVul's held-out test set, REVA on GLM-5.3-Flash reaches 60.0% accuracy in about one second per function.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：60.0%、59.2%。
- [Free to Look, Free to Reason: Simple LLM Harnesses Outdiagnose Hand-Crafted Root Cause Analysis Agents](https://arxiv.org/abs/2610.35767v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing，核心内容是《Free to Look, Free to Reason: Simple LLM Harnesses Outdiagnose Hand-Crafted Root Cause Analysis Agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The simple harnesses are the most accurate (PR@1 65-77% on three mid-tier models), ahead of the published agents (16-53%) and the non-LLM methods (6-39%), on every model on which both families were run.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：77%、53%、39%。
- [EdgePace: Deadline- and Freshness-Aware LLM Scheduling on Unified-Memory Platforms](https://arxiv.org/abs/2610.37307v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《EdgePace: Deadline- and Freshness-Aware LLM Scheduling on Unified-Memory Platforms》在 arXiv API 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Relative to unmanaged inference, it reduces foreground deadline misses by 24.1%--96.1% while retaining 64.9%--98.5% of LLM throughput.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：24.1%、96.1%、64.9%。
- [WAKMan: Workload Aware KVCache Manager](https://arxiv.org/abs/2610.36355v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《WAKMan: Workload Aware KVCache Manager》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across 20 mixes, no single policy is always best: vLLM's default strategy LRU provides 12% higher cache hits as compared to the frequency-oriented S3FIFO on agentic-heavy mixes but trails it by up to 22% elsewhere, and even a single workload parameter can flip the winner even for any particular mix.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：12%、22%。
- [Do Coding Agents Still Need a Debugger? Frontier-Model-Based Fault Localization at the Accuracy Ceiling](https://arxiv.org/abs/2610.36015v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《Do Coding Agents Still Need a Debugger? Frontier-Model-Based Fault Localization at the Accuracy Ceiling》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Results: Without tools, the agents localized 98.2 to 99.9% of faults in original and 96.7 to 99.9% in transformed programs, losing accuracy mainly where recipes restructured loops and conditions.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：99.9%、3.8 s。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

