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

- 日期: 2026-09-12
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 6
- 日报: `papers/2026-09-12.md`
- 周报: `digests/weekly-2026-09-12.md`

## 今日最值得看

- [Studying Without a Syllabus: Task-Agnostic Environment Preprocessing](https://arxiv.org/abs/2609.10824)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《Studying Without a Syllabus: Task-Agnostic Environment Preprocessing》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，We compare unaided and archive-equipped meta-agents with fixed synthetic-practice and corpus-processing methods across six heterogeneous benchmarks.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [From Agent Traces to Trust: A Survey of Evidence Tracing and Execution Provenance in LLM Agents](https://arxiv.org/abs/2606.04990)
  - 主题: Agent systems and multi-agent efficiency
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency，核心内容是《From Agent Traces to Trust: A Survey of Evidence Tracing and Execution Provenance in LLM Agents》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Finally, we discuss benchmarks, datasets, metrics, and open challenges for building provenance-aware, auditable, and recoverable agent systems.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [FlexComp: One Model for Every Ratio in Context Compression](https://arxiv.org/abs/2609.11192v1)
  - 主题: Cost-efficient LLM inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、LLM routing，核心内容是《FlexComp: One Model for Every Ratio in Context Compression》在 arXiv API 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，At serving-scale batch sizes, the $K$ predictor cuts context KV cache by 50% and improves decoding throughput by 47%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：50%、47%、98%。
- [Calibration-Aware Uncertainty Cascades for Efficient Heterogeneous Model Collaboration](https://arxiv.org/abs/2609.11446)
  - 主题: Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference、LLM routing，核心内容是《Calibration-Aware Uncertainty Cascades for Efficient Heterogeneous Model Collaboration》在 arXiv cs.AI 这一方向上的推进。强调异构硬件协同推理。从实验上看，Extensive experiments demonstrate that, across six language benchmarks, CAUC achieves an average relative accuracy improvement of 1.9% over strong-model-only inference while avoiding approximately 47% of strong-model calls.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.9%、47%、57%。
- [Learning What to Retain: Gated-Memory Routing for Efficient Collaboration in Multi-Agent LLM Systems](https://arxiv.org/abs/2609.00237)
  - 主题: Agent systems and multi-agent efficiency, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、LLM routing，核心内容是《Learning What to Retain: Gated-Memory Routing for Efficient Collaboration in Multi-Agent LLM Systems》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across five reasoning and code-generation benchmarks, our framework is both effective and efficient: it attains the best average accuracy, exceeding the strongest baseline by 2.44 points, while reducing HumanEval inference cost by 31.9% relative to that baseline.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：31.9%。
- [A Voice-Interactive Multi-Agent System for Smart Operating Rooms: Architecture Design and Key Technologies](https://arxiv.org/abs/2609.11231v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《A Voice-Interactive Multi-Agent System for Smart Operating Rooms: Architecture Design and Key Technologies》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Three key technologies are investigated: (1) KV Cache prefix warming for low-latency inference, reducing recomputation overhead from approximately 500 ms to tens of milliseconds via byte-level Longest Common Prefix reuse; (2) streaming partial JSON parsing with early parallel task execution, reducing end-to-end latency by approximately 30%; and (3) progressive skill prompt disclosure, which dynamically filters system prompts based on user role, connected devices, and surgical phase to maximize information density within limited context windows.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：500 ms、30%。
- [Why Is Video Still So Expensive? A Survey of Inference-Efficiency Mechanisms in Video and Audiovisual LLMs](https://arxiv.org/abs/2609.10355v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Why Is Video Still So Expensive? A Survey of Inference-Efficiency Mechanisms in Video and Audiovisual LLMs》在 arXiv API 这一方向上的推进。强调异构硬件协同推理。从实验上看，This survey covers inference-efficiency mechanisms for visual and audiovisual VideoLLMs that report concrete reductions in parameter count, FLOPs per input, latency, memory, or visual and audio token count.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Recursive Code World Models: Building Complex Worlds through Recursive Scene Programs](https://arxiv.org/abs/2609.11499v1)
  - 主题: Coding agent routing, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Coding agent routing、Cost-efficient LLM inference，核心内容是《Recursive Code World Models: Building Complex Worlds through Recursive Scene Programs》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across complex scenes, RCWM outperforms prior code-based image-to-scene reconstruction methods.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Lightweight LiDAR-Based Cone Detection Framework Using Random Forest for Formula Student Driverless](https://arxiv.org/abs/2609.11527)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Lightweight LiDAR-Based Cone Detection Framework Using Random Forest for Formula Student Driverless》在 arXiv cs.AI 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Evaluated on 2,371 labeled clusters collected from real FSD events, the pipeline achieves an F1-score of 98.33% and an end-to-end runtime of 3.13 ms on CPU-only hardware.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：98.33%、3.13 ms。
- [SaltBench: A Referee-Gated Protocol for Measuring Method Effects in Machine-Checked Software Work](https://arxiv.org/abs/2609.11076v1)
  - 主题: Coding agent routing
  - 中文解读: 这项工作主要关注Coding agent routing，核心内容是《SaltBench: A Referee-Gated Protocol for Measuring Method Effects in Machine-Checked Software Work》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Four arms are tested: a plain agent; an agent that is also instructed to create a specification and verify the code against it, in a reduced rendering of the method, as registered; and two arms where the specification is provided a priori, extended under a dated amendment to $k=4$, where the registered sign test reached no verdict (3 of 4, $p = 0.3125$, every premium below the resolvable floor).
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

