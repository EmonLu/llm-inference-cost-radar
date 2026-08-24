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

- 日期: 2026-08-24
- 今日新论文: 5
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 2
- 日报: `papers/2026-08-24.md`
- 周报: `digests/weekly-2026-08-24.md`

## 今日最值得看

- [SPICE: Speculative Prefetching with Low-Rank Expert Surrogates and Heterogeneous Orchestration for MoE Inference Acceleration](https://arxiv.org/abs/2608.21240v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《SPICE: Speculative Prefetching with Low-Rank Expert Surrogates and Heterogeneous Orchestration for MoE Inference Acceleration》在 arXiv API 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，However, the large expert parameter footprint often exceeds GPU memory capacity, making inference latency dominated by the host-to-device PCIe transfers for expert loading.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Fuzzy-MoE: Interpretable Regime-Conditioned Expert Routing for Non-Stationary Multivariate Time Series Forecasting](https://arxiv.org/abs/2608.20761v1)
  - 主题: Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference、LLM routing，核心内容是《Fuzzy-MoE: Interpretable Regime-Conditioned Expert Routing for Non-Stationary Multivariate Time Series Forecasting》在 arXiv API 这一方向上的推进。强调异构硬件协同推理。从实验上看，Experimental results on multiple public time series benchmark datasets show that Fuzzy-MoE significantly outperforms mainstream forecasting methods in forecasting accuracy.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Just Noticeable Difference Modeling for Token Compression in Vision-Language-Action Models](https://arxiv.org/abs/2608.21247v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《Just Noticeable Difference Modeling for Token Compression in Vision-Language-Action Models》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experiments on the LIBERO benchmark with OpenVLA and OpenVLA-OFT demonstrate that Action-JND consistently improves compression reliability, especially under aggressive compression ratios.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Memory Augmentation Unlocks Efficient Chain-of-Thought Reasoning](https://arxiv.org/abs/2608.21265v1)
  - 主题: Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference，核心内容是《Memory Augmentation Unlocks Efficient Chain-of-Thought Reasoning》在 arXiv API 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，Experiments show that Memory consistently improves prompt-based Chain-of-Draft (CoD) compression across mathematical reasoning, complex reasoning, and science question answering tasks, yielding accuracy gains of 21.4, 28.0, 29.5, and 6.61 points over CoD on GSM8K, MATH, BBH, and MMLU-Sci, while achieving a 1.14--1.49$\times$ latency speedup over standard CoT.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [$Z^2$-ACT: End-to-End Verifiable Agentic Intent Control for Open 6G RAN](https://arxiv.org/abs/2608.21049v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《$Z^2$-ACT: End-to-End Verifiable Agentic Intent Control for Open 6G RAN》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Our experimental evaluation on public ColO-RAN measurements compares the full architecture against targeted ablations and a conventional reinforcement-learning baseline.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

