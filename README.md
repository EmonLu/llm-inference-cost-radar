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

- 日期: 2026-11-09
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 4
- 日报: `papers/2026-11-09.md`
- 周报: `digests/weekly-2026-11-09.md`

## 今日最值得看

- [Nebula: Distributed Position-Independent Caching for LLM Serving](https://arxiv.org/abs/2611.09474)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Nebula: Distributed Position-Independent Caching for LLM Serving》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across four models and four real-world RAG and agentic workloads, Nebula reduces median TTFT by an average of 61.4% compared with the strongest existing baseline and recovers an average of 76.1% of the tokens missed by prefix caching.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：61.4%、76.1%。
- [Introducing Cluster Efficiency to LLM Serving: Pooling Economical Accelerators over Fast Interconnects](https://arxiv.org/abs/2611.02975)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Introducing Cluster Efficiency to LLM Serving: Pooling Economical Accelerators over Fast Interconnects》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Emulating TCP-class communication on the same chips reduces throughput by 23.5-67.4% and eliminates the cost advantage in every evaluated configuration.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：67.4%。
- [ELDR: Expert-Locality-Aware Decode Routing for PD-Disaggregated MoE Serving](https://arxiv.org/abs/2607.00466)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《ELDR: Expert-Locality-Aware Decode Routing for PD-Disaggregated MoE Serving》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Across three MoE models on 12 public task benchmarks and multilingual WildChat, it reduces median time-per-output-token (TPOT) by 5.4-14.5% on average across request rates and up to 17.8% over the best of four load-balancing baselines, preserving model outputs and token-to-expert assignments.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：14.5%、17.8%。
- [BitDecoding-FP4: Native FP4 KV Cache Decoding via Algorithm-System Co-Design](https://arxiv.org/abs/2611.09825)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《BitDecoding-FP4: Native FP4 KV Cache Decoding via Algorithm-System Co-Design》在 arXiv cs.CL 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，We mitigate three error sources: Dual-Residual Query Quantization splits queries into two FP4 tensors, cutting query logit error from 60% to 1%; Underflow-Aware Probability Scaling prevents E4M3 scales from rounding long-context probabilities to zero; and Outlier-Aware Key Quantization combines static smoothing, Hadamard rotation, and scale search to suppress key outliers under token-wise scaling.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：60%、1%、3 s。
- [ISER-MoE: Dynamic In-Switch Replication of Hot Experts for Load Balancing in Expert-Parallel](https://arxiv.org/abs/2611.09008)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《ISER-MoE: Dynamic In-Switch Replication of Hot Experts for Load Balancing in Expert-Parallel》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，In trace replay, the scheduler removed 98-99% of the excess load; in prefill serving of DeepSeek-V4-Pro, throughput rose 17.4% on a math benchmark and 7.2% on agentic prompts.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：99%、17.4%、7.2%。
- [MeshRT: Compile-Time Governed Wafer-Scale Runtime for Low-Latency High-Throughput Inference](https://arxiv.org/abs/2611.08508)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《MeshRT: Compile-Time Governed Wafer-Scale Runtime for Low-Latency High-Throughput Inference》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Against measured single-instance SGLang results on H200, MeshRT achieves 4.5-7.0$\times$ lower latency.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Enabling Privacy-Preserving Natural Language Access to Industrial Smart Meter Data](https://arxiv.org/abs/2611.09372v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Enabling Privacy-Preserving Natural Language Access to Industrial Smart Meter Data》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Multi-scenario ablation studies over this environment demonstrate that full multi-agent orchestration shows its largest observed accuracy gains on resource-constrained local hardware (+6.1 pp EX-R over the strongest single-agent configuration); at frontier scale, individual components retain value but should be enabled selectively, indicating that the cost of full orchestration is justified specifically where privacy demands local execution.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [RPEG: Training Reasoning Language Models Scalably and Cost-Effectively](https://arxiv.org/abs/2611.09207)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《RPEG: Training Reasoning Language Models Scalably and Cost-Effectively》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Across systems with up to 256 GH200 GPUs, our distributed runtime engine implementing RPEG improves performance by up to 2x over ReaL and reduces step latency by up to 2.48x over verl, while increasing hardware utilization by up to 30%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：2x、2.48x、30%。
- [MINE: Entropy-coded Memory-efficient Inference for Large Language Models](https://arxiv.org/abs/2611.09424v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《MINE: Entropy-coded Memory-efficient Inference for Large Language Models》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，It exploits the non-uniform distribution of weights, which persists even after quantization, and exposes hyper-parameters that trade compression ratio against decoding cost.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Same Request, Different Answer: Quantization Amplifies Cache-Induced Divergence in LLM Serving](https://arxiv.org/abs/2609.04748)
  - 主题: Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference，核心内容是《Same Request, Different Answer: Quantization Amplifies Cache-Induced Divergence in LLM Serving》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，We measure what this prefix reuse costs in reproducibility.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

