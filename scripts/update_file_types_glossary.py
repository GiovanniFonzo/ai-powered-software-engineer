from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / "docs/glossary.md"

content = path.read_text(encoding="utf-8")

section = """
## Project File Types

### .py files

Python files are used for application code and test code.

Examples:

    src/calculator.py
    tests/test_calculator.py

### .md files

Markdown files are used for documentation, lesson notes, dojo answers, and project summaries.

Examples:

    README.md
    docs/glossary.md
    lessons/01-test-driven-development/11-continuous-integration.md

### .yml files

YAML files are used for automation and configuration instructions for tools like GitHub Actions.

Example:

    .github/workflows/python-tests.yml

In this project, the .yml workflow tells GitHub Actions to set up Python, install pytest, and run the test suite automatically.
"""

if "## Project File Types" not in content:
    content = content.rstrip() + "\n\n" + section.strip() + "\n"

path.write_text(content, encoding="utf-8")

print(f"Updated {path}")
