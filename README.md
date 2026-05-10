# LLM Inference Cost Radar

A daily-updated research radar for:
- LLMRouter and LLM routing
- model routing inside coding agents
- CPU/GPU heterogeneous inference for MoE models
- cost-saving LLM inference, serving, scheduling, and optimization
- agent systems / multi-agent efficiency and routing-related work

Now includes:
- 每日论文雷达
- 每周精选
- 权威工程来源更新（NVIDIA / PyTorch / GitHub Blog / LMSYS / vLLM / SemiAnalysis / DeepSpeed）
- 基于 LLM 的中文一句话摘要

## 最新更新

- 日期: 2026-05-07
- 今日新论文: 15
- 今日新权威来源更新: 2
- 本周精选论文: 25
- 本周精选权威来源更新: 3
- 日报: `papers/2026-05-07.md`
- 周报: `digests/weekly-2026-05-07.md`

## 今日最值得看

- [SplitZip: Ultra Fast Lossless KV Compression for Disaggregated LLM Serving](https://arxiv.org/abs/2605.01708)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文一句话: SplitZip实现了GPU友好的KV cache极速无损压缩，大幅降低LLM异构推理中的通信瓶颈。
- [Agentic AI Systems Should Be Designed as Marginal Token Allocators](https://arxiv.org/abs/2605.01214)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, Cost-efficient LLM inference, LLM routing
  - 中文一句话: 提出将agentic AI系统设计为边际token分配器，实现跨路由、agent等层的系统成本最优。
- [SMoE: An Algorithm-System Co-Design for Pushing MoE to the Edge via Expert Substitution](https://arxiv.org/abs/2508.18983)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文一句话: SMoE通过专家替换和缓存复用，大幅降低MoE在边缘设备上的GPU内存和PCIe成本。
- [6G Needs Agents: Toward Agentic AI-Native Networks for Autonomous Intelligence](https://arxiv.org/abs/2605.01546)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文一句话: 提出用LLM驱动agent提升6G网络智能与自治，重塑控制系统核心价值。
- [Distributed Generative Inference of LLM at Internet Scales with Multi-Dimensional Communication Optimization](https://arxiv.org/abs/2604.21072)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文一句话: BloomBee通过多维通信优化显著降低分布式LLM推理的系统成本。
- [Agentic AI-Based Joint Computing and Networking via Mixture of Experts and Large Language Models](https://arxiv.org/abs/2605.02911)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文一句话: 该工作用MoE和LLM实现智能agent路由，动态优化6G网络资源分配，提升系统灵活性和可扩展性。
- [Tutti: Making SSD-Backed KV Cache Practical for Long-Context LLM Serving](https://arxiv.org/abs/2605.03375v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文一句话: Tutti通过GPU主导的KV cache对象存储，实现SSD支持下长上下文推理高效且低CPU成本。
- [Stochastic Sparse Attention for Memory-Bound Inference](https://arxiv.org/abs/2605.01910)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文一句话: SANTA方法通过稀疏化KV cache访问显著提升长上下文推理速度，兼容GPU并保持精度。
- [Silicon Showdown: Performance, Efficiency, and Ecosystem Barriers in Consumer-Grade LLM Inference](https://arxiv.org/abs/2605.00519)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文一句话: 系统性分析Nvidia与Apple芯片LLM推理，量化与推理优化显著提升性能但引入复杂系统权衡。
- [ZeRO-Prefill: Zero Redundancy Overheads in MoE Prefill Serving](https://arxiv.org/abs/2605.02960)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文一句话: ZeRO-Prefill通过解耦专家分配与激活路由，极大降低MoE预填推理的冗余和系统成本。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

