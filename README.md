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

- 日期: 2026-05-13
- 今日新论文: 15
- 今日新权威来源更新: 1
- 本周精选论文: 25
- 本周精选权威来源更新: 3
- 日报: `papers/2026-05-13.md`
- 周报: `digests/weekly-2026-05-13.md`

## 今日最值得看

- [Rethinking LLMOps for Fraud and AML: Building a Compliance-Grade LLM Serving Stack](https://arxiv.org/abs/2605.11232)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Rethinking LLMOps for Fraud and AML: Building a Compliance-Grade LLM Serving Stack》在 arXiv cs.LG 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Across public-synthetic AML workloads and controlled serving benchmarks, workload-aware tuning improved throughput from 612-650 to 3,600 requests/hour, reduced P99 latency from 31-38 seconds to 6.4-8.7 seconds, and increased GPU utilization from 12% to 78%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：38 s、8.7 s、12%。
- [Ada-MK: Adaptive MegaKernel Optimization via Automated DAG-based Search for LLM Inference](https://arxiv.org/abs/2605.11581v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Ada-MK: Adaptive MegaKernel Optimization via Automated DAG-based Search for LLM Inference》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，On an NVIDIA L20, Ada-MK improves single-batch throughput by up to 23.6% over vanilla TensorRT-LLM and 50.2% over vLLM, achieving positive gains across all tested scenarios--the first industrial deployment of MegaKernel in a commercial online advertising system.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：23.6%、50.2%、50%。
- [Patterns behind Chaos: Forecasting Data Movement for Efficient Large-Scale MoE LLM Inference](https://arxiv.org/abs/2510.05497)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Patterns behind Chaos: Forecasting Data Movement for Efficient Large-Scale MoE LLM Inference》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，We perform systematic analysis from both temporal and spatial perspectives and distill six key insights to guide the design of diverse serving systems.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Sieve: Dynamic Expert-Aware PIM Acceleration for Evolving Mixture-of-Experts Models](https://arxiv.org/abs/2605.11277v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Sieve: Dynamic Expert-Aware PIM Acceleration for Evolving Mixture-of-Experts Models》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Compared to state-of-the-art PIM systems for MoE, Sieve improves both throughput and interactivity by 1.3x, 1.3x, and 1.6x on Qwen3.5-397B-A17B, GPT-OSS-120B, and Qwen3-30B-A3B, respectively.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.3x、1.6x。
- [SPECTRE: Hybrid Ordinary-Parallel Speculative Serving for Resource-Efficient LLM Inference](https://arxiv.org/abs/2605.08151)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《SPECTRE: Hybrid Ordinary-Parallel Speculative Serving for Resource-Efficient LLM Inference》在 arXiv cs.DC 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，Results show that SPECTRE consistently improves large-model serving throughput while causing only minor interference to the native workloads of tail-model services.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [DisagMoE: Computation-Communication overlapped MoE Training via Disaggregated AF-Pipe Parallelism](https://arxiv.org/abs/2605.11005)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《DisagMoE: Computation-Communication overlapped MoE Training via Disaggregated AF-Pipe Parallelism》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，DisagMoE is implemented on Megatron-LM, and evaluation shows that DisagMoE improves training efficiency across multiple MoE models with up to 1.8x speedup on 16-node 8xH800 clusters.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.8x、8x。
- [Analytical Provisioning for Attention-FFN Disaggregated LLM Serving under Stochastic Workloads](https://arxiv.org/abs/2601.21351)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Analytical Provisioning for Attention-FFN Disaggregated LLM Serving under Stochastic Workloads》在 arXiv cs.LG 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，A trace-calibrated AFD simulator supports the framework across workloads: the predicted optimal ratio matches the simulation-optimal within 10%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：10%。
- [DWDP: Distributed Weight Data Parallelism for High-Performance LLM Inference on NVL72](https://arxiv.org/abs/2604.01621)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《DWDP: Distributed Weight Data Parallelism for High-Performance LLM Inference on NVL72》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Implemented in TensorRT-LLM and evaluated with DeepSeek-R1 on GB200 NVL72, DWDP improves end-to-end output TPS/GPU by 8.8% at comparable TPS/user in the 20-100 TPS/user serving range under 8K input sequence length and 1K output sequence length.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：8.8%。
- [CATS: Cascaded Adaptive Tree Speculation for Memory-Limited LLM Inference Acceleration](https://arxiv.org/abs/2605.11186v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《CATS: Cascaded Adaptive Tree Speculation for Memory-Limited LLM Inference Acceleration》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，CATS can achieve a wall-clock speedup of up to 5.08x with no degradation in generation quality, outperforming the SOTA method by up to 1.45x under edge memory constraints.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：5.08x、1.45x。
- [Fast MoE Inference via Predictive Prefetching and Expert Replication](https://arxiv.org/abs/2605.11537v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Fast MoE Inference via Predictive Prefetching and Expert Replication》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Experimental evaluations conducted on large-scale MoE models, including Switch-base-128 and Switch-base-256, demonstrate that our method achieves near-complete GPU utilization (approx 100%), leading to upto 3x improvement in inference speed while preserving approximately 90-95% of the performance of baseline architectures
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：100%、3x、95%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

