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

- 日期: 2026-11-11
- 今日新论文: 15
- 今日新权威来源更新: 1
- 本周精选论文: 25
- 本周精选权威来源更新: 4
- 日报: `papers/2026-11-11.md`
- 周报: `digests/weekly-2026-11-11.md`

## 今日最值得看

- [SHADOWPREFILL: Keeping Your Next Model Warm for Per-Step Model Routing in Agentic LLM Serving](https://arxiv.org/abs/2611.13176v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《SHADOWPREFILL: Keeping Your Next Model Warm for Per-Step Model Routing in Agentic LLM Serving》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，With LLMRouter routing 24 model pairs over five agentic benchmark suites, SHADOWPREFILL cuts switch-call latency by 8.5-21.4%, LLM-call latency by 3.7-17.7%, and routed token cost by 22.5-46.1%, while normal traffic keeps its SLO and energy per request rises by 0.4%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：21.4%、17.7%、46.1%。
- [Multi-Objective Scheduling of LLM-Based Multi-Agent Workflows in Cloud Computing](https://arxiv.org/abs/2611.13740)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Multi-Objective Scheduling of LLM-Based Multi-Agent Workflows in Cloud Computing》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Existing agentic workflow frameworks mostly focus on output quality and task success rates over popular benchmarks, rarely accounting for execution dynamics of LLM-based agents such as inference latency, computation power of heterogeneous resources, cloud-specific billing period and resource provisioning overheads.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Dynamic Mixed-Precision Routing for Efficient Multi-step LLM Interaction](https://arxiv.org/abs/2602.02711)
  - 主题: Cost-efficient LLM inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、LLM routing，核心内容是《Dynamic Mixed-Precision Routing for Efficient Multi-step LLM Interaction》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across three long-horizon agentic benchmarks with nested quantization, DMR achieves an average 2.44x decode speedup over FP16 at comparable task success rates, without fine-tuning the underlying model.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：2.44x、1.71x、86.9%。
- [One-Sided Expert-Parallel All-to-All for Mixture-of-Experts Inference over NVLink](https://arxiv.org/abs/2611.13188v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《One-Sided Expert-Parallel All-to-All for Mixture-of-Experts Inference over NVLink》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，It even outperforms the fused DeepGEMM MegaMoE at up to 128 tokens per GPU, making it still competitive for decoding.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [EngineAgent: Agentizing On-Device LLM Inference Engines with Inference Stack Hierarchy Awareness and Hardware Abilities](https://arxiv.org/abs/2611.14356v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Heterogeneous MoE inference，核心内容是《EngineAgent: Agentizing On-Device LLM Inference Engines with Inference Stack Hierarchy Awareness and Hardware Abilities》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across 12 tasks spanning three mobile LLMs and four engine--backend pairs on CPUs, GPUs, and NPUs, EngineAgent achieves 75% end-to-end success with either of two underlying LLMs, versus 33.3% for the strongest coding-agent baseline.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：75%、33.3%。
- [AgentWeave: Efficient Distributed Agent Serving via Flow Decomposition](https://arxiv.org/abs/2610.14804)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《AgentWeave: Efficient Distributed Agent Serving via Flow Decomposition》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experiments across four representative agent applications demonstrate that AgentWeave improves throughput by 1.28-1.81x, reduces average latency by 2.08-2.45x, and reduces P90 latency by 1.56-2.04x over state-of-the-art baselines.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.81x、2.45x、2.04x。
- [Deterministic, Reproducible Inference in Exact Integer Arithmetic, and Verifiable Distributed Inference as Its Consequence](https://arxiv.org/abs/2611.13730v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Deterministic, Reproducible Inference in Exact Integer Arithmetic, and Verifiable Distributed Inference as Its Consequence》在 arXiv API 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，GLM-4.5-Air (106,852,251,264 parameters, 427 GB of integer codes) generated its answer across three machines, none of which can hold its integer codes in RAM, bit-identically to a single-host reference.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：427 GB。
- [Scaling Shapley Energy Attribution to Large LLM Batches](https://arxiv.org/abs/2611.13802v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《Scaling Shapley Energy Attribution to Large LLM Batches》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Under static batching with batch sizes of 8-256, StepSplit achieves an $L_1$ error of 0.4-4.3%, compared with 13.4-61.3% for token-proportional allocation.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：4.3%、61.3%、6.4%。
- [DrugCoding: A Scientific Programming Agent for Drug Discovery](https://arxiv.org/abs/2611.13651v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、LLM routing，核心内容是《DrugCoding: A Scientific Programming Agent for Drug Discovery》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experimental results demonstrate that DrugCoding achieves an average session-level Pass@1 of 97.35% on the full benchmark, outperforming the strongest baseline, Codex, by 9.24%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：97.35%、9.24%、97.92%。
- [ForeSpark: Joint Draft and Verification Budget Scheduling for Parallel Speculative Decoding](https://arxiv.org/abs/2611.13442)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《ForeSpark: Joint Draft and Verification Budget Scheduling for Parallel Speculative Decoding》在 arXiv cs.DC 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，Implemented on vLLM, ForeSpark improves throughput by up to 1.77x over the state-of-the-art DSpark and by 2.49x over autoregressive decoding at a matched per-request generation rate, without changing the output distribution.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.77x、2.49x、1.51x。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

