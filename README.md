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

- 日期: 2026-06-05
- 今日新论文: 15
- 今日新权威来源更新: 1
- 本周精选论文: 25
- 本周精选权威来源更新: 7
- 日报: `papers/2026-06-05.md`
- 周报: `digests/weekly-2026-06-05.md`

## 今日最值得看

- [Large-Scale LLM Inference with Heterogeneous Workloads: Prefill-Decode Contention and Asymptotically Optimal Control](https://arxiv.org/abs/2602.02987)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Large-Scale LLM Inference with Heterogeneous Workloads: Prefill-Decode Contention and Asymptotically Optimal Control》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Numerical experiments calibrated to empirical iteration-time data demonstrate that our policies outperform standard serving heuristics.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Tangram: Unlocking Non-Uniform KV Cache for Efficient Multi-turn LLM Serving](https://arxiv.org/abs/2606.06302)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Tangram: Unlocking Non-Uniform KV Cache for Efficient Multi-turn LLM Serving》在 arXiv cs.LG 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Experimental results show that Tangram improves throughput by up to 2.6x compared to existing baselines, while fully preserving model accuracy.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：2.6x。
- [Learning to Route LLMs from Implicit Cost-Performance Preferences via Meta-Learning](https://arxiv.org/abs/2606.06178)
  - 主题: Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference、LLM routing，核心内容是《Learning to Route LLMs from Implicit Cost-Performance Preferences via Meta-Learning》在 arXiv cs.CL 这一方向上的推进。强调异构硬件协同推理。从实验上看，Experimental results show that MetaRouter outperforms strong baselines on both in-distribution and out-of-distribution tasks.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Domain-Adapted Small Language Models with Hybrid Post-Processing: Achieving Cost-Efficient, Low-Latency Multi-Label Structured Prediction via LoRA Fine-Tuning on Scarce Data](https://arxiv.org/abs/2606.05781)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Domain-Adapted Small Language Models with Hybrid Post-Processing: Achieving Cost-Efficient, Low-Latency Multi-Label Structured Prediction via LoRA Fine-Tuning on Scarce Data》在 arXiv cs.LG 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，In blind evaluation on 53 previously unseen production transcripts, it achieves 100% JSON structural validity, 83.0% human-validated overall accuracy, and 100% accuracy on the most critical classification field.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：100%、83.0%。
- [Selective Sinkhorn Routing for Improved Sparse Mixture of Experts](https://arxiv.org/abs/2511.08972)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Selective Sinkhorn Routing for Improved Sparse Mixture of Experts》在 arXiv cs.LG 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，Experiments on language modeling and image classification show that SSR improves training efficiency, accuracy, and robustness to input corruption.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [A Virtual Processor brings back the Free Lunch](https://arxiv.org/abs/2605.30507)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《A Virtual Processor brings back the Free Lunch》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The current VP primarily targets low-latency strong scaling on local heterogeneous hardware, covering workloads from small, latency-sensitive array operations to large data-parallel computations.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Ask or Assume? Uncertainty-Aware Clarification-Seeking in Coding Agents](https://arxiv.org/abs/2603.26233)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《Ask or Assume? Uncertainty-Aware Clarification-Seeking in Coding Agents》在 arXiv cs.CL 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across both proprietary and open-weight frontier LLMs, our scaffold achieves a 69.40% task resolve rate, significantly outperforming a standard single-agent setup and closing the performance gap with agents operating on fully specified instructions.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：69.40%。
- [Less is MoE: Trimming Experts in Domain-Specialist Language Models](https://arxiv.org/abs/2606.05538)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Less is MoE: Trimming Experts in Domain-Specialist Language Models》在 arXiv cs.CL 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，At the same 50% MoE compression ratio, Fisher-MoE preserves model capability, while reducing weight memory by ~45% and improving inference throughput by 21%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：50%、45%、21%。
- [SOLARIS: Speculative Offloading of Latent-bAsed Representation for Inference Scaling](https://arxiv.org/abs/2604.12110)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《SOLARIS: Speculative Offloading of Latent-bAsed Representation for Inference Scaling》在 arXiv cs.LG 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，Deployed across Meta's advertising system serving billions of daily requests, SOLARIS achieves 0.67% revenue-driving top-line metrics gain, demonstrating its effectiveness at scale.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：0.67%。
- [Exact Linear Attention](https://arxiv.org/abs/2605.18848)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Exact Linear Attention》在 arXiv cs.LG 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Experimental results demonstrate that ELA achieves up to 6x faster decoding speed and 75% reduction in KV cache memory usage compared to full attention, while maintaining comparable or superior training performance.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：6x、75%、4.3x。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

