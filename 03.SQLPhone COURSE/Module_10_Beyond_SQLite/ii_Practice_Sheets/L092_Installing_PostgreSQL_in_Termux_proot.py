import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "📦  proot‑distro Installation Command\n\n"
        "Write Python code that prints the exact Termux\n"
        "command to install proot‑distro (as shown in\n"
        "the lecture).\n\n"
        "Expected output:\npkg install proot-distro -y"
    ),
    expected_output="pkg install proot-distro -y",
    level=Level.EASY,
    mode="python",
    hints=[
        "The command uses pkg, not apt.",
        "Look in the lecture under 'Installing proot‑distro'.",
        "print('pkg install proot-distro -y')",
    ]
)

easy2 = Task(
    description=(
        "🐘  PostgreSQL Installation Inside Debian\n\n"
        "Write Python code that prints the command to\n"
        "install PostgreSQL inside the Debian proot\n"
        "container.\n\n"
        "Expected output:\napt update && apt install postgresql -y"
    ),
    expected_output="apt update && apt install postgresql -y",
    level=Level.EASY,
    mode="python",
    hints=[
        "Inside Debian, use apt.",
        "The lecture shows two commands combined with &&.",
        "print('apt update && apt install postgresql -y')",
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🚀  Start & Connect – The Full Sequence\n\n"
        "Write Python code that prints the three commands\n"
        "needed to start the PostgreSQL cluster (version 15)\n"
        "and connect to psql as the postgres user.\n"
        "Print each command on its own line in order.\n\n"
        "Expected output:\npg_ctlcluster 15 main start\nsu - postgres\npsql"
    ),
    expected_output="pg_ctlcluster 15 main start\nsu - postgres\npsql",
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "First command starts the cluster.",
        "Second switches to the postgres user.",
        "Third opens the psql shell.",
        "print('pg_ctlcluster 15 main start\\nsu - postgres\\npsql')",
    ]
)

medium2 = Task(
    description=(
        "🔍  Cluster Status Check\n\n"
        "Write Python code that prints the command to\n"
        "list all PostgreSQL clusters and their status.\n\n"
        "Expected output:\npg_lsclusters"
    ),
    expected_output="pg_lsclusters",
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "The command starts with pg_ls...",
        "It's used to check if the cluster is online.",
        "print('pg_lsclusters')",
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🏛️  First Database & Table – Full SQL Script\n\n"
        "Write Python code that prints the exact SQL\n"
        "statements from the lecture that:\n"
        "  1. Create the `empire` database\n"
        "  2. Connect to it (use psql meta‑command)\n"
        "  3. Create the `soldiers` table with constraints\n"
        "  4. Insert Emperor's row\n"
        "  5. Select all soldiers\n"
        "Print all statements in order, exactly as they\n"
        "appear in the lecture (capitalization matters).\n"
        "Each statement on its own line.\n\n"
        "Expected output:\nCREATE DATABASE empire;\n\\c empire\nCREATE TABLE soldiers (id SERIAL PRIMARY KEY, name TEXT NOT NULL, rank TEXT, salary NUMERIC(10,2) CHECK(salary > 0));\nINSERT INTO soldiers (name, rank, salary) VALUES ('Emperor', 'General', 5000.00);\nSELECT * FROM soldiers;"
    ),
    expected_output="CREATE DATABASE empire;\n\\c empire\nCREATE TABLE soldiers (id SERIAL PRIMARY KEY, name TEXT NOT NULL, rank TEXT, salary NUMERIC(10,2) CHECK(salary > 0));\nINSERT INTO soldiers (name, rank, salary) VALUES ('Emperor', 'General', 5000.00);\nSELECT * FROM soldiers;",
    level=Level.HARD,
    mode="python",
    hints=[
        "Use one print with a multi‑line string.",
        "The psql meta‑command is \\c empire (backslash-c).",
        "CREATE TABLE must include SERIAL and NUMERIC(10,2).",
        "INSERT uses single quotes and the exact values from lecture.",
        "Last line is SELECT * FROM soldiers;",
    ]
)

hard2 = Task(
    description=(
        "⚡  Startup Alias – The pg‑start Shortcut\n\n"
        "Write Python code that prints the exact .bashrc\n"
        "alias line shown in the lecture for starting\n"
        "PostgreSQL quickly after reboot.\n\n"
        "Expected output:\nalias pg-start='proot-distro login debian -- pg_ctlcluster 15 main start'"
    ),
    expected_output="alias pg-start='proot-distro login debian -- pg_ctlcluster 15 main start'",
    level=Level.HARD,
    mode="python",
    hints=[
        "The alias name is pg-start.",
        "It uses single quotes around the command.",
        "The command is: proot-distro login debian -- pg_ctlcluster 15 main start",
        "print(\"alias pg-start='proot-distro login debian -- pg_ctlcluster 15 main start'\")",
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L92.json",
        module_name="Module_10_Beyond_SQLite",
        lesson_name="L92_Installing_PostgreSQL_in_Termux_proot"
    )