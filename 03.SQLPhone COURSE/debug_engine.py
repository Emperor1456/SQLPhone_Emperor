import sys, io, sqlite3

R = "\033[0m"
G = "\033[32m"
RD = "\033[31m"
Y = "\033[33m"
C = "\033[36m"
M = "\033[35m"
B = "\033[1m"

SEP = "━" * 43

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
        output = repr([tuple(r) for r in rows])
        return output, None
    except sqlite3.Error as e:
        return None, str(e)

def run_debug(lesson_title, setup_sql, broken_code, expected_output, hints=None):
    if hints is None:
        hints = []
    print("\n" + SEP)
    cprint(f"🐞  DEBUGGING CHALLENGE – {lesson_title}", B)
    print(SEP)
    cprint("Here is the broken SQL:", M)
    print("─" * 43)
    for line in broken_code.split('\n'):
        print(f"  {line}")
    print("─" * 43)
    cprint("Find the bug and type the corrected SQL below.", C)
    cprint("(empty line to submit, :hint for a clue)", C)
    hint_idx = 0

    # Setup database once
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    if setup_sql:
        try:
            conn.executescript(setup_sql)
        except sqlite3.Error as e:
            cprint(f"❌ Setup SQL Error: {e}", RD)
            conn.close()
            return False

    while True:
        print()
        fixed = read_multiline()
        cmd = fixed.strip().lower()
        if cmd in (":quit", "quit", "exit", "q"):
            cprint("⏏️  Debugging ended.", Y)
            conn.close()
            return False
        if cmd == ":hint":
            if hint_idx < len(hints):
                cprint(f"💡 Hint {hint_idx+1}: {hints[hint_idx]}", C)
                hint_idx += 1
            else:
                cprint("No more hints.", Y)
            continue
        if not fixed.strip():
            continue

        out, err = execute_sql(conn, fixed)
        if err:
            cprint(f"❌ SQL Error: {err}", RD)
            continue
        if out == expected_output:
            cprint("✅  Bug squashed! The SQL now runs correctly.", G)
            conn.close()
            return True
        else:
            cprint("❌  Not quite. The output is still wrong.", RD)
            cprint(f"Expected:\n{expected_output}", G)
            cprint(f"Got:\n{out}", RD)
            continue

if __name__ == "__main__":
    cprint("SQL Debug engine loaded. Import and use run_debug().", C)
