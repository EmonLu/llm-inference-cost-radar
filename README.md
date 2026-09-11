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

- 日期: 2026-09-11
- 今日新论文: 15
- 今日新权威来源更新: 1
- 本周精选论文: 25
- 本周精选权威来源更新: 6
- 日报: `papers/2026-09-11.md`
- 周报: `digests/weekly-2026-09-11.md`

## 今日最值得看

- [Phase-Decoupled, Model-Calibrated Power Control for Disaggregated LLM Serving](https://arxiv.org/abs/2609.11133v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Phase-Decoupled, Model-Calibrated Power Control for Disaggregated LLM Serving》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Deploying NVIDIA's Max-Q inference profile on a disaggregated B200 system, we found its realized gain modest (+8.6% tokens/J), model-dependent, and carrying a mean end-to-end latency cost (+5.2%) that throughput-only evaluation does not surface; the profile also applies one setting to prefill and decode GPUs that operate in opposite hardware regimes.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：200 s、8.6%、5.2%。
- [FluxMoE: Decoupling Expert Residency for High-Performance MoE Serving](https://arxiv.org/abs/2604.02715)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《FluxMoE: Decoupling Expert Residency for High-Performance MoE Serving》在 arXiv cs.LG 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，For Mixtral-8$\times$7B-Instruct on 2$\times$L40S GPUs, where weight-resident vLLM cannot fit, FluxMoE delivers 4.3$\times$ KTransformers's throughput and 29.1\% lower average TPOT.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：40S。
- [Composable CXL Memory as a Kubernetes-Native Shared Memory for LLM Serving](https://arxiv.org/abs/2609.10790)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Composable CXL Memory as a Kubernetes-Native Shared Memory for LLM Serving》在 arXiv cs.DC 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，On a two-node cluster with a 512\,GiB CXL appliance and Qwen2.5-7B-Instruct, cross-node prefix reuse reduces TTFT by 5.5$\times$--36.6$\times$ at an external hit rate of 95.4--99.5\,\%, while node-local tiers (GPU prefix caching, CPU-DRAM offload) fall back to full recompute.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [MAVEN-T: Reinforced Heterogeneous Distillation for Real-Time Multi-Agent Trajectory Prediction](https://arxiv.org/abs/2604.10169)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《MAVEN-T: Reinforced Heterogeneous Distillation for Real-Time Multi-Agent Trajectory Prediction》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experiments on NGSIM, HighD, MoCAD, Argoverse~2, and the Waymo Open Motion Dataset evaluate accuracy, efficiency, generalization, robustness, and closed-loop safety.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Optimizing AI Inference Across the Deployment Stack](https://arxiv.org/abs/2609.10550)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Optimizing AI Inference Across the Deployment Stack》在 arXiv cs.LG 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Published benchmarks often report latency and throughput under incomparable conditions, limiting their use for deployment decisions.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [OUTLETS: Output-Length Prediction from Speculative Decoding Backbones](https://arxiv.org/abs/2609.01068)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《OUTLETS: Output-Length Prediction from Speculative Decoding Backbones》在 arXiv cs.CL 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，Under saturated disaggregated serving, OUTLETS predictions enable standard scheduling policies to prioritize shorter requests and distribute requests more evenly across decoding instances, reducing short-request P99 latency by 34.8%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：34.8%。
- [ORCH: Organizational Principles Enable Collective Intelligence in Embodied AI](https://arxiv.org/abs/2609.11737v1)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《ORCH: Organizational Principles Enable Collective Intelligence in Embodied AI》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Organizations generated automatically by language models improved these measures by 43.63% and 52.53%, respectively.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：43.63%、52.53%、63.97%。
- [Modality-Decoupled Federated Learning for Privacy-Preserving Embodied Intelligence in 6G](https://arxiv.org/abs/2609.09591)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Modality-Decoupled Federated Learning for Privacy-Preserving Embodied Intelligence in 6G》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，A case study on federated robotic manipulation over the Third Generation Partnership Project (3GPP)-based wireless substrate, covering fading, co-channel interference, and malicious jamming, shows that FedMVLA achieves an 84.8% task success rate, exceeds FedAvg by 22.2 percentage points, sustains a widening margin when scaling to 128 clients across eight cells, and reduces the schedule-averaged per-client uplink model-update payload by 95.6% (approximately 96%), while keeping the 95th percentile (p95) of the round-critical uplink completion time near 1.5s.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：84.8%、95.6%、96%。
- [From Document Silos to Process Intelligence: A Multi-Layer Knowledge Graph for CMC Process Development](https://arxiv.org/abs/2609.11493v1)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference、LLM routing，核心内容是《From Document Silos to Process Intelligence: A Multi-Layer Knowledge Graph for CMC Process Development》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Tier-1 multiple-choice accuracy of 95% signals strong platform reliability; the stricter Tier-2 LLM-judge pass rate of 85%, which degrades on comparative and corpus-wide questions, reveals a failure taxonomy that Tier-1 accuracy alone fails to capture.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：95%、85%。
- [T1: Terminal Agent Reinforcement Learning for Long-Horizon Tasks](https://arxiv.org/abs/2609.11042)
  - 主题: Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference、LLM routing，核心内容是《T1: Terminal Agent Reinforcement Learning for Long-Horizon Tasks》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On Long-Horizon Terminal Bench, T1 reaches 27.9% and surpasses GPT-5.4 and GLM-5.1.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：27.9%、43.8%、64.0%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

