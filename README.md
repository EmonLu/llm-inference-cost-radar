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

- 日期: 2026-07-28
- 今日新论文: 15
- 今日新权威来源更新: 1
- 本周精选论文: 25
- 本周精选权威来源更新: 6
- 日报: `papers/2026-07-28.md`
- 周报: `digests/weekly-2026-07-28.md`

## 今日最值得看

- [DraftExpert: Expansion-Aware Self-Speculative Decoding for End-Device MoE Inference](https://arxiv.org/abs/2607.24434v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《DraftExpert: Expansion-Aware Self-Speculative Decoding for End-Device MoE Inference》在 arXiv API 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，On DeepSeek-V2-Lite and Moonlight-16B-A3B across CPU-GPU and Flash-NPU offload, DraftExpert improves decode throughput by 1.45x on average, raises draft acceptance to 84~87%, and achieves 86~88% prefetch hit rates.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.45x、87%、88%。
- [Decoding the Skew: Distribution-Aware MoE Inference with Adaptive Kernel Dispatch](https://arxiv.org/abs/2607.23099v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Decoding the Skew: Distribution-Aware MoE Inference with Adaptive Kernel Dispatch》在 arXiv API 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，On HumanEval-X serving traces, DA-MoE improves geomean fused-MoE latency by 1.16X on DeepSeek-V3 and 1.29X on Kimi K2, with peak speedups of 1.40X and 1.56X.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.16X、1.29X、1.40X。
- [Focus Is All You Need: Adaptive Goal-aware Attention Orchestration for Multi-Agent Graph Systems](https://arxiv.org/abs/2607.23678v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Focus Is All You Need: Adaptive Goal-aware Attention Orchestration for Multi-Agent Graph Systems》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experiments across diverse multi-agent workloads show that AGAO improves task effectiveness while reducing unnecessary computation, latency, and token consumption compared with existing graph-based execution strategies.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Where Is the Cost of Third-Party API Routers in Agentic Software Development?](https://arxiv.org/abs/2607.23624v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、LLM routing，核心内容是《Where Is the Cost of Third-Party API Routers in Agentic Software Development?》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，In coding-agent workflows, high-autonomy operation is widely adopted because it reduces interaction overhead.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [SpecBox: Speculative Sandbox Scheduling for Efficient LLM Agent Serving](https://arxiv.org/abs/2607.23933v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《SpecBox: Speculative Sandbox Scheduling for Efficient LLM Agent Serving》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Evaluated on high-concurrency multi-turn agent traces, our prototype demonstrates that SpecBox cuts P99 end-to-end latency by up to $2.9\times$ relative to the on-demand sandbox baseline, while slashing peak memory consumption by $45.9\%$ compared to permanently reserved sandbox deployments.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Moral Hazard in Multi-Agent Language Models](https://arxiv.org/abs/2607.23982v1)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《Moral Hazard in Multi-Agent Language Models》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Their effects are heterogeneous: OLMo-7B shows the clearest mechanism-consistent weight-level improvement, whereas GEPA sometimes improves team success while reducing or eliminating costly queries.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [A Few Words Go a Long Way: Language Guided Robot Policy Synthesis](https://arxiv.org/abs/2607.23784v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing，核心内容是《A Few Words Go a Long Way: Language Guided Robot Policy Synthesis》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，In a benchmark evaluation on a Franka Panda robot, ARCHITECT outperforms state-of-the-art VLA models and program synthesis baselines on complex, long-horizon tasks, including articulated object manipulation and cloth folding.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Kimi K3: Open Frontier Intelligence](https://arxiv.org/abs/2607.24653v1)
  - 主题: Coding agent routing, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Coding agent routing、Heterogeneous MoE inference，核心内容是《Kimi K3: Open Frontier Intelligence》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Together with Stable LatentMoE, which effectively activates 16 of 896 routed experts per token, and refined training and data recipes, these advances yield an approximately 2.5x improvement in overall scaling efficiency over Kimi K2.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：2.5x。
- [State-dependent error correlations shape voting thresholds in committees of AI agents](https://arxiv.org/abs/2607.23931v1)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《State-dependent error correlations shape voting thresholds in committees of AI agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Modeling dependence reduced it further to 50.77, an incremental improvement of 1.73 units (95% bootstrap CI, 0.68-2.33).
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：95%、15.73%。
- [WISERouter: LLM Routing with Workload Budget Constraint](https://arxiv.org/abs/2607.23765v1)
  - 主题: LLM routing
  - 中文解读: 这项工作主要关注LLM routing，核心内容是《WISERouter: LLM Routing with Workload Budget Constraint》在 arXiv API 这一方向上的推进。聚焦大模型路由/小模型分流，直接相关。从实验上看，LLM routing exploits diversity in model capability and cost by assigning each query to a suitable model to balance utility and budget.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

