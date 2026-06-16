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

- 日期: 2026-06-16
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 3
- 日报: `papers/2026-06-16.md`
- 周报: `digests/weekly-2026-06-16.md`

## 今日最值得看

- [Frontier: Towards Comprehensive and Accurate LLM Inference Simulation](https://arxiv.org/abs/2605.21312)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Frontier: Towards Comprehensive and Accurate LLM Inference Simulation》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On 16-H800 GPU testbed, Frontier achieves an average throughput error below 4%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：4%、44.9%、6.4%。
- [MARS: Efficient, Adaptive Co-Scheduling for Heterogeneous Agentic Systems](https://arxiv.org/abs/2604.26963)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《MARS: Efficient, Adaptive Co-Scheduling for Heterogeneous Agentic Systems》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Our evaluations show that MARS reduces end-to-end latency by up to 5.94x while maintaining nearly maximal system throughput.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：5.94x、1.87x。
- [SwiftCache: Efficient LLM Serving for Multi-turn Conversations with Heterogeneous KV Cache Sharing](https://arxiv.org/abs/2606.16135)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《SwiftCache: Efficient LLM Serving for Multi-turn Conversations with Heterogeneous KV Cache Sharing》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Our experiments on real-world workloads show that SwiftCache reduces P99 time-to-first-token (TTFT) by up to 69% and extends maximum context length by up to 3.98x compared to vLLM and SGLang, with minimal interference to co-located models.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：69%、3.98x。
- [Tangram: Unlocking Non-Uniform KV Cache Compression for Efficient Multi-turn LLM Serving](https://arxiv.org/abs/2606.06302)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Tangram: Unlocking Non-Uniform KV Cache Compression for Efficient Multi-turn LLM Serving》在 arXiv cs.LG 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Non-uniform KV compression, which allocates heterogeneous budgets across attention heads, preserves accuracy far better than uniform schemes, yet remains impractical: modern serving stacks assume identical KV lengths across heads, so heterogeneity traps freed memory as page fragmentation, spends up to 25% of prefill time reclaiming scattered pages, and skews GPU workloads that inflate decode latency by up to $1.7\times$ or burn 15--20% of each decode step on re-planning.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：25%、20%。
- [RollArt: Disaggregated Multi-Task Agentic RL Training at Scale](https://arxiv.org/abs/2512.22560)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《RollArt: Disaggregated Multi-Task Agentic RL Training at Scale》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Our results demonstrate that ROLLART effectively improves training throughput and achieves 1.31--2.05 \(\times\) training time reduction compared to various RL systems.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Nightjar: Dynamic Adaptive Speculative Decoding for Large Language Models Serving](https://arxiv.org/abs/2512.22420)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Nightjar: Dynamic Adaptive Speculative Decoding for Large Language Models Serving》在 arXiv cs.DC 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Experiments show that Nightjar achieves up to 14.76% higher throughput than standard speculative decoding and up to 20.18% lower latency in the main benchmark suite under dynamic request arrival rates for real-time LLM serving scenarios.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：14.76%、20.18%。
- [Coordinated Scheduling for MoE LLM Serving](https://arxiv.org/abs/2606.15177)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Coordinated Scheduling for MoE LLM Serving》在 arXiv cs.DC 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，Our evaluation shows that Gimbal reduces average Time To First Token (TTFT) by 42.9% and average Time Per Output Token (TPOT) by 33.3% compared with the state-of-the-art serving system vLLM, while improving high-load request throughput by 3.0%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：42.9%、33.3%、3.0%。
- [Multi-Modal Spatio-Temporal Graph Neural Network with Mixture of Experts for Soil Organic Carbon Prediction](https://arxiv.org/abs/2606.16580)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Multi-Modal Spatio-Temporal Graph Neural Network with Mixture of Experts for Soil Organic Carbon Prediction》在 arXiv cs.LG 这一方向上的推进。强调异构硬件协同推理。从实验上看，Ablations confirm the heterogeneous graph, MoE fusion and fine-tuned backbone each contribute substantively, and the ensemble UQ stack achieves post-calibration ECE of $0.031$ (hybrid) and $0.026$ ($\beta$-NLL).
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [CacheWise: Understanding Workloads and Optimizing KVCache Management for Efficiently Serving LLM Coding Agents](https://arxiv.org/abs/2606.16824)
  - 主题: Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Coding agent routing、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《CacheWise: Understanding Workloads and Optimizing KVCache Management for Efficiently Serving LLM Coding Agents》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Implemented in vLLM and evaluated on the collected traces, CacheWise reduces KVCache evictions by up to 2-2.6x and improves total agent session completion time by up to 3.5x.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：2.6x、3.5x。
- [CoAgent: Concurrency Control for Multi-Agent Systems](https://arxiv.org/abs/2606.15376v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《CoAgent: Concurrency Control for Multi-Agent Systems》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On ten contended workloads, CoAgent stays within 5\% of serial correctness at a $1.4\times$ speedup and near-serial token cost, where 2PL and OCC surrender nearly all concurrency gains; on a bash-only target system, it grows a 25-tool library online and lifts the task pass rate from 45/71 to 63/71 at $0.80\times$ the time and $0.86\times$ the cost.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

