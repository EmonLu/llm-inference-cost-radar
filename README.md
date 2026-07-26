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

- 日期: 2026-07-26
- 今日新论文: 4
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 5
- 日报: `papers/2026-07-26.md`
- 周报: `digests/weekly-2026-07-26.md`

## 今日最值得看

- [EmoAgent-R1: Towards Multimodal Emotion Understanding with Reinforcement Learning-based Dynamic Agent Specialization](https://arxiv.org/abs/2607.21013v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、LLM routing，核心内容是《EmoAgent-R1: Towards Multimodal Emotion Understanding with Reinforcement Learning-based Dynamic Agent Specialization》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Extensive experiments on MER benchmarks demonstrate the superiority of our EmoAgent-R1 in stronger emotion reasoning performance and improved optimization stability.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [C-PTQ: Fisher-weighted Channel-wise Sensitivity for Post-training Quantization of MLLMs](https://arxiv.org/abs/2607.21076v1)
  - 主题: Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference，核心内容是《C-PTQ: Fisher-weighted Channel-wise Sensitivity for Post-training Quantization of MLLMs》在 arXiv API 这一方向上的推进。通过量化降低部署成本或加速推理。从实验上看，Experiments on Qwen2.5VL, InternVL2 and LLaVA-OV across 8 benchmarks demonstrate our effectiveness in both weight-only and weight-activation settings.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [HiMe: Real-Time Self-Hosted Personal Agent Platform for Health Insights with Wearable Devices](https://arxiv.org/abs/2607.21019v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《HiMe: Real-Time Self-Hosted Personal Agent Platform for Health Insights with Wearable Devices》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Effectiveness and efficiency are jointly optimised to achieve a low-cost Pareto-optimal balance.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Same Dangerous Objective, Opposite Advice: Direct Exposure versus Multi-Agent Mediation](https://arxiv.org/abs/2607.21518v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《Same Dangerous Objective, Opposite Advice: Direct Exposure versus Multi-Agent Mediation》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Even a current high-capability LLM can appear safer when shown a dangerous objective directly than when other agents transform and relay its direction.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

