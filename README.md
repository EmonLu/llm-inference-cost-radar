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

- 日期: 2026-09-10
- 今日新论文: 15
- 今日新权威来源更新: 1
- 本周精选论文: 25
- 本周精选权威来源更新: 5
- 日报: `papers/2026-09-10.md`
- 周报: `digests/weekly-2026-09-10.md`

## 今日最值得看

- [KVShareArena: KV-Cache Reuse Across Contexts and Model Checkpoints](https://arxiv.org/abs/2609.10266v1)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《KVShareArena: KV-Cache Reuse Across Contexts and Model Checkpoints》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Repair methods for such caches have appeared in three separate communities, each measured on its own terms, and existing benchmarks test only exact-prefix reuse, where nothing is lost.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Epoch: Compiling Diffusion Blocks for Sparse MoE Serving](https://arxiv.org/abs/2609.09748)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Epoch: Compiling Diffusion Blocks for Sparse MoE Serving》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，\sys{} improves end-to-end execution time by up to 2.7$\times$ over the strongest surviving baseline under the same 8-GPU placement and remains feasible at the largest batch sizes where multiple baselines run out of memory, while preserving task quality relative to the dense reference.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [AgentServeSim: Serving-System Simulation and Policy Search for LLM Agent Programs](https://arxiv.org/abs/2606.09613)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《AgentServeSim: Serving-System Simulation and Policy Search for LLM Agent Programs》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Mean JCT error remains within 5.5% on B200 and 5.2% in the saturated RTX PRO 6000 regime.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：5.5%、5.2%、0.5%。
- [EcoFair: Energy-Efficient Inference Routing for Edge AI under Data Degradation](https://arxiv.org/abs/2603.26483)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《EcoFair: Energy-Efficient Inference Routing for Edge AI under Data Degradation》在 arXiv cs.LG 这一方向上的推进。强调异构硬件协同推理。从实验上看，Results show that EcoFair can reduce per-sample image-inference energy by up to 68\% relative to always using the heavyweight encoder, while selectively allocating additional computation under difficult data regimes to support inference reliability.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Distribution-Consistent Inference for Dynamic Sparse Mixture-of-Experts](https://arxiv.org/abs/2609.09241v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Distribution-Consistent Inference for Dynamic Sparse Mixture-of-Experts》在 arXiv API 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，Across multiple SMoE LLMs, benchmarks, and routing strategies, LDA recovers much of the performance lost induced by the distributional shift under reduced routing while preserving sparse-inference efficiency with negligible overhead.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [EStream: Fast and Memory-Efficient MoE Prefill through Expert Virtualization on Mobile NPUs](https://arxiv.org/abs/2609.06551)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《EStream: Fast and Memory-Efficient MoE Prefill through Expert Virtualization on Mobile NPUs》在 arXiv cs.LG 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Compared to the fastest baseline at each setting, EStream achieves a 2.25--27.57X pure-prefill TTFT speedup and reduces peak physical memory by 1.19--12.29X.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：27.57X、12.29X。
- [Where Is the Tradeoff in Using Third-Party API Routers for Agentic Software Development?](https://arxiv.org/abs/2607.23624)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing, LLM routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing、LLM routing，核心内容是《Where Is the Tradeoff in Using Third-Party API Routers for Agentic Software Development?》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，In coding-agent workflows, high-autonomy operation is widely adopted because it reduces interaction overhead.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Can We Trust Video Hallucination Detectors? VidHalLoc for Evaluating the Evaluators](https://arxiv.org/abs/2609.09895v1)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《Can We Trust Video Hallucination Detectors? VidHalLoc for Evaluating the Evaluators》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Evaluation of fifteen methods reveals that the four dedicated detectors peak at an Overall accuracy of only 34.63%, indicating limited reliability across video hallucination types [Dataset Repository: https://huggingface.co/datasets/wesfggfd/VidHalLoc].
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：34.63%。
- [Less is MoE: Trimming Experts in Domain-Specialist Language Models](https://arxiv.org/abs/2606.05538)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Less is MoE: Trimming Experts in Domain-Specialist Language Models》在 arXiv cs.CL 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，At the same 50% MoE compression ratio, Fisher-MoE preserves model capability, while reducing weight memory by ~45% and improving inference throughput by 21%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：50%、45%、21%。
- [XAgent: eXecution-guided Agentic AI for Effective Localization and Resolution of GitHub Issues](https://arxiv.org/abs/2609.09769v1)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing，核心内容是《XAgent: eXecution-guided Agentic AI for Effective Localization and Resolution of GitHub Issues》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，The experimental results on the SWE-bench-lite dataset demonstrate that XAgent outperforms other existing approaches, achieving a resolve rate of 62.0% and a function localization accuracy of 72.8%, while maintaining cost efficiency.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：62.0%、72.8%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

