#!/usr/bin/env python3
"""One-shot build for Your Chronicle.

Runs the content generators, (re)builds the SQLite database from all YAML/JSON
sources, and exports the UI snapshot. Use this after editing any data file.

    python build_all.py            # build everything
    python build_all.py --stats    # build everything, then print a summary
"""
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
GEN = HERE / "generators"


def run(cmd):
    print(f"\n$ {' '.join(cmd)}")
    subprocess.run(cmd, check=True, cwd=HERE)


def main():
    py = sys.executable
    run([py, str(GEN / "gen_materials.py")])
    run([py, str(GEN / "gen_quests.py")])
    run([py, str(GEN / "gen_achievements.py")])
    build = [py, str(HERE / "build_database.py")]
    if "--stats" in sys.argv:
        build.append("--stats")
    run(build)
    run([py, str(GEN / "export_ui_data.py")])
    print("\nDone. Open ui/index.html (served over http) to view the prototype.")


if __name__ == "__main__":
    main()
