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

- 日期: 2026-10-22
- 今日新论文: 15
- 今日新权威来源更新: 4
- 本周精选论文: 25
- 本周精选权威来源更新: 9
- 日报: `papers/2026-10-22.md`
- 周报: `digests/weekly-2026-10-22.md`

## 今日最值得看

- [TraceLite: Efficient Trace Reduction for SWE Agents via Optical Compression and Redundancy Removal](https://arxiv.org/abs/2610.28612v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《TraceLite: Efficient Trace Reduction for SWE Agents via Optical Compression and Redundancy Removal》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On SWE-bench Verified, TraceLite achieves 78.25% resolve rate, outperforming the evaluated compression baselines while reducing average input-token consumption and API cost by 33.05% and 21.30%, respectively.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：78.25%、33.05%、21.30%。
- [To Keep or Not to Keep: Learning KV Cache Retention in Disaggregated LLM Serving Systems](https://arxiv.org/abs/2610.28637)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《To Keep or Not to Keep: Learning KV Cache Retention in Disaggregated LLM Serving Systems》在 arXiv cs.DC 这一方向上的推进。强调异构硬件协同推理。从实验上看，On MM-Session, throughput remains within ${\sim}5%$ of oracle.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：5%、56%、38%。
- [UlaCache: Unified Logical Addressing for Sparse LLM Serving](https://arxiv.org/abs/2610.29820)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《UlaCache: Unified Logical Addressing for Sparse LLM Serving》在 arXiv cs.DC 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，With speculative decoding enabled under matched CPU and GPU memory budgets, UlaCache achieves peak decoding throughput speedups of 1.16 $\times$ (DP) and 1.70 $\times$ (TP) on H200, and 1.73 $\times$ (DP) and 2.51 $\times$ (TP) on B300, compared with the state-of-the-art baseline.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [NanoCP: Taming Load Imbalance in Data-Expert Parallel Decoding under Variable-Length Workloads](https://arxiv.org/abs/2605.21100)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《NanoCP: Taming Load Imbalance in Data-Expert Parallel Decoding under Variable-Length Workloads》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Experimental results show that, under 99% TPOT-SLO attainment, NanoCP achieves $3.27\times$ and $2.11\times$ the maximum sustainable request rate of the best-performing vLLM baseline on the DeepSeek-V3 Issue 1% and Issue 5% workloads, respectively, while reducing P99 TPOT by $1.94\times$ and $2.01\times$ on the same two workloads, respectively.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：99%、1%、5%。
- [HAWK: Heterogeneity-Aware KV Cache Transfer for Efficient GPU-NPU Phase-Disaggregated LLM Inference](https://arxiv.org/abs/2610.29873v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《HAWK: Heterogeneity-Aware KV Cache Transfer for Efficient GPU-NPU Phase-Disaggregated LLM Inference》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，We implement and evaluate HAWK on a system built with commercially available GPUs and NPUs, demonstrating performance within 7.88% of a GPU-only system under the same SLO constraints while achieving up to 1.26$\times$ higher power efficiency and 1.72$\times$ higher cost efficiency.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：7.88%。
- [EGI-BENCH: An Enterprise General Intelligence Benchmark Suite](https://arxiv.org/abs/2610.27234)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《EGI-BENCH: An Enterprise General Intelligence Benchmark Suite》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，We describe the suite, the sub-metric routing, and the quick/deep budgets, and report results for fourteen frontier and cost-efficient LLMs spanning the GPT, Claude, and Gemini families under quick mode.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Toward Agentic AI for the 6G Physical Layer: From Algorithm Discovery to Verified Baseband Silicon](https://arxiv.org/abs/2610.27797v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Heterogeneous MoE inference，核心内容是《Toward Agentic AI for the 6G Physical Layer: From Algorithm Discovery to Verified Baseband Silicon》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，It also yields a new detector shaped by the chip's measured costs that needs 13.9% fewer cycles than the port of the discovered detector while matching its error rate, with a measured edge our evaluation cannot statistically resolve, a structure that a hardware-blind search objective had no reason to find.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：13.9%。
- [Cache Engineering for Agents](https://arxiv.org/abs/2610.28577v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《Cache Engineering for Agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experiments show that a tool-response rolling-drop cache policy improves average benchmark scores by 1.7 points and reduces average cost by 27.7%, compared with conventional threshold-triggered summarization.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：27.7%、1.2x、1.5x。
- [Service-Induced Congestion in Memory-Constrained LLM Serving](https://arxiv.org/abs/2606.15555)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Service-Induced Congestion in Memory-Constrained LLM Serving》在 arXiv cs.AI 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，For homogeneous workloads, we show that the eviction-free equilibrium is unstable and that, except for a Lebesgue-measure-zero exact-capture set, the system converges to a unique worst-case limit cycle that is asymptotically stable outside this exceptional set, with throughput losses as large as 50%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：50%。
- [Policy Search in Code Space for Multi-Agent Pathfinding](https://arxiv.org/abs/2610.25946)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《Policy Search in Code Space for Multi-Agent Pathfinding》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，In simulated real-world warehouses with irregular lanes, continuous robot geometry, and asynchronous motion, a week-long search discovered an entirely new class of multi-agent pathfinding algorithm that outperforms a calibrated proprietary solution in throughput by 58.9%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：58.9%、35.0%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

