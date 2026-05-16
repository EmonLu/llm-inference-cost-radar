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

- 日期: 2026-05-16
- 今日新论文: 15
- 今日新权威来源更新: 0
- 本周精选论文: 25
- 本周精选权威来源更新: 3
- 日报: `papers/2026-05-16.md`
- 周报: `digests/weekly-2026-05-16.md`

## 今日最值得看

- [Coding Agent Is Good As World Simulator](https://arxiv.org/abs/2605.14398)
  - 主题: Coding agent routing
  - 中文解读: 这项工作主要关注Coding agent routing，核心内容是《Coding Agent Is Good As World Simulator》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experimental results show that our framework outperforms advanced video-based models in physical accuracy, instruction fidelity and visual quality, which could be applied to various scenarios including driving simulation and embodied robot tasks.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [BEAM: Binary Expert Activation Masking for Dynamic Routing in MoE](https://arxiv.org/abs/2605.14438v1)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《BEAM: Binary Expert Activation Masking for Dynamic Routing in MoE》在 arXiv API 这一方向上的推进。重点优化延迟，通常可带来更高性价比。从实验上看，Experiments show that BEAM retains over 98\% of the original model's performance while reducing MoE layer FLOPs by up to 85\%, achieving up to 2.5$\times$ faster decoding and 1.4$\times$ higher throughput, demonstrating its effectiveness as a practical, plug-and-play solution for efficient MoE inference.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Collider-Bench: Benchmarking AI Agents with Particle Physics Analysis Reproduction](https://arxiv.org/abs/2605.13950)
  - 主题: Agent systems and multi-agent efficiency, Coding agent routing
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency、Coding agent routing，核心内容是《Collider-Bench: Benchmarking AI Agents with Particle Physics Analysis Reproduction》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，arXiv:2605.13950v1 Announce Type: cross Abstract: Autonomous language-model agents are increasingly evaluated on long-horizon tool-use tasks, but existing benchmarks rarely capture the complexity and nuance of real scientific work.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [L2R: Low-Rank and Lipschitz-Controlled Routing for Mixture-of-Experts](https://arxiv.org/abs/2601.21349)
  - 主题: Cost-efficient LLM inference, Heterogeneous MoE inference, LLM routing
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference、Heterogeneous MoE inference、LLM routing，核心内容是《L2R: Low-Rank and Lipschitz-Controlled Routing for Mixture-of-Experts》在 arXiv cs.AI 这一方向上的推进。围绕 MoE 模型推理/部署优化，强相关。从实验上看，Extensive experiments on an OLMoE-based language MoE model and a vision MoE setting on ImageNet demonstrate that L2R consistently improves routing geometry, expert discrimination, and overall model performance.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [Agentic AI Ecosystems in Higher Education: A Perspective on AI Agents to Emerging Inclusive, Agentic Multi-Agent AI Framework for Learning, Teaching and Institutional Intelligence](https://arxiv.org/abs/2605.14266)
  - 主题: Agent systems and multi-agent efficiency
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency，核心内容是《Agentic AI Ecosystems in Higher Education: A Perspective on AI Agents to Emerging Inclusive, Agentic Multi-Agent AI Framework for Learning, Teaching and Institutional Intelligence》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，arXiv:2605.14266v1 Announce Type: new Abstract: Integration of artificial intelligent (AI) agents in higher education is transforming teaching, learning and administrative processes.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [LEMON: Learning Executable Multi-Agent Orchestration via Counterfactual Reinforcement Learning](https://arxiv.org/abs/2605.14483)
  - 主题: Agent systems and multi-agent efficiency
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency，核心内容是《LEMON: Learning Executable Multi-Agent Orchestration via Counterfactual Reinforcement Learning》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Experiments on six reasoning and coding benchmarks, including MMLU, GSM8K, AQuA, MultiArith, SVAMP, and HumanEval, show that LEMON achieves state-of-the-art performance among the evaluated multi-agent orchestration methods.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [GAMBIT: A Three-Mode Benchmark for Adversarial Robustness in Multi-Agent LLM Collectives](https://arxiv.org/abs/2605.09027)
  - 主题: Agent systems and multi-agent efficiency
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency，核心内容是《GAMBIT: A Three-Mode Benchmark for Adversarial Robustness in Multi-Agent LLM Collectives》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，Our contributions are threefold: (1) Using chess as a substrate deep reasoning problem and Gemini 3.1 Pro for agents, we release GAMBIT and its dataset to evaluate imposter detectors under realistic constraints against a stealthy adaptive imposter; (2) We introduce an adaptive imposter agent based on an efficient evolutionary framework, generalizable beyond chess, that collapses collective task performance while remaining essentially undetectable (50.5% F1-score with a Gemini-based detector); (3) We show that zero-shot evaluation can be highly misleading for adaptive adversaries: two detectors with near-identical zero-shot scores differ by 8x on few-shot adaptation, while the meta-learned variant converges 20x faster, a gap only visible in the recalibration mode.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：50.5%、8x、20x。
- [ReasonCache: Accelerating Large Reasoning Model Serving through KV Cache Sharing](https://arxiv.org/abs/2507.21433)
  - 主题: Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference，核心内容是《ReasonCache: Accelerating Large Reasoning Model Serving through KV Cache Sharing》在 arXiv cs.AI 这一方向上的推进。通过 KV cache 优化长上下文推理成本。从实验上看，Experimental evaluation demonstrates that ReasonCache achieves a peak throughput improvement of 89.2% and an average gain of 40-60%, leading to more responsive and cost-effective AI inference services.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：89.2%、60%。
- [PreFT: Prefill-only finetuning for efficient inference](https://arxiv.org/abs/2605.14217v1)
  - 主题: Cost-efficient LLM inference
  - 中文解读: 这项工作主要关注Cost-efficient LLM inference，核心内容是《PreFT: Prefill-only finetuning for efficient inference》在 arXiv API 这一方向上的推进。关注在线 serving 系统优化，适合成本控制。从实验上看，On SFT, we observe that the evaluation loss of PreFTs is higher than PEFTs, but can be compensated by increasing rank with nearly no reduction in throughput.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：请查看下方英文实验结论。
- [MetaAgent-X : Breaking the Ceiling of Automatic Multi-Agent Systems via End-to-End Reinforcement Learning](https://arxiv.org/abs/2605.14212)
  - 主题: Agent systems and multi-agent efficiency
  - 中文解读: 这项工作主要关注Agent systems and multi-agent efficiency，核心内容是《MetaAgent-X : Breaking the Ceiling of Automatic Multi-Agent Systems via End-to-End Reinforcement Learning》在 arXiv cs.AI 这一方向上的推进。与 agent 系统/工作流有关，纳入重点跟踪。从实验上看，MetaAgent-X consistently outperforms existing automatic MAS baselines, achieving up to 21.7% gains.
  - 中文实验结论: 实验结果的自动翻译暂时不可用，请优先参考下方英文实验结论；当前可先重点关注这些数值：21.7%。

## 配置

- 搜索规则: `config/topics.json`
- 论文去重状态: `data/seen_papers.json`
- 来源去重状态: `data/seen_feed_items.json`
- 抓取脚本: `scripts/fetch_arxiv_radar.py`

