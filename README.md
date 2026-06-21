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

- 日期: 2026-06-21
- 今日新论文: 3
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 4
- 日报: `papers/2026-06-21.md`
- 周报: `digests/weekly-2026-06-21.md`

## 今日最值得看

- [Probe-and-Refine Tuning of Repository Guidance for Coding Agents](https://arxiv.org/abs/2606.20512v1)
  - 主题: Coding agent routing
  - 中文解读: 这项工作主要关注Coding agent routing，核心内容是《Probe-and-Refine Tuning of Repository Guidance for Coding Agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The improvement comes from coverage rather than precision: refined guidance produces evaluable patches for 14.5 percentage points (pp) more instances while per-patch precision remains statistically constant ($\sim$59\,\%, $p = 0.119$), showing that improved guidance helps agents reach the correct file rather than improving the quality of the changes they make.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Human-on-the-Loop Orchestration for AI-Assisted Legal Discovery](https://arxiv.org/abs/2606.19812v1)
  - 主题: Agent systems and multi-agent efficiency, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、LLM routing，核心内容是《Human-on-the-Loop Orchestration for AI-Assisted Legal Discovery》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Our results suggest that calibrated uncertainty thresholds can reduce privilege-waiver risk by up to 61% versus fully autonomous deployment, while routing fewer than one quarter of documents to attorney review.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：61%。
- [Activation- and Influence-Aware Ranks (AIR): Function-Preserving SVD Compression for LLMs](https://arxiv.org/abs/2606.19993v1)
  - 主题: Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference，核心内容是《Activation- and Influence-Aware Ranks (AIR): Function-Preserving SVD Compression for LLMs》在 arXiv API 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，AIR improves perplexity over SVD-LLM(W) by >18% at <=60% parameter retention, matches its quality with ~90% less calibration data, and turns parameter savings into FLOP, peak-memory, and per-token latency gains.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：18%、60%、90%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

