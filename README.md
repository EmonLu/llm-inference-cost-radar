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

- 日期: 2026-07-29
- 今日新论文: 15
- 今日新权威来源更新: 1
- 本周精选论文: 25
- 本周精选权威来源更新: 5
- 日报: `papers/2026-07-29.md`
- 周报: `digests/weekly-2026-07-29.md`

## 今日最值得看

- [Beyond Prefill-Decode Disaggregation: Dissecting LLM Inference for Heterogeneous Platforms via Dynamic Operator Scheduling](https://arxiv.org/abs/2607.25498v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Beyond Prefill-Decode Disaggregation: Dissecting LLM Inference for Heterogeneous Platforms via Dynamic Operator Scheduling》在 arXiv API 这一方向上的推进。强调异构硬件协同推理。从实验上看，Across representative heterogeneous systems combining neural processing units (NPUs) and processing-in-memory (PIM) devices, Bifocal achieves geometric-mean speedups of 1.20$\times$ to 2.23$\times$ over the PD baseline.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [HyMCache: A KV Cache Framework for Multi-Turn LLM Serving with CXL-Hybrid Memory](https://arxiv.org/abs/2607.18141)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《HyMCache: A KV Cache Framework for Multi-Turn LLM Serving with CXL-Hybrid Memory》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Compared with 1 TB distributed-DRAM Mooncake, HyMCache incurs about 30% lower performance but uses 16x less DRAM.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：30%、16x、3.0x。
- [The Hitchhiker's Guide to Agentic AI: From Foundations to Systems](https://arxiv.org/abs/2606.24937)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《The Hitchhiker's Guide to Agentic AI: From Foundations to Systems》在 arXiv cs.CL 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The book concludes with agent development frameworks, agentic UI design, evaluation methodology for agentic tasks, and production deployment.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Gleam: Adaptive Network-Efficient CUDA API Remoting for Cross-Device GPU Sharing over LANs](https://arxiv.org/abs/2607.23115)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Gleam: Adaptive Network-Efficient CUDA API Remoting for Cross-Device GPU Sharing over LANs》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Extensive experiments on heterogeneous NVIDIA GPUs and diverse AI workloads show Gleam consistently outperforms state-of-the-art baselines, achieving 1.4-24.2 times improvements in API remoting efficiency and up to 1.79 times higher system throughput.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [HeraSys: Collaborative Serving of Multiple LLM Workflows via Fine-Grained End-to-End Optimization](https://arxiv.org/abs/2607.22578)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《HeraSys: Collaborative Serving of Multiple LLM Workflows via Fine-Grained End-to-End Optimization》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Extensive experiments demonstrate that HeraSys reduces P99 latency by up to 2.17$\times$ and increases serving throughput by up to 1.85$\times$ under strict latency guarantees.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [LIBMoE: A Library for comprehensive benchmarking Mixture of Experts in Large Language Models](https://arxiv.org/abs/2411.00918)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《LIBMoE: A Library for comprehensive benchmarking Mixture of Experts in Large Language Models》在 arXiv cs.CL 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，By lowering the barrier to entry and standardizing evaluation, along with our comprehensive analysis, LibMoE broadens access to MoE research and establishes a reliable benchmark to guide future innovations.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [HeteroMosaic: Exposing and Exploiting Heterogeneous Execution Opportunities for Energy-Efficient Edge LLM Inference](https://arxiv.org/abs/2607.12839)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《HeteroMosaic: Exposing and Exploiting Heterogeneous Execution Opportunities for Energy-Efficient Edge LLM Inference》在 arXiv cs.DC 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，On the balanced platform, HeteroMosaic achieves up to 1.73X speedup over an iGPU baseline, 1.78X over an NPU baseline, and 2.05X over frameworks such as llama dot cpp, while reducing energy by up to 45.3%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.73X、1.78X、2.05X。
- [LongStraw: Long-Context RL Beyond 2M Tokens under a Fixed GPU Budget](https://arxiv.org/abs/2607.14952)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《LongStraw: Long-Context RL Beyond 2M Tokens under a Fixed GPU Budget》在 arXiv cs.DC 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，This schedule bounds the live training graph by the response suffix while reusing the expensive prompt computation across the complete GRPO group.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Context Assembly as the Controlled Variable: A Control-Theoretic View of Harness Policies for Frozen LLM Agents](https://arxiv.org/abs/2607.25408v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、LLM routing，核心内容是《Context Assembly as the Controlled Variable: A Control-Theoretic View of Harness Policies for Frozen LLM Agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，(2026) (non-decreasing expected reward under bounded policy change), and reports an uncertainty-calibration analysis of the controller's own confidence against realized task outcomes.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [VibeVoice-ASR-BitNet Technical Report](https://arxiv.org/abs/2607.21075)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《VibeVoice-ASR-BitNet Technical Report》在 arXiv cs.CL 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，VibeVoice-ASR-BitNet is 1.6--2.3x faster than Whisper.cpp at comparable model sizes (~1.6 GB), with only modest accuracy degradation compared to the FP16 baseline.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：2.3x、1.6 GB。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

