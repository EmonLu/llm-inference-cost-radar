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

- 日期: 2026-06-18
- 今日新论文: 15
- 今日新权威来源更新: 2
- 本周精选论文: 25
- 本周精选权威来源更新: 4
- 日报: `papers/2026-06-18.md`
- 周报: `digests/weekly-2026-06-18.md`

## 今日最值得看

- [Towards Scalable Customization and Deployment of Multi-Agent Systems for Enterprise Applications](https://arxiv.org/abs/2606.18502v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《Towards Scalable Customization and Deployment of Multi-Agent Systems for Enterprise Applications》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across enterprise workloads, our framework enables rapid domain adaptation and achieves a 4.48x speedup in throughput while maintaining performance and improving robustness on long-tail scenarios.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：4.48x。
- [TurboServe: Serving Streaming Video Generation Efficiently and Economically](https://arxiv.org/abs/2606.19271)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《TurboServe: Serving Streaming Video Generation Efficiently and Economically》在 arXiv cs.DC 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Compared with baseline serving configurations, TurboServe reduces worst-case per-chunk latency by 37.5% and total GPU operating cost by 37.2% on average.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：37.5%、37.2%。
- [ShuntServe: Cost-Efficient LLM Serving on Heterogeneous Spot GPU Clusters](https://arxiv.org/abs/2606.18600)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《ShuntServe: Cost-Efficient LLM Serving on Heterogeneous Spot GPU Clusters》在 arXiv cs.DC 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Evaluation on Llama-3.1-70B and Qwen3-32B with a heterogeneous AWS cluster of L4, A10G, and L40S GPUs shows that ShuntServe achieves 1.42x and 1.35x higher throughput than state-of-the-art baselines and attains 31.9% and 31.2% cost efficiency improvements over on-demand instances for offline and online serving, respectively.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：40S、1.42x、1.35x。
- [Multi-Agent Systems are Mixtures of Experts: Who Becomes an Influencer?](https://arxiv.org/abs/2605.25929)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference、LLM routing，核心内容是《Multi-Agent Systems are Mixtures of Experts: Who Becomes an Influencer?》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，This perspective implies that multi-agent systems can outperform single agents and static ensembles when routing reflects agent competence.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [JetFlow: Breaking the Scaling Ceiling of Speculative Decoding with Parallel Tree Drafting](https://arxiv.org/abs/2606.18394)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《JetFlow: Breaking the Scaling Ceiling of Speculative Decoding with Parallel Tree Drafting》在 arXiv cs.CL 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，On H100 GPUs, JetFlow achieves up to 9.64x speedup on MATH-500 and 4.58x on open-ended conversational workloads, with further latency gains demonstrated through vLLM integration under realistic serving loads.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：9.64x、4.58x。
- [OmniPlan: An Adaptive Framework for Timely and Near-Optimal Network Planning Optimization](https://arxiv.org/abs/2606.18105v2)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《OmniPlan: An Adaptive Framework for Timely and Near-Optimal Network Planning Optimization》在 arXiv API 这一方向上的推进。强调异构硬件协同推理。从实验上看，Our experiments on a real-world testbed indicate that OmniPlan achieves near-optimal and low-execution-time offloading for real-world ML inference tasks, reducing latency by up to 97.8\% and network device resource consumption by up to 11.5\%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Beyond Prediction: Tail-Aware Scheduling for LLM Inference](https://arxiv.org/abs/2606.18431)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Beyond Prediction: Tail-Aware Scheduling for LLM Inference》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Evaluated on production and open-source traces, our method reduces P99 TTLT by up to 35-50% relative to SRPT with perfect length knowledge and reduces TTFT by 34-47% across workloads, including reasoning-heavy and chat-heavy tasks.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：50%、47%。
- [Do as the Romans Do: Learning Universal Behaviors from Heterogeneous Agents](https://arxiv.org/abs/2606.18537)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Do as the Romans Do: Learning Universal Behaviors from Heterogeneous Agents》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experiments across a synthetic basis function decomposition, multi-agent Craftax, and a continuous autonomous driving simulator (Highway-Env) confirm that GRID successfully disentangles reward structure in a semantically meaningful way, outperforms standard learning from demonstration baselines, and enables more efficient and stable specialization.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [EfficientRollout: System-Aware Self-Speculative Decoding for RL Rollouts](https://arxiv.org/abs/2606.18967v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《EfficientRollout: System-Aware Self-Speculative Decoding for RL Rollouts》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，EfficientRollout reduces rollout and end-to-end latency by up to 19.6% and 12.7%, respectively, over an accelerated AR rollout baseline, while preserving final model quality.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：19.6%、12.7%。
- [Decoupling Search from Reasoning: A Vendor-Agnostic Grounding Architecture for LLM Agents](https://arxiv.org/abs/2606.18947v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、LLM routing，核心内容是《Decoupling Search from Reasoning: A Vendor-Agnostic Grounding Architecture for LLM Agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，87.7%) at 91% lower search cost, preserves concise answer contracts, and reaches a 99.4% warm-cache hit rate with 68% lower latency.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：87.7%、91%、99.4%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

