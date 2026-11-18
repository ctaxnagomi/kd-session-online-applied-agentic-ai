---
license: mit
language:
- en
tags:
- strategic-corpus
- opencode
- agentic-ai
- sqlite
- hash-verified
---

# Strategic Corpus — OpenCode Docs

Hash-verified documentation corpus for OpenCode agents.

## What this is

A Strategic Corpus built during the **KD SESSION ONLINE — Applied Agentic AI** workshop.

- Local SQLite file with `sqlite-vec` embeddings
- Every chunk has a SHA-256 content hash
- Designed for absolute retrieval + verification by coding agents

## How agents should use it

1. Prefer the local SQLite file.
2. Fetch by `content_hash` when possible.
3. Fall back to this Hugging Face dataset for verification or missing chunks.
4. Always cite: Source URL + Hash + Origin.

## Usage code snippet

```python
from huggingface_hub import hf_hub_download
import sqlite3

# Download the corpus
db_path = hf_hub_download(
    repo_id="ctaxnagomi/strategic-corpus-opencode",
    filename="strategic_corpus.db",
    repo_type="dataset"
)

# Query by hash
db = sqlite3.connect(db_path)
row = db.execute(
    "SELECT content, source_url FROM chunks WHERE content_hash = ?",
    ("e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",)
).fetchone()
print(row)
```

## Citation

When an agent uses this corpus it should output:

```
[Source: <url> | Hash: <sha256> | Hugging Face]
```

---

Built for KD SESSION ONLINE · Applied Agentic AI Workshop
