#!/usr/bin/env python3
"""Validate a board definition.json against the WipperSnapper schema."""
import json, sys, pathlib
from jsonschema import validate, ValidationError

if len(sys.argv) != 2:
    print("Usage: python3 boards/validate.py <path/to/definition.json>")
    sys.exit(1)

repo_root = None
for candidate in pathlib.Path(__file__).resolve().parents:
    if (candidate / "boards" / "schema.json").exists():
        repo_root = candidate
        break

if repo_root is None:
    print("❌ Could not locate repository root (boards/schema.json not found)")
    sys.exit(1)

schema_path = repo_root / "boards" / "schema.json"
schema = json.loads(schema_path.read_text())
definition = json.loads(pathlib.Path(sys.argv[1]).read_text())

try:
    validate(instance=definition, schema=schema)
    print(f"✅ {sys.argv[1]} is valid")
except ValidationError as e:
    print(f"❌ {sys.argv[1]} is invalid")
    print(f"   Path: {' > '.join(str(p) for p in e.absolute_path)}")
    print(f"   Error: {e.message}")
    sys.exit(1)
