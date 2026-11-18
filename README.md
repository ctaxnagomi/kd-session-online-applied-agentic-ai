# KD SESSION ONLINE — Applied Agentic AI

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Workshop](https://img.shields.io/badge/Workshop-Applied%20Agentic%20AI-orange.svg)](https://github.com/ctaxnagomi/kd-session-online-applied-agentic-ai)
[![OpenCode](https://img.shields.io/badge/OpenCode-Skill-green.svg)](https://opencode.ai/docs/skills/)
[![Hugging%20Face](https://img.shields.io/badge/Hugging%20Face-Corpus-yellow.svg)](https://huggingface.co)
[![SQLite](https://img.shields.io/badge/SQLite-vec-blueviolet.svg)](https://github.com/asg017/sqlite-vec)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)]()

**Strategic Corpus for OpenCode**  
Hash-Verified · Local SQLite + Vector · Hugging Face · OpenCode Skill

Hosted by: Rikayu / ctaxnagomi (KD Ambassador SWK)  
Format: Online Discord session

---

## Goal

By the end of this session, participants will have built a **Strategic Corpus** that:

- Contains the real OpenCode documentation (Console, CLI, Build, API, etc.)
- Is stored locally as a single SQLite file with vector embeddings
- Uses content hashes so every chunk is verifiable
- Is published to Hugging Face so others can fetch it
- Is packaged as an OpenCode `SKILL.md` (with CTECX Instruct.ZIP formatter) so the agent knows how to use the absolute corpus

Result: OpenCode (or any agent that can read skills) becomes competent on the docs because it fetches absolute, hash-verified context instead of relying on memory.

---

## Why this matters

Most agents “know” documentation only because it was in their training data. That knowledge is incomplete, outdated, and not citable.

A Strategic Corpus gives the agent:

- Exact text (not a paraphrase)
- A content hash so it can verify what it received
- Local-first retrieval (fast, private)
- Remote verification / distribution via Hugging Face
- A skill that tells the agent exactly how to query and cite it

This is applied agentic AI.

---

## Session Outline

1. **Harvest the Docs** — Official OpenCode documentation  
2. **Chunk + Hash + Embed** — SHA-256 + sqlite-vec  
3. **Local Query Demo** — Hybrid search + hash fetch  
4. **Publish to Hugging Face** — Versioned, shareable corpus  
5. **Package as OpenCode Skill** — `SKILL.md` + CTECX Instruct.ZIP  
6. **End-to-end Demo** — Agent answers with citations + hashes  

---

## RULESET-101

The foundational rules for the agent are defined in **[RULESET-101.md](RULESET-101.md)**.

- Open and configure it using **Notepad++**
- Include it inside the OpenCode skill so the agent must follow absolute-corpus + hash-verification rules
- Forces local-first retrieval, hash verification, and mandatory citation

See the full ruleset in the file for the exact instructions the agent must obey.

---

## Key Principles

- **Absolute corpus** — the agent gets the real text
- **Hash-fetch** — content-addressable and verifiable
- **Local-first + remote verification** — SQLite on device, Hugging Face for sharing
- **Skill as the interface** — the agent knows how to use the corpus
- **Citation by default** — source URL + content hash on every answer

---

## Deliverables

Participants leave with:

1. A working SQLite Strategic Corpus of the OpenCode docs  
2. The corpus published on Hugging Face  
3. An OpenCode skill (`SKILL.md` + optional Instruct.ZIP)  
4. RULESET-101 configured and ready to enforce the pattern  

---

## Prerequisites

- Basic Python (or TypeScript)
- OpenCode installed
- Hugging Face account
- Notepad++ (for configuring RULESET-101)

---

**KD SESSION ONLINE — Applied Agentic AI**  
Strategic Corpus · Hash-Verified · Local + Hugging Face · OpenCode Skill