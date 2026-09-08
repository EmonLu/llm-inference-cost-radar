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

- 日期: 2026-09-08
- 今日新论文: 0
- 今日新权威来源更新: 3
- 本周精选论文: 25
- 本周精选权威来源更新: 4
- 日报: `papers/2026-09-08.md`
- 周报: `digests/weekly-2026-09-08.md`

## 今日最值得看

- [GLM 5.3 Optimizations, Part 1: Hybrid HiSparse Offloading in vLLM](https://vllm.ai/blog/2026-09-08-glm53-part1-hybrid-sparse-offloading)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《GLM 5.3 Optimizations, Part 1: Hybrid HiSparse Offloading in vLLM》在 vLLM Blog 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，vLLM integrates HiSparse as a pressure-driven memory tier that composes with the Hybrid Memory Allocator and KV offloading, letting GLM 5.3 requests keep decoding when their KV no longer fits in GPU memory, so concurrency stays high.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Serving LLMs on Tenstorrent Hardware: Inside the vLLM TT Plugin](https://vllm.ai/blog/2026-09-07-vllm-tt-plugin)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Serving LLMs on Tenstorrent Hardware: Inside the vLLM TT Plugin》在 vLLM Blog 这一方向上的推进。关注在线 serving 系统优化，适合成本控制。从实验上看，Tenstorrent accelerators join vLLM as an out-of-tree platform plugin, driven by mesh-architecture choices: phase-based scheduling, single-process data parallelism on Galaxy, on-device sampling with host fallback, and async decode overlap.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [PyTorch x Hugging Face in Bengaluru: Building India’s Next Generation of ML Systems Contributors](https://pytorch.org/blog/pytorch-x-hugging-face-in-bengaluru-building-indias-next-generation-of-ml-systems-contributors/)
  - 主题: 
  - 中文解读: 这项工作主要关注大模型推理效率优化，核心内容是《PyTorch x Hugging Face in Bengaluru: Building India’s Next Generation of ML Systems Contributors》在 PyTorch Blog 这一方向上的推进。它重点讨论系统效率、成本控制或推理路径优化带来的实际价值。从实验上看，TL;DR More than 170 students, engineers, researchers, and open-source contributors gathered in Bengaluru for a technical evening hosted by Red Hat and Hugging Face around PyTorch, large-scale inference, reinforcement learning...
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：170 s。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

