# RULESET-101
## Strategic Corpus Rules for OpenCode / Agentic AI
### Configure using Notepad++

**KD SESSION ONLINE - Applied Agentic AI Workshop**

This is the foundational ruleset. Open it in **Notepad++**, edit as needed, then place it where your agent can read it (or package it inside the OpenCode skill).

---

## How to configure in Notepad++

1. Install Notepad++ (latest version recommended).
2. Open this file: `File -> Open -> RULESET-101.md`
3. Recommended settings:
   - Language: Markdown (or set to None and use plugins)
   - Encoding: UTF-8 (without BOM)
   - Line endings: Unix (LF) preferred for cross-platform
4. Useful plugins (Plugins Admin):
   - MarkdownViewer++ or PreviewHTML (for live preview)
   - NppFTP / Compare / XML Tools if working with related configs
5. Optional: Define a User Defined Language for `.skill.md` or custom extensions if you use CTECX Instruct.ZIP format.

Save as `RULESET-101.md` and keep it next to your skill or in the project root.

---

## RULESET-101 - Absolute Corpus Rules

You are an agent that has access to a **Strategic Corpus**.  
You must follow these rules without exception when the corpus is available.

### 1. Prefer Absolute Corpus over Memory
- Never invent or paraphrase documentation when the corpus can provide the exact text.
- Always attempt to retrieve from the local SQLite corpus first.
- Only fall back to general knowledge if the corpus explicitly has no matching content.

### 2. Hash-First Retrieval
- Every chunk in the corpus has a SHA-256 `content_hash`.
- When you need a specific piece of information, prefer requesting it by hash when possible.
- After retrieval, verify that the returned text matches the expected hash.
- If the hash does not match, discard the result and re-query or fall back to Hugging Face.

### 3. Local First, Then Hugging Face
- Query the local SQLite database (with sqlite-vec + optional FTS5) first.
- If the local corpus is missing the chunk or the hash fails verification, fetch the same hash from the published Hugging Face dataset.
- Never treat an unverified remote result as authoritative.

### 4. Mandatory Citation
Every answer that uses corpus content must include:
- Source URL (from the chunk metadata)
- Content hash (SHA-256)
- Indication whether it came from local SQLite or Hugging Face

Example citation format:
```
[Source: https://opencode.ai/docs/console/policies | Hash: a1b2c3d4... | Local]
```

### 5. Skill Integration
- This ruleset is to be included inside the OpenCode skill (`SKILL.md` or CTECX Instruct.ZIP).
- The skill must instruct the agent to load and obey RULESET-101 before answering any documentation-related question.
- If the skill is loaded, treat these rules as higher priority than the base system prompt for corpus-related tasks.

### 6. What You Must Not Do
- Do not summarize or rewrite corpus content unless the user explicitly asks for a summary.
- Do not invent source URLs or hashes.
- Do not claim a chunk is from the corpus if you did not retrieve it via the defined process.
- Do not ignore a hash mismatch.

### 7. Update Protocol
- When the corpus is updated, the host will publish a new version to Hugging Face with a new root hash or version tag.
- Prefer the latest version unless the user specifies a pinned version.
- Record the corpus version/hash you used in the citation when relevant.

---

## Quick Reference (copy into skill if needed)

```
RULESET-101 ACTIVE
- Use absolute corpus text only
- Hash-verify every chunk
- Local SQLite first -> HF fallback
- Cite: URL + Hash + Origin
- Never invent documentation
```

---

## Code Snippets (for agents & builders)

### Verify a chunk by hash

```python
import hashlib

def verify_chunk(content: str, expected_hash: str) -> bool:
    return hashlib.sha256(content.encode("utf-8")).hexdigest() == expected_hash
```

### Citation template the agent must emit

```text
[Source: https://opencode.ai/docs/console/policies | Hash: e3b0c44298fc1c14... | Local]
```

### Minimal skill load instruction

```markdown
Before answering any documentation question:
1. Load RULESET-101
2. Query local SQLite by content_hash or semantic search
3. Verify hash
4. Cite URL + hash + origin
```

---

**RULESET-101**  
Strategic Corpus | Hash-Verified | Local + Hugging Face | OpenCode Skill  
KD SESSION ONLINE - Applied Agentic AI
