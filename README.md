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

- 日期: 2026-10-25
- 今日新论文: 4
- 今日新权威来源更新: 1
- 本周精选论文: 25
- 本周精选权威来源更新: 10
- 日报: `papers/2026-10-25.md`
- 周报: `digests/weekly-2026-10-25.md`

## 今日最值得看

- [DuoCook: An Overcooked-Inspired Benchmark for Visual Planning and Coordination](https://arxiv.org/abs/2610.31511v1)
  - 主题: Coding agent routing
  - 中文解读: 这项工作主要关注Coding agent routing，核心内容是《DuoCook: An Overcooked-Inspired Benchmark for Visual Planning and Coordination》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，A memory ablation on the same 20 maps examines the effect of a shared, self-authored notebook while retaining six-response action history in both conditions.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Low-Latency MoE Inference in Space Data Centers: A Wireless-Power-Transfer Perspective](https://arxiv.org/abs/2610.30923v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Low-Latency MoE Inference in Space Data Centers: A Wireless-Power-Transfer Perspective》在 arXiv API 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，Simulations with Mixtral-8x7B and Phi-3.5-MoE show up to 29.25% lower inference latency than without WPT, with larger gains under more compact formations and higher transfer efficiencies.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：8x、29.25%。
- [Predictable performance is suboptimal, and what it means for model routing](https://arxiv.org/abs/2610.31428v1)
  - 主题: LLM routing
  - 中文解读: 这项工作主要关注LLM routing，核心内容是《Predictable performance is suboptimal, and what it means for model routing》在 arXiv API 这一方向上的推进。直接讨论模型选择或路由策略，与你的主线高度一致。从实验上看，Experiments with 16 language models on four benchmarks show that predictors gain a larger advantage over self-confidence on more suboptimal models.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [SCOPE: Compiling Natural-Language Policies into Neurosymbolic Predicate Programs](https://arxiv.org/abs/2610.31062v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、LLM routing，核心内容是《SCOPE: Compiling Natural-Language Policies into Neurosymbolic Predicate Programs》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，We evaluate SCOPE on a benchmark of real-world policy tasks against prompt optimization, task decomposition, and workflow generation methods, achieving the highest average accuracy across tasks and models.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Serving DeepSeek-V4.1-Flash at Scale: vLLM Matches DeepInfer and Scales to GB300 NVL72](https://vllm.ai/blog/2026-10-23-deepseek-v41-flash-pd-wide-ep)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Serving DeepSeek-V4.1-Flash at Scale: vLLM Matches DeepInfer and Scales to GB300 NVL72》在 vLLM Blog 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，With P/D disaggregation and Wide-EP on a GB300 NVL72 rack, vLLM serves DeepSeek-V4.1-Flash on SemiAnalysis AgentX at 954K tokens/s per GPU at a P90 of 196 tokens/s per user, 7.9x our aggregated single-node result.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：196 tokens/s、7.9x。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

