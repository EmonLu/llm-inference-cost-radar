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

- 日期: 2026-07-30
- 今日新论文: 15
- 今日新权威来源更新: 1
- 本周精选论文: 25
- 本周精选权威来源更新: 4
- 日报: `papers/2026-07-30.md`
- 周报: `digests/weekly-2026-07-30.md`

## 今日最值得看

- [NELSSA: A GPU-PNM Heterogeneous System for Mixed-Length LLM Serving via Length-based Request Placement](https://arxiv.org/abs/2607.26633v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《NELSSA: A GPU-PNM Heterogeneous System for Mixed-Length LLM Serving via Length-based Request Placement》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across mixed-length LLM workloads, NELSSA improves decode throughput by up to 5.5x in tokens/sec and reduces P99 latency by up to 15x compared to GPU-only baselines.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：5.5x、15x。
- [DualDecoder: Accelerate Long Context LLM Inference by Predictive Prefetch](https://arxiv.org/abs/2607.26475v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《DualDecoder: Accelerate Long Context LLM Inference by Predictive Prefetch》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experimental results show that DualDecoder improves decoding throughput by up to 2.62$\times$ over state-of-the-art systems while preserving decoding latency and model quality.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [SpecPrefetch: Parameter-Efficient Expert Prefetching for Sparse MoE Foundation Models](https://arxiv.org/abs/2607.24787)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《SpecPrefetch: Parameter-Efficient Expert Prefetching for Sparse MoE Foundation Models》在 arXiv cs.AI 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，On a Snapdragon 8 Elite device, SpecPrefetch further improves decoding throughput by up to \(20\%\) over a compute-optimized offloading runtime, demonstrating practical benefits for storage-constrained MoE deployment.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [FedWeave: Rethinking the Unit of Specialization in Heterogeneous Federated MoE-LoRA](https://arxiv.org/abs/2607.26618v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《FedWeave: Rethinking the Unit of Specialization in Heterogeneous Federated MoE-LoRA》在 arXiv API 这一方向上的推进。强调异构硬件协同推理。从实验上看，On a heterogeneous multi-task benchmark with mainstream LLM backbones, FedWeave consistently outperforms strong baselines, while ablations verify the effectiveness of our design.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [DisDP: Disaggregating Compute, Network, and Storage for Model-Sharded Data-Parallel Training](https://arxiv.org/abs/2409.00918)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《DisDP: Disaggregating Compute, Network, and Storage for Model-Sharded Data-Parallel Training》在 arXiv cs.DC 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，DisDP on 8 distributed GPUs outperforms the state-of-the-art training systems by 3.98x when training on a 175B model, validating the efficiency of disaggregation.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：3.98x、10%、41%。
- [StrataCL: Fabric-Native Communication Library for Production Supernodes](https://arxiv.org/abs/2607.26444v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《StrataCL: Fabric-Native Communication Library for Production Supernodes》在 arXiv API 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，Across three production workloads, StrataCL improves LLM inference throughput by 1.9x, reduces P99 TTFT by 2.2x, and reduces LLM and Recsys training iteration time by 1.4x and 1.3x, respectively.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.9x、2.2x、1.4x。
- [Scores Are Not Decisions: Cost-Aware Stopping for Tool Acquisition in LLM Agents](https://arxiv.org/abs/2607.27083v1)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference、LLM routing，核心内容是《Scores Are Not Decisions: Cost-Aware Stopping for Tool Acquisition in LLM Agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Our approach is state-of-the-art under heterogeneous costs and high cost pressure, with larger gains under weaker rankings.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Sheet As Token: A Graph-Enhanced Representation for Multi-Sheet Spreadsheet Understanding](https://arxiv.org/abs/2605.05811)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Sheet As Token: A Graph-Enhanced Representation for Multi-Sheet Spreadsheet Understanding》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，SAT therefore improves both retrieval accuracy and serving efficiency: on IndustryTab-1K, it exceeds a Qwen3.5-9B RAG reranker by 12.5% while reducing online latency from 2.61 s to 9.24 ms, approximately 283X faster.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：12.5%、2.61 s、9.24 ms。
- [LazyMem: Retrieve Broadly, Construct Selectively for Efficient Long-Term Agent Memory](https://arxiv.org/abs/2607.22690)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《LazyMem: Retrieve Broadly, Construct Selectively for Efficient Long-Term Agent Memory》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On LongMemEval, LazyMem-4B achieves an LLM-judge accuracy of 0.85, outperforming the strongest non-oracle baseline while using only 213 answer-context memory tokens, 21.0 times fewer than the baseline.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Moral Hazard in Multi-Agent Language Models](https://arxiv.org/abs/2607.23982)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《Moral Hazard in Multi-Agent Language Models》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Their effects are heterogeneous: OLMo-7B shows the clearest mechanism-consistent weight-level improvement, whereas GEPA sometimes improves team success while reducing or eliminating costly queries.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

