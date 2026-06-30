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

- 日期: 2026-06-30
- 今日新论文: 15
- 今日新权威来源更新: 1
- 本周精选论文: 25
- 本周精选权威来源更新: 3
- 日报: `papers/2026-06-30.md`
- 周报: `digests/weekly-2026-06-30.md`

## 今日最值得看

- [HBM Is Not All You Need: Efficient Disaggregated LLM Serving across Memory-heterogeneous Accelerators](https://arxiv.org/abs/2606.29986)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《HBM Is Not All You Need: Efficient Disaggregated LLM Serving across Memory-heterogeneous Accelerators》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Across four Qwen3 models (4B--32B) and three production traces, HMA-Serve delivers up to $3.2\times$ higher goodput than state-of-the-art memory-homogeneous methods and $4.8\times$ higher goodput-per-dollar, with no measurable loss on generation-quality benchmarks.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [SwarmX: Agentic Scheduling for Low-Latency Agentic Systems](https://arxiv.org/abs/2606.21401)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《SwarmX: Agentic Scheduling for Low-Latency Agentic Systems》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across multi-agent code generation, deep research, and multimodal agentic workflows, SwarmX reduces tail latency by up to 61.5% compared to state-of-the-art schedulers and sustains up to 2x the throughput of production schedulers under the same SLO.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：61.5%、2x。
- [KernelFlume: Elastic Core-Attention Scaling for Agentic Long-Context Decoding](https://arxiv.org/abs/2606.29207)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《KernelFlume: Elastic Core-Attention Scaling for Agentic Long-Context Decoding》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Replaying the same trace at larger model scale in simulation projects a 56--66% cost reduction over ServerlessLLM, widening to 80--85% with cheaper heterogeneous attention-node hardware and persisting into the million-token context range.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：66%、85%、74 ms。
- [TraceLab: Characterizing Coding Agent Workloads for LLM Serving](https://arxiv.org/abs/2606.30560v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《TraceLab: Characterizing Coding Agent Workloads for LLM Serving》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，These findings point to concrete opportunities for optimizing serving, including lower-overhead tool calling, append-length-aware prefill, semantic-aware tool-latency prediction, and improved KV-cache management around human-paced gaps.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [LLM Serving Optimization with Variable Prefill and Decode Lengths](https://arxiv.org/abs/2508.06133)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《LLM Serving Optimization with Variable Prefill and Decode Lengths》在 arXiv cs.LG 这一方向上的推进。强调异构硬件协同推理。从实验上看，Experiments on public workloads that combine short conversations and long-document summarization show that F-metric-based scheduling consistently reduces latency relative to standard baselines and remains close to the LP relaxation lower bound for tractable instances.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [A Multi-task Mixture of Experts Framework for Malware Classification, Packing Detection, and Family Attribution](https://arxiv.org/abs/2606.30572)
  - 主题: Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference、LLM routing，核心内容是《A Multi-task Mixture of Experts Framework for Malware Classification, Packing Detection, and Family Attribution》在 arXiv cs.AI 这一方向上的推进。强调异构硬件协同推理。从实验上看，The obtained results demonstrate that the Multi-Gate MoE model achieves the best performance, reaching a combined detection rate of 0.9744 with only $2.56\%$ failure rate.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Mixture of Debaters: Learn to Debate at Architectural Level in Multi-Agent Reasoning](https://arxiv.org/abs/2606.29425)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Mixture of Debaters: Learn to Debate at Architectural Level in Multi-Agent Reasoning》在 arXiv cs.CL 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Extensive experiments on multimodal benchmarks demonstrate that MoD outperforms both single-model baselines and conventional multi-agent systems, achieving superior accuracy with 3.7x lower latency and 87% reduction in token consumption.The source code can be accessed at https://github.com/YongLD/MoD.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：3.7x、87%。
- [CLEAR-MoE: Shared-Basis Expert Extraction from Frozen Vision Transformers via Calibration-Driven Layer Selection](https://arxiv.org/abs/2606.28516)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《CLEAR-MoE: Shared-Basis Expert Extraction from Frozen Vision Transformers via Calibration-Driven Layer Selection》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，On Imagenette with DeiT-Small, CLEAR-MoE retains 99.9% of the dense model's accuracy (86.70 +/- 0.02% versus 86.73%).
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：99.9%、0.02%、86.73%。
- [xGR: Efficient Generative Recommendation Serving at Scale](https://arxiv.org/abs/2512.11529)
  - 主题: Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference，核心内容是《xGR: Efficient Generative Recommendation Serving at Scale》在 arXiv cs.LG 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，The experiments on real-world datasets demonstrate that xGR achieves at least 2.89x throughput compared to the state-of-the-art baseline under strict latency constraints.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：2.89x。
- [Beyond Uniform Experts: Cost-Aware Expert Execution for Efficient Multi-Device MoE Inference](https://arxiv.org/abs/2606.29982v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Beyond Uniform Experts: Cost-Aware Expert Execution for Efficient Multi-Device MoE Inference》在 arXiv API 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，Evaluations on the 671B DeepSeek-R1 model show that CAEE can reduce end-to-end inference latency by 8\%-18\% across diverse deployment settings, including expert offloading and on-device execution on multi-device systems, while maintaining a model accuracy drop of less than 1\%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

