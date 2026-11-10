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

- 日期: 2026-11-10
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 5
- 日报: `papers/2026-11-10.md`
- 周报: `digests/weekly-2026-11-10.md`

## 今日最值得看

- [Evolving Infra: Agent-Adaptive LLM Serving at Scale](https://arxiv.org/abs/2611.12304v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Evolving Infra: Agent-Adaptive LLM Serving at Scale》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across coding, math, and computer-use tasks with GLM-5.2 and Kimi K2.6 on up to 256 GB300 GPUs, Evolving Infra reduces mean end-to-end request latency and P95 TTFT by up to 4.1x and 14x over Dynamo, NVIDIA's production framework.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：256 GB、4.1x、14x。
- [Verify Before You Fetch: Reliable KV Cache Compression for LLM Inference](https://arxiv.org/abs/2611.11319v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Verify Before You Fetch: Reliable KV Cache Compression for LLM Inference》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Combined with KVFetch, it achieves near-dense performance (90-100% of dense quality at 32K context length, averaged over RULER and LOFT), using Qwen3-4B, Qwen3.5-9B and Ministral-3-8B, while reducing the GPU memory footprint by 8-32x and keeping CPU-to-GPU memory fetches within 2-23% of the cache per generated token, depending on the model.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：100%、32x、23%。
- [Ostinato: Fast CPU-GPU MoE Inference for Local Agents via Resident Experts in Every Forward Pass](https://arxiv.org/abs/2611.11533v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Ostinato: Fast CPU-GPU MoE Inference for Local Agents via Resident Experts in Every Forward Pass》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Against llama.cpp and KTransformers, it cuts the median wait after a tool output by 22-55% and finishes sessions 1.4-2.5$\times$ sooner.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：55%、84%。
- [Agents Propose, Code Verifies, Humans Decide: Verified Agentic Ingestion of Heterogeneous Scientific Tables into Relational Databases](https://arxiv.org/abs/2611.11045v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Heterogeneous MoE inference，核心内容是《Agents Propose, Code Verifies, Humans Decide: Verified Agentic Ingestion of Heterogeneous Scientific Tables into Relational Databases》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Code compiles PostgreSQL DDL, reshapes the data, quarantines rows it cannot place, records provenance, and reconciles every staged row against the database.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [InfraRSI: Harnessing Recursive Self-Improvement for Training Infrastructure](https://arxiv.org/abs/2611.11558v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、Heterogeneous MoE inference，核心内容是《InfraRSI: Harnessing Recursive Self-Improvement for Training Infrastructure》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Across four single- and multi-node dense and Mixture-of-Experts (MoE) LLM workloads, InfraRSI achieves a speedup of up to $2.75\times$ and lifts mean Model FLOPs Utilization (MFU) from $17.4\%$ to $30.0\%$, outperforming existing tuners and coding agents while transferring experience across GPUs.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Direct GPU Energy Measurements of Batch-Level Sharing in Mixture-of-Experts and Recurrent Models](https://arxiv.org/abs/2611.11696v1)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference、LLM routing，核心内容是《Direct GPU Energy Measurements of Batch-Level Sharing in Mixture-of-Experts and Recurrent Models》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On MoE models the answer is yes, and granularity decides how much: on Qwen3-30B-A3B, batch-aware routing reads 25-31% fewer expert weights within KL 0.05, with benchmark changes within noise at 500 items, and uses 12-18% less energy per token on a fused forward.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：31%、18%、40%。
- [Toward Sustainable Agentic AI: Carbon Tradeoffs Across Iterative Self-Refinement and Tool-Augmented Coding](https://arxiv.org/abs/2611.12128v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing，核心内容是《Toward Sustainable Agentic AI: Carbon Tradeoffs Across Iterative Self-Refinement and Tool-Augmented Coding》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，In Study~2, GPT-5.3-codex achieves the highest resolution rate in this sample (81.2\%), ahead of Claude Opus~4.6 (68.9\%) and GPT-4.1-mini (25.0\%), but resolved-task-normalized efficiency remains mixed: GPT-4.1-mini is lowest on estimated carbon and cost per resolved task, while GPT-5.3-codex delivers substantially higher task success.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [BridgeKV: Large-Model Prefill and Small-Model Decoding for LLM Inference via KV Cache Translation](https://arxiv.org/abs/2611.11761v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《BridgeKV: Large-Model Prefill and Small-Model Decoding for LLM Inference via KV Cache Translation》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，On one A40 GPU, Llama-3.1-Instruct-8B to Llama-3.2-Instruct-1B achieves 3.0X faster requests than the larger model alone, with latency close to the smaller model alone.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：3.0X、33.86X、27.5X。
- [Detent: Batch-Invariant LLM Serving and RL Rollouts at Near-Stock Speed](https://arxiv.org/abs/2611.10611v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Detent: Batch-Invariant LLM Serving and RL Rollouts at Near-Stock Speed》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Tuned per load, it serves at 1.04-1.17x the latency per output token of Stock (each engine with its standard settings), against 1.67-10.3x for the deterministic modes.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.17x、10.3x、1.03x。
- [OverlapAdvisor: Modeling and Adapting Computation-Communication Overlap for Distributed MoE Serving](https://arxiv.org/abs/2611.11857v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《OverlapAdvisor: Modeling and Adapting Computation-Communication Overlap for Distributed MoE Serving》在 arXiv API 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，In SGLang and vLLM, it improves end-to-end throughput up to 31.7%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：31.7%、1.16x、1.59x。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

