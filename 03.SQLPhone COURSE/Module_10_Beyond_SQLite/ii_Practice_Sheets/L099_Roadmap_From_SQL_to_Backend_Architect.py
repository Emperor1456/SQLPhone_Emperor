import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🗺️  The Backend Architect Path – Phases\n\n"
        "Write Python code that prints the four phases\n"
        "of the career roadmap from the lecture, each on\n"
        "its own line, in the correct order.\n\n"
        "Expected output:\n"
        "Backend Developer\n"
        "DevOps Engineer\n"
        "System Designer\n"
        "Backend Architect"
    ),
    expected_output="Backend Developer\nDevOps Engineer\nSystem Designer\nBackend Architect",
    level=Level.EASY,
    mode="python",
    hints=[
        "Use a single print with a multi‑line string.",
        "The four phases are exactly those names.",
    ]
)

easy2 = Task(
    description=(
        "🧑‍💻  Phase 1 – Where You Are Now\n\n"
        "Print the current phase title and its project\n"
        "exactly as shown in the lecture:\n"
        "\"Phase 1: Backend Developer – Companion API\"\n\n"
        "Expected output:\n"
        "Phase 1: Backend Developer – Companion API"
    ),
    expected_output="Phase 1: Backend Developer – Companion API",
    level=Level.EASY,
    mode="python",
    hints=[
        "Print exactly that string.",
        "No extra punctuation.",
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🧱  The Full‑Stack Architect Skill Stack\n\n"
        "Print the complete skill progression shown in\n"
        "the lecture, from SQL to Architect, using arrows\n"
        "and no extra spaces around arrows.\n\n"
        "Expected output:\n"
        "SQL → Python Backend → REST APIs → Docker → CI/CD → Cloud → System Design → Architect"
    ),
    expected_output="SQL → Python Backend → REST APIs → Docker → CI/CD → Cloud → System Design → Architect",
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "It's a single line with the arrow symbol →.",
        "Copy the exact string from the lecture.",
    ]
)

medium2 = Task(
    description=(
        "🧠  The Architect's Mindset – Core Principle\n\n"
        "Print the first principle of the architect's\n"
        "mindset as stated in the lecture:\n\n"
        "\"Build, deploy, share — the cycle never stops.\"\n\n"
        "Expected output:\n"
        "Build, deploy, share — the cycle never stops."
    ),
    expected_output="Build, deploy, share — the cycle never stops.",
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "The em dash is — (Unicode U+2014).",
        "Print that exact sentence.",
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🐳  Phase 2 Project – DevOps Milestone\n\n"
        "Print the exact description of the Phase 2\n"
        "DevOps project from the lecture.\n\n"
        "Expected output:\n"
        "Deploy Companion with Docker on an AWS EC2 instance, fully automated via GitHub Actions."
    ),
    expected_output="Deploy Companion with Docker on an AWS EC2 instance, fully automated via GitHub Actions.",
    level=Level.HARD,
    mode="python",
    hints=[
        "The lecture says: Deploy Companion with Docker on an AWS EC2 instance, fully automated via GitHub Actions.",
        "Print that string.",
    ]
)

hard2 = Task(
    description=(
        "🚀  Final Motto – Your Next Step\n\n"
        "Print the final motivating line from the lecture's\n"
        "key takeaway, which starts with \"Build, deploy,\"\n"
        "and ends with \"Companion awaits.\"\n\n"
        "Expected output:\n"
        "Build, deploy, and never stop. Companion awaits."
    ),
    expected_output="Build, deploy, and never stop. Companion awaits.",
    level=Level.HARD,
    mode="python",
    hints=[
        "It's from the Key Takeaway section.",
        "Print exactly: Build, deploy, and never stop. Companion awaits.",
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L99.json",
        module_name="Module_10_Beyond_SQLite",
        lesson_name="L99_Roadmap_From_SQL_to_Backend_Architect"
    )