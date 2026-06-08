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

- 日期: 2026-06-08
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 7
- 日报: `papers/2026-06-08.md`
- 周报: `digests/weekly-2026-06-08.md`

## 今日最值得看

- [Reversible Foundations: Training a 120B Sparse MoE through State-Preserving Scaling](https://arxiv.org/abs/2606.07404)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Reversible Foundations: Training a 120B Sparse MoE through State-Preserving Scaling》在 arXiv cs.LG 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Each larger model is grown from the trained weights of the smaller one; active parameters rise monotonically from 1.78B at the dense seed to 5.93B at 120B (about 5% of the 118.67B stored).
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：5%。
- [UltraEP: Unleash MoE Training and Inference on Rack-Scale Nodes with Near-Optimal Load Balancing](https://arxiv.org/abs/2606.04101)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《UltraEP: Unleash MoE Training and Inference on Rack-Scale Nodes with Near-Optimal Load Balancing》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Averaged across MoE models from 106B to 671B parameters in training and prefill, UltraEP achieves 94.3% of the force-balanced ideal throughput, delivering 1.49$\times$ improvement over non-balancing, while reducing the final inter-rank imbalance from 1.30$-$4.01 to 1.01$-$1.04.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：94.3%。
- [Scalable Joint Resource Allocation for SLO-Constrained LLM Inference in Heterogeneous GPU Clouds](https://arxiv.org/abs/2604.07472)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Scalable Joint Resource Allocation for SLO-Constrained LLM Inference in Heterogeneous GPU Clouds》在 arXiv cs.LG 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Under out-of-sample stress with up to 1.5x delay and accuracy inflation, AGH degrades gracefully through provisioned headroom, yielding substantially lower cost and SLO violations than cost-minimal MILP solutions.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.5x。
- [Uncertainty-Aware LLM-Guided Policy Shaping for Sparse-Reward Reinforcement Learning](https://arxiv.org/abs/2606.06673)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Uncertainty-Aware LLM-Guided Policy Shaping for Sparse-Reward Reinforcement Learning》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，ULPS achieves more than 9% improvement in execution accuracy after fine-tuning, requires fewer environment interactions, and yields higher reward AUC.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：9%。
- [OPENPATH: A Supervisor--Specialist Agent System for Personalized, Accessible, and Multi-stop Urban Trip Planning](https://arxiv.org/abs/2606.07486v1)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《OPENPATH: A Supervisor--Specialist Agent System for Personalized, Accessible, and Multi-stop Urban Trip Planning》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Urban trip-planning systems are commonly optimized for travel time and cost, but they offer limited support for the heterogeneous needs that real travelers bring, such as personalized preferences, multi-stop itinerary construction, and end-to-end wheelchair accessibility.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [SW-$A^2$-Bench: Benchmarking Autonomous Software Agent Generation for Agentic Web](https://arxiv.org/abs/2604.04226)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing，核心内容是《SW-$A^2$-Bench: Benchmarking Autonomous Software Agent Generation for Agentic Web》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Our experiments demonstrate that our approach effectively activates the functional capabilities of code repositories and enables interoperable multi-agent collaboration in Agentic Web.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [SCALE: Scalable Cross-Attention Learning with Extrapolation for Agentic Workflow Scheduling](https://arxiv.org/abs/2606.06820)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《SCALE: Scalable Cross-Attention Learning with Extrapolation for Agentic Workflow Scheduling》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Trained on 16 nodes and tested directly on 32 and 48 nodes, SCALE reduces average response time by 8.9% at N=48 relative to the same architecture without SRR, confirming that explicit regularization is necessary to close the scale-generalization gap.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：8.9%。
- [Sparsely gated tiny linear experts](https://arxiv.org/abs/2606.07414)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Sparsely gated tiny linear experts》在 arXiv cs.LG 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，arXiv:2606.07414v1 Announce Type: new Abstract: Sparsity allows scaling model parameters without proportionally increasing computational cost.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Simple is Better: Multiplication May Be All You Need for LLM Request Scheduling](https://arxiv.org/abs/2603.15202)
  - 主题: Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Coding agent routing、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Simple is Better: Multiplication May Be All You Need for LLM Request Scheduling》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Our extensive experiments show that this simple approach can reduce TTFT by 92% and 39%, and TPOT by 24% and 51%, compared to vLLM-v1 and an in-production scheduler on real-world workloads covering chatbots and coding agents.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：92%、39%、24%。
- [RhinoVLA Technical Report](https://arxiv.org/abs/2606.07383)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《RhinoVLA Technical Report》在 arXiv cs.LG 这一方向上的推进。强调异构硬件协同推理。从实验上看，Experiments show that RhinoVLA achieves downstream performance comparable to {\pi}0.5 at a similar parameter scale, while reaching 11.69 Hz end-to-end inference on Huixi R1, meeting the 10 Hz real-time closedloop control target.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

