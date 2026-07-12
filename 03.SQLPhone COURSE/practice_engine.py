import sys, io, os, json, time, textwrap, sqlite3
from enum import Enum
from datetime import datetime

# Colors
R = "\033[0m"
B = "\033[1m"
G = "\033[32m"
RD = "\033[31m"
Y = "\033[33m"
C = "\033[36m"
M = "\033[35m"

SEP = "━" * 43
BOX_W = 43
INNER_W = BOX_W - 4

class Level(Enum):
    EASY = ("🟢 Easy", G)
    MEDIUM = ("🟡 Medium", Y)
    HARD = ("🔴 Hard", RD)
    def __new__(cls, label, color):
        obj = object.__new__(cls)
        obj._value_ = len(cls.__members__) + 1
        obj.label = label
        obj.color = color
        return obj

class Task:
    def __init__(self, description, setup_sql="", expected_output=None,
                 verify_func=None, level=Level.EASY, hints=None, note=None):
        self.description = description
        self.setup_sql = setup_sql        # SQL to create/seed tables
        self.expected_output = expected_output
        self.verify_func = verify_func
        self.level = level
        self.hints = hints or []
        self.note = note

def cprint(msg, color=""):
    print(f"{color}{msg}{R}")

def prompt(msg, color=""):
    return input(f"{color}{msg}{R} ").strip().lower()

def read_multiline():
    lines = []
    first = True
    while True:
        try:
            line = input("... " if not first else ">>> ").rstrip()
        except EOFError:
            break
        first = False
        if line == "":
            break
        lines.append(line)
    return "\n".join(lines)

def execute_sql(conn, sql):
    """Execute SQL and return (output_rows, error_string)."""
    try:
        cur = conn.execute(sql)
        rows = cur.fetchall()
        # Convert to list of tuples for string comparison
        output = repr([tuple(r) for r in rows])
        return output, None
    except sqlite3.Error as e:
        return None, str(e)

def wrap_text(text, width):
    lines = []
    for paragraph in text.split('\n'):
        if paragraph == '':
            lines.append('')
        else:
            wrapped = textwrap.wrap(paragraph, width=width)
            if not wrapped:
                lines.append('')
            else:
                lines.extend(wrapped)
    return lines

def show_preview(code, output, error=None):
    def top_border(title):
        dash_len = max(BOX_W - 5 - len(title), 0)
        return "┌─ " + title + " " + "─"*dash_len + "┐"

    print(top_border("Your SQL"))
    for line in code.split('\n'):
        wrapped = wrap_text(line, INNER_W)
        for wline in wrapped:
            print(f"│ {wline.ljust(INNER_W)} │")
    print("└" + "─"*(BOX_W-2) + "┘")

    if error:
        print(top_border("Error"))
        for line in error.split('\n'):
            wrapped = wrap_text(line, INNER_W)
            for wline in wrapped:
                print(f"│ {wline.ljust(INNER_W)} │")
        print("└" + "─"*(BOX_W-2) + "┘")
    else:
        print(top_border("Output"))
        out_lines = output.split('\n')
        if out_lines == ['']:
            print(f"│ {'(no output)'.ljust(INNER_W)} │")
        else:
            for line in out_lines:
                wrapped = wrap_text(line, INNER_W)
                for wline in wrapped:
                    print(f"│ {wline.ljust(INNER_W)} │")
        print("└" + "─"*(BOX_W-2) + "┘")

def log_mistake(lesson_name, level, code, reason):
    notes_dir = os.path.join(os.path.dirname(__file__), "..", "04.SQLPhone NOTES")
    os.makedirs(notes_dir, exist_ok=True)
    filepath = os.path.join(notes_dir, "MY_MISTAKES.md")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"""
### {timestamp} — {lesson_name} ({level})
**What I wrote:**
```sql
{code.strip()}
```
**Why it failed:** {reason}

---
"""
    with open(filepath, "a", encoding="utf-8") as f:
        f.write(entry)

def _run_single(task, lesson_name="", show_timer=True):
    print("\n" + SEP)
    print(f"  {task.level.label}  {task.level.color}{'★'*task.level.value}{R}")
    print(SEP)
    print(task.description)
    print("─" * 43)

    # Setup fresh in‑memory database
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    if task.setup_sql:
        try:
            conn.executescript(task.setup_sql)
        except sqlite3.Error as e:
            cprint(f"❌ Setup SQL Error: {e}", RD)
            conn.close()
            return False, 0, 0, 0, []

    attempts = 0
    hints_used = 0
    start_time = time.time()
    hint_idx = 0
    mistakes = []
    code = ""

    while True:
        if not code:
            print("⌨️  Write your SQL (empty line to finish):")
            code = read_multiline()
            if code.strip().lower() in (":quit", "quit", "exit", "q"):
                cprint("⏏️  Practice ended.", Y)
                conn.close()
                return False, attempts, hints_used, time.time()-start_time, mistakes
            if code.strip() == ":hint":
                if hint_idx < len(task.hints):
                    cprint(f"💡 Hint {hint_idx+1}: {task.hints[hint_idx]}", C)
                    hint_idx += 1
                    hints_used += 1
                else:
                    cprint("No more hints.", Y)
                code = ""
                continue
            if not code.strip():
                continue

        out, err = execute_sql(conn, code)
        show_preview(code, out, err)

        while True:
            ans = prompt("(s)ubmit  (e)dit  (q)uit :", M)
            if ans in ('s', 'submit'):
                break
            elif ans in ('e', 'edit'):
                cprint("Editing your SQL. Paste/type your new version:", C)
                cprint("(previous SQL shown below for reference)", C)
                print("─── Previous SQL ───")
                print(code)
                print("──────────────────────")
                code = read_multiline()
                break
            elif ans in ('q', 'quit', 'exit'):
                cprint("⏏️  Practice ended.", Y)
                conn.close()
                return False, attempts, hints_used, time.time()-start_time, mistakes
            else:
                cprint("Invalid. Choose s, e, or q.", Y)
        if ans in ('s', 'submit'):
            attempts += 1
            if err:
                cprint(f"❌ SQL Error: {err}", RD)
                mistakes.append((code, f"Error: {err}"))
                log_mistake(lesson_name, task.level.name, code, f"Error: {err}")
                code = ""
            else:
                ok = False
                if task.expected_output is not None:
                    if out == task.expected_output:
                        ok = True
                    else:
                        cprint(f"❌ Expected:\n{task.expected_output}\nGot:\n{out}", RD)
                        mistakes.append((code, f"Expected: {task.expected_output}, Got: {out}"))
                        log_mistake(lesson_name, task.level.name, code, f"Expected: {task.expected_output}, Got: {out}")
                elif task.verify_func:
                    try:
                        if task.verify_func(conn):
                            ok = True
                        else:
                            cprint("❌ Verification failed.", RD)
                            mistakes.append((code, "Verification failed"))
                            log_mistake(lesson_name, task.level.name, code, "Verification failed")
                    except Exception as e:
                        cprint(f"❌ Verification error: {e}", RD)
                        mistakes.append((code, f"Verification error: {e}"))
                        log_mistake(lesson_name, task.level.name, code, f"Verification error: {e}")
                else:
                    ok = True

                if ok:
                    elapsed = time.time() - start_time
                    cprint("✅ Correct!", G)
                    stats = f"   Attempts: {attempts}  |  Hints: {hints_used}"
                    if show_timer:
                        stats += f"  |  Time: {elapsed:.1f}s"
                    cprint(stats, C)

                    if mistakes:
                        cprint("📝  Mistakes you made (learn from them):", M)
                        for idx, (bad_code, reason) in enumerate(mistakes, 1):
                            cprint(f"  {idx}. {reason}", RD)
                            for line in bad_code.split('\n'):
                                cprint(f"     {line}", C)
                        mistakes.clear()

                    if task.note:
                        cprint("💬 " + task.note, M)

                    while True:
                        ans = prompt("(r)etry  (n)ext  (q)uit :", M)
                        if ans in ('r', 'retry'):
                            attempts = 0
                            hints_used = 0
                            hint_idx = 0
                            start_time = time.time()
                            code = ""
                            # Reset database for retry
                            conn.close()
                            conn = sqlite3.connect(":memory:")
                            conn.row_factory = sqlite3.Row
                            if task.setup_sql:
                                conn.executescript(task.setup_sql)
                            break
                        elif ans in ('n', 'next', ''):
                            conn.close()
                            return True, attempts, hints_used, elapsed, mistakes
                        elif ans in ('q', 'quit', 'exit'):
                            conn.close()
                            return False, attempts, hints_used, elapsed, mistakes
                        else:
                            cprint("   Invalid. Choose r, n, or q.", Y)
                    break
                else:
                    cprint("❌ Try again.", RD)
                    code = ""
                    break
    conn.close()
    return False, attempts, hints_used, 0, mistakes

def update_global_progress(module_name, lesson_name):
    progress_dir = os.path.join(os.path.dirname(__file__), "..")
    progress_file = os.path.join(progress_dir, "progress.json")
    if os.path.exists(progress_file):
        with open(progress_file, "r") as f:
            data = json.load(f)
    else:
        data = {}
    if module_name not in data:
        data[module_name] = []
    if lesson_name not in data[module_name]:
        data[module_name].append(lesson_name)
    with open(progress_file, "w") as f:
        json.dump(data, f, indent=2)

def run_sequence(tasks, save_path=None, progress_name=".progress.json",
                 auto_continue=False, show_timer=True,
                 module_name="", lesson_name=""):
    completed = []
    if save_path:
        progress_file = os.path.join(save_path, progress_name)
        if os.path.exists(progress_file):
            try:
                with open(progress_file, 'r') as f:
                    completed = json.load(f)
            except:
                completed = []
            if completed:
                ans = prompt("📂 Saved progress found. Resume from where you left? (y/n) [y]:", M)
                if ans in ('n', 'no'):
                    completed = []

    for i, task in enumerate(tasks):
        if i in completed and auto_continue:
            continue
        if i in completed:
            print(f"\n{SEP}")
            print(f"  ✅ TASK {i+1} of {len(tasks)} (already completed)")
            ans = prompt("⏭️  Skip this task? (y/n) [y]:", M)
            if ans in ('n', 'no'):
                pass
            else:
                continue

        print(f"\n{SEP}")
        print(f"  📌 TASK {i+1} of {len(tasks)}")
        success, _, _, _, _ = _run_single(task, lesson_name=lesson_name, show_timer=show_timer)
        if not success:
            return
        if save_path and i not in completed:
            completed.append(i)
            with open(progress_file, 'w') as f:
                json.dump(completed, f)
        update_global_progress(module_name, lesson_name)

    cprint("\n🏆 All levels complete! Module mastery unlocked.", G)
