import sys
import json

REQUIRED_PATTERNS = [
    "pd.read_",
    "train_test_split",
    ".fit(",
]

def check_notebook(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        nb = json.load(f)

    source_code = ""
    for cell in nb.get("cells", []):
        if cell.get("cell_type") == "code":
            source_code += "".join(cell.get("source", []))

    missing = [p for p in REQUIRED_PATTERNS if p not in source_code]

    if missing:
        print(f"\nCOMMIT BLOQUE — {filepath}")
        print("Patterns manquants dans le notebook :")
        for m in missing:
            print(f"  - {m}")
        return False

    print(f"OK : {filepath} — toutes les verifications passees.")
    return True

if __name__ == "__main__":
    success = all(check_notebook(f) for f in sys.argv[1:])
    sys.exit(0 if success else 1)
