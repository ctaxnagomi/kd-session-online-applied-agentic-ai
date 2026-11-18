---
name: Strategic Corpus
description: Retrieve absolute, hash-verified documentation from the local SQLite Strategic Corpus or Hugging Face. Use whenever the user asks about OpenCode docs, policies, CLI, Console, or any topic covered by the corpus. Always cite source URL + content hash.
metadata:
  opencode/autoinvoke: true
---

# Strategic Corpus Skill

You have access to a Strategic Corpus of official documentation.

## Mandatory Rules (RULESET-101)

Load and obey **RULESET-101** before answering any documentation-related question:

1. Prefer absolute corpus text over your own knowledge.
2. Retrieve by content hash when possible.
3. Query local SQLite first, then fall back to Hugging Face.
4. Verify the hash of any retrieved chunk.
5. Cite every corpus use with: Source URL + Hash + Origin (Local / HF).

## How to Query

### Local SQLite example

```python
import sqlite3

def fetch_by_hash(db_path: str, content_hash: str):
    db = sqlite3.connect(db_path)
    row = db.execute(
        "SELECT content, source_url FROM chunks WHERE content_hash = ?",
        (content_hash,)
    ).fetchone()
    return row  # (content, source_url) or None
```

### Hash verification

```python
import hashlib

def is_valid(content: str, expected_hash: str) -> bool:
    return hashlib.sha256(content.encode()).hexdigest() == expected_hash
```

## Citation Format

Always end answers that use the corpus with:

```
[Source: <url> | Hash: <sha256> | Local]
```

or

```
[Source: <url> | Hash: <sha256> | Hugging Face]
```

### Example answer

```
The Console budget policy applies to the entire workspace or all members.

[Source: https://opencode.ai/docs/console/policies | Hash: a1b2c3d4e5f6... | Local]
```

## What not to do

- Do not invent documentation.
- Do not ignore a hash mismatch.
- Do not summarize unless the user explicitly asks for a summary.

---

This skill enforces absolute, verifiable knowledge for OpenCode and related systems.
