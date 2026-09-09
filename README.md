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

- 日期: 2026-09-09
- 今日新论文: 15
- 今日新权威来源更新: 1
- 本周精选论文: 25
- 本周精选权威来源更新: 5
- 日报: `papers/2026-09-09.md`
- 周报: `digests/weekly-2026-09-09.md`

## 今日最值得看

- [Typed Federated Artifacts for the Agentic Web:Sharing Tool-Routing Knowledge Across Frozen,Heterogeneous LLM Agents](https://arxiv.org/abs/2609.06815v1)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference、LLM routing，核心内容是《Typed Federated Artifacts for the Agentic Web:Sharing Tool-Routing Knowledge Across Frozen,Heterogeneous LLM Agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The same experience merged and shown to the router as typed fields rather than one flat string is worth 8.5 points on clean data and 7.4 under 60% injected contradiction.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：60%。
- [BIO-MEMART: Biometric-Aware KV Cache Memory for Multi-User LLM Agents](https://arxiv.org/abs/2609.08566v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《BIO-MEMART: Biometric-Aware KV Cache Memory for Multi-User LLM Agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across face benchmarks, the average owner and non-owner biometric success rates are 95.71% and 0.86%; across palmprint benchmarks, they are 97.60% and 2.00%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：95.71%、0.86%、97.60%。
- [Unified AI Gateway: A Framework for Joint Model Routing and KV Cache Management](https://arxiv.org/abs/2609.06940v1)
  - 主题: Cost-efficient LLM inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、LLM routing，核心内容是《Unified AI Gateway: A Framework for Joint Model Routing and KV Cache Management》在 arXiv API 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，At request time, the gateway jointly selects a target model, an execution site, and a KV cache action under task-quality, latency, cost, and resource constraints.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [HDA-MoE: Hybrid Parallelism and Dynamic, Adaptive Scheduling for Mixture-of-Experts with 3D Near-Memory Processing](https://arxiv.org/abs/2609.08682v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《HDA-MoE: Hybrid Parallelism and Dynamic, Adaptive Scheduling for Mixture-of-Experts with 3D Near-Memory Processing》在 arXiv API 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，Experimental results show that HDA-MoE achieves a speedup of 1.1x--3.4x over TP, 1.1x--1.5x over EP, 1.1x--3.7x over the Hybrid TP-EP compute-balanced baseline, and 1.1x--1.3x over HD-MoE.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.1x、3.4x。
- [A Measurement Study of LLM Inference Trade-offs Across Edge Continuum Hardware](https://arxiv.org/abs/2609.08307v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《A Measurement Study of LLM Inference Trade-offs Across Edge Continuum Hardware》在 arXiv API 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，We evaluate multiple open-weight LLMs and quantization variants using a fixed question-answering workload, and compare them against GPT-4o as a cloud-hosted accuracy and latency reference.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [HoneyRoute: Honeypot-Model Routing for Adversarial LLM Serving](https://arxiv.org/abs/2609.08306v1)
  - 主题: Cost-efficient LLM inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、LLM routing，核心内容是《HoneyRoute: Honeypot-Model Routing for Adversarial LLM Serving》在 arXiv API 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，On a production trace plus a seven-domain attack corpus, the router reaches F1=.911 at 38 ms median added latency, matching 96% of a two-tier guard-LLM cascade's F1 at 1/385 of its latency with 0% evasion under 13 adversarial transformations; diverting the malicious share cuts production-model token consumption under concurrent flooding with real GCG-suffix payloads by 97.8%; the trained replica agrees with the production model on 92.9% of benign holdout requests, while naive unconditional bait injection collapses to 7.6% and selective camouflaged injection recovers to 88.9%, mapping the recoverable fidelity-traceability frontier; and a loop-trained correction head cuts misrouting of legitimate security research 9x while raising detection F1 to .933.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：38 ms、96%、0%。
- [Detokenization Leaks: Reconstructing Local LLM Outputs From Cache Traces](https://arxiv.org/abs/2609.06674v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Detokenization Leaks: Reconstructing Local LLM Outputs From Cache Traces》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Unlike prior attacks that rely on deployment-specific assumptions, such as shared data memory, CPU offloading, or Mixture-of-Experts architectures, our approach targets the detokenizer, a component used in default LLM inference pipelines.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [PhysMAS: Physics-Grounded Multi-Agent Synthesis of Compositional 4D Gaussians](https://arxiv.org/abs/2609.07174v1)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《PhysMAS: Physics-Grounded Multi-Agent Synthesis of Compositional 4D Gaussians》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Extensive experiments demonstrate that, compared with recent physics-based 4D Gaussian baselines that rely on SDS, PhysMAS achieves better semantic alignment and perceived physical plausibility while requiring less runtime.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [MoEMB: Scaling Universal Multimodal Embeddings with Efficient Mixture-of-Experts Models](https://arxiv.org/abs/2609.08663v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《MoEMB: Scaling Universal Multimodal Embeddings with Efficient Mixture-of-Experts Models》在 arXiv API 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，Through a systematic study of the design space and training recipes for MoE-based UME, MoEMB sets a new state of the art on both MMEB-V2 and MRMR among models trained on public MMEB-family data: with only 3B active parameters, MoEMB surpasses TTE-based methods with >4x active parameters, using significantly less computes.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：4x。
- [FrogNano: Training a 4B Coding Agent via Online Task Synthesis](https://arxiv.org/abs/2609.07925v1)
  - 主题: Coding agent routing, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Coding agent routing、Cost-efficient LLM inference，核心内容是《FrogNano: Training a 4B Coding Agent via Online Task Synthesis》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，We report details on the training methodology, evaluations across diverse environments, and in-depth analyses, serving as a foundation for our ongoing exploration of lightweight yet capable coding agents that can run on minimal hardware.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

