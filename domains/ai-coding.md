# AI coding assistants and agents

[Back to the index](../README.md)

## In short

AI coding moved from autocomplete to agents that read the repository, run commands and open pull requests. What separates good results from bad ones is no longer the model alone but the harness around it: instructions, context and verification.

- **Instructions are code.** A short `AGENTS.md` or `CLAUDE.md` with project rules, plus reusable skills for repeated workflows, gives more than switching models. Keep them small and specific; long rule files get ignored.
- **Context beats cleverness.** Agents fail on what they cannot see. Tools such as Repomix, gitingest and DeepWiki turn a repository into something a model can read in one go.
- **MCP is the plug standard.** The Model Context Protocol connects agents to databases, browsers and APIs. Start with the official docs, then pick servers from curated directories rather than installing everything.
- **Spec first, code second.** Spec-driven toolkits (spec-kit, OpenSpec) make the agent write and agree a plan before touching files, which cuts rework on larger tasks.
- **Verify, don't trust.** The essays below share one lesson: agents produce plausible code fast, so the bottleneck becomes review and tests. Quality drops when nobody owns that step.

**Where to start:** Aider or Claude Code for terminal work, Continue or Cline inside the editor, the AGENTS.md format for instructions, and the MCP docs once you need tools.

## Contents

- [Coding agents and IDEs](#coding-agents-and-ides)
- [Agent rules, instructions and skills](#agent-rules-instructions-and-skills)
- [Practices and essays](#practices-and-essays)
- [Codebase context tools](#codebase-context-tools)
- [MCP](#mcp)
- [Learning](#learning)

## Coding agents and IDEs

- [Aider](https://aider.chat/) ⭐ - Open-source AI pair programming tool that works in the terminal with git.
- [Claude Code subagents docs](https://code.claude.com/docs/en/sub-agents) ⭐ - Official Claude Code documentation on creating and using custom subagents.
- [Continue](https://github.com/continuedev/continue) ⭐ - Open-source AI coding assistant that connects any model to VS Code and JetBrains.
- [Bolt.new](https://bolt.new/) - AI tool that builds websites and apps from text prompts in the browser.
- [Claude Code Unpacked](https://ccunpacked.dev/) - Map of Claude Code internals: agent loop, tools, orchestration and unreleased features.
- [Cline](https://docs.cline.bot/getting-started/what-is-cline) - Open-source coding agent that reads files, edits code and runs commands with approval.
- [crush](https://github.com/charmbracelet/crush) - Terminal-based AI coding agent with a polished TUI, from Charmbracelet.
- [goose](https://github.com/block/goose) - Open-source extensible AI agent that installs, edits, runs and tests code with any LLM.
- [JetBrains Junie](https://github.com/JetBrains/junie) - JetBrains AI coding agent that works from the terminal, IDE or CI/CD with any LLM.
- [Kilo Code](https://kilocode.ai/) - Open-source AI coding agent for VS Code, JetBrains, CLI and cloud, with own keys or local models.
- [Lovable](https://lovable.dev/) - AI app builder that generates full-stack web apps from natural-language prompts.
- [opencode](https://github.com/sst/opencode) - Open-source AI coding agent for the terminal, usable with many model providers.
- [pi](https://github.com/badlogic/pi-mono) - Toolkit with unified LLM API, agent loop, TUI and coding agent CLI.
- [qwen-code](https://github.com/QwenLM/qwen-code) - Open-source AI coding agent for the terminal, from the Qwen team.
- [trae-agent](https://github.com/bytedance/trae-agent) - LLM-based agent for general software engineering tasks, released by ByteDance.
- [v0](https://v0.dev/) - Vercel AI assistant that generates and iterates on full-stack web apps from prompts.
- [vibe-kanban](https://github.com/BloopAI/vibe-kanban) - Kanban board for running and reviewing Claude Code, Codex and other coding agents.
- [Zed](https://zed.dev/) - High-performance multiplayer code editor with built-in AI assistance.
- [Archon](https://github.com/coleam00/Archon) - Open-source harness builder that makes AI coding workflows deterministic and repeatable.
- [bolt.diy](https://github.com/stackblitz-labs/bolt.diy) - Open-source fork of bolt.new for prompting, running and deploying full-stack apps with any LLM.
- [cc-wf-studio](https://github.com/breaking-brake/cc-wf-studio) - Visual workflow studio for designing Claude Code workflows as diagrams.
- [claude-powerline](https://github.com/Owloops/claude-powerline) - Vim-style powerline statusline for Claude Code.
- [claw](https://getclaw.site/) - Single POSIX shell script that runs an LLM agent with shell tools, using OpenAI or Anthropic.
- [clsh](https://github.com/my-claude-utils/clsh) - Access your terminal and AI agent from a phone, tablet or desktop.
- [Codebuddy](https://codebuddy.ca/) - AI coding plugin for JetBrains and VS Code that proposes diffs for approval.
- [Devin Desktop](https://codeium.com/download) - Download page for Devin Desktop, an AI coding agent for Mac, Windows and Linux.
- [ditto](https://github.com/yoheinakajima/ditto) - Minimal coding agent that can build and extend itself, by Yohei Nakajima.
- [Google Antigravity](https://antigravity.google/use-cases) - Google's use-cases page for Antigravity, an agentic development environment.
- [humanlayer](https://github.com/humanlayer/humanlayer) - Toolkit for getting AI coding agents to solve hard problems in complex codebases.
- [JetBrains Air](https://air.dev/) - JetBrains environment for running multiple coding agents, including ACP-compatible ones.
- [localforge](https://github.com/rockbite/localforge) - Local coding agent with a desktop-style user interface.
- [OpenAlternative: Cursor alternatives](https://openalternative.co/alternatives/cursor) - Directory listing open-source alternatives to Cursor, including Zed, Neovim and Cline.
- [opencode alternatives (Product Hunt)](https://www.producthunt.com/products/opencode/alternatives) - Product Hunt comparison of opencode alternatives such as Claude Code, Cursor and Cline.
- [Refio](https://plugins.jetbrains.com/plugin/30487-refio) - Local-first AI coding plugin for JetBrains IDEs (by the author of this list).
- [SuperCoder](https://github.com/TransformerOptimus/SuperCoder) - Open-source autonomous software development system built on AI agents.
- [TestSprite](https://www.testsprite.com/) - Agentic testing tool that writes end-to-end tests and runs them after each code change.

## Agent rules, instructions and skills

- [AGENTS.md](https://agents.md/) ⭐ - Open format for guiding coding agents with a README-style AGENTS.md file.
- [Complete Guide to Building Skills for Claude](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf) ⭐ - Anthropic PDF guide on creating skills for Claude.
- [Agent Skills Directory](https://skills.sh/) - Directory for discovering and installing skills for AI coding agents.
- [agent-skills](https://github.com/addyosmani/agent-skills) - Production-grade engineering skills and workflows for AI coding agents, by Addy Osmani.
- [andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) - Single CLAUDE.md file with guidelines against common LLM coding mistakes, based on Karpathy's notes.
- [awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) - Curated list of Claude Skills, resources and tools for customizing Claude workflows.
- [Compound Engineering plugin](https://github.com/EveryInc/compound-engineering-plugin) - Plugin for Claude Code, Codex, Cursor and other coding agents.
- [Cursor Directory](https://cursor.directory/) - Directory of community rules and prompts for AI code editors such as Cursor; blocked, judged from title.
- [mattpocock/skills](https://github.com/mattpocock/skills) - Collection of Claude Code skills for engineers, from the author's .claude directory.
- [OpenSpec](https://github.com/Fission-AI/OpenSpec) - Spec-driven development framework for AI coding assistants.
- [spec-kit](https://github.com/github/spec-kit) - Toolkit for spec-driven development to work with AI coding agents, from GitHub.
- [adamsreview](https://github.com/adamjgmiller/adamsreview) - Multi-lens code review pipeline for Claude Code with auto-fix loop and interactive walkthrough.
- [agent-skill-manager](https://github.com/luongnv89/agent-skill-manager) - Skill manager for AI coding agents, to install and organize skills across tools.
- [agentic-os](https://github.com/KbWen/agentic-os) - Rules and guardrails that make coding agents show evidence at each workflow step.
- [Anatomy of the .claude/ Folder](https://blog.dailydoseofds.com/p/anatomy-of-the-claude-folder) - Guide to CLAUDE.md, commands, skills, agents and permissions in Claude Code.
- [awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules) - Collection of .cursorrules configuration files for customizing Cursor AI behavior.
- [caveman](https://github.com/JuliusBrussee/caveman) - Claude Code skill and proxy that claims to cut about 65% of tokens with terse answers.
- [Continue rules docs](https://docs.continue.dev/customize/deep-dives/rules) - Documentation on rules that steer Continue's agent, chat and edit modes.
- [ECC](https://github.com/affaan-m/ECC) - Agent harness with skills, memory and security rules for Claude Code, Codex and Cursor.
- [evanflow](https://github.com/evanklem/evanflow) - Set of 16 Claude Code skills that take an idea through brainstorm, plan, execute and iterate with TDD.
- [fire-flow](https://github.com/ThierryN/fire-flow) - Orchestration system for Claude Code with structured workflow, session memory and quality gates.
- [oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) - Multi-agent orchestration for Claude Code with team-style workflows.
- [the-library](https://github.com/disler/the-library) - Meta-skill for privately distributing skills, agents and prompts across agents, devices and teams.

## Practices and essays

- [eng-practices](https://google.github.io/eng-practices) - Google's engineering practices documentation covering code review and development guidance.
- [Unrolling the Codex agent loop](https://openai.com/pl-PL/index/unrolling-the-codex-agent-loop) - OpenAI article explaining how the Codex agent loop works internally.
- [cclogs.pl](https://cclogs.pl/) - Polish-language summaries of each Claude Code update.
- [Claude Code prompt steganography analysis](https://thereallo.dev/blog/claude-code-prompt-steganography) - Blog post reporting hidden system prompt markers found in Claude Code, tied to API base URL and timezone.
- [Coding Models Are Doing Too Much](https://nrehiew.github.io/blog/minimal_editing) - Blog post on unnecessary edits by coding models and minimal-editing approaches.
- [If AI coding is lowering your code quality](https://www.i-kh.net/p/if-ai-coding-is-lowering-your-code) - Essay arguing that AI code quality problems come from weak quality management, not from the agents.
- [Simon Willison blog](https://simonwillison.net/2025/Oct/7/vibe-engineering) - Essay by Simon Willison on "vibe engineering", a more careful form of AI-assisted coding.
- [Ten custom subagents for a Clojure codebase (Metabase)](https://www.metabase.com/blog/ten-custom-subagents) - Metabase engineering post on building ten domain-expert subagents to manage context.
- [The Neural Maze: real agents](https://theneuralmaze.substack.com/p/lets-build-real-agents-not-just-demos) - Substack article on building production-ready AI agents instead of prototypes.
- [Using Agent Skills wrong](https://notes.ansonbiggs.com/youre-probably-using-agent-skills-wrong) - Blog post on writing agent skills for coding agents and common bad patterns.
- [When I reject AI code even if it works](https://vinibrasil.com/when-i-reject-ai-code-even-if-it-works) - Essay arguing that AI makes implementation cheap while review and judgment become more expensive.

## Codebase context tools

- [DeepWiki](https://deepwiki.com/) - Generates AI-written documentation and Q&A for any GitHub repository.
- [gitingest](https://github.com/coderamp-labs/gitingest) - Turns a GitHub repository URL into a prompt-friendly text digest of the codebase.
- [Repomix](https://repomix.com/) - Packs a code repository into one AI-friendly file in XML, Markdown, JSON or text.
- [GitReverse](https://www.gitreverse.com/) - Turns a GitHub repo or website into a prompt for rebuilding it.
- [Pieces](https://pieces.app/) - Developer tool that keeps work context so AI tools can reuse past decisions and snippets.
- [Prometheus](https://github.com/EuniAI/Prometheus) - AI agent that builds a knowledge graph of a codebase to locate and repair issues.
- [recall](https://github.com/raiyanyahya/recall) - Keeps project context across sessions for Claude Code and Opencode, reducing re-explanation.

## MCP

- [Model Context Protocol docs](https://modelcontextprotocol.io/docs/getting-started/intro) ⭐ - Official introduction to the Model Context Protocol for connecting AI apps to external tools.
- [awesome-mcp-servers](https://github.com/appcypher/awesome-mcp-servers) - Curated list of Model Context Protocol servers.
- [MCP Market](https://mcpmarket.com/) - Directory for discovering MCP servers that connect Claude and Cursor to external tools.
- [MCP quickstart](https://modelcontextprotocol.io/quickstart) - Quickstart for building an MCP server to use with Claude and other clients.
- [HexStrike AI](https://github.com/0x4m4/hexstrike-ai/tree/master) - MCP server that lets AI agents run over 150 security tools for pentesting.
- [MCP is dead (Quandri)](https://www.quandri.io/engineering-blog/mcp-is-dead) - Engineering essay arguing MCP has context, reliability and overlap problems versus CLI and API.

## Learning

- [Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action) - Anthropic course on running, configuring and automating long Claude Code sessions.
- [claude-code-for-beginners](https://github.com/koki7o/claude-code-for-beginners) - Beginner course on AI-assisted development with Claude Code.
