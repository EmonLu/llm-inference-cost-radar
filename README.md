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

- 日期: 2026-11-04
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 1
- 日报: `papers/2026-11-04.md`
- 周报: `digests/weekly-2026-11-04.md`

## 今日最值得看

- [ROCm InferaSim: Cut LLM Serving Trial Costs and Deploy the Best Configuration](https://arxiv.org/abs/2611.04032v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《ROCm InferaSim: Cut LLM Serving Trial Costs and Deploy the Best Configuration》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On AMD Instinct MI355X GPUs with vLLM, SGLang, and ATOM, 11 anchors took 9.1 GPU-hours, against 204 GPU-hours to measure the 226 fixed-length configurations they cover.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：355X、8%。
- [Asymptotic Optimality of $cμ$-Rule for LLM Inference Scheduling under Memory Constraint](https://arxiv.org/abs/2611.04807v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Asymptotic Optimality of $cμ$-Rule for LLM Inference Scheduling under Memory Constraint》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Finally, experiments on a real LLM serving engine using an NVIDIA H800 show that practical implementations of the proposed priority rule substantially reduce average latency while maintaining high throughput relative to existing scheduling policies.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：800 s。
- [What Sets the Serving Speed of Looped Language Models? Measurements and Optimizations Graded by Exactness](https://arxiv.org/abs/2611.05150v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《What Sets the Serving Speed of Looped Language Models? Measurements and Optimizations Graded by Exactness》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，At batch 1, fusing all loop submissions leaves Ouro throughput at 0.99x; the 5689 small kernels per token are the real cost, and fusing them behind rounding fences raises throughput 1.11-1.59x while 1014/1014 requests remain identical.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：0.99x、5689 s、1.59x。
- [HyPAIC: Personal AI Computer with High Bandwidth Flash for High Performance Trillion-Parameter LLM Inference](https://arxiv.org/abs/2611.04144v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《HyPAIC: Personal AI Computer with High Bandwidth Flash for High Performance Trillion-Parameter LLM Inference》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Through simulation-based evaluation, we show that a single HyPAIC improves end-to-end system throughput by up to 1.04x and TDP-normalized throughput by up to 3.59x during 1T-parameter MoE inference versus the aggregate of eight baseline systems without HBF, one HyPAIC thus approaches the raw performance of eight baselines with far superior power efficiency.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.04x、3.59x、10x。
- [GC-MoE: Overlapping Expert-Parallel Token Dispatch with FP8/FP4 Grouped GEMM via CUDA Green Contexts](https://arxiv.org/abs/2611.04222v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《GC-MoE: Overlapping Expert-Parallel Token Dispatch with FP8/FP4 Grouped GEMM via CUDA Green Contexts》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，On 8 H20 GPUs GC-MoE accelerates DeepSeek-V4.1-Flash decode by 1.188x on average on both the routed and shared-expert suites (peaks 1.296x and 1.353x); on 8 B300 GPUs it accelerates GLM-5.2 and DeepSeek-V4.1-Flash by 1.106x (1.123x with fused shared experts, peak 1.209x), beating Mega MoE at all 54 measured points at matched accuracy.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.188x、1.296x、1.353x。
- [Accelerating Offloading-Based MoE Inference by Interleaving Concurrent Requests](https://arxiv.org/abs/2611.04794v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Accelerating Offloading-Based MoE Inference by Interleaving Concurrent Requests》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Imprecise prediction, however, wastes bandwidth and GPU memory on fetching unnecessary experts.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [MAS-Guard: Unified Guardrails from Individual Agents to Multi-Agent LLM Systems](https://arxiv.org/abs/2610.28397)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《MAS-Guard: Unified Guardrails from Individual Agents to Multi-Agent LLM Systems》在 arXiv cs.CL 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Evaluated across six benchmarks covering diverse single- and multi-agent scenarios with three agent LLMs from different providers, MAS-Guard reduces the overall attack success rate by 71.5-86.3% relative to unguarded agents, while meeting the utility reference criterion on benign tasks.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：86.3%。
- [PyRUA-DataFarm: LLM Agent as a Cost-Efficient Teleoperator for Real-Ready Robot Data](https://arxiv.org/abs/2611.05320v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《PyRUA-DataFarm: LLM Agent as a Cost-Efficient Teleoperator for Real-Ready Robot Data》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Teleoperation remains the default way to collect robot demonstrations, but every episode costs robot and operator time, and every new task starts from scratch.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [DepthGraft: Structural Regularization through Hierarchical Cross-Layer KV Reconstruction](https://arxiv.org/abs/2611.03142)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《DepthGraft: Structural Regularization through Hierarchical Cross-Layer KV Reconstruction》在 arXiv cs.CL 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，Notably, on the 16B MoE model, DepthGraft achieves a 7.0% absolute improvement on MMLU-Pro, along with gains of 6.6% on CMMLU and 6.4% on C3.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：7.0%、6.6%、6.4%。
- [GeoFaham: Domain-Specialized Multi-Agent Geospatial Analytics for Disaster Response](https://arxiv.org/abs/2611.04977v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《GeoFaham: Domain-Specialized Multi-Agent Geospatial Analytics for Disaster Response》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，We evaluate GeoFaham on GeoFaham-Bench against strong general-purpose coding-agent baselines, including Codex, Claude Code, and OpenCode.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

