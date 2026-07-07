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

- 日期: 2026-07-07
- 今日新论文: 15
- 今日新权威来源更新: 1
- 本周精选论文: 25
- 本周精选权威来源更新: 3
- 日报: `papers/2026-07-07.md`
- 周报: `digests/weekly-2026-07-07.md`

## 今日最值得看

- [Nemotron-Labs-3-Puzzle-75B-A9B: Compressing Hybrid MoE LLMs](https://arxiv.org/abs/2607.04371v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Nemotron-Labs-3-Puzzle-75B-A9B: Compressing Hybrid MoE LLMs》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，In interactive serving workloads on a single 8xB200 node, Puzzle-75B-A9B achieves approximately 2x higher server throughput than Nemotron-3-Super at matched user throughput constraints.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：8x、2x。
- [Prima.cpp: Fast 30-70B LLM Inference on Heterogeneous and Low-Resource Home Clusters](https://arxiv.org/abs/2504.08791)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Prima.cpp: Fast 30-70B LLM Inference on Heterogeneous and Low-Resource Home Clusters》在 arXiv cs.DC 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，On four consumer home devices, a 70B model reaches 674 ms/token TPOT with <6% memory pressure, and a 32B model with speculative decoding achieves 26 tokens/s.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：674 ms、6%、26 tokens/s。
- [From Tensor Buffer to Distributed Memory Hierarchy: A Survey of KV Cache Management for LLM Serving](https://arxiv.org/abs/2607.02574)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《From Tensor Buffer to Distributed Memory Hierarchy: A Survey of KV Cache Management for LLM Serving》在 arXiv cs.DC 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，The axes reveal five architectural archetypes -- local-paged, disaggregated-pipeline, shared-store, memory-pool, and hybrid-tier.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Adaptive Inference Batching using Policy Gradients](https://arxiv.org/abs/2607.05272)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Adaptive Inference Batching using Policy Gradients》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，In multi-GPU heterogeneous routing, however, where fast and slow requests compete for shared resources, the agent discovers a workload-segregation policy that eliminates Head-of-Line blocking, yielding a 3.5x (348%) improvement over Round-Robin and a 48% improvement over the strongest heuristic baseline (Shortest-Queue), with 60% higher throughput and 25% lower latency while respecting SLA constraints.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：3.5x、348%、48%。
- [Council Mode: A Heterogeneous Multi-Agent Consensus Framework for Reducing LLM Hallucination and Bias](https://arxiv.org/abs/2604.02923)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《Council Mode: A Heterogeneous Multi-Agent Consensus Framework for Reducing LLM Hallucination and Bias》在 arXiv cs.CL 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，In our evaluation, conducted under controlled no-web settings, the Council Mode achieved a 41.7% relative reduction in hallucination rates on a 1,200-sample HaluEval subset and a 7.5-point improvement on TruthfulQA compared to the top-performing individual model.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：41.7%、95.4%。
- [Quantize the Target, Quantize the Drafter: Efficient Inference with Qwen3.5-4B](https://arxiv.org/abs/2607.04244v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Quantize the Target, Quantize the Drafter: Efficient Inference with Qwen3.5-4B》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Because the drafter is invoked at every speculative decoding step, we further reduce its overhead with quantization and sliding-window attention, preserving draft-token acceptance while improving long-context decoding latency.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Sangam: Efficiently Serving Diffusion LLMs with the AR Stack](https://arxiv.org/abs/2607.04206)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Sangam: Efficiently Serving Diffusion LLMs with the AR Stack》在 arXiv cs.DC 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，Colocated serving is most effective on decode-heavy workloads, cutting mean latency by 9-20% over hybrid execution on LLaDA-8B ShareGPT; while hybrid execution is most effective on prefill-heavy workloads, cutting mean latency by 8-20% over colocated execution on Dream-7B arXiv.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：20%。
- [PEEK: Predictive Queue-Informed KV Cache Management for LLM Serving](https://arxiv.org/abs/2607.02525)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《PEEK: Predictive Queue-Informed KV Cache Management for LLM Serving》在 arXiv cs.DC 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，On SGLang and vLLM across five workloads up to 4$\times$H100 (DP=2 over TP=2), PEEK delivers up to 3.0$\times$/2.6$\times$ cache hit, 7.9$\times$/7.1$\times$ TTFT, 6.7$\times$/5.5$\times$ E2E, and 3.6$\times$/4.5$\times$ throughput gains over each engine's strongest stock baseline (SGLang/vLLM), while matching baselines within noise on workloads with no exploitable prefix structure.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [A Workflow-Aware Serving Layer for Agentic Applications](https://arxiv.org/abs/2607.02942)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《A Workflow-Aware Serving Layer for Agentic Applications》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Because no single latency-quality preference fits every workload mix, Dyserve pre-solves the program at several pressure levels at admission and shifts a workflow's uncommitted suffix among these strategies under load, keeping the solver off the load-shift path; a failed tool call triggers a one-time residual re-solve that preserves committed work.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [PuzzleMoE: Efficient Compression of Large Mixture-of-Experts Models via Sparse Expert Merging and Bit-packed inference](https://arxiv.org/abs/2511.04805)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《PuzzleMoE: Efficient Compression of Large Mixture-of-Experts Models via Sparse Expert Merging and Bit-packed inference》在 arXiv cs.LG 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Specifically, it outperforms prior MoE compression methods by up to 16.7% on MMLU at 50% compression ratio, and achieves up to 1.28\times inference speedup.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：16.7%、50%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

