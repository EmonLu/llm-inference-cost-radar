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

- 日期: 2026-08-13
- 今日新论文: 15
- 今日新权威来源更新: 1
- 本周精选论文: 25
- 本周精选权威来源更新: 6
- 日报: `papers/2026-08-13.md`
- 周报: `digests/weekly-2026-08-13.md`

## 今日最值得看

- [MEGA: Self-Evolving Agent Optimization Infrastructure via Wisdom Graph](https://arxiv.org/abs/2608.10504)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Heterogeneous MoE inference，核心内容是《MEGA: Self-Evolving Agent Optimization Infrastructure via Wisdom Graph》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Layer 3 performs multi-agent collaborative optimization over heterogeneous agent workflows (code nodes, LLM calls, and tool-using agents), attributing improvement effects to specific strategy changes through controlled evaluation that eliminates data variance.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Janus: Disaggregating Attention and Experts for Scalable MoE Inference](https://arxiv.org/abs/2512.13525)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Janus: Disaggregating Attention and Experts for Scalable MoE Inference》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Evaluation shows that JANUS improves per-GPU throughput by up to 4.7x over state-of-the-art MoE inference baselines while satisfying token-level latency SLOs.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：4.7x。
- [Astrolabe: Balancing Load in LLM Serving with Randomized Prediction-Guided Scheduling](https://arxiv.org/abs/2508.03611)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Astrolabe: Balancing Load in LLM Serving with Randomized Prediction-Guided Scheduling》在 arXiv cs.DC 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，With migration enabled on A100 GPUs, Astrolabe outperforms Llumnix by up to 2.6 times in throughput while achieving orders-of-magnitude lower per-token latency at saturation.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [TideRL: Boosting Agentic RL Goodput with Readiness-Aware Scheduling](https://arxiv.org/abs/2608.10402)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《TideRL: Boosting Agentic RL Goodput with Readiness-Aware Scheduling》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，It also improves KV cache hit rate by 1.58$\times$, reduces per-step training time by up to 44.3%, and cuts total waiting time by up to 77.6%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：44.3%、77.6%、33%。
- [XBridge: Entity-Grounded Latent Bridge for Heterogeneous LLM Communication](https://arxiv.org/abs/2608.11676v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《XBridge: Entity-Grounded Latent Bridge for Heterogeneous LLM Communication》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across three model families (Llama, Qwen, and Mistral), seven benchmarks, and both communication directions, XBRIDGE outperforms text-based communication on all seven tasks for each model pair while achieving 11x lower latency, and in a same-architecture setting it also exceeds a KV-sharing baseline on six of seven tasks.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：11x、3.8%。
- [Better, Faster, Stronger: Programmatic Skill Learning Best Reduces Agent Cost](https://arxiv.org/abs/2608.11338v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《Better, Faster, Stronger: Programmatic Skill Learning Best Reduces Agent Cost》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across three different embodied environments, we show that SpeedRunner consistently achieves the frontier in learning and cost reduction while remaining robust against distribution shifts and environmental randomness.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [StrataCL: Fabric-Native Communication Library for Production Supernodes](https://arxiv.org/abs/2607.26444)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《StrataCL: Fabric-Native Communication Library for Production Supernodes》在 arXiv cs.DC 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，Across three production workloads, StrataCL improves LLM inference throughput by 1.9x, reduces P99 TTFT by 2.2x, and reduces LLM and Recsys training iteration time by 1.4x and 1.3x, respectively.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.9x、2.2x、1.4x。
- [Taming Request Imbalance: SLO-Aware Scheduling for Disaggregated LLM Inference](https://arxiv.org/abs/2605.02329)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Taming Request Imbalance: SLO-Aware Scheduling for Disaggregated LLM Inference》在 arXiv cs.DC 这一方向上的推进。关注在线 serving 系统优化，适合成本控制。从实验上看，Experimental results demonstrate that, compared with state-of-the-art baselines, Kairos improves TTFT SLO attainment by up to 23.9\%, TPOT SLO attainment by up to 27.1\%, end-to-end SLO attainment by up to 33.8\%, and decode throughput by up to 19.3\%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [ForestBench: A Unified Graph Framework for Evaluating Multi-Agent Collaboration](https://arxiv.org/abs/2608.08605)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《ForestBench: A Unified Graph Framework for Evaluating Multi-Agent Collaboration》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Outcome-only benchmarks discard collaborations, whereas LLM-as-Judge evaluation requires additional, model-dependent inference and can vary with the LLM and rubric.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Bandwidth-Efficient Multi-Agent Communication through Information Bottleneck and Vector Quantization](https://arxiv.org/abs/2602.02035)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《Bandwidth-Efficient Multi-Agent Communication through Information Bottleneck and Vector Quantization》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experimental evaluation on challenging coordination tasks demonstrates that our method achieves 181.8% performance improvement over no-communication baselines while reducing bandwidth usage by 71.4%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：181.8%、71.4%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

