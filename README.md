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

- 日期: 2026-07-21
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 2
- 日报: `papers/2026-07-21.md`
- 周报: `digests/weekly-2026-07-21.md`

## 今日最值得看

- [FlashRT: Agent Harness for Guiding Agents to Deploy Real-Time Multimodal Applications](https://arxiv.org/abs/2607.18171v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《FlashRT: Agent Harness for Guiding Agents to Deploy Real-Time Multimodal Applications》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On AMD MI355X GPUs, FlashRT matches the peak latency reduction while increasing peak throughput improvement to 3.6x, demonstrating that agent-driven optimization can be more scalable on platforms with less mature expert optimization.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：355X、3.6x、70x。
- [ThAME: 3D Memory-Enabled Heterogeneous Accelerator for LLM Mixture of Experts](https://arxiv.org/abs/2607.17074v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《ThAME: 3D Memory-Enabled Heterogeneous Accelerator for LLM Mixture of Experts》在 arXiv API 这一方向上的推进。强调异构硬件协同推理。从实验上看，Experimental results demonstrate that ThAME outperforms state-of-the-art counterparts by up to 15.7x in terms of speedup and improves energy efficiency by up to 9.8x.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：15.7x、9.8x。
- [HyMCache: A KV Cache Framework for Multi-Turn LLM Serving with CXL-Hybrid Memory](https://arxiv.org/abs/2607.18141v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《HyMCache: A KV Cache Framework for Multi-Turn LLM Serving with CXL-Hybrid Memory》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Compared with 1 TB distributed-DRAM Mooncake, HyMCache incurs about 30% lower performance but uses 16x less DRAM.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：30%、16x、3.0x。
- [LMEdge: QoS-Aware LLM Inference Orchestration on Edge Clusters](https://arxiv.org/abs/2607.17175v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《LMEdge: QoS-Aware LLM Inference Orchestration on Edge Clusters》在 arXiv API 这一方向上的推进。强调异构硬件协同推理。从实验上看，Evaluation on a Kubernetes-based edge testbed with 57 instances and diverse query categories shows that LMEdge reduces latency, preserves accuracy, improves resource utilization, and increases serving ratio compared to two baselines.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [C$^2$KV: Compressed and Composable KV Cache Reuse for Efficient LLM Inference](https://arxiv.org/abs/2607.17715v1)
  - 主题: Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference，核心内容是《C$^2$KV: Compressed and Composable KV Cache Reuse for Efficient LLM Inference》在 arXiv API 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，Extensive experiments across multiple long-context benchmarks and model families demonstrate that C$^2$KV significantly reduces KV cache storage and transfer costs, achieving up to 17$\times$ inference speedup under long contexts, while preserving generation quality.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Can Experts Adapt Without Training? On Test-Time Modality Generalization in MVLMs](https://arxiv.org/abs/2607.16726v1)
  - 主题: Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference、LLM routing，核心内容是《Can Experts Adapt Without Training? On Test-Time Modality Generalization in MVLMs》在 arXiv API 这一方向上的推进。强调异构硬件协同推理。从实验上看，Without parametric updates, MoBE augments a static MVLM with test-time routing and online statistics, achieving average accuracy gains of +4.72, +7.17, and +4.3 over state-of-the-art TTA methods across seen, unseen, and heterogeneous medical benchmarks, highlighting the effectiveness of training-free expert adaptation for robust modality generalization.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [OrderMoE: An expert similarity driven distributed edge MoE inference](https://arxiv.org/abs/2607.17154v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《OrderMoE: An expert similarity driven distributed edge MoE inference》在 arXiv API 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，Experimental results on a real distributed edge testbed show that OrderMoE significantly reduces average latency, tail latency, cross-server traffic, and remote expert invocation ratio, while introducing only small and controllable inference quality degradation.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Reward-Driven LLM Agent Workflows: Synthesizing POMDP Routing and Self-Correction for Autonomous Decision-Making](https://arxiv.org/abs/2607.17038v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、LLM routing，核心内容是《Reward-Driven LLM Agent Workflows: Synthesizing POMDP Routing and Self-Correction for Autonomous Decision-Making》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Empirical experiments on the ALFWorld embodied simulation environment and the WebShop online navigation benchmark demonstrate a 24.5% absolute improvement in task success rate and trajectory efficiency over mainstream baselines like the standard ReAct framework.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：24.5%。
- [Talaria: Session-Aware Serverless Serving of Hundred-Billion-Parameter LLMs](https://arxiv.org/abs/2607.17181v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《Talaria: Session-Aware Serverless Serving of Hundred-Billion-Parameter LLMs》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Against an otherwise identical round scheduler with SP, host-KV restoration, and D2D staging disabled, Talaria cuts p50 SCT from 1000 s to 189 s and p95 from 2296 s to 867 s, speedups of 5.3x and 2.6x.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：50 S、1000 s、189 s。
- [SWE-Pruner Pro: The Coder LLM Already Knows What to Prune](https://arxiv.org/abs/2607.18213v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《SWE-Pruner Pro: The Coder LLM Already Knows What to Prune》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across two open-weight backbones and four multi-turn benchmarks, SWE-Pruner Pro saves up to 39% of prompt and completion tokens while preserving task quality, with bounded inference overhead.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：39%、3.8%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

