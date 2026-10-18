# LLMs, local inference and RAG

[Back to the index](../README.md)

## In short

Large language models are now a commodity layer with three ways to use them: hosted APIs, gateways that route between providers, and local inference on your own hardware. Most real work is in what surrounds the model.

- **Pick models by measurement, not by hype.** Leaderboards disagree because they measure different things. Artificial Analysis and LMArena cover general quality, speed and price; task benchmarks (SWE-bench style, long context like RULER, memory like LongMemEval) tell you more about your use case. Run your own small eval with Promptfoo or DeepEval before switching.
- **Local is practical.** Ollama, LM Studio and llama.cpp-based tools run quantized open models on a laptop or a single GPU box. vLLM is the standard when you need throughput. llmfit tells you what fits your hardware before you download 40 GB.
- **One API in front of many.** LiteLLM or OpenRouter give you an OpenAI-compatible interface over dozens of providers, which makes fallbacks and cost routing (RouteLLM) cheap to add.
- **Agents are loops with tools.** Frameworks come and go (AutoGPT and BabyAGI were the first wave; LangChain, CrewAI and smolagents the current one). The durable knowledge is in the pattern guides from OpenAI and Anthropic: start with a single agent and add more only when the task really splits.
- **RAG starts with clean input.** Converting documents to Markdown (markitdown) and chunking them well matters more than the vector database you pick.
- **Prompting is still a skill.** The vendor guides (Claude prompting best practices, Prompt Engineering Guide) are short and worth reading once.

**Where to start:** Ollama plus Open WebUI locally, LiteLLM as the gateway, Artificial Analysis to choose models, the OpenAI and Claude cookbooks for patterns.

## Contents

- [Learning and newsletters](#learning-and-newsletters)
- [Evaluation and benchmarks](#evaluation-and-benchmarks)
- [Models and model hubs](#models-and-model-hubs)
- [Agent frameworks](#agent-frameworks)
- [Local inference](#local-inference)
- [Prompting](#prompting)
- [Agent patterns and research](#agent-patterns-and-research)
- [Serving, gateways and routing](#serving-gateways-and-routing)
- [Safety and security](#safety-and-security)
- [RAG and memory](#rag-and-memory)
- [Fine-tuning](#fine-tuning)

## Learning and newsletters

- [OpenAI Cookbook](https://cookbook.openai.com/) ⭐ - Example notebooks and guides for building with OpenAI models.
- [2025: The year in LLMs](https://simonw.substack.com/p/2025-the-year-in-llms) - Simon Willison yearly review of major developments in large language models.
- [agents-course](https://huggingface.co/agents-course) - Hugging Face course on building AI agents, with tutorials and notebooks.
- [Ahead of AI](https://magazine.sebastianraschka.com/) - Sebastian Raschka newsletter on machine learning and AI research.
- [ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub) - In-depth tutorials on LLMs, RAG and real-world AI agent applications.
- [aie-book](https://github.com/chiphuyen/aie-book) - Supporting resources and materials for the book AI Engineering by Chip Huyen.
- [Anthropic AI Fluency](https://www.anthropic.com/ai-fluency) - Free Anthropic course on collaborating with AI systems effectively, efficiently, ethically and safely.
- [awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents) - Curated list of AI autonomous agent projects and frameworks.
- [Awesome-LLM](https://github.com/Hannibal046/Awesome-LLM) - Curated list of large language model papers, models and resources.
- [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) - Large collection of LLM apps, AI agents and RAG examples on OpenAI, Anthropic, Gemini and open models.
- [claude-cookbooks](https://github.com/anthropics/anthropic-cookbook) - Official notebooks and recipes showing practical ways to use Claude; formerly anthropic-cookbook.
- [LLM Visualization](https://bbycroft.net/llm) - Interactive 3D walkthrough of how a large language model works internally.
- [The Big LLM Architecture Comparison](https://magazine.sebastianraschka.com/p/the-big-llm-architecture-comparison) - Sebastian Raschka overview comparing the architecture designs of modern open LLMs.
- [Transformer Explainer](https://poloclub.github.io/transformer-explainer) - Interactive visualization explaining step by step how transformer language models work.
- [Vision Language Models 2025](https://huggingface.co/blog/vlms-2025) - Hugging Face blog overview of vision language models in 2025, covering architectures and progress.
- [AI Resources (airesources.dev)](https://web.archive.org/web/20250622074232/https://www.airesources.dev) - Curated list of AI resources, here saved as a 2025 web archive copy.
- [annotateai](https://github.com/neuml/annotateai) - Automatically annotates research papers using LLMs.
- [awesome-opensource-ai](https://github.com/alvinreal/awesome-opensource-ai) - Curated list of open-source AI projects, models, tools and infrastructure.
- [awesome_ai_agents](https://github.com/jim-schwoebel/awesome_ai_agents) - Large curated list of more than 1,500 resources and tools related to AI agents.
- [ChatGPT Prompt Engineering for Developers](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers) - Short free course on prompt engineering for developers using LLM APIs.
- [GPT from Scratch](https://jaketae.github.io/study/gpt) - Blog post walking through building a GPT-style language model with Hugging Face transformers.
- [LabLab.ai](https://lablab.ai/) - Community platform running hackathons for AI builders.
- [LLM Wiki course](https://pawel.lipowczan.pl/llm-wiki/kurs) - Free course on building a self-updating knowledge base for an AI agent from a template.
- [llm-from-scratch](https://github.com/angelos-p/llm-from-scratch) - Repository for building a language model from scratch, as a learning project.
- [Miniature GPT text generation example](https://keras.io/examples/generative/text_generation_with_miniature_gpt) - Keras code example showing how to train a small GPT for text generation.
- [OpenAI Academy](https://academy.openai.com/) - OpenAI's free learning hub with courses on using AI effectively.
- [Oracle AI Developer Hub](https://oracle-devrel.github.io/oracle-ai-developer-hub) - Technical resources for building AI apps and agents with Oracle AI Database and OCI.
- [Promptowy](https://promptowy.com/) - Polish-language blog on AI news, model reviews and tools.
- [Spring AI in Practice e-book](https://effectivedev.pl/ebook/spring-ai) - Free e-book on building a conversational agent with Spring AI in Java.
- [Towards AI](https://towardsai.net/) - AI education and deployment firm that trains AI engineers and builds custom AI systems for enterprises.

## Evaluation and benchmarks

- [Artificial Analysis](https://artificialanalysis.ai/) ⭐ - Independent benchmarks comparing AI models and API providers on quality, price and speed.
- [arena-hard-auto](https://github.com/lmarena/arena-hard-auto) - Automatic LLM benchmark that uses LLM judges to compare models on hard prompts.
- [Big Benchmarks Collection](https://huggingface.co/collections/open-llm-leaderboard/the-big-benchmarks-collection-64faca6335a7fc7d4ffe974a) - Hugging Face collection of benchmark spaces beyond the Open LLM Leaderboard.
- [DeepEval](https://deepeval.com/docs/getting-started) - Open-source LLM evaluation framework; this page is its quickstart guide.
- [Helicone](https://github.com/helicone/helicone) - Open-source LLM observability platform to monitor, evaluate and experiment with prompts.
- [LiveBench](https://livebench.ai/) - LLM benchmark with questions refreshed over time to limit test contamination.
- [LLM Stats](https://llm-stats.com/) - Leaderboard ranking AI models by intelligence, speed and price from public benchmark data.
- [LMArena](https://lmarena.ai/) - Crowdsourced platform for comparing and ranking AI chat models through blind votes.
- [LongMemEval](https://github.com/xiaowu0162/LongMemEval) - Benchmark for long-term interactive memory in chat assistants, published at ICLR 2025.
- [MT Bench PL](https://huggingface.co/spaces/speakleash/mt-bench-pl) - Hugging Face Space for comparing language model answers in Polish, with pairwise evaluation.
- [Open LLM Leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard) - Hugging Face space ranking open-source language models on standard benchmark suites.
- [Promptfoo](https://www.promptfoo.dev/) - Open-source tool for testing and red-teaming LLM applications and prompts.
- [RULER](https://github.com/NVIDIA/RULER) - Benchmark source code measuring the effective context length of long-context LLMs.
- [llmperf-leaderboard](https://github.com/ray-project/llmperf-leaderboard) - Leaderboard comparing LLM inference performance across models and providers.
- [OpenRouter Rankings](https://openrouter.ai/rankings) - Model rankings based on tokens processed through the OpenRouter API.
- [quanteval.ai](https://quanteval.ai/) - Independent benchmark reports and speed tests for quantized open models.
- [RemakeBench](https://remakebench.com/tests) - Archive of AI game-building, graphics and CAD experiments used as benchmarks.
- [Senior SWE-Bench](https://senior-swe-bench.snorkel.ai/) - Benchmark evaluating AI agents on senior-level software engineering tasks.
- [Spark Arena](https://spark-arena.com/leaderboard) - LLM leaderboard for models running on NVIDIA DGX Spark hardware.
- [SparkBench](https://wesche.com/dgx) - Benchmarks of local LLM deployments on one, two and four DGX Spark systems.
- [Style control in Chatbot Arena](https://lmsys.org/blog/2024-08-28-style-control) - LMSYS blog on separating answer style from substance in chatbot rankings.
- [SWELancer-Benchmark](https://github.com/openai/SWELancer-Benchmark) - Dataset and code for SWE-Lancer, a benchmark of freelance software engineering tasks for LLMs.
- [Unofficial Aider Polyglot leaderboard](https://leaderboard.techfren.net/) - Unofficial leaderboard of LLM results on the Aider polyglot coding benchmark.

## Models and model hubs

- [Hugging Face](https://huggingface.co/) ⭐ - Hub for open-source ML models, datasets and demo apps, run by Hugging Face.
- [Hugging Face (GitHub org)](https://github.com/huggingface) ⭐ - GitHub organization of Hugging Face, maintaining transformers, diffusers and other ML libraries.
- [BLOOM](https://huggingface.co/bigscience/bloom) - Open multilingual large language model from the BigScience project.
- [DeepSeek](https://github.com/deepseek-ai) - Official GitHub organization of DeepSeek, publisher of open-weight models and research code.
- [DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437) - arXiv technical report describing the DeepSeek-V3 large language model.
- [Google AI Studio](https://aistudio.google.com/) - Google web studio for trying prompts and building apps with Gemini models.
- [Hugging Face docs](https://huggingface.co/docs) - Official documentation for Hugging Face libraries and hub.
- [Mistral AI](https://mistral.ai/) - Company offering open-weight frontier models that can run on-prem, in a VPC or in its cloud.
- [Models.dev](https://models.dev/) - Open-source database of AI model specifications, pricing and features.
- [NVIDIA NGC Catalog](https://catalog.ngc.nvidia.com/) - NVIDIA catalog of GPU-optimized AI, ML and HPC containers, models and resources.
- [OpenAI](https://github.com/openai) - Official GitHub organization of OpenAI, publishing open-source SDKs, evals and research code.
- [DeepClaude](https://deepclaude.com/) - Project combining DeepSeek R1 reasoning traces with Anthropic Claude models.
- [Falcon-40B](https://huggingface.co/tiiuae/falcon-40b) - Hugging Face model page for the Falcon-40B open language model.
- [LLaVA model zoo](https://github.com/haotian-liu/LLaVA/blob/main/docs/MODEL_ZOO.md) - Model zoo for LLaVA, a visual instruction-tuned multimodal model.
- [LMSYS Org](https://lmsys.org/) - Research organization behind open large model evaluation and serving projects.
- [MiniGPT-4](https://minigpt-4.github.io/) - Project page for MiniGPT-4, a vision-language model built on a frozen LLM.
- [model-catalog](https://github.com/lmstudio-ai/model-catalog/tree/main) - Standardized JSON descriptors for LLM model files, maintained by LM Studio.
- [multislav-4slav](https://huggingface.co/allegro/multislav-4slav) - Slavic-language model released by Allegro on Hugging Face.
- [NVIDIA NIM API models](https://build.nvidia.com/models) - NVIDIA catalog of hosted AI models accessible through NIM APIs.
- [Reka](https://www.reka.ai/) - Company building natively multimodal models for video, image, audio and text.
- [Sky-T1](https://novasky-ai.github.io/posts/sky-t1) - Project for training an o1-preview-level reasoning model for under $450.
- [tencent-ailab (GitHub org)](https://github.com/tencent-ailab) - GitHub organization of Tencent AI Lab with research code repositories.
- [xAI](https://x.ai/) - AI company behind the Grok models and API.

## Agent frameworks

- [LangChain](https://github.com/hwchase17/langchain) ⭐ - Framework for building applications with large language models, with components and agent tooling.
- [AutoGPT](https://github.com/Significant-Gravitas/Auto-GPT) - Project for building and running autonomous GPT-based agents, an early influential agent project.
- [BabyAGI](https://github.com/yoheinakajima/babyagi) - Original task-driven autonomous agent script that spawned many agent projects.
- [crewAI](https://github.com/joaomdmoura/crewAI) - Framework for orchestrating role-based autonomous AI agents that collaborate on tasks.
- [E2B](https://e2b.dev/) - Cloud sandboxes where AI agents run code, browse and use tools in isolation.
- [elizaOS](https://github.com/elizaos/eliza) - Open-source framework for building autonomous AI agents across platforms and integrations.
- [hermes-agent](https://github.com/nousresearch/hermes-agent) - AI agent from Nous Research that builds skills and memory over time with the user.
- [LangChain docs](https://python.langchain.com/v0.2/docs/introduction) - Documentation for LangChain, a framework for building LLM applications with agents and tools.
- [langchain4j](https://github.com/langchain4j/langchain4j) - Open-source Java library for building LLM-powered applications on the JVM.
- [MetaGPT](https://github.com/geekan/MetaGPT) - Multi-agent framework where LLM agents take software company roles to build projects.
- [smolagents](https://github.com/huggingface/smolagents) - Lightweight Hugging Face library for agents that write and run Python code to call tools.
- [AgentGPT](https://agentgpt.reworkd.ai/) - Browser-based platform for configuring and running autonomous AI agents.
- [agenticSeek](https://github.com/Fosowl/agenticSeek) - Autonomous agent meant to run locally, browsing the web and writing code.
- [AutoGPT docs](https://docs.agpt.co/setup) - Setup and documentation for AutoGPT, an autonomous agent platform.
- [CopilotKit OpenBot](https://github.com/CopilotKit/openbot) - Open-source AI agents, each with its own browser and files, with actions approved before running.
- [CrewAI platform](https://www.crewai.com/) - Commercial hosted platform for building and deploying multi-agent AI systems.
- [hermes-desktop](https://github.com/fathah/hermes-desktop) - Desktop companion app for the Hermes Agent.
- [meta-agent](https://github.com/DannyMac180/meta-agent) - Agent built on the OpenAI Agents SDK that generates new agents.
- [Open-Assistant](https://github.com/LAION-AI/Open-Assistant) - Open-source chat assistant project from LAION that can use tools and retrieve information.
- [OpenManus](https://openmanus.github.io/) - Open-source framework for building AI agents, as an open alternative to Manus.
- [Paperclip docs](https://paperclipai-paperclip.mintlify.app/introduction) - Open-source orchestration platform docs for running teams of autonomous AI agents.
- [PocketFlow](https://github.com/The-Pocket/PocketFlow/blob/main/pocketflow/__init__.py) - Minimal framework of about 100 lines for building LLM and agent workflows as graphs.

## Local inference

- [Ollama](https://ollama.com/) ⭐ - Tool to run and build with open AI models locally on macOS, Windows and Linux.
- [exo](https://github.com/exo-explore/exo) - Runs AI models across a home cluster of everyday devices.
- [ollama-cluster](https://github.com/shadoq/ollama-cluster) - Ollama fork that splits models too large for one machine across two NVIDIA DGX Spark over the llama.cpp RPC backend (by the author of this list).
- [GPT4All](https://github.com/nomic-ai/gpt4all) - Desktop app and library for running local LLMs on consumer hardware.
- [ipex-llm](https://github.com/intel/ipex-llm) - Library that accelerates local LLM inference and fine-tuning on Intel XPUs, including iGPU and NPU.
- [llmfit](https://github.com/AlexsJones/llmfit) - CLI that shows which local LLMs and providers fit a given machine's hardware.
- [LM Studio](https://lmstudio.ai/) - Desktop app for discovering, downloading and running local LLMs.
- [LocalAI](https://github.com/mudler/LocalAI) - OpenAI-compatible local AI engine that runs LLMs, vision, voice and image models on any hardware.
- [Open WebUI](https://docs.openwebui.com/) - Self-hosted web interface for Ollama and OpenAI-compatible LLM APIs.
- [text-generation-webui](https://github.com/oobabooga/text-generation-webui) - Gradio web UI for running local LLMs, now published as the textgen desktop app.
- [airllm](https://github.com/lyogavin/airllm) - Library that runs very large models on a single 4 GB GPU by loading layers one at a time.
- [amd-strix-halo-toolboxes](https://github.com/kyuz0/amd-strix-halo-toolboxes) - Toolboxes for running LLMs on AMD Strix Halo hardware.
- [K/V Cache Quantization in Ollama](https://mitjamartini.com/blog/kv-cache-quantization-in-ollama) - Blog post explaining K/V cache quantization for memory savings in Ollama.
- [LLM Benchmark (Ollama results)](https://llm.aidatatools.com/results-linux.php) - Community table of Ollama throughput results for local LLMs on various hardware.
- [NVIDIA DGX Spark forum](https://forums.developer.nvidia.com/c/accelerated-computing/dgx-spark-gb10/dgx-spark-gb10/721) - NVIDIA developer forum section for DGX Spark / GB10 users.
- [Pinokio](https://pinokio.co/) - Launcher that installs and runs open-source AI apps with one click.
- [RC-Home-Assistant-Low-VRAM](https://github.com/RoyalCities/RC-Home-Assistant-Low-VRAM) - Local voice assistant stack for Home Assistant with Ollama models tuned for low-VRAM GPUs.

## Prompting

- [Claude prompting best practices](https://docs.anthropic.com/en/prompt-library/library) ⭐ - Anthropic guide to prompting Claude models, covering examples, XML tags and agentic use.
- [DSPy](https://github.com/stanfordnlp/dspy) - Framework for programming language models with modules and optimizers instead of hand-written prompts.
- [Fabric](https://github.com/danielmiessler/fabric) - Open-source framework that applies crowdsourced AI prompt patterns to specific tasks.
- [Learn Prompting](https://learnprompting.org/docs/introduction) - Free guide to generative AI and prompt engineering for beginners and advanced users.
- [Prompt Engineering Guide](https://www.promptingguide.ai/) - Comprehensive open guide to prompt engineering techniques.
- [prompts.chat (awesome-chatgpt-prompts)](https://github.com/f/awesome-chatgpt-prompts) - Open-source community prompt library for ChatGPT and other LLMs, also self-hostable.
- [agency-agents](https://github.com/msitarzewski/agency-agents) - Collection of AI agent personas, from frontend developers to community managers, as prompt files.
- [Claude use cases (Claude Academy)](https://www.claude.com/resources/use-cases) - Practical examples of Claude use across research, writing, coding and analysis.
- [claude-prompt-generator](https://github.com/aws-samples/claude-prompt-generator/tree/main) - AWS sample project for generating prompts for Claude models.
- [grok-prompts](https://github.com/xai-org/grok-prompts/tree/main) - Published system prompts for xAI's Grok chat assistant and the @grok bot on X.
- [headroom](https://github.com/chopratejas/headroom) - Compresses tool outputs, logs and RAG chunks before they reach the LLM, reducing tokens.
- [Snack Prompt](https://www.snackprompt.com/) - Marketplace for sharing and remixing AI prompts and automations.
- [system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) - Collection of extracted system prompts from popular chatbots and coding tools.
- [Wordware](https://www.wordware.ai/) - Environment for building LLM apps and agents as structured prompts.

## Agent patterns and research

- [CAMEL-AI](https://www.camel-ai.org/) - Open-source community researching multi-agent systems for data generation and simulation.
- [Claude multi-agent coordination patterns](https://claude.com/blog/multi-agent-coordination-patterns) - Anthropic article comparing five multi-agent coordination patterns and their trade-offs.
- [GenAI_Agents](https://github.com/NirDiamant/GenAI_Agents) - Tutorials and implementations of generative AI agent techniques, from basic bots to multi-agent systems.
- [OpenAI practical guide to building agents](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf) - OpenAI's PDF guide on designing and building AI agents.
- [UI-TARS](https://github.com/bytedance/UI-TARS) - Open-source native GUI agent models for automating desktop and mobile interfaces.
- [25 Days of Agents](https://www.25daysofagents.com/) - Advent calendar of AI agent tutorials and examples.
- [Agentic Design Patterns (Google Doc)](https://docs.google.com/document/u/0/d/1rsaK53T3Lg5KoGwvf8ukOUvbELRtH-V0LnOIFDxBryE/mobilebasic) - Book on agentic AI design patterns, shared as a Google Doc.
- [claw0](https://github.com/shareAI-lab/claw0) - Step-by-step sections for building an AI agent from scratch, as a learning project.
- [cua](https://github.com/trycua/cua) - Open-source sandboxes and drivers for computer-use AI agents, with benchmarks.
- [LLM agents are simply graphs (tutorial)](https://zacharyhuang.substack.com/p/llm-agent-internal-as-a-graph-tutorial) - Tutorial explaining LLM agents as graph-based workflows.
- [ottomator-agents](https://github.com/coleam00/ottomator-agents/tree/main) - Collection of open-source AI agents from the oTTomator Live Agent Studio platform.
- [rea](https://github.com/morluto/rea) - Reverse-engineering toolkit where agents analyze app behavior down to native binaries.
- [TinyTroupe](https://github.com/microsoft/TinyTroupe) - Library for LLM-powered multi-agent persona simulations, for imagination and business insights.

## Serving, gateways and routing

- [LiteLLM](https://github.com/BerriAI/litellm) ⭐ - Python SDK and proxy gateway for calling 100+ LLM APIs in OpenAI format.
- [vLLM](https://vllm.ai/) ⭐ - High-throughput, memory-efficient inference and serving engine for large language models.
- [LiteLLM docs](https://docs.litellm.ai/) - Documentation for LiteLLM, a library and proxy for calling many LLM APIs in OpenAI format.
- [OpenRouter](https://openrouter.ai/) - Unified API gateway for accessing many LLMs with a comparable pricing view.
- [Replicate](https://replicate.com/) - Platform for running open-source machine learning models through a cloud API.
- [RouteLLM](https://github.com/lm-sys/RouteLLM) - Framework for serving and evaluating LLM routers that cut costs without losing quality.
- [tiny-vllm](https://github.com/jmaczan/tiny-vllm) - Educational LLM inference engine in C++ and CUDA, a small version of vLLM.
- [Together AI](https://www.together.ai/) - Cloud platform for LLM inference, fine-tuning and GPU clusters.
- [Cog](https://github.com/replicate/cog) - Tool that packages machine learning models into Docker containers with a standard API.
- [Fireworks AI](https://fireworks.ai/models) - Hosted inference platform for open-source LLMs and image models, with fine-tuning.
- [langchain-serve](https://github.com/jina-ai/langchain-serve) - Tool for deploying LangChain applications to production with FastAPI and Jina.
- [SiliconFlow](https://www.siliconflow.com/) - Hosted API platform for running and fine-tuning over 200 LLM and multimodal models.
- [vLLM 2023 launch post](https://blog.vllm.ai/2023/06/20/vllm.html) - Original 2023 vLLM announcement on PagedAttention for KV cache memory management.

## Safety and security

- [Neuronpedia](https://www.neuronpedia.org/) - Open-source platform for exploring and interpreting neural network features.
- [AdvBench](https://huggingface.co/datasets/walledai/AdvBench) - Benchmark dataset of harmful prompts used to evaluate LLM safety and refusals.
- [AI agent compliance checklist (Secra)](https://www.sec-ra.com/blog/ai-agent-compliance-checklist-enterprise-security) - 28-item checklist covering logging and access controls for enterprise AI agent approval.
- [Broken Hill (Bishop Fox)](https://bishopfox.com/blog/brokenhill-attack-tool-largelanguagemodels-llm) - Bishop Fox write-up of the GCG jailbreak attack and their Broken Hill testing tool.
- [CAI](https://github.com/aliasrobotics/cai) - Open framework for building AI agents for cybersecurity testing and AI security.
- [JailbreakHub](https://huggingface.co/datasets/walledai/JailbreakHub) - Research dataset of jailbreak prompts for LLM safety evaluation.
- [Superagent](https://github.com/superagent-ai/superagent) - Open-source guardrails that protect AI applications against prompt injection and data leaks.
- [The Provenance Tax (Lasso Security)](https://www.lasso.security/blog/the-provenance-tax-understanding-the-impact-of-llm-watermarking-on-ai-agent-behavior) - Research post on how SynthID-Text watermarking changes agent tool-call correctness and refusals.

## RAG and memory

- [LlamaIndex](https://github.com/run-llama/llama_index) - Data framework for building LLM applications over your own documents.
- [markitdown](https://github.com/microsoft/markitdown) - Python tool that converts Office documents, PDFs and other files to Markdown for LLMs.
- [EmbedAnything](https://github.com/StarlightSearch/EmbedAnything) - Rust library for multimodal embedding ingestion, local inference and indexing.
- [memU](https://github.com/NevaMind-AI/MemU) - Memory framework for long-running proactive AI agents, storing personal memory shared across agents.
- [screenpipe](https://github.com/mediar-ai/screenpipe) - Library that continuously records computer activity to build personalized AI from it.

## Fine-tuning

- [Drag-and-Drop LLMs](https://jerryliang24.github.io/DnD) - Project page for a paper on generating LLM weights from a prompt without training.
- [H2O LLM Studio](https://github.com/h2oai/h2o-llmstudio) - Framework and no-code GUI for fine-tuning large language models.
- [lora-speedrun](https://github.com/Saivineeth147/lora-speedrun) - Speedrun benchmark for LoRA fine-tuning with a fixed task, fixed hardware and a public leaderboard.
