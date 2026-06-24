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

- 日期: 2026-06-24
- 今日新论文: 15
- 今日新权威来源更新: 1
- 本周精选论文: 25
- 本周精选权威来源更新: 3
- 日报: `papers/2026-06-24.md`
- 周报: `digests/weekly-2026-06-24.md`

## 今日最值得看

- [A 35B Hybrid-Attention Mixture-of-Experts Model on a 6GB 2011 GPU: Hand-Written 4-bit CUDA Inference for Fermi](https://arxiv.org/abs/2606.24031v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《A 35B Hybrid-Attention Mixture-of-Experts Model on a 6GB 2011 GPU: Hand-Written 4-bit CUDA Inference for Fermi》在 arXiv API 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，On a 947-token prompt we reduce prefill latency from 57.2\,s to 37.5\,s ($-34\%$) through expert pinning, single-pass prefill, and NUMA interleaving, and we raise decode throughput from 2.8 to 8.6\,\tps{} ($\approx 3\times$) with the integer-SIMD kernel.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [CrossPool: Efficient Multi-LLM Serving for Cold MoE Models through KV-Cache and Weight Disaggregation](https://arxiv.org/abs/2606.24506)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《CrossPool: Efficient Multi-LLM Serving for Cold MoE Models through KV-Cache and Weight Disaggregation》在 arXiv cs.DC 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，With efficient GPU memory pooling, CrossPool underpins bursty long-context requests and outperforms the state-of-the-art kvcached-based multi-LLM serving system, reducing P99 TBT by up to $10.4\times$.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Collaborative Lossless LLM Inference Serving with Offloading-based Pipeline Parallelism on Edge Devices](https://arxiv.org/abs/2512.21835)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Collaborative Lossless LLM Inference Serving with Offloading-based Pipeline Parallelism on Edge Devices》在 arXiv cs.DC 这一方向上的推进。强调异构硬件协同推理。从实验上看，Extensive experiments demonstrate that LOIP achieves 8.8$\times$$\sim$20.3$\times$ speedups over the SOTA baselines under different bandwidth conditions and request patterns without compromising model accuracy.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [VoltanaLLM: Energy-Efficient and SLO-Aware Disaggregated LLM Serving via Adaptive Frequency Control and State-Space Routing](https://arxiv.org/abs/2509.04827)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《VoltanaLLM: Energy-Efficient and SLO-Aware Disaggregated LLM Serving via Adaptive Frequency Control and State-Space Routing》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Our results show VoltanaLLM reduces end-to-end energy by up to 36.3% versus a static max-frequency baseline while maintaining high SLO attainment, and generalizes to newer GPUs.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：36.3%。
- [SkyChain Intelligence: A Blockchain-Secured Multi-Agent DRL Framework for Low-Altitude Embodied Artificial Intelligence](https://arxiv.org/abs/2606.24193)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《SkyChain Intelligence: A Blockchain-Secured Multi-Agent DRL Framework for Low-Altitude Embodied Artificial Intelligence》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Extensive simulations demonstrate that our framework outperforms state-of-the-art baselines in task completion latency and energy consumption, while achieving a 94.1% task completion rate in the baseline scenario and stable convergence within 300 training episodes.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：94.1%。
- [Does Mixture-of-Experts Actually Help Inference on Consumer and Edge Hardware? An Empirical Study](https://arxiv.org/abs/2606.21428)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《Does Mixture-of-Experts Actually Help Inference on Consumer and Edge Hardware? An Empirical Study》在 arXiv cs.AI 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，We benchmark OLMoE-1B-7B (1.3 B active of 6.9 B total) against three dense baselines on an Apple M2 Pro and an NVIDIA Jetson Orin Nano 8 GB through \texttt{llama.cpp}, measuring throughput, memory, and on-device energy.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：8 GB、9%。
- [The Serialized Bridge: Understanding and Recovering LLM Serving Performance under Blackwell GPU Confidential Computing](https://arxiv.org/abs/2606.23969)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《The Serialized Bridge: Understanding and Recovering LLM Serving Performance under Blackwell GPU Confidential Computing》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Yet LLM serving under Intel TDX plus GPU-CC still loses 13-27% of throughput, and KV-cache restore latency can more than double.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：27%、131%、34x。
- [Accelerating Disaggregated RL for Visual Generative LLMs with Diffusion-Based Parallelism and Trainer-Assisted Generation](https://arxiv.org/abs/2606.24369)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《Accelerating Disaggregated RL for Visual Generative LLMs with Diffusion-Based Parallelism and Trainer-Assisted Generation》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Experimental results show that DigenRL achieves 1.56-2.10x throughput improvements over state-of-the-art diffusion RL systems, veRL-Omni and GenRL.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：2.10x。
- [Systematic Exploration of 4-Expert Heterogeneous Mixture-of-Experts via Automated Pipeline Search](https://arxiv.org/abs/2606.23739)
  - 主题: Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference，核心内容是《Systematic Exploration of 4-Expert Heterogeneous Mixture-of-Experts via Automated Pipeline Search》在 arXiv cs.LG 这一方向上的推进。强调异构硬件协同推理。从实验上看，A critical finding emerged from the campaign: due to alphabetical enumeration via itertools.combinations, the entire explored search space (4.8% of the theoretical 23,751 possible 4-family combinations) is anchored to a single family, AirNet.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：4.8%。
- [Sakana Fugu Technical Report](https://arxiv.org/abs/2606.21228)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《Sakana Fugu Technical Report》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，We release two models: Fugu, which balances performance with latency for everyday use, and Fugu-Ultra, which prioritizes answer quality on the hardest problems.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

