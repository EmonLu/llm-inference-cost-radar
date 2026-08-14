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

- 日期: 2026-08-14
- 今日新论文: 15
- 今日新权威来源更新: 1
- 本周精选论文: 25
- 本周精选权威来源更新: 5
- 日报: `papers/2026-08-14.md`
- 周报: `digests/weekly-2026-08-14.md`

## 今日最值得看

- [HetRoute Heterogeneous and Cost-aware Collaborative Routing Framework for Distributed Edge MoE Inference](https://arxiv.org/abs/2608.00577)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《HetRoute Heterogeneous and Cost-aware Collaborative Routing Framework for Distributed Edge MoE Inference》在 arXiv cs.CL 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Trace-driven evaluation on three MoE models over a heterogeneous 10-server edge testbed shows that HetRoute reduces average inference latency by up to 59.0% and P99 latency by up to 58.0%, cuts cross-server traffic by up to 72.1%, and achieves 2.13x throughput improvement compared with representative baselines, while keeping quality degradation within the configured budget.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：59.0%、58.0%、72.1%。
- [LazyTrain: Limited-resource Allocation toward Zero-waste Yield Optimization in Large Language Model Training](https://arxiv.org/abs/2608.11919)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《LazyTrain: Limited-resource Allocation toward Zero-waste Yield Optimization in Large Language Model Training》在 arXiv cs.CL 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，In the primary Qwen3.6-27B H800 MetaMathQA run, LazyTrain reaches 219.95 TFLOPS and 1361 tokens/s at batch size 72, peaks at 68.84\,GB of GPU memory, and obtains 95.42\% exact-match accuracy on the full evaluation split.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1361 tokens/s。
- [TrimMoE A communication aware and adaptive depth framework for distributed edge inference](https://arxiv.org/abs/2608.00573)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《TrimMoE A communication aware and adaptive depth framework for distributed edge inference》在 arXiv cs.CL 这一方向上的推进。强调异构硬件协同推理。从实验上看，On a heterogeneous 10-server testbed with Switch-Base-8E, Qwen-MoE-A2.7B, and Mixtral-8x7B, TrimMoE reduces the average latency by up to 62.8%, lowers the cross-server traffic and the remote-execution ratio, and sustains high throughput under load, while keeping the task-quality degradation within a 2% bound.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：8x、62.8%、2%。
- [OrderMoE: An expert similarity driven distributed edge MoE inference](https://arxiv.org/abs/2607.17154)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《OrderMoE: An expert similarity driven distributed edge MoE inference》在 arXiv cs.DC 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，Experimental results on a real distributed edge testbed show that OrderMoE significantly reduces average latency, tail latency, cross-server traffic, and remote expert invocation ratio, while introducing only small and controllable inference quality degradation.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [RecSys Factory: Bounding LLM Agent Autonomy to Decision Points in the Industrial Recommender Lifecycle](https://arxiv.org/abs/2608.11241)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《RecSys Factory: Bounding LLM Agent Autonomy to Decision Points in the Industrial Recommender Lifecycle》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across the 78-day window the platform recorded 1,624 CLI-tool dispatches at a 78.6% aggregate success rate.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：78.6%、94%。
- [ReCodeAgent: A Multi-agent Workflow for Language-Agnostic Translation and Validation of Large-Scale Repositories](https://arxiv.org/abs/2604.07341)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing，核心内容是《ReCodeAgent: A Multi-agent Workflow for Language-Agnostic Translation and Validation of Large-Scale Repositories》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Our results demonstrate that ReCodeAgent consistently outperforms prior techniques on translation correctness, improving test pass rate by 60.8% on ground-truth tests, with an average cost of $15.3.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：60.8%、40.4%、28%。
- [HybridSB-MoE: Dual-Domain Schrödinger Bridges with Scene-Adaptive Expert Routing for Speech Enhancement](https://arxiv.org/abs/2608.12715v1)
  - 主题: Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference、LLM routing，核心内容是《HybridSB-MoE: Dual-Domain Schrödinger Bridges with Scene-Adaptive Expert Routing for Speech Enhancement》在 arXiv API 这一方向上的推进。强调异构硬件协同推理。从实验上看，On VoiceBank+DEMAND, HybridSB-MoE outperforms diffusion- and SB-based baselines at their step budgets while remaining competitive with consistency-distilled few-step methods.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [APEX: Adaptive Expert Prefetching for Memory-Efficient Edge MoE Inference](https://arxiv.org/abs/2608.11688)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《APEX: Adaptive Expert Prefetching for Memory-Efficient Edge MoE Inference》在 arXiv cs.LG 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，Across multiple MoE models, the correctness-preserving mode reduces per-token latency by up to 26% and improves energy-delay product (EDP) by up to 41% over state-of-the-art baselines, while the stall-free mode provides additional efficiency gains with negligible impact on application accuracy.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：26%、41%、99%。
- [RoutePack: Expert Placement and Attention-Aware Data Packing for MoE Reinforcement Learning](https://arxiv.org/abs/2608.12146)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《RoutePack: Expert Placement and Attention-Aware Data Packing for MoE Reinforcement Learning》在 arXiv cs.DC 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，Overall, RoutePack improves throughput by 8.85% and 14.89% over the baseline.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：8.85%、14.89%、3.80%。
- [Quantization-Aware Neuromorphic Architecture for Skin Lesion Classification on Resource-Constrained Devices](https://arxiv.org/abs/2507.15958)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Quantization-Aware Neuromorphic Architecture for Skin Lesion Classification on Resource-Constrained Devices》在 arXiv cs.AI 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，On a clinical dataset, QANA achieves 90.8% Top-1 accuracy and 81.7% macro F1, improving the strongest baseline by 3.2 points in accuracy and 3.6 points in macro F1.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：90.8%、81.7%、91.6%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

