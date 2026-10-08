#!/usr/bin/env python3
"""Allow only reviewed, byte-identical upstream documentation assets."""
import hashlib
import json
from pathlib import Path
manifest = json.loads(Path('.guardrails/upstream-assets.json').read_text())
for name, expected in manifest['sha256'].items():
    actual = hashlib.sha256(Path(name).read_bytes()).hexdigest()
    if actual != expected:
        raise SystemExit(f'Imported upstream asset changed: {name}; review its provenance before updating the manifest.')
print('Verified pinned upstream documentation assets.')
