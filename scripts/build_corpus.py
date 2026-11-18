#!/usr/bin/env python3
"""
Sample script: Build a Strategic Corpus
Chunk → Hash → Embed → SQLite (sqlite-vec)

Usage:
  pip install sqlite-vec sentence-transformers
  python build_corpus.py
"""

import hashlib
import json
import sqlite3
from pathlib import Path

try:
    import sqlite_vec
except ImportError:
    print("Install: pip install sqlite-vec")
    raise

try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("Install: pip install sentence-transformers")
    raise

# --- Config ---
DB_PATH = "strategic_corpus.db"
EMBED_MODEL = "all-MiniLM-L6-v2"  # 384 dimensions
EMBED_DIM = 384

# Sample documents (replace with real OpenCode docs in the workshop)
SAMPLE_DOCS = [
    {
        "source_url": "https://opencode.ai/docs/console/policies",
        "content": "Owners and admins manage policies in Controls. Budget levels apply to entire workspace or all members."
    },
    {
        "source_url": "https://opencode.ai/docs/skills/",
        "content": "Create a skill by placing a SKILL.md file in .opencode/skills/<skill-id>. The description field is used for discovery."
    },
    {
        "source_url": "https://opencode.ai/docs/cli/",
        "content": "The OpenCode CLI starts the TUI by default. Use opencode run for one-off commands."
    },
]

def content_hash(text: str) -> str:
    """SHA-256 hash of the exact content."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def main():
    print("Loading embedding model...")
    model = SentenceTransformer(EMBED_MODEL)

    # Connect and load sqlite-vec
    db = sqlite3.connect(DB_PATH)
    db.enable_load_extension(True)
    sqlite_vec.load(db)
    db.enable_load_extension(False)

    # Schema
    db.executescript(f"""
        CREATE TABLE IF NOT EXISTS chunks (
            id INTEGER PRIMARY KEY,
            content TEXT NOT NULL,
            source_url TEXT,
            content_hash TEXT UNIQUE NOT NULL,
            metadata TEXT
        );

        CREATE VIRTUAL TABLE IF NOT EXISTS chunks_vec USING vec0(
            rowid INTEGER PRIMARY KEY,
            embedding FLOAT[{EMBED_DIM}]
        );
    """)

    print("Processing sample documents...")
    for doc in SAMPLE_DOCS:
        text = doc["content"].strip()
        h = content_hash(text)
        emb = model.encode(text).tolist()

        # Insert chunk
        cur = db.execute(
            "INSERT OR IGNORE INTO chunks (content, source_url, content_hash, metadata) VALUES (?, ?, ?, ?)",
            (text, doc["source_url"], h, json.dumps({"workshop": "kd-session-online"}))
        )
        rowid = cur.lastrowid or db.execute(
            "SELECT id FROM chunks WHERE content_hash = ?", (h,)
        ).fetchone()[0]

        # Insert vector
        db.execute(
            "INSERT OR REPLACE INTO chunks_vec (rowid, embedding) VALUES (?, ?)",
            (rowid, json.dumps(emb))
        )
        print(f"  ✓ {h[:12]}... | {doc['source_url']}")

    db.commit()
    print(f"\nCorpus written to {DB_PATH}")

    # --- Extra code snippet: simple hash lookup ---
    print("\n--- Example lookup ---")
    example_hash = content_hash(SAMPLE_DOCS[0]["content"])
    row = db.execute(
        "SELECT content, source_url FROM chunks WHERE content_hash = ?",
        (example_hash,)
    ).fetchone()
    if row:
        print(f"Retrieved: {row[0][:60]}...")
        print(f"Source: {row[1]}")

    db.close()

    print("\nNext steps in workshop:")
    print("  1. Query locally with hybrid search")
    print("  2. Upload the .db file to Hugging Face")
    print("  3. Package the skill that knows how to use it")

if __name__ == "__main__":
    main()
