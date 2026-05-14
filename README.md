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

- 日期: 2026-05-14
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 3
- 日报: `papers/2026-05-14.md`
- 周报: `digests/weekly-2026-05-14.md`

## 今日最值得看

- [KVServe: Service-Aware KV Cache Compression for Communication-Efficient Disaggregated LLM Serving](https://arxiv.org/abs/2605.13734)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《KVServe: Service-Aware KV Cache Compression for Communication-Efficient Disaggregated LLM Serving》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Integrated into vLLM and evaluated across datasets, models, GPUs and networks, KVServe achieves up to $9.13\times$ JCT speedup in PD-separated serving and up to $32.8\times$ TTFT reduction in KV-disaggregated serving.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [MinT: Managed Infrastructure for Training and Serving Millions of LLMs](https://arxiv.org/abs/2605.13779)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《MinT: Managed Infrastructure for Training and Serving Millions of LLMs》在 arXiv cs.DC 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Scale Down moves only the exported LoRA adapter, which can be under 1% of base-model size in rank-1 settings; adapter-only handoff reduces the measured step by 18.3x on a 4B dense model and 2.85x on a 30B MoE, while concurrent multi-policy GRPO shortens wall time by 1.77x and 1.45x without raising peak memory.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1%、1 s、18.3x。
- [MultiPath Memory Access: Breaking Host-GPU Bandwidth Bottlenecks in LLM Services](https://arxiv.org/abs/2512.16056)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《MultiPath Memory Access: Breaking Host-GPU Bandwidth Bottlenecks in LLM Services》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，On an 8-GPU NVIDIA H20 server, MMA achieves 245 GB/s peak host-to-GPU bandwidth, a 4.62x improvement over native CUDA copies, and reduces TTFT for KV cache fetching by 1.14-2.38x and model wake-up/switching latency by 1.12-2.48x.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：20 s、245 GB、4.62x。
- [REAP the Experts: Why Pruning Prevails for One-Shot MoE compression](https://arxiv.org/abs/2510.13999)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《REAP the Experts: Why Pruning Prevails for One-Shot MoE compression》在 arXiv cs.LG 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，Across a diverse set of SMoE models ranging from 20B to 1T parameters, REAP consistently outperforms merging and other pruning methods on generative benchmarks, especially at 50% compression.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：50%。
- [An Agentic AI Framework with Large Language Models and Chain-of-Thought for UAV-Assisted Logistics Scheduling with Mobile Edge Computing](https://arxiv.org/abs/2605.13221v1)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference、LLM routing，核心内容是《An Agentic AI Framework with Large Language Models and Chain-of-Thought for UAV-Assisted Logistics Scheduling with Mobile Edge Computing》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Simulation results show that the proposed framework yields more consistent formulations, while the hierarchical PPO achieves full product collection in 99.6% of the last 500 episodes and maintains a 100% deadline satisfaction rate, with more stable performance than the advantage actor-critic approach.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：99.6%、100%。
- [EnergyLens: Interpretable Closed-Form Energy Models for Multimodal LLM Inference Serving](https://arxiv.org/abs/2605.10556v2)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《EnergyLens: Interpretable Closed-Form Energy Models for Multimodal LLM Inference Serving》在 arXiv API 这一方向上的推进。强调异构硬件协同推理。从实验上看，Fitted from as few as 50 profiling measurements, EnergyLens achieves 88.2% Top-1 configuration selection accuracy across many evaluation scenarios compared to 60.9% for the closest prior analytical baseline, matches the predictive accuracy of ensemble ML methods with 10x fewer profiling samples, and extrapolates reliably to unseen batch sizes and hardware platforms without structural modification, making it a practical, interpretable tool for energy-optimal LLM deployment.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：88.2%、60.9%、10x。
- [AB-Sparse: Sparse Attention with Adaptive Block Size for Accurate and Efficient Long-Context Inference](https://arxiv.org/abs/2605.12110v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《AB-Sparse: Sparse Attention with Adaptive Block Size for Accurate and Efficient Long-Context Inference》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Evaluation results demonstrate that AB-Sparse achieves an accuracy improvement of up to 5.43% over existing block sparse attention baselines without throughput overhead.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：5.43%。
- [PipeSD: An Efficient Cloud-Edge Collaborative Pipeline Inference Framework with Speculative Decoding](https://arxiv.org/abs/2605.13319)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《PipeSD: An Efficient Cloud-Edge Collaborative Pipeline Inference Framework with Speculative Decoding》在 arXiv cs.DC 这一方向上的推进。涉及 KV/参数/专家的卸载策略，可节约显存或成本。从实验上看，Results show that PipeSD consistently outperforms state-of-the-art baselines, achieving 1.16x-2.16x speedup and reducing energy consumption by 14.3%-25.3%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.16x、2.16x、14.3%。
- [Slicing and Dicing: Configuring Optimal Mixtures of Experts](https://arxiv.org/abs/2605.11689)
  - 主题: Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference、LLM routing，核心内容是《Slicing and Dicing: Configuring Optimal Mixtures of Experts》在 arXiv cs.CL 这一方向上的推进。强调异构硬件协同推理。从实验上看，Overall, our results suggest a simpler recipe: focus on expert count and granularity, other choices have minimal effect on final quality.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Beyond Inefficiency: Systemic Costs of Incivility in Multi-Agent Monte Carlo Simulations](https://arxiv.org/abs/2605.11789v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《Beyond Inefficiency: Systemic Costs of Incivility in Multi-Agent Monte Carlo Simulations》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The convergence latency of 25% reported in the previous study was confirmed.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：25%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

