# CTECX Instruct.ZIP (Formatter Note)

In the workshop we package the skill using the CTECX Instruct.ZIP format.

## Minimal structure

```text
strategic-corpus.zip
├── SKILL.md
├── RULESET-101.md
└── references/
    └── corpus-schema.md
```

## Packaging code snippet (Python)

```python
import zipfile
from pathlib import Path

def make_instruct_zip(output="strategic-corpus-instruct.zip"):
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as z:
        z.write("skills/strategic-corpus/SKILL.md", "SKILL.md")
        z.write("RULESET-101.md", "RULESET-101.md")
        # Optional references
        # z.write("samples/corpus-schema.md", "references/corpus-schema.md")
    print(f"Created {output}")

make_instruct_zip()
```

## Shell alternative

```bash
zip -r strategic-corpus-instruct.zip \
  skills/strategic-corpus/SKILL.md \
  RULESET-101.md
```

The formatter wraps these so OpenCode (or other agents that support the CTECX format) can load the absolute corpus rules cleanly.

During the session we will demonstrate packing the skill + RULESET-101 into Instruct.ZIP so participants can drop it into their OpenCode skills folder.
