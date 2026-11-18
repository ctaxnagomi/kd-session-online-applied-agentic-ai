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

## Quick Start Code

### 1. Build the corpus (sample)

```bash
cd scripts
pip install sqlite-vec sentence-transformers
python build_corpus.py
```

### 2. Query by hash (Python)

```python
import sqlite3, hashlib

def verify_and_fetch(db_path, expected_hash):
    db = sqlite3.connect(db_path)
    row = db.execute(
        "SELECT content, source_url FROM chunks WHERE content_hash = ?",
        (expected_hash,)
    ).fetchone()
    if not row:
        return None
    content, url = row
    actual = hashlib.sha256(content.encode()).hexdigest()
    assert actual == expected_hash, "Hash mismatch!"
    return {"content": content, "url": url, "hash": actual}
```

### 3. Drop the skill into OpenCode

```bash
mkdir -p ~/.config/opencode/skills/strategic-corpus
cp skills/strategic-corpus/SKILL.md ~/.config/opencode/skills/strategic-corpus/
cp RULESET-101.md ~/.config/opencode/skills/strategic-corpus/
```

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

---

## Files in this Workshop

| File | Purpose |
|------|---------|
| `README.md` | This file |
| `RULESET-101.md` | Agent rules (configure in Notepad++) |
| `skills/strategic-corpus/SKILL.md` | Sample OpenCode skill |
| `scripts/build_corpus.py` | Sample script to chunk, hash, embed into SQLite |
| `samples/sample_chunk.json` | Example chunk format |
| `samples/DATASET_CARD.md` | Hugging Face dataset card template |
| `samples/INSTRUCT_ZIP_NOTE.md` | CTECX Instruct.ZIP note |

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
- `pip install sqlite-vec sentence-transformers` (for the sample script)

---

**KD SESSION ONLINE — Applied Agentic AI**  
Strategic Corpus · Hash-Verified · Local + Hugging Face · OpenCode Skill
