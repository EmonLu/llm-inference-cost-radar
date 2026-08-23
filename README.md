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

- 日期: 2026-08-23
- 今日新论文: 8
- 今日新权威来源更新: 2
- 本周精选论文: 25
- 本周精选权威来源更新: 3
- 日报: `papers/2026-08-23.md`
- 周报: `digests/weekly-2026-08-23.md`

## 今日最值得看

- [FlashPrefill V2: Block-Sparse Prefill Attention for Long-Context LLM Serving](https://arxiv.org/abs/2608.19758v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《FlashPrefill V2: Block-Sparse Prefill Attention for Long-Context LLM Serving》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Extensive evaluations on NVIDIA H20 GPUs---among the most widely deployed inference accelerators---demonstrate that FlashPrefill V2 delivers up to 47.26x and 27.19x speedups over FlashAttention-2 at 128K context length under FP8 and BF16 precision, respectively, and, in FP8, still achieves a 30.49x speedup against an FA3/4-aligned dense baseline.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：47.26x、27.19x、30.49x。
- [ReCache: Efficient KV Cache Reuse and Compression for Tool-Augmented LLM Agents](https://arxiv.org/abs/2608.19662v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《ReCache: Efficient KV Cache Reuse and Compression for Tool-Augmented LLM Agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The complete framework reduces allocated KV-tensor memory by 92.43\% and accelerates attention by 1.423$\times$.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Pandora's AI Model Routing Box: Efficient Allocation with Costly Value Estimation](https://arxiv.org/abs/2608.20316v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Pandora's AI Model Routing Box: Efficient Allocation with Costly Value Estimation》在 arXiv API 这一方向上的推进。强调异构硬件协同推理。从实验上看，Experiments across three domains---a standard multi-LLM benchmark, retrieval-augmented specialists, and LLMs with variable inference-time reasoning---show that Pandora's Router matches the routing quality of exhaustive estimation, while querying the expensive estimator far less often.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [OrthoSkillVLA: Continual Skill Learning via Gradient-Informed Skill Subspace Adaptation](https://arxiv.org/abs/2608.19589v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《OrthoSkillVLA: Continual Skill Learning via Gradient-Informed Skill Subspace Adaptation》在 arXiv API 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，Extensive simulated and real-world evaluations, together with ablations, demonstrate that OrthoSkillVLA better preserves prior skills while acquiring new ones.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Reward-Guided Autoregressive Graph Generation for Efficient Multi-Agent Communication Topology Design](https://arxiv.org/abs/2608.20099v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《Reward-Guided Autoregressive Graph Generation for Efficient Multi-Agent Communication Topology Design》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Our method preserves task accuracy at the level of ARG-Designer while reducing token consumption by an average of 20.5%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：20.5%。
- [Multi-Agent Orchestration with the Common-Sense Reasoning Capabilities of LLMs for Autonomous Driving](https://arxiv.org/abs/2608.20129v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《Multi-Agent Orchestration with the Common-Sense Reasoning Capabilities of LLMs for Autonomous Driving》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The results demonstrate the potential of integrating LLM-based reasoning with conventional autonomous driving methods while retaining structured control and safety mechanism.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Credit Without Ground Truth: Auditing Step-Level Credit Assignment in LLM Agents Against Executed Replay](https://arxiv.org/abs/2608.19760v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、LLM routing，核心内容是《Credit Without Ground Truth: Auditing Step-Level Credit Assignment in LLM Agents Against Executed Replay》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，A confidence-only router recovers pivotal steps at chance level, but cuts judge cost by 13.1% per turn (14.0% per trajectory).
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：13.1%、14.0%、26.8%。
- [Optimal Skill Selection for LLM Agents with Provable Bicriteria Guarantees](https://arxiv.org/abs/2608.19993v1)
  - 主题: Agent systems and multi-agent efficiency, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、LLM routing，核心内容是《Optimal Skill Selection for LLM Agents with Provable Bicriteria Guarantees》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On a contamination-controlled BigCodeBench variant, BPS outperforms all the baselines, reaching $0.73$ measured task success versus $0.20$--$0.52$ for released skill routers, text retrievers, and the executor's own selection, on $28\%$ fewer tokens than the strongest released router.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Exploring Speculative Decoding in vLLM on AMD GPUs](https://vllm.ai/blog/2026-08-23-speculative-decoding-amd-gpus)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Exploring Speculative Decoding in vLLM on AMD GPUs》在 vLLM Blog 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，A practical guide to speculative decoding in vLLM on AMD GPUs, covering draft-and-verify mechanics, MTP, EAGLE-3, DFlash, DSpark, configuration, tuning, and benchmark results.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [IsoExec: Unified Execution to Eliminate Trainer-Inference Mismatch in SkyRL](https://vllm.ai/blog/2026-08-21-isoexec)
  - 主题: 
  - 中文解读: 这项工作主要关注大模型推理效率优化，核心内容是《IsoExec: Unified Execution to Eliminate Trainer-Inference Mismatch in SkyRL》在 vLLM Blog 这一方向上的推进。来自 vLLM 官方生态，通常代表推理引擎的一线工程实践。从实验上看，IsoExec unifies numerical execution across SkyRL's vLLM and Megatron runtimes, reducing the average rollout-versus-training logprob difference below 1e-6 on Qwen3.5-35B-A3B with 25% overhead.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：25%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

