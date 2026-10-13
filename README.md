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

- 日期: 2026-10-13
- 今日新论文: 15
- 今日新权威来源更新: 1
- 本周精选论文: 25
- 本周精选权威来源更新: 5
- 日报: `papers/2026-10-13.md`
- 周报: `digests/weekly-2026-10-13.md`

## 今日最值得看

- [Collaborative Learning and Reasoning over Model Slices](https://arxiv.org/abs/2610.12927)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《Collaborative Learning and Reasoning over Model Slices》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The trained heterogeneous models achieve comparable or better task performance than the original large model and established multi-agent baselines, including reinforcement-learning-based methods, while also achieving higher inference efficiency than the multi-agent baselines and exhibiting differentiated collaboration patterns across tasks.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Measuring Harness-Induced Belief Divergence in Multi-Step LLM Agents](https://arxiv.org/abs/2607.04528)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing，核心内容是《Measuring Harness-Induced Belief Divergence in Multi-Step LLM Agents》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，arXiv:2607.04528v2 Announce Type: replace Abstract: Software agents are becoming increasingly important in modern coding workflows, where they solve complex tasks through multi-step interaction with code repositories.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [ReplaySSM: Cache SSM Inputs, Not State](https://arxiv.org/abs/2610.13778)
  - 主题: Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference，核心内容是《ReplaySSM: Cache SSM Inputs, Not State》在 arXiv cs.AI 这一方向上的推进。通过量化降低部署成本或加速推理。从实验上看，Separate state precisions also reduce output KL divergence and downstream accuracy losses compared with a shared low-precision checkpoint.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Do More Agents Help? Evaluating Accuracy and Cost in LLM Multi-Agent Workflows](https://arxiv.org/abs/2606.05670)
  - 主题: Agent systems and multi-agent efficiency
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency，核心内容是《Do More Agents Help? Evaluating Accuracy and Cost in LLM Multi-Agent Workflows》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，EvoAgent reaches 79.70% mean pooled accuracy versus 76.65% for Core and exceeds Core in all three runs; the other five MAS trail by 1.71-8.76 percentage points.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：79.70%、76.65%。
- [AgentSWE: Can Coding Agents Build the Agent You Actually Want?](https://arxiv.org/abs/2610.13361)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing，核心内容是《AgentSWE: Can Coding Agents Build the Agent You Actually Want?》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Each of its 25 tasks is framed as a commission rather than an exam: the builder iterates against a handful of illustrative cases, while acceptance exercises the frozen submission on held-out cases designed to span the full requirement, grading behavior against requirement-derived rubrics under hard pass/fail gates or, for Optimization, against the source benchmark's own objective.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Orthros: Phase-Aware Heterogeneous Attention for Efficient Transformers](https://arxiv.org/abs/2610.13735)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Orthros: Phase-Aware Heterogeneous Attention for Efficient Transformers》在 arXiv cs.AI 这一方向上的推进。强调异构硬件协同推理。从实验上看，Finally, Orthros achieves a $21.9\times$ prefilling speedup over Transformers with end-to-end inference gains, while preserving long-context capabilities, as demonstrated by near-perfect 128K needle-in-a-haystack results and Transformer-level performance on real-world in-context recall tasks.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Selection-Based Structured Reasoning: Toward Efficient Multimodal Search Agents](https://arxiv.org/abs/2610.01892)
  - 主题: Cost-efficient LLM inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、LLM routing，核心内容是《Selection-Based Structured Reasoning: Toward Efficient Multimodal Search Agents》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，SSR achieves an average success rate competitive with leading search agents of the same scale, while reducing per-turn reasoning latency by over 90% and total per-question model inference latency by 28-54%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：90%、54%。
- [ProgramGym: Scaling Training Environments for Long-Horizon Program Reproduction Agents](https://arxiv.org/abs/2610.13395)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing，核心内容是《ProgramGym: Scaling Training Environments for Long-Horizon Program Reproduction Agents》在 arXiv cs.CL 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Program-Agent further raises the base and SFT models to 55.71% and 56.25%, both exceeding some flagship models.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：55.71%、56.25%、34.87%。
- [TRACE: Rollout-Guided Quantization-Aware Training for FP4 Reinforcement Learning of MoE Language Models](https://arxiv.org/abs/2610.07767)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《TRACE: Rollout-Guided Quantization-Aware Training for FP4 Reinforcement Learning of MoE Language Models》在 arXiv cs.CL 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，Our results demonstrate that TRACE enables joint FP4 weight/activation and FP4 KV-cache rollout with RL performance comparable to BF16 rollout, while achieving up to 5.4xrollout speedup and strong final FP4 performance compared with post-hoc FP4 quantization of BF16-trained policies.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：5.4x。
- [Scale and Selection: What Makes Automatic Harness Evolution Work for Visual-Interface Robot Agents](https://arxiv.org/abs/2609.39304)
  - 主题: Coding agent routing, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Coding agent routing、Cost-efficient LLM inference，核心内容是《Scale and Selection: What Makes Automatic Harness Evolution Work for Visual-Interface Robot Agents》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Combining the evolved harness with a pretrained policy, through one tool that hands it control, reaches 71.2% on the RoboCasa365 leaderboard benchmark, 13.1 points above the best published entry.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：71.2%、51%、67%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

