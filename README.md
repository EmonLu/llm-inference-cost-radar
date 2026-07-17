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

- 日期: 2026-07-17
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 3
- 日报: `papers/2026-07-17.md`
- 周报: `digests/weekly-2026-07-17.md`

## 今日最值得看

- [Active Beyond-Diagonal RIS Empowered Heterogeneous Edge Computing: A Distributional Reinforcement Learning Approach](https://arxiv.org/abs/2607.13160)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Active Beyond-Diagonal RIS Empowered Heterogeneous Edge Computing: A Distributional Reinforcement Learning Approach》在 arXiv cs.AI 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Compared with other baseline algorithms, DSAC-T achieves the best energy-latency reward, the highest feasibility ratio of 81.67%, and a fast online decision time of 0.0267 s per scenario.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：81.67%、0.0267 s。
- [Human-Robot Interaction in GenAI Architectures via the Agent-Client Protocol](https://arxiv.org/abs/2607.14919v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《Human-Robot Interaction in GenAI Architectures via the Agent-Client Protocol》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，We experimentally evaluate the proposed architecture on a physical mobile robot, demonstrating interoperability across three heterogeneous user interfaces and validating real-time human-in-the-loop workflows with negligible latency overhead.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [D-cut: Adaptive Verification Depth Pruning for Batched Speculative Decoding](https://arxiv.org/abs/2607.14647v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《D-cut: Adaptive Verification Depth Pruning for Batched Speculative Decoding》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Experiments on dense and mixture-of-experts (MoE) models show that, under high concurrency, D-Cut improves the average speedup from \(1.26\times\) to \(1.65\times\), restores acceleration in dense-model configurations where long-draft baselines are slower than autoregressive decoding, and achieves up to \(3.0\times\) speedup over autoregressive decoding on MoE models.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [HeteroMosaic: Exposing and Exploiting Heterogeneous Execution Opportunities for Energy-Efficient Edge LLM Inference](https://arxiv.org/abs/2607.12839v3)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《HeteroMosaic: Exposing and Exploiting Heterogeneous Execution Opportunities for Energy-Efficient Edge LLM Inference》在 arXiv API 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，On the balanced platform, HeteroMosaic achieves up to 1.73X speedup over an iGPU baseline, 1.78X over an NPU baseline, and 2.05X over frameworks such as llama dot cpp, while reducing energy by up to 45.3%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.73X、1.78X、2.05X。
- [PolyQ: Codesigning End-to-End Quantization Framework for Scalable Edge CPU LLM Inference](https://arxiv.org/abs/2607.14618v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《PolyQ: Codesigning End-to-End Quantization Framework for Scalable Edge CPU LLM Inference》在 arXiv API 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，End-to-end measurements on three representative CPUs -- workstation, laptop, and mobile -- show that compiler layout regularization reduces activation reorder traffic by up to 70.8\%, prefill latency and decode throughput scale nearly proportionally with the configured bit budget, and energy/token overhead stays below 2\% relative to an optimized LUT-based back-end.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Are LLM-Generated GPU Kernels Production-Ready? A Trace-Driven Benchmark and Optimization Agent](https://arxiv.org/abs/2607.14541v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Cost-efficient LLM inference，核心内容是《Are LLM-Generated GPU Kernels Production-Ready? A Trace-Driven Benchmark and Optimization Agent》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Existing GPU kernel generation benchmarks draw problems from synthetic or curated sources that diverge from deployed workloads.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [A Modern Multimodal Assistant on a 6 GB 2011 GPU: Stage-Validated, All-GPU CUDA Inference for Fermi](https://arxiv.org/abs/2607.14568v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《A Modern Multimodal Assistant on a 6 GB 2011 GPU: Stage-Validated, All-GPU CUDA Inference for Fermi》在 arXiv API 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，(iii) Long context exposes an O(N^2) wall short benchmarks hide: prefill falls from 114 tok/s at 2k tokens to 21 at 10k in a naive attention kernel; per-head vendor-GEMM calls writing into the existing score buffer (zero extra memory) restore a flat profile (408 at 2k, 361 at 10k; 17x), verified by exact needle retrieval from 60% depth.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：17x、60%、64%。
- [Multi-Agent Collaborative Reasoning with Tool-Augmented Evidence for Urban Region Profiling](https://arxiv.org/abs/2607.13558)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《Multi-Agent Collaborative Reasoning with Tool-Augmented Evidence for Urban Region Profiling》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Extensive experiments on global urban datasets for Carbon emissions, GDP, and Population estimation show that UrbanAgent consistently outperforms existing baselines, achieving an average improvement of 8.1% in R2, and exhibiting strong generalization performance in unseen-city settings.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：8.1%。
- [Hybrid multi-objective evolutionary algorithms for service placement in the computing continuum: a comparative study with genetic traceability](https://arxiv.org/abs/2607.13200)
  - 主题: Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference，核心内容是《Hybrid multi-objective evolutionary algorithms for service placement in the computing continuum: a comparative study with genetic traceability》在 arXiv cs.DC 这一方向上的推进。强调异构硬件协同推理。从实验上看，Across 30 independent runs, the hybrid method outperforms most of the standalone baselines, and statistical tests confirm significant improvements.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [SPINE: Bridging the Cyber-Physical Gap with Agentic AI](https://arxiv.org/abs/2607.13049)
  - 主题: Agent systems and multi-agent efficiency
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency，核心内容是《SPINE: Bridging the Cyber-Physical Gap with Agentic AI》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across seven DOBOT X-Trainer debugging scenarios, a robotics novice using SPINE outperformed human operators using Claude Code with the same reference materials, but without SPINE's structured workflow, improving operationalization success from 75% to 100% and reducing mean time-to-teleoperation from 16 min 45 s to 13 min 47 s.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：75%、100%、45 s。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

