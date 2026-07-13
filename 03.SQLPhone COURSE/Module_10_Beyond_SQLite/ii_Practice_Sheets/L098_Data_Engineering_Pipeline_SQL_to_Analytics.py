import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🔄  ETL Stages – The Three Core Steps\n\n"
        "Print the three stages of a data pipeline\n"
        "as described in the lecture, one per line:\n"
        "Extract, Transform, Load.\n\n"
        "Expected output:\nExtract\nTransform\nLoad"
    ),
    expected_output="Extract\nTransform\nLoad",
    level=Level.EASY,
    mode="python",
    hints=[
        "Use print('Extract\\nTransform\\nLoad')",
    ]
)

easy2 = Task(
    description=(
        "🐼  Extract with Pandas\n\n"
        "Print the two lines of Python code from the\n"
        "lecture that import pandas and read a SQL query\n"
        "into a DataFrame (using sqlite3 connection `conn`).\n"
        "Use the exact query and variable names.\n\n"
        "Expected output:\n"
        "import pandas as pd\n"
        "df = pd.read_sql(\"SELECT name, rank, salary FROM soldiers\", conn)"
    ),
    expected_output='import pandas as pd\ndf = pd.read_sql("SELECT name, rank, salary FROM soldiers", conn)',
    level=Level.EASY,
    mode="python",
    hints=[
        "First: import pandas as pd",
        "Second: df = pd.read_sql(...) with the exact query string.",
        "Print both lines separated by \\n.",
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🔗  The Data Pipeline Pattern\n\n"
        "Print the exact pipeline pattern shown in the\n"
        "lecture that illustrates the flow from source\n"
        "database to dashboard.\n\n"
        "Expected output:\n"
        "Source DB (SQLite/PostgreSQL) → Python (pandas) → Cleaned CSV → Data Warehouse → Dashboard"
    ),
    expected_output="Source DB (SQLite/PostgreSQL) → Python (pandas) → Cleaned CSV → Data Warehouse → Dashboard",
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "It's a single line with arrows.",
        "Print exactly that string.",
    ]
)

medium2 = Task(
    description=(
        "⚙️  Transformation Code – Add Taxed Salary & Rank Level\n\n"
        "Print the exact transformation snippet from the\n"
        "lecture that adds `salary_taxed` and maps `rank_level`.\n"
        "The output must be the two Python statements exactly\n"
        "as they appear (including the dictionary indentation).\n\n"
        "Expected output:\n"
        'df["salary_taxed"] = df["salary"] * 0.9\n'
        'df["rank_level"] = df["rank"].map({\n'
        '    "General": 1, "Colonel": 2, "Private": 3\n'
        '})'
    ),
    expected_output=(
        'df["salary_taxed"] = df["salary"] * 0.9\n'
        'df["rank_level"] = df["rank"].map({\n'
        '    "General": 1, "Colonel": 2, "Private": 3\n'
        '})'
    ),
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "First line: salary_taxed calculation.",
        "Second statement: .map() with the dictionary on multiple lines.",
        "Use a multi‑line string (triple quotes) to print.",
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "📦  Complete ETL Pipeline – Full Script\n\n"
        "Print the entire ETL pipeline Python script exactly\n"
        "as shown in the lecture (imports, extract, transform,\n"
        "load, and the final print statement).\n\n"
        "Expected output (matches the lecture code block):\n"
        "import sqlite3\n"
        "import pandas as pd\n"
        "\n"
        "# Extract\n"
        "conn = sqlite3.connect(\"empire.db\")\n"
        "df = pd.read_sql(\"SELECT name, rank, salary FROM soldiers\", conn)\n"
        "\n"
        "# Transform\n"
        "df[\"salary_taxed\"] = df[\"salary\"] * 0.9\n"
        "df[\"rank_level\"] = df[\"rank\"].map({\n"
        '    "General": 1, "Colonel": 2, "Private": 3\n'
        "})\n"
        "\n"
        "# Load\n"
        "df.to_csv(\"soldiers_cleaned.csv\", index=False)\n"
        "print(\"Pipeline complete — cleaned data exported.\")"
    ),
    expected_output=(
        'import sqlite3\n'
        'import pandas as pd\n'
        '\n'
        '# Extract\n'
        'conn = sqlite3.connect("empire.db")\n'
        'df = pd.read_sql("SELECT name, rank, salary FROM soldiers", conn)\n'
        '\n'
        '# Transform\n'
        'df["salary_taxed"] = df["salary"] * 0.9\n'
        'df["rank_level"] = df["rank"].map({\n'
        '    "General": 1, "Colonel": 2, "Private": 3\n'
        '})\n'
        '\n'
        '# Load\n'
        'df.to_csv("soldiers_cleaned.csv", index=False)\n'
        'print("Pipeline complete — cleaned data exported.")'
    ),
    level=Level.HARD,
    mode="python",
    hints=[
        "Copy the entire script from the lecture.",
        "Use a triple‑quoted string to preserve newlines and quotes.",
        "The final print uses an em dash (—).",
    ]
)

hard2 = Task(
    description=(
        "📊  dbt Model – Soldier Summary by Regiment\n\n"
        "Print the dbt model SQL file from the lecture\n"
        "that aggregates soldiers by regiment and filters\n"
        "regiments with more than 5 soldiers.\n\n"
        "Expected output (exact dbt model content):\n"
        "-- models/soldier_summary.sql\n"
        "WITH ranked AS (\n"
        "    SELECT\n"
        "        regiment_id,\n"
        "        COUNT(*) AS soldiers,\n"
        "        AVG(salary) AS avg_salary\n"
        "    FROM {{ ref('soldiers') }}\n"
        "    GROUP BY regiment_id\n"
        ")\n"
        "SELECT * FROM ranked WHERE soldiers > 5"
    ),
    expected_output=(
        "-- models/soldier_summary.sql\n"
        "WITH ranked AS (\n"
        "    SELECT\n"
        "        regiment_id,\n"
        "        COUNT(*) AS soldiers,\n"
        "        AVG(salary) AS avg_salary\n"
        "    FROM {{ ref('soldiers') }}\n"
        "    GROUP BY regiment_id\n"
        ")\n"
        "SELECT * FROM ranked WHERE soldiers > 5"
    ),
    level=Level.HARD,
    mode="python",
    hints=[
        "Include the comment line.",
        "The ref('soldiers') uses curly braces exactly as shown.",
        "Indent the SELECT list with 8 spaces.",
        "Use a multi‑line string.",
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L98.json",
        module_name="Module_10_Beyond_SQLite",
        lesson_name="L98_Data_Engineering_Pipeline_SQL_to_Analytics"
    )