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

- 日期: 2026-07-15
- 今日新论文: 15
- 今日新权威来源更新: 2
- 本周精选论文: 25
- 本周精选权威来源更新: 3
- 日报: `papers/2026-07-15.md`
- 周报: `digests/weekly-2026-07-15.md`

## 今日最值得看

- [Multi-Agent Routing as Set-Valued Prediction: A WildChat Benchmark and Cost-Aware Evaluation](https://arxiv.org/abs/2606.28925)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、LLM routing，核心内容是《Multi-Agent Routing as Set-Valued Prediction: A WildChat Benchmark and Cost-Aware Evaluation》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Overall, the benchmark and evaluation protocol support reproducible study of accuracy-cost trade-offs in fixed-catalog multi-agent routing.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Towards Autonomous and Auditable Medical Imaging Model Development](https://arxiv.org/abs/2607.10522)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《Towards Autonomous and Auditable Medical Imaging Model Development》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Translating this capability to medical imaging remains difficult because each task imposes modality-specific experimentation and strict requirements for validation protocols and prediction artifacts.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [HYPIC: Accelerating Hybrid-Attention LLM Serving with Position-Independent Caching](https://arxiv.org/abs/2607.01299)
  - 主题: Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference，核心内容是《HYPIC: Accelerating Hybrid-Attention LLM Serving with Position-Independent Caching》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Evaluated across four hybrid-attention models and five workloads, Hypic reduces time-to-first-token by $3.25\times$ on average and improves QPS by $1.66\times$ over Prefix Cache, while preserving task quality with a 1.71-point gap from Full Recompute.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [PFAdapter: Hierarchical LoRA Decomposition for Personalized Federated MLLMs](https://arxiv.org/abs/2607.12111v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《PFAdapter: Hierarchical LoRA Decomposition for Personalized Federated MLLMs》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Extensive experiments on VQA-RAD, SLAKE, Hateful Memes, and CrisisMMD datasets demonstrate that PFAdapter consistently outperforms state-of-the-art baselines, achieving accuracy improvements ranging from 2.4% to 4.8% across diverse edge intelligence tasks.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：2.4%、4.8%、50%。
- [HeteroMosaic: Exposing and Exploiting Heterogeneous Execution Opportunities for Energy-Efficient Edge LLM Inference](https://arxiv.org/abs/2607.12839v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《HeteroMosaic: Exposing and Exploiting Heterogeneous Execution Opportunities for Energy-Efficient Edge LLM Inference》在 arXiv API 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，On the balanced platform, HeteroMosaic achieves up to 1.73X speedup over an iGPU baseline, 1.78X over an NPU baseline, and 2.05X over frameworks such as \texttt{llama.cpp}, while reducing energy by up to 45.3%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.73X、1.78X、2.05X。
- [Recursive Multi-Agent Systems](https://arxiv.org/abs/2604.25917)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《Recursive Multi-Agent Systems》在 arXiv cs.CL 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，In comparison with advanced single/multi-agent and recursive computation baselines, RecursiveMAS consistently delivers an average accuracy improvement of 8.3%, together with 1.2$\times$-2.4$\times$ end-to-end inference speedup, and 34.6%-75.6% token usage reduction.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：8.3%、34.6%、75.6%。
- [RouteRec: Strict Evaluation of Recommender-Agent Selection and Aggregation](https://arxiv.org/abs/2607.09908)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《RouteRec: Strict Evaluation of Recommender-Agent Selection and Aggregation》在 arXiv cs.CL 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，0.114), while gated all-agent aggregation reaches HR@10 = 0.295 with 70.2\% LLM calls.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Scheduling Techniques of AI Models on Modern Heterogeneous Edge GPU -- A Critical Review](https://arxiv.org/abs/2506.01377)
  - 主题: Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference，核心内容是《Scheduling Techniques of AI Models on Modern Heterogeneous Edge GPU -- A Critical Review》在 arXiv cs.DC 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Therefore, efforts have been made to create schedulers that can manage complex data processing needs while ensuring the efficient utilization of all available accelerators within these devices, including the CPU, GPU, deep learning accelerator (DLA), programmable vision accelerator (PVA), and video image compositor (VIC).
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [StanceMoE: Mixture-of-Experts Architecture for Stance Detection](https://arxiv.org/abs/2604.00878)
  - 主题: Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference、LLM routing，核心内容是《StanceMoE: Mixture-of-Experts Architecture for Stance Detection》在 arXiv cs.CL 这一方向上的推进。强调异构硬件协同推理。从实验上看，StanceMoE achieves a macro-F1 score of 94.26%, outperforming traditional baselines, and alternative BERT-based variants.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1 s、94.26%。
- [Knowledge-Constrained Shape Optimization with a Mixture-of-Experts Neural Operator for High-Confidence Design](https://arxiv.org/abs/2607.09763)
  - 主题: Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference，核心内容是《Knowledge-Constrained Shape Optimization with a Mixture-of-Experts Neural Operator for High-Confidence Design》在 arXiv cs.LG 这一方向上的推进。强调异构硬件协同推理。从实验上看，Experiments on in-house MPV, SUV, and Sedan datasets show that MoE-NO achieves a test-set MAPE of $1.16\%$ and a trend-prediction accuracy of $94.34\%$, outperforming the best baseline results of $1.52\%$ and $90.34\%$, respectively.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

