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

- 日期: 2026-07-06
- 今日新论文: 0
- 今日新权威来源更新: 1
- 本周精选论文: 25
- 本周精选权威来源更新: 2
- 日报: `papers/2026-07-06.md`
- 周报: `digests/weekly-2026-07-06.md`

## 今日最值得看

- [vLLM × HPC-Ops: High-Performance Attention and MoE Backends from Tencent Hunyuan](https://vllm.ai/blog/2026-07-06-vllm-hpc-ops)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《vLLM × HPC-Ops: High-Performance Attention and MoE Backends from Tencent Hunyuan》在 vLLM Blog 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，How HPC-Ops integrates Hopper-optimized attention and FP8 MoE backends into vLLM for Tencent Hunyuan Hy3, improving mixed-length decode, MoE latency, TTFT, and TPOT on NVIDIA H20.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

