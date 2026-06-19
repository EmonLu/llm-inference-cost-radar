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

- 日期: 2026-06-19
- 今日新论文: 15
- 今日新权威来源更新: 1
- 本周精选论文: 25
- 本周精选权威来源更新: 4
- 日报: `papers/2026-06-19.md`
- 周报: `digests/weekly-2026-06-19.md`

## 今日最值得看

- [Execution-State Capsules: Graph-Bound Execution-State Checkpoint and Restore for Low-Latency, Small-Batch, On-Device Physical-AI Serving](https://arxiv.org/abs/2606.20537)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Execution-State Capsules: Graph-Bound Execution-State Checkpoint and Restore for Low-Latency, Small-Batch, On-Device Physical-AI Serving》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，GPU-resident snapshot and restore are sub-millisecond, and TTFT speedup over cold prefill grows from 3.9x at 2k tokens to 27x at 16k tokens.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：3.9x、27x。
- [UltraQuant: 4-bit KV Caching for Context-Heavy Agents](https://arxiv.org/abs/2606.20474)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《UltraQuant: 4-bit KV Caching for Context-Heavy Agents》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On a long-context, multi-turn agentic workload, UltraQuant cuts P50 time-to-first-token by 3.47x in the cache-pressured late rounds (2.3x across all rounds) and raises output throughput by 1.63x over the FP8 KV baseline.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：3.47x、2.3x、1.63x。
- [UltraEP: Unleash MoE Training and Inference on Rack-Scale Nodes with Near-Optimal Load Balancing](https://arxiv.org/abs/2606.04101)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《UltraEP: Unleash MoE Training and Inference on Rack-Scale Nodes with Near-Optimal Load Balancing》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Averaged across training and serving, UltraEP achieves 94.3% of the force-balanced ideal throughput, delivering 1.49$\times$ improvement over no-balancing, while reducing the final inter-rank imbalance from 1.30$-$4.01 to 1.01$-$1.04.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：94.3%。
- [SAC: Disaggregated KV Cache System for Sparse Attention LLMs with CXL](https://arxiv.org/abs/2606.19746)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《SAC: Disaggregated KV Cache System for Sparse Attention LLMs with CXL》在 arXiv cs.DC 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，Evaluations on DeepSeek-V3.2 using SGLang show that SAC achieves 2.1x higher throughput, 9.7x lower TTFT, and 1.8x lower TBT compared to RDMA-based baselines, establishing CXL-based disaggregation as the superior infrastructure for emerging sparse attention models.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：2.1x、9.7x、1.8x。
- [TetriServe: Efficiently Serving Mixed DiT Workloads](https://arxiv.org/abs/2510.01565)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《TetriServe: Efficiently Serving Mixed DiT Workloads》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Extensive evaluation on state-of-the-art DiT models shows that TetriServe achieves up to 32% higher SLO attainment compared to existing solutions without degrading image quality.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：32%。
- [Techniques for Peak Memory Reduction for LoRA Fine-tuning of LLMs on Edge Devices](https://arxiv.org/abs/2606.19528)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Techniques for Peak Memory Reduction for LoRA Fine-tuning of LLMs on Edge Devices》在 arXiv cs.LG 这一方向上的推进。涉及 KV/参数/专家的卸载策略，可节约显存或成本。从实验上看，Experiments on Llama-3.2 3B and Qwen-2.5 3B demonstrate up to $26\times$ and $28\times$ reduction in peak memory, enabling fine-tuning on resource-constrained devices.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Oranits: Mission Assignment and Task Offloading in Open RAN-based ITS using Metaheuristic and Deep Reinforcement Learning](https://arxiv.org/abs/2507.19712)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Oranits: Mission Assignment and Task Offloading in Open RAN-based ITS using Metaheuristic and Deep Reinforcement Learning》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Meanwhile, MA-DDQN achieves even greater improvements of 11.0% in terms of mission completions and 12.5% in terms of the overall benefit.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：11.0%、12.5%、7.1%。
- [Before the Pull Request: Mining Multi-Agent Coordination](https://arxiv.org/abs/2606.19616)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《Before the Pull Request: Mining Multi-Agent Coordination》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，We show that (i) this shared substrate reduces duplicate and conflicting work at bounded overhead - the share of work that merely re-does a teammate's task falls from 78% to 0% while useful throughput more than triples; (ii) every agent's copy of the log converges to the same state with no write silently dropped, where a file-based tracker loses concurrent writes; and (iii) the log is a mineable artefact from which concrete failure modes - conflicting edits, lock starvation, redundant rediscovery, race-to-close - are automatically recoverable with provenance, several invisible in pull-request history.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：78%、0%。
- [Rethinking Shrinkage Bias in LLM FP4 Pretraining: Geometric Origin, Systemic Impact, and UFP4 Recipe](https://arxiv.org/abs/2606.20381)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Rethinking Shrinkage Bias in LLM FP4 Pretraining: Geometric Origin, Systemic Impact, and UFP4 Recipe》在 arXiv cs.AI 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，In contrast, uniform grids (E1M2/INT4) bypass this grid-geometry error and better convert the improved bucket utilization from RHT into higher quantization quality.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Beyond the GUI Paradigm: Do Mobile Agents Need the Phone Screen?](https://arxiv.org/abs/2606.19388)
  - 主题: Coding agent routing
  - 中文解读: 这项工作主要关注Coding agent routing，核心内容是《Beyond the GUI Paradigm: Do Mobile Agents Need the Phone Screen?》在 arXiv cs.CL 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Every CLI agent outperforms every GUI baseline in all five categories, with substantially fewer steps per task (10.7 vs.\ 18.6).
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

