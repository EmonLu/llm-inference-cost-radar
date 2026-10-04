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

- 日期: 2026-10-04
- 今日新论文: 6
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 2
- 日报: `papers/2026-10-04.md`
- 周报: `digests/weekly-2026-10-04.md`

## 今日最值得看

- [Oneira: From Open-Ended Generation to Open-World Interaction in Video World Models](https://arxiv.org/abs/2610.01614v1)
  - 主题: Coding agent routing, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Coding agent routing、Cost-efficient LLM inference，核心内容是《Oneira: From Open-Ended Generation to Open-World Interaction in Video World Models》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experiments show that Oneira enables direct and consistent interaction with newly generated objects, while preserving the effects of prior interactions over long horizons.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [TRACE: Tackling Real-World Resource Assignment Problems via Agentic Heuristic Design](https://arxiv.org/abs/2610.01887v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《TRACE: Tackling Real-World Resource Assignment Problems via Agentic Heuristic Design》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，TRACE consistently outperforms state-of-the-art AHD methods in resource assignment problems and yields more auditable heuristics at under 2% overhead.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：2%。
- [Agents Are Systems, Not Models: Rethinking Agentic Evaluation](https://arxiv.org/abs/2610.01618v1)
  - 主题: Coding agent routing
  - 中文解读: 这项工作主要关注Coding agent routing，核心内容是《Agents Are Systems, Not Models: Rethinking Agentic Evaluation》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，We find substantial run-to-run variability, with approximately 54% of the outcome variance coming from repeating the same configuration rather than changing it.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：54%。
- [LiteReality-Agent: An Agentic System for Interactable 3D Indoor Scene Reconstruction](https://arxiv.org/abs/2610.01863v1)
  - 主题: Coding agent routing
  - 中文解读: 这项工作主要关注Coding agent routing，核心内容是《LiteReality-Agent: An Agentic System for Interactable 3D Indoor Scene Reconstruction》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，We present LiteReality-Agent, an agentic system for reconstructing real indoor environments as realistic, articulated, and simulation-ready 3D scenes from RGB-D scans.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [A Multi-Agent LLM Framework for Personalized Health Checkup Interpretation and Guidance](https://arxiv.org/abs/2610.01451v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《A Multi-Agent LLM Framework for Personalized Health Checkup Interpretation and Guidance》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The gains came from usefulness, consistency, and the handling of every requirement in compound queries, whereas numerical accuracy and grounding improved significantly under only one of the four judges and medical safety did not differ, and critical failures occurred at similar rates (Single Agent 15.0% vs.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：15.0%、13.3%。
- [Mimir: Physics-Grounded LLM Agents for Long-Horizon Irrigation Control](https://arxiv.org/abs/2610.02038v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《Mimir: Physics-Grounded LLM Agents for Long-Horizon Irrigation Control》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Under a common retrospective evaluator across multiple sites, crops, and years, Mimir attains the lowest reported aggregate control cost among the evaluated references and uses about 51% less irrigation than the historical schedule replay.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：51%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

