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

- 日期: 2026-05-12
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 4
- 日报: `papers/2026-05-12.md`
- 周报: `digests/weekly-2026-05-12.md`

## 今日最值得看

- [Nautilus Compass: Black-box Persona Drift Detection for Production LLM Agents](https://arxiv.org/abs/2605.09863v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing，核心内容是《Nautilus Compass: Black-box Persona Drift Detection for Production LLM Agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，End-to-end reproduction cost is $3.50 (~14x cheaper than GPT-4o-judged stacks).
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：14x、56.6%。
- [Scaling Mobile Agent Systems: From Capability Density to Collective Intelligence](https://arxiv.org/abs/2605.08124)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《Scaling Mobile Agent Systems: From Capability Density to Collective Intelligence》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，arXiv:2605.08124v1 Announce Type: new Abstract: Mobile agent systems are emerging as a key paradigm for enabling intelligent applications on edge devices and in AIoT ecosystems.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Uncovering Intra-expert Activation Sparsity for Efficient Mixture-of-Expert Model Execution](https://arxiv.org/abs/2605.08575)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Uncovering Intra-expert Activation Sparsity for Efficient Mixture-of-Expert Model Execution》在 arXiv cs.LG 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，Surprisingly, substantial intra-expert sparsity is readily available in existing pre-trained MoE models, without any modification to the activation function or model parameters, providing up to 90% sparsity within each expert without significant accuracy loss.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：90%。
- [Sparsity Moves Computation: How FFN Architecture Reshapes Attention in Small Transformers](https://arxiv.org/abs/2605.09403)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Sparsity Moves Computation: How FFN Architecture Reshapes Attention in Small Transformers》在 arXiv cs.LG 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，We decompose this redistribution into reduced per-token FFN capacity and sparse partitioning across experts.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [GenCellAgent: Generalizable, Training-Free Cellular Image Segmentation via Large Language Model Agents](https://arxiv.org/abs/2510.13896)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference、LLM routing，核心内容是《GenCellAgent: Generalizable, Training-Free Cellular Image Segmentation via Large Language Model Agents》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across seven cell-segmentation benchmarks spanning diverse microscopy modalities (4,718 images), this routing consistently matches or exceeds the best individual tool on every dataset and outperforms all baselines in overall accuracy.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [RDKV: Rate-Distortion Bit Allocation for Joint Eviction and Quantization of the KV Cache](https://arxiv.org/abs/2605.08317)
  - 主题: Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference，核心内容是《RDKV: Rate-Distortion Bit Allocation for Joint Eviction and Quantization of the KV Cache》在 arXiv cs.LG 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，Experiments on LongBench, RULER, and InfiniteBench show that RDKV outperforms the best evaluated baseline by 9.1% on average.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：9.1%、4.5x、1.9x。
- [An Empirical Study of Multi-Agent Collaboration for Automated Research](https://arxiv.org/abs/2603.29632)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《An Empirical Study of Multi-Agent Collaboration for Automated Research》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Utilizing a rigorously controlled, execution-based testbed equipped with Git worktree isolation and explicit global memory, we benchmark a single-agent baseline against two multi-agent paradigms: a subagent architecture (parallel exploration with post-hoc consolidation) and an agent team architecture (experts with pre-execution handoffs).
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [FLAME: Adaptive Mixture-of-Experts for Continual Multimodal Multi-Task Learning](https://arxiv.org/abs/2605.09355)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《FLAME: Adaptive Mixture-of-Experts for Continual Multimodal Multi-Task Learning》在 arXiv cs.LG 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，However, neither regime alone suffices: the pretraining task set is never exhaustive, while bypassing joint training forfeits the transfer gains and efficiency among co-trainable tasks.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Mixture-of-Top-k Attention: Efficient Attention via Scalable Fast Weights](https://arxiv.org/abs/2602.01219)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Mixture-of-Top-k Attention: Efficient Attention via Scalable Fast Weights》在 arXiv cs.LG 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，We conduct extensive experiments on vision tasks showing the superior effectiveness and efficiency of our MiTA, and also uncovering intriguing properties such as an emergent token-pruning effect and easy generalization from standard attention.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [CalBench: Evaluating Coordination-Privacy Trade-offs in Multi-Agent LLMs](https://arxiv.org/abs/2605.09823v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《CalBench: Evaluating Coordination-Privacy Trade-offs in Multi-Agent LLMs》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Unlike multi-agent benchmarks where a single capable agent can often substitute for the group, CalBench is inherently decentralized: no agent has access to another agent's private calendar, yet agents must still reach mutually consistent decisions over shared meeting scheduling.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

