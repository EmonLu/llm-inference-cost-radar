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

- 日期: 2026-05-27
- 今日新论文: 15
- 今日新权威来源更新: 2
- 本周精选论文: 25
- 本周精选权威来源更新: 2
- 日报: `papers/2026-05-27.md`
- 周报: `digests/weekly-2026-05-27.md`

## 今日最值得看

- [ReMoE: Boosting Expert Reuse through Router Fine-Tuning in Memory-Constrained MoE LLM Inference](https://arxiv.org/abs/2605.27081v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《ReMoE: Boosting Expert Reuse through Router Fine-Tuning in Memory-Constrained MoE LLM Inference》在 arXiv API 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Experiments on DeepSeek and Qwen models show that ReMoE improves expert reuse by 26% while maintaining downstream task performance.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：26%、8.4%、49.8%。
- [Stateful Inference for Low-Latency Multi-Agent Tool Calling](https://arxiv.org/abs/2605.26289v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《Stateful Inference for Low-Latency Multi-Agent Tool Calling》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Multi-agent tool calling is becoming the dominant interaction pattern for LLM-based systems, yet existing inference frameworks treat each tool call as an independent request, re-processing the entire conversation from scratch even though 85-95% of the prompt is unchanged from the previous turn.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：95%。
- [Helicase: Uncertainty-Guided Supply Chain Knowledge Graph Construction with Autonomous Multi-Agent LLMs](https://arxiv.org/abs/2605.26835v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Heterogeneous MoE inference，核心内容是《Helicase: Uncertainty-Guided Supply Chain Knowledge Graph Construction with Autonomous Multi-Agent LLMs》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Its three-layer uncertainty framework tracks uncertainty at the action, trajectory, and memory layers, enabling both structural inference and calibrated confidence assessment.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [ECHO-2: A Large-Scale Distributed Rollout Framework for Cost-Efficient Reinforcement Learning](https://arxiv.org/abs/2602.02192)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《ECHO-2: A Large-Scale Distributed Rollout Framework for Cost-Efficient Reinforcement Learning》在 arXiv cs.DC 这一方向上的推进。强调异构硬件协同推理。从实验上看，Experiments on GRPO post-training of LLMs ranging from 4B to 32B parameters under real wide-area bandwidth regimes show that ECHO-2 significantly improves cost efficiency while preserving RL reward comparable to strong baselines.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：2 s。
- [MinT: Managed Infrastructure for Training and Serving Millions of LLMs](https://arxiv.org/abs/2605.13779)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《MinT: Managed Infrastructure for Training and Serving Millions of LLMs》在 arXiv cs.DC 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Scale Down moves only the exported LoRA adapter, which can be under 1% of base-model size in rank-1 settings; adapter-only handoff reduces the measured step by 18.3x on a 4B dense model and 2.85x on a 30B MoE, while concurrent multi-policy GRPO shortens wall time by 1.77x and 1.45x without raising peak memory.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1%、1 s、18.3x。
- [XGrammar-2: Efficient Dynamic Structured Generation Engine for Agentic LLMs](https://arxiv.org/abs/2601.04426)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《XGrammar-2: Efficient Dynamic Structured Generation Engine for Agentic LLMs》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experiments show that XGrammar-2 achieves over 6x faster compilation than prior structured generation engines, and incurs near-zero end-to-end overhead in modern LLM serving systems.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：6x。
- [MobileMoE: Scaling On-Device Mixture of Experts](https://arxiv.org/abs/2605.27358v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《MobileMoE: Scaling On-Device Mixture of Experts》在 arXiv API 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，Across 14 benchmarks, MobileMoE matches or exceeds leading on-device dense LLMs with 2-4$\times$ fewer inference FLOPs, and matches or surpasses the state-of-the-art MoE OLMoE-1B-7B with up to 60% fewer parameters.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：60%。
- [Dense2MoE: Pushing the Pareto Frontier of On-Device LLMs via Unified Pruning and Upcycling](https://arxiv.org/abs/2605.26496v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Dense2MoE: Pushing the Pareto Frontier of On-Device LLMs via Unified Pruning and Upcycling》在 arXiv API 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，The Mixture of Experts MoE architecture is highly promising for resource constrained on device deployments yet training these models from scratch incurs prohibitive costs Current methods attempt to alleviate this by upcycling dense models into MoEs however they often introduce parameter redundancy that degrades inference efficiency Alternatively standard layer pruning mitigates redundancy but inevitably compromises model accuracy To resolve this dilemma we propose Dense2MoE a novel framework that unifies pruning and upcycling through Layer Fusion UpCycling LF UC Guided by hardware Roofline theory Dense2MoE systematically overcomes the inference memory wall by pruning bandwidth heavy attention modules from redundant layers while repurposing their Multi Layer Perceptrons MLPs into MoE experts This structural innovation preserves the models core capabilities and strictly limits active parameters via selective token routing With a modest continual pre training budget Dense2MoE efficiently converts publicly available dense LLMs into on device ready MoE models Extensive experiments demonstrate that Dense2MoE significantly advances the Pareto frontier for on device inference latency versus model accuracy outperforming dense baselines state of the art compression and standard upcycling methods
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [BioFact-MoE: Biologically Factorized Mixture of Experts for Vision-Language Prognostic Modeling in Hepatocellular Carcinoma](https://arxiv.org/abs/2605.26376)
  - 主题: Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference，核心内容是《BioFact-MoE: Biologically Factorized Mixture of Experts for Vision-Language Prognostic Modeling in Hepatocellular Carcinoma》在 arXiv cs.LG 这一方向上的推进。强调异构硬件协同推理。从实验上看，On a HCC cohort of N=588 patients (pretrained on 4,582 3D MRI image-report pairs), BioFact-MoE consistently improves survival prediction over all baselines across time horizons, achieving 12-, 18-, and 24-month AUCs of 75.33%, 75.85%, and 73.96%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：75.33%、75.85%、73.96%。
- [Agentic AI Workload Characteristics](https://arxiv.org/abs/2605.26297v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《Agentic AI Workload Characteristics》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，These results show that efficient agentic serving must jointly manage repeated model re-entry, persistent context state, and workload-dependent tool behavior.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

