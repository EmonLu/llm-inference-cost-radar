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

- [ReaLB: Real-Time Load Balancing for Multimodal MoE Inference](https://arxiv.org/abs/2604.19503)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《ReaLB: Real-Time Load Balancing for Multimodal MoE Inference》在 arXiv cs.DC 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，Experiments on representative MMoE models show that ReaLB achieves 1.10$\times$-1.32$\times$ end-to-end speedup while limiting average accuracy degradation to within 1%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1%。
- [PRISM: Fast Online LLM Serving via Scheduling-Memory Co-design](https://arxiv.org/abs/2605.08581)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《PRISM: Fast Online LLM Serving via Scheduling-Memory Co-design》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Our evaluation results show that, versus the strongest baseline, PRISM reduces average per-QPS P99 TTFT by 23.3\% and 37.1\% while increasing exact-prefix KV-cache hit rate by 5.9 and 12.2 percentage points on 4B and 13B models, respectively.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Iterative Critique-and-Routing Controller for Multi-Agent Systems with Heterogeneous LLMs](https://arxiv.org/abs/2605.08686)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference、LLM routing，核心内容是《Iterative Critique-and-Routing Controller for Multi-Agent Systems with Heterogeneous LLMs》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Extensive experiments across multiple heterogeneous multi-agent systems and seven reasoning benchmarks show that our method consistently outperforms state-of-the-art baselines and substantially narrows the gap to the strongest agent, while using it for fewer than 25% of total calls.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：25%。
- [Expert Upcycling: Shifting the Compute-Efficient Frontier of Mixture-of-Experts](https://arxiv.org/abs/2604.19835)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Expert Upcycling: Shifting the Compute-Efficient Frontier of Mixture-of-Experts》在 arXiv cs.LG 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，In our 7B-13B total parameter experiments, the upcycled model matches the fixed-size baseline on validation loss while saving 32% of GPU hours.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：32%。
- [KV-RM: Regularizing KV-Cache Movement for Static-Graph LLM Serving](https://arxiv.org/abs/2605.09735)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《KV-RM: Regularizing KV-Cache Movement for Static-Graph LLM Serving》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，On a 2-GPU NVIDIA A100 node, KV-RM improves mixed-length decoding throughput and tail latency relative to a static-graph baseline, reduces reserved KV memory across workload families, and removes severe burst-time latency spikes under production-trace replay.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Large Language Models over Networks: Collaborative Intelligence under Resource Constraints](https://arxiv.org/abs/2605.08626)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Large Language Models over Networks: Collaborative Intelligence under Resource Constraints》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Such collaboration strives for superior response quality under heterogeneous resource constraints spanning computation, memory, communication, and cost across network tiers.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Not All Thoughts Need HBM: Semantics-Aware Memory Hierarchy for LLM Reasoning](https://arxiv.org/abs/2605.09490)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Not All Thoughts Need HBM: Semantics-Aware Memory Hierarchy for LLM Reasoning》在 arXiv cs.CL 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，A head-to-head reproduction of R-KV -- the current SOTA eviction method -- on our setup achieves only 0-32% at comparable budgets.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：32%、7%、48 GB。
- [HiRL: Hierarchical Reinforcement Learning for Coordinated Resource Management in Heterogeneous Edge Computing](https://arxiv.org/abs/2605.10443)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《HiRL: Hierarchical Reinforcement Learning for Coordinated Resource Management in Heterogeneous Edge Computing》在 arXiv cs.DC 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Experimental results show that HiRL achieves effective latency-energy trade-offs with 28% latency reduction compared to Single-DDQN and maintains nearly 100% task completion rates under all load conditions.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：28%、100%、51%。
- [Accelerating Compound LLM Training Workloads with Maestro](https://arxiv.org/abs/2605.10501)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Accelerating Compound LLM Training Workloads with Maestro》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Deployed in production for millions of GPU hours, Maestro reduces GPU consumption by ~40% on key workloads-including knowledge distillation and MLLM training-validating its real-world impact.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：40%。
- [EnergyLens: Interpretable Closed-Form Energy Models for Multimodal LLM Inference Serving](https://arxiv.org/abs/2605.10556v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《EnergyLens: Interpretable Closed-Form Energy Models for Multimodal LLM Inference Serving》在 arXiv API 这一方向上的推进。强调异构硬件协同推理。从实验上看，Fitted from as few as 50 profiling measurements, EnergyLens achieves 88.2% Top-1 configuration selection accuracy across many evaluation scenarios compared to 60.9% for the closest prior analytical baseline, matches the predictive accuracy of ensemble ML methods with 10x fewer profiling samples, and extrapolates reliably to unseen batch sizes and hardware platforms without structural modification, making it a practical, interpretable tool for energy-optimal LLM deployment.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：88.2%、60.9%、10x。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

