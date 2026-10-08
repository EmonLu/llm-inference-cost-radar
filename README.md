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

- 日期: 2026-10-08
- 今日新论文: 15
- 今日新权威来源更新: 1
- 本周精选论文: 25
- 本周精选权威来源更新: 4
- 日报: `papers/2026-10-08.md`
- 周报: `digests/weekly-2026-10-08.md`

## 今日最值得看

- [Cost-Efficient Theorem Proving via Agent Orchestration in Program Verification](https://arxiv.org/abs/2610.09681v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《Cost-Efficient Theorem Proving via Agent Orchestration in Program Verification》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On five program verification benchmarks in Lean 4 including function-level CLEVER, VERINA, and AlgoVeri, and repository-level NTP4VC and Vero, we show that CoCo-Prover achieves a better success-vs-cost frontier than baselines including frontier coding agents and state-of-the-art LLM-based provers: it achieves the best solve rate on every benchmark and up to 100% on two benchmarks.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：100%、30.9%。
- [vLLM-Omni Technical Report: A Unified Serving Runtime for Omni-Modality Generation](https://arxiv.org/abs/2610.09307)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《vLLM-Omni Technical Report: A Unified Serving Runtime for Omni-Modality Generation》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，This report covers the architecture (stage-level KV paths, replica pools, multi-hardware platforms, and efficiency stack) and OpenAI-compatible and OpenPI APIs for omni, TTS, image/video, world-model, robot, and duplex workloads.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [SPIN: Shadow Predictive Indexer for Sparse Attention](https://arxiv.org/abs/2610.09025)
  - 主题: Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference，核心内容是《SPIN: Shadow Predictive Indexer for Sparse Attention》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，In end-to-end vLLM serving, SPIN improves output throughput by up to 14.9% and reduces median inter-token latency by up to 13.2%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：14.9%、13.2%、40%。
- [Democratizing MoE inference on commodity GPUs with CoMoE](https://arxiv.org/abs/2610.09424)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Democratizing MoE inference on commodity GPUs with CoMoE》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Evaluation on RTX 5090 GPUs shows that CoMoE improves inference throughput by up to 1.46x, approaching the performance of NVLink-capable A800 GPUs at only 23.4% of the hardware cost.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.46x、23.4%。
- [Large Language Model Orchestration under Heterogeneous Preferences via Explicit Persona Inference](https://arxiv.org/abs/2610.07587v2)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Large Language Model Orchestration under Heterogeneous Preferences via Explicit Persona Inference》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Empirical results on three substrates, ranging from payoffs the preferences fully determine, through payoffs that depend on more than them, to scales where explicit joint inference is infeasible, demonstrate that HARP\textsuperscript{+} is the strongest non-oracle method across the class our theory identifies.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [FedGuide: Diffusion Prior Alignment and Value Baseline Guidance for Heterogeneous Federated Reinforcement Learning](https://arxiv.org/abs/2609.18964)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《FedGuide: Diffusion Prior Alignment and Value Baseline Guidance for Heterogeneous Federated Reinforcement Learning》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experiments across heterogeneous environments show that FedGuide outperforms representative FRL methods in client-average returns, final-round performance, and worst-round robustness, while maintaining stable learning under stronger heterogeneity.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Shared Low-rank Basis Factorization for Data-free Mixture-of-Experts Compression](https://arxiv.org/abs/2610.09342)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Shared Low-rank Basis Factorization for Data-free Mixture-of-Experts Compression》在 arXiv cs.LG 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，Across five MoE architectures spanning 16B to 122B parameters, SLBF consistently outperforms methods from all three compression families.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Agentic AI-Assisted Modeling for Production Scheduling: Assessment in Constraint Programming](https://arxiv.org/abs/2610.10184v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Agentic AI-Assisted Modeling for Production Scheduling: Assessment in Constraint Programming》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The multi-agent workflow raises the share of scripts that run correctly as generated from 14.8% with a direct LLM call to 59.3%, reaching 80.6% on the four less complex problems, while tightly coupled intralogistics models remain an open challenge.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：14.8%、59.3%、80.6%。
- [Expert Coupling in MoE Pretraining: Reducing All-to-All Overhead with Correlated Placement and Token Shuffling](https://arxiv.org/abs/2610.09372)
  - 主题: Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference、LLM routing，核心内容是《Expert Coupling in MoE Pretraining: Reducing All-to-All Overhead with Correlated Placement and Token Shuffling》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，On a cluster with 8 AMD Instinct MI300X GPUs per node, these collectives can take 45% of the training step at EP32 with top-2 routing and 60% with top-6 routing.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：300X、45%、60%。
- [Humanize: Judgement Engineering for Agentic Coding](https://arxiv.org/abs/2610.08900v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing，核心内容是《Humanize: Judgement Engineering for Agentic Coding》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Agentic coding makes code generation cheap, but reliable completion remains difficult: the agent that writes the code is a weak judge of whether it is done.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

