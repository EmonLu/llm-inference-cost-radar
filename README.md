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

- 日期: 2026-07-02
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 2
- 日报: `papers/2026-07-02.md`
- 周报: `digests/weekly-2026-07-02.md`

## 今日最值得看

- [ELDR: Expert-Locality-Aware Decode Routing for PD-Disaggregated MoE Serving](https://arxiv.org/abs/2607.00466)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《ELDR: Expert-Locality-Aware Decode Routing for PD-Disaggregated MoE Serving》在 arXiv cs.DC 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Implemented in vLLM and evaluated on deployments of up to 40 GPUs, ELDR reduces median TPOT by 5.9-13.9% over the strongest of four load-balancing baselines across three MoE models and two workloads, with model outputs unchanged.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：13.9%。
- [SmoothAgent: Efficient Long-Horizon LLM-Based Agent Serving with Lookahead Context Engineering](https://arxiv.org/abs/2607.00151)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《SmoothAgent: Efficient Long-Horizon LLM-Based Agent Serving with Lookahead Context Engineering》在 arXiv cs.DC 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experiments show that our approach effectively eliminates transformation overhead and reduces TTFT by up to 11.9x.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：11.9x。
- [MosaicKV: Serving Long-Context LLM with Dynamic Two-D KV Cache Compression](https://arxiv.org/abs/2607.00760)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《MosaicKV: Serving Long-Context LLM with Dynamic Two-D KV Cache Compression》在 arXiv cs.DC 这一方向上的推进。涉及 CPU 侧参与推理或加速。从实验上看，Evaluation on an H800 GPU with multiple LLMs shows that MosaicKV delivers up to 16x attention speedup, 4.8x lower decode latency, and 7.3x higher throughput than the uncompressed baseline.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：16x、4.8x、7.3x。
- [Rise From The Ashes: LLM-based Static Analysis for Deep Learning Framework Bugs](https://arxiv.org/abs/2607.00555v1)
  - 主题: Agent systems and multi-agent efficiency, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Heterogeneous MoE inference，核心内容是《Rise From The Ashes: LLM-based Static Analysis for Deep Learning Framework Bugs》在 arXiv API 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Our evaluation shows that Phoenix is a practical complement to dynamic DL framework testing for bug finding.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Multi-scale Mixture of World Models for Embodied Agents in Evolving Environments](https://arxiv.org/abs/2607.00457)
  - 主题: Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Heterogeneous MoE inference、LLM routing，核心内容是《Multi-scale Mixture of World Models for Embodied Agents in Evolving Environments》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experiments on EmbodiedBench and HAZARD show that MuSix improves over state-of-the-art baselines on multi-scale reasoning and dynamic adaptation.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [When Less Latent Leads to Better Relay: Information-Preserving Compression for Latent Multi-Agent LLM Collaboration](https://arxiv.org/abs/2604.13349)
  - 主题: Agent systems and multi-agent efficiency, Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Cost-efficient LLM inference，核心内容是《When Less Latent Leads to Better Relay: Information-Preserving Compression for Latent Multi-Agent LLM Collaboration》在 arXiv cs.LG 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，With only 9.9%-20.2% of the prompt KV states retained, H-OBF delivers between $97%$ and $120%$ of full KV relay's per-benchmark accuracy across the nine benchmarks.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：9.9%、20.2%、97%。
- [ComplianceGate: Classifier-Gated Multi-Tier LLM Routing for Inference in Regulated Industries](https://arxiv.org/abs/2606.31163v2)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《ComplianceGate: Classifier-Gated Multi-Tier LLM Routing for Inference in Regulated Industries》在 arXiv API 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，Our evaluation on 600 queries demonstrates 39% median latency reduction, 33-52% cost savings depending on query distribution, and generation throughput of 122-200 tokens/second versus 50-64 for the baseline.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：39%、52%、200 tokens/s。
- [FED-FSTQ: Fisher-Guided Token Quantization for Communication-Efficient Federated Fine-Tuning of LLMs on Edge Devices](https://arxiv.org/abs/2604.25421)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference，核心内容是《FED-FSTQ: Fisher-Guided Token Quantization for Communication-Efficient Federated Fine-Tuning of LLMs on Edge Devices》在 arXiv cs.LG 这一方向上的推进。强调异构硬件协同推理。从实验上看，Experiments on multilingual QA and medical QA under non-IID partitions show that Fed-FSTQ reduces cumulative uplink traffic required to reach a fixed quality threshold by 46x relative to a standard LoRA baseline, and improves end-to-end wall-clock time-to-accuracy by 52%.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：46x、52%、1.55x。
- [PersistentKV: Page-Aware Decode Scheduling for Long-Context LLM Serving on Commodity GPUs](https://arxiv.org/abs/2606.26666)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《PersistentKV: Page-Aware Decode Scheduling for Long-Context LLM Serving on Commodity GPUs》在 arXiv cs.LG 这一方向上的推进。涉及 GPU 侧推理优化。从实验上看，With cost-model constants fixed on calibration traces, five held-out seeds improve mean wall decode-token throughput by 1.04x to 1.08x on B8 bimodal, uniform, and Zipf-like workloads, and by 1.40x on a B1 bucketed trace.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：1.04x、1.08x、1.40x。
- [FRAME: Learning the Adaptation Domain with a Mixture of Fractional-Fourier Experts](https://arxiv.org/abs/2607.00162)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《FRAME: Learning the Adaptation Domain with a Mixture of Fractional-Fourier Experts》在 arXiv cs.LG 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，Across commonsense, mathematical, code, and knowledge benchmarks on LLaMA-3.1-8B and Qwen2.5-7B, Fractional-Fourier Mixture of Experts improves over strong MoE-LoRA and spectral baselines -- including FlyLoRA, FourierMoE, and HMoRA -- while keeping the active-parameter budget small, and analysis shows that the learned orders specialize by task and layer in interpretable ways.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

