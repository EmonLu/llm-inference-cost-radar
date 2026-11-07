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

- 日期: 2026-11-07
- 今日新论文: 15
- 今日新权威来源更新: 2
- 本周精选论文: 25
- 本周精选权威来源更新: 4
- 日报: `papers/2026-11-07.md`
- 周报: `digests/weekly-2026-11-07.md`

## 今日最值得看

- [StrataFlux: Memory-Hierarchy-Native Low-Bit LLM Inference](https://arxiv.org/abs/2611.08363v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《StrataFlux: Memory-Hierarchy-Native Low-Bit LLM Inference》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，With 2-bit weights and KV, StrataFlux raises Qwen3-8B's AIME 2024/2025 accuracy from 11.0% to 47.1% at unchanged GPU memory use.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：11.0%、47.1%、95.4%。
- [Enabling AWS Cloud FPGA Development Using High-Level Vitis HLS](https://arxiv.org/abs/2611.06829v1)
  - 主题: Coding agent routing, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Coding agent routing、Heterogeneous MoE inference，核心内容是《Enabling AWS Cloud FPGA Development Using High-Level Vitis HLS》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，We present a toolchain for development of ML models on AWS EC2 F2 cloud FPGA infrastructure from high-level language, implementing a complete Vitis HLS to HDK bridge to AFI workflow that has been absent from the academic literature despite eight years of AWS FPGA availability.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [ReproBridge: Building Reproducibility into ML Research Artifacts](https://arxiv.org/abs/2611.08452v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《ReproBridge: Building Reproducibility into ML Research Artifacts》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across four evaluated models, refined artifacts raise mean reproduction success from 76.4% to 92.6% and reduce downstream API spending by 19.7% on average.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：76.4%、92.6%、19.7%。
- [How Do AI Agents Waste Your Money?](https://arxiv.org/abs/2611.07238v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《How Do AI Agents Waste Your Money?》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，In online pruning experiments, we remove 41-46% of the model's reasoning while largely preserving task performance across two distinct agent benchmarks.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：46%。
- [Generative Retrieval under Real-Time Supply Constraints in Local Commerce](https://arxiv.org/abs/2611.06323v2)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Generative Retrieval under Real-Time Supply Constraints in Local Commerce》在 arXiv API 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，A different-host comparison with 30,000 supplied entries reports a 0.6 ms service-side latency increment, while client measurements expose additional request costs.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：000 s、0.6 ms。
- [Rules, Traces and Routing Statistics: Training and Calibration Data for Open Models on ARC-AGI-2](https://arxiv.org/abs/2611.06827v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Rules, Traces and Routing Statistics: Training and Calibration Data for Open Models on ARC-AGI-2》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，For the Qwen3.8-Flash-Next mixture-of-experts model (125B parameters, 6B active), GPU memory limited concurrency.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Resource-Efficient Reinforcement Learning Post-Training through Elastic Expert Parallelism](https://arxiv.org/abs/2611.06984v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Resource-Efficient Reinforcement Learning Post-Training through Elastic Expert Parallelism》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Compared with the verl baseline, FlexFloor generates approximately 65.40% more response tokens per unit of occupied computing time and increases response generation throughput by 52.74%, with little observed variation in rollout reward.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：65.40%、52.74%。
- [HarnessFlow: MCTS-Guided Harness Optimization for LLM Agents](https://arxiv.org/abs/2611.06254v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing，核心内容是《HarnessFlow: MCTS-Guided Harness Optimization for LLM Agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The optimized harnesses achieve an average score of 69.48%, outperforming the initial harnesses and Meta-Harness by 10.89 and 3.95 percentage points, respectively, while incurring lower average per-task execution costs than hand-engineered baselines.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：69.48%。
- [SCALE: Real-Time Latent Communication for Cyber-Physical Agents](https://arxiv.org/abs/2611.08390v1)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《SCALE: Real-Time Latent Communication for Cyber-Physical Agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，It then profiles the semantic gain and communication cost of transmitting different amounts of latent information.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [QRAE: Query-Relevant Attention Entropy for Context Compression in DeepSearch Agents](https://arxiv.org/abs/2611.07976v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《QRAE: Query-Relevant Attention Entropy for Context Compression in DeepSearch Agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across multiple DeepSearch benchmarks and reasoning models, QRAE improves task success by an average of 2.35 percentage points and reduces end-to-end latency and reported token usage by an average of 30% and 45%, respectively.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：30%、45%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

