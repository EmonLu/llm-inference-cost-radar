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

- 日期: 2026-09-01
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 1
- 日报: `papers/2026-09-01.md`
- 周报: `digests/weekly-2026-09-01.md`

## 今日最值得看

- [WiSP: A Working-Set View of Mixture-of-Experts Serving on Extremely Low-Resource Hardware](https://arxiv.org/abs/2606.21868)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《WiSP: A Working-Set View of Mixture-of-Experts Serving on Extremely Low-Resource Hardware》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，On a real 24 GiB RTX 3090, WiSP achieves up to 2.0x the decode throughput of static offload at the same memory budget when the model does not fit.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：24 GiB、2.0x、1.19x。
- [A Universal Context-Reuse Layer for Cross-Model KV Sharing](https://arxiv.org/abs/2608.30963v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《A Universal Context-Reuse Layer for Cross-Model KV Sharing》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，In a more heterogeneous Llama3.1-70B $\rightarrow$ Qwen2.5-7B setting, cross-family handoff achieves 44.0\% accuracy compared with 45.7\% for native Qwen2.5-7B inference, while reducing measured latency from 899ms to 138ms.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：899ms、138ms。
- [PRIME: Mitigating Subgroup Optimization Competition in Shared CTR Top Networks with Plug-in Residual Input-Conditioned Mixture of Expert](https://arxiv.org/abs/2608.30449v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《PRIME: Mitigating Subgroup Optimization Competition in Shared CTR Top Networks with Plug-in Residual Input-Conditioned Mixture of Expert》在 arXiv API 这一方向上的推进。强调异构硬件协同推理。从实验上看，On FiBiNET and DCNv2, PRIME outperforms APG in all ten seed-level AUC comparisons while using fewer parameters and lower inference latency on both backbones.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Measure Before You Manage: Evaluating Agent Working Memory in Coding Agents](https://arxiv.org/abs/2608.31057v1)
  - 主题: Coding agent routing, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Coding agent routing、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Measure Before You Manage: Evaluating Agent Working Memory in Coding Agents》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Their evaluation shows that calibration gains may not transfer to held-out tasks, and that equal token budgets do not imply equal delivered context or management cost.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Structure Aware Neural Architecture Search for Mixture of Experts](https://arxiv.org/abs/2608.29817)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Structure Aware Neural Architecture Search for Mixture of Experts》在 arXiv cs.LG 这一方向上的推进。强调异构硬件协同推理。从实验上看，On a heterogeneous image-classification mixture the method recovers the underlying domain partition on 95% of clusters without ever observing domain labels, and on that benchmark and a four-domain time-series forecasting one alike it outperforms the MoE and NAS baselines that likewise use no label information.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：95%。
- [A-MADiff: Attention-Guided Multi-Agent DRL with Diffusion Policies for Memory-Aware Task Orchestration in Mobile AIGC Networks](https://arxiv.org/abs/2608.29255)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《A-MADiff: Attention-Guided Multi-Agent DRL with Diffusion Policies for Memory-Aware Task Orchestration in Mobile AIGC Networks》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Numerical results demonstrate that A-MADiff significantly improves the cumulative reward over the state-of-the-art baseline.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Pro-Router: Token-Aware Progressive Model Routing with Adaptive Edge-Cloud Collaboration for Efficient Multimodal LLM Inference](https://arxiv.org/abs/2608.28726)
  - 主题: Cost-efficient LLM inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、LLM routing，核心内容是《Pro-Router: Token-Aware Progressive Model Routing with Adaptive Edge-Cloud Collaboration for Efficient Multimodal LLM Inference》在 arXiv cs.AI 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，Compared to other methods, it achieves the highest routing accuracy and improves routing speed by more than 10x.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：10x、75%。
- [Strong Drafts Need Compact Memories: Long-Context Speculative Decoding with Compressed KV Cache](https://arxiv.org/abs/2608.30252v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《Strong Drafts Need Compact Memories: Long-Context Speculative Decoding with Compressed KV Cache》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experiments on Llama~3.1-8B and 70B targets at prefix lengths up to 32K show that our method reduces draft-side memory by over 70%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：70%、2.08x、3.33x。
- [Uncertainty Makes It Stable: Curiosity-Driven Quantized Mixture-of-Experts](https://arxiv.org/abs/2511.11743)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Uncertainty Makes It Stable: Curiosity-Driven Quantized Mixture-of-Experts》在 arXiv cs.LG 这一方向上的推进。强调异构硬件协同推理。从实验上看，Evaluated on audio classification benchmarks (ESC-50, Quinn, UrbanSound8K), our 4-bit quantization maintains 99.9 percent of full-precision F1 (0.858 vs 0.859) with 4x compression and 31 percent energy savings versus 8-bit, while both achieve statistical parity with full precision (p > 0.05).
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：4x。
- [WnW: Waxing-and-Waning KV Cache for Long-Form Speech LLMs](https://arxiv.org/abs/2608.22704)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《WnW: Waxing-and-Waning KV Cache for Long-Form Speech LLMs》在 arXiv cs.CL 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，On LibriSpeech-Long with two 3B backbones (Voxtral-mini-3b and Qwen2.5-Omni-3B), WnW preserves near-Full-Cache accuracy while keeping only 20% of audio tokens on GPU, where prefill-only baselines fail to terminate.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：20%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

