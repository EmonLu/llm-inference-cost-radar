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

- 日期: 2026-06-27
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 2
- 日报: `papers/2026-06-27.md`
- 周报: `digests/weekly-2026-06-27.md`

## 今日最值得看

- [Experience Compression Spectrum: Unifying Memory, Skills, and Rules in LLM Agents](https://arxiv.org/abs/2604.15877)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《Experience Compression Spectrum: Unifying Memory, Skills, and Rules in LLM Agents》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Agent memory systems and agent skill discovery both address this challenge, extracting reusable knowledge from interaction traces, yet a citation analysis of 1{,}136 references across 22 primary papers reveals a cross-community citation rate below 1\%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Adaptive Utility driven Resource Orchestration for Resilient AI (AURORA-AI)](https://arxiv.org/abs/2606.27005)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Adaptive Utility driven Resource Orchestration for Resilient AI (AURORA-AI)》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The framework is evaluated in a stress-rich discrete-time simulation that concurrently injects demographic bias shocks, gradual concept drift, and abrupt black-swan disruptions, and is compared against five established controllers including Static, Round Robin, Greedy, LinUCB, and a deep reinforcement-learning agent based on Proximal Policy Optimisation.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Latent-Mark: An Audio Watermark Robust to Neural Codec Compression](https://arxiv.org/abs/2603.05310)
  - 主题: Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference，核心内容是《Latent-Mark: An Audio Watermark Robust to Neural Codec Compression》在 arXiv cs.AI 这一方向上的推进。通过量化降低部署成本或加速推理。从实验上看，Extensive evaluations demonstrate robust zero-shot transferability to unseen neural codecs, achieving competitive resilience against traditional DSP attacks while preserving perceptual imperceptibility.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [NOVA: A Verification-Aware Agent Harness for Architecture Evolution in Industrial Recommender Systems](https://arxiv.org/abs/2606.27243v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、LLM routing，核心内容是《NOVA: A Verification-Aware Agent Harness for Architecture Evolution in Industrial Recommender Systems》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Deployed in an industrial advertising system, NOVA achieves the highest effective pass rate on L2 ScaleUp and L3 Literature-to-Production tasks (54.5% and 60.0%), reduces silent failures compared with coding-agent baselines, and shortens one literature-to-production cycle by over 13x in human-attended time.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：2 S、54.5%、60.0%。
- [SpaceRipple: Lightweight Semantic Delivery for Mission-Oriented LEO Earth Observation Satellite Networks](https://arxiv.org/abs/2606.26559)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《SpaceRipple: Lightweight Semantic Delivery for Mission-Oriented LEO Earth Observation Satellite Networks》在 arXiv cs.AI 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，Experimental results show that SpaceRipple achieves favorable reconstruction quality, improved semantic detection performance, and substantial bandwidth savings, demonstrating its potential for efficient and reliable Earth observation under constrained satellite-network resources.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [CAT-Q: Cost-efficient and Accurate Ternary Quantization for LLMs](https://arxiv.org/abs/2606.26650)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《CAT-Q: Cost-efficient and Accurate Ternary Quantization for LLMs》在 arXiv cs.AI 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，We show that, for pre-trained LLMs with 1.7B to 8B parameters, CAT-Q can efficiently quantize them into ternary models using only 512 calibration samples, while achieving superior performance than the seminal BitNet 1.58-bit v1 and v2 families (with 1.3B to 7B parameters) trained with 100B tokens, yielding about a 100,000X reduction in training tokens.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：000X、80GB。
- [How Do Tool-Augmented LLM Agents Perform on Real-World Energy Analytics Tasks?](https://arxiv.org/abs/2606.26346v1)
  - 主题: Agent systems and multi-agent efficiency, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、LLM routing，核心内容是《How Do Tool-Augmented LLM Agents Perform on Real-World Energy Analytics Tasks?》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Agentic benchmarks have emerged across general-purpose and domain-specific settings, including finance, coding, law, and drug discovery, yet energy-domain evaluations remain largely limited to static knowledge recall.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [MedPruner: Training-Free Hierarchical Token Pruning for Efficient 3D Medical Image Understanding in Vision-Language Models](https://arxiv.org/abs/2603.11625)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《MedPruner: Training-Free Hierarchical Token Pruning for Efficient 3D Medical Image Understanding in Vision-Language Models》在 arXiv cs.AI 这一方向上的推进。强调异构硬件协同推理。从实验上看，Extensive experiments on three 3D medical benchmarks and across three diverse medical VLMs reveal massive token redundancy in existing architectures.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [The Spec Growth Engine: Spec-Anchored, Code-Coupled, Drift-Enforced Architecture for AI-Assisted Software Development](https://arxiv.org/abs/2606.27045v1)
  - 主题: Coding agent routing
  - 中文解读: 这项工作主要关注Coding agent routing，核心内容是《The Spec Growth Engine: Spec-Anchored, Code-Coupled, Drift-Enforced Architecture for AI-Assisted Software Development》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，AI coding agents dramatically accelerate implementation speed but introduce two structural failure modes that existing spec-driven approaches do not fully solve: (1) context explosion -- the agent must reason over an entire repository at once, degrading output quality as the context window fills; and (2) silent spec-code drift -- code evolves, the specification does not, and the divergence becomes invisible until it is costly to repair.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Semantic Early-Stopping for Iterative LLM Agent Loops](https://arxiv.org/abs/2606.27009v1)
  - 主题: Agent systems and multi-agent efficiency
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency，核心内容是《Semantic Early-Stopping for Iterative LLM Agent Loops》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On the 60-question test split, a judge-free semantic stopper reduces operational tokens by 38% relative to max_iterations at parity quality (Delta-IS = -0.004, p = 0.81), whereas the full quality-gated variant is counter-productive because its per-round judging dominates cost.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：38%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

