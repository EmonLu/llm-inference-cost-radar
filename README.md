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

- 日期: 2026-07-04
- 今日新论文: 3
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 2
- 日报: `papers/2026-07-04.md`
- 周报: `digests/weekly-2026-07-04.md`

## 今日最值得看

- [MxGLUT: A Reconfigurable LUT-Centric Broadcast Dataflow Accelerator for Mixed-Precision GEMM](https://arxiv.org/abs/2607.01607v1)
  - 主题: Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference，核心内容是《MxGLUT: A Reconfigurable LUT-Centric Broadcast Dataflow Accelerator for Mixed-Precision GEMM》在 arXiv API 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，Across the Llama family, MxGLUT achieves up to $2.16\times$ and $1.49\times$ latency speedup, and reduces normalized energy to $0.44\times$ and $0.71\times$ in prefill and decode, respectively, with at most $1.70\%$ perplexity increase.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [BaseRT: Best-in-Class LLM Inference on Apple Silicon via Native Metal](https://arxiv.org/abs/2607.00501v1)
  - 主题: Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference，核心内容是《BaseRT: Best-in-Class LLM Inference on Apple Silicon via Native Metal》在 arXiv API 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，BaseRT achieves up to 1.56x higher decode throughput than llama.cpp and up to 1.35x higher than MLX, with substantially larger margins on prefill for mixture-of-experts models, delivering consistent best-in-class throughput from sub-1B to 30B parameter models.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.56x、1.35x。
- [DecompRL: Solving Harder Problems by Learning Modular Code Generation](https://arxiv.org/abs/2607.02390v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《DecompRL: Solving Harder Problems by Learning Modular Code Generation》在 arXiv API 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Repeated sampling scales test-time compute but GPU cost grows linearly with attempts, while reinforcement learning (RL) with verifiable rewards improves single-attempt accuracy at the expense of sample diversity.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

