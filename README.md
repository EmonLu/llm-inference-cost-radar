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

- 日期: 2026-08-17
- 今日新论文: 7
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 4
- 日报: `papers/2026-08-17.md`
- 周报: `digests/weekly-2026-08-17.md`

## 今日最值得看

- [FreeBalance: Pre-Routing Online Moe Load Balancing via Residual Workload Prediction](https://arxiv.org/abs/2608.14205v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《FreeBalance: Pre-Routing Online Moe Load Balancing via Residual Workload Prediction》在 arXiv API 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，Experiments across models and datasets show that FreeBalance reduces the max-to-mean rank load ratio by 32.8% and end-to-end prefill latency by 13.1%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：32.8%、13.1%、8.5%。
- [Beyond Capacity: Scalable MoE LLM Inference via High-Bandwidth Flash with Direct GPU and HBM Paths](https://arxiv.org/abs/2608.14333v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Beyond Capacity: Scalable MoE LLM Inference via High-Bandwidth Flash with Direct GPU and HBM Paths》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，For a representative workload, the proposed architecture can achieve 1.94$\times$ higher throughput and 1.90$\times$ end-to-end speedup over a design that delivers all HBF-resident expert weights to the GPU through the HBM base die.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [CoRun: Padding is Simple and Efficient for Deterministic LLM Inference](https://arxiv.org/abs/2608.14376v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《CoRun: Padding is Simple and Efficient for Deterministic LLM Inference》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Experiments on LLMs with diverse architectures, including Qwen and DeepSeek, show that CoRun ensures determinism while improving throughput by 15-324 % over batch-invariant approaches, reducing time-to-first-token by 51.8 % and time-per-output-token by 48.6 % on average.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：324 %、51.8 %、48.6 %。
- [DeaMoE: Efficient MoE Structure for Fast Small-Batch Decoding](https://arxiv.org/abs/2608.14385v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《DeaMoE: Efficient MoE Structure for Fast Small-Batch Decoding》在 arXiv API 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，Compared with vanilla MoE, DeaMoE reduces per-step loaded weights by up to 50.9% and achieves up to 1.33 end-to-end TPOT speedup for the pre-trained 7B model on A40, and up to 2.00x and 1.97x peak speedup for DeepSeek-V3 on A40 and H100 in microbenchmarks.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：50.9%、2.00x、1.97x。
- [Consensus-gated Multi-Agent Neural Architecture Search for Seismic Fault Segmentation](https://arxiv.org/abs/2608.13889v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Consensus-gated Multi-Agent Neural Architecture Search for Seismic Fault Segmentation》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The search cost 101 LLM calls ($\sim$1.15M input / 0.39M output tokens) and roughly one GPU-day, making consensus-gated LLM panels a practical, low-cost route to domain-specific architecture discovery.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Twin: Playing an Unknown Game with a Test-Time Digital Twin](https://arxiv.org/abs/2608.14490v1)
  - 主题: Coding agent routing
  - 中文解读: 这项工作主要关注Coding agent routing，核心内容是《Twin: Playing an Unknown Game with a Test-Time Digital Twin》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Twin clears 179 out of 183 levels (97.8%), and does so more efficiently than humans in 158 out of 179 levels (88.3%).
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：97.8%、88.3%、87.2%。
- [AppLooper: An Agentic Application Engineering Loop for Accountable Release with Virtual-User Feedback](https://arxiv.org/abs/2608.14093v1)
  - 主题: Coding agent routing
  - 中文解读: 这项工作主要关注Coding agent routing，核心内容是《AppLooper: An Agentic Application Engineering Loop for Accountable Release with Virtual-User Feedback》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Much existing research on coding agents organizes application development as an iterative loop of requirement interpretation, implementation, tool execution, evaluation, and repair.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

