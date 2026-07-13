import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🧱  SQLAlchemy Base & Engine – Code Snippet\n\n"
        "Write Python code that prints the two lines\n"
        "of code that set up SQLAlchemy's declarative\n"
        "Base and create an engine for an SQLite database\n"
        "('empire.db'), exactly as shown in the lecture.\n\n"
        "Expected output:\n"
        "from sqlalchemy.orm import declarative_base\n"
        "Base = declarative_base()\n"
        "engine = create_engine('sqlite:///empire.db')"
    ),
    expected_output=(
        "from sqlalchemy.orm import declarative_base\n"
        "Base = declarative_base()\n"
        "engine = create_engine('sqlite:///empire.db')"
    ),
    level=Level.EASY,
    mode="python",
    hints=[
        "First import declarative_base.",
        "Second assign Base = declarative_base()",
        "Third engine = create_engine('sqlite:///empire.db')",
        "Print exactly that block.",
    ]
)

easy2 = Task(
    description=(
        "🧑‍💻  Soldier Model – SQLAlchemy Class\n\n"
        "Print the exact Python code that defines the\n"
        "`Soldier` model class with columns id, name,\n"
        "rank, salary (as in the lecture). Use proper\n"
        "indentation (4 spaces).\n\n"
        "Expected output:\n"
        "class Soldier(Base):\n"
        "    __tablename__ = 'soldiers'\n"
        "    id = Column(Integer, primary_key=True)\n"
        "    name = Column(String, nullable=False)\n"
        "    rank = Column(String)\n"
        "    salary = Column(Float)"
    ),
    expected_output=(
        "class Soldier(Base):\n"
        "    __tablename__ = 'soldiers'\n"
        "    id = Column(Integer, primary_key=True)\n"
        "    name = Column(String, nullable=False)\n"
        "    rank = Column(String)\n"
        "    salary = Column(Float)"
    ),
    level=Level.EASY,
    mode="python",
    hints=[
        "Class Soldier(Base):",
        "__tablename__ = 'soldiers'",
        "Four column definitions.",
        "Print exactly as shown.",
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🔍  High‑Paid Soldiers Query – SQLAlchemy\n\n"
        "Print the exact SQLAlchemy ORM query that\n"
        "selects all soldiers with salary > 4000 and\n"
        "then prints each soldier's name and rank.\n"
        "The output should be the two lines of code\n"
        "(the query assignment and the for loop).\n\n"
        "Expected output:\n"
        "high_paid = session.query(Soldier).filter(Soldier.salary > 4000).all()\n"
        "for s in high_paid:\n"
        "    print(s.name, s.rank)"
    ),
    expected_output=(
        "high_paid = session.query(Soldier).filter(Soldier.salary > 4000).all()\n"
        "for s in high_paid:\n"
        "    print(s.name, s.rank)"
    ),
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "Use session.query(Soldier).filter(...).all()",
        "Loop through results.",
        "Indentation: for loop body indented 4 spaces.",
        "Print exactly these three lines.",
    ]
)

medium2 = Task(
    description=(
        "➕  Add a Soldier – ORM Insert\n\n"
        "Print the two lines of code that create a new\n"
        "Soldier instance and add it to the session,\n"
        "exactly as in the lecture.\n\n"
        "Expected output:\n"
        "session.add(Soldier(name=\"Emperor\", rank=\"General\", salary=5000))\n"
        "session.commit()"
    ),
    expected_output=(
        'session.add(Soldier(name="Emperor", rank="General", salary=5000))\n'
        'session.commit()'
    ),
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "session.add(...)",
        "session.commit()",
        "Use double quotes inside the string.",
        "Print both lines.",
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🛠️  Django Models – Full Definition\n\n"
        "Print the exact Django models code from the\n"
        "lecture that defines `Regiment` and `Soldier`\n"
        "with a ForeignKey from Soldier to Regiment.\n"
        "Use proper indentation (4 spaces) and blank line\n"
        "between classes.\n\n"
        "Expected output:\n"
        "class Regiment(models.Model):\n"
        "    name = models.CharField(max_length=100)\n"
        "\n"
        "class Soldier(models.Model):\n"
        "    name = models.CharField(max_length=100)\n"
        "    regiment = models.ForeignKey(Regiment, on_delete=models.CASCADE)"
    ),
    expected_output=(
        "class Regiment(models.Model):\n"
        "    name = models.CharField(max_length=100)\n"
        "\n"
        "class Soldier(models.Model):\n"
        "    name = models.CharField(max_length=100)\n"
        "    regiment = models.ForeignKey(Regiment, on_delete=models.CASCADE)"
    ),
    level=Level.HARD,
    mode="python",
    hints=[
        "Two classes, separated by a blank line.",
        "Regiment has one field: name (CharField).",
        "Soldier has name and a ForeignKey to Regiment.",
        "Print exactly as shown.",
    ]
)

hard2 = Task(
    description=(
        "🔗  Django Query – Access Related Regiment\n\n"
        "Print the exact Django code that retrieves the\n"
        "soldier with id=1 and prints the regiment name.\n"
        "Include both lines.\n\n"
        "Expected output:\n"
        "soldier = Soldier.objects.get(id=1)\n"
        "print(soldier.regiment.name)"
    ),
    expected_output=(
        "soldier = Soldier.objects.get(id=1)\n"
        "print(soldier.regiment.name)"
    ),
    level=Level.HARD,
    mode="python",
    hints=[
        "Soldier.objects.get(id=1)",
        "print(soldier.regiment.name)",
        "Print both lines.",
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L94.json",
        module_name="Module_10_Beyond_SQLite",
        lesson_name="L94_ORMs_SQLAlchemy_Django_ORM_Introduction"
    )