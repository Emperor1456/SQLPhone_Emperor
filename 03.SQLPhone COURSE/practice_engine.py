import sys, io, textwrap, traceback

class Level:
    EASY = "Easy"
    MEDIUM = "Medium"
    HARD = "Hard"

class Task:
    def __init__(self, description, arg2, level=Level.EASY, hints=None):
        self.description = description
        self.level = level
        self.hints = hints or []
        self.hint_index = 0
        if callable(arg2):
            self.verify_func = arg2
            self.expected_output = None
        else:
            self.verify_func = None
            self.expected_output = arg2.strip()

    def next_hint(self):
        if self.hint_index < len(self.hints):
            hint = self.hints[self.hint_index]
            self.hint_index += 1
            return hint
        return None

def run_task(task):
    print("=" * 44)
    print(f"🧱 TASK [{task.level.upper()}]")
    wrapped = textwrap.fill(task.description, width=48,
                            initial_indent="  📋 ", subsequent_indent="     ")
    print(wrapped)
    print("-" * 44)

    attempts = 0
    while True:
        attempts += 1
        print("
Enter your code below.")
        print("(Blank line to finish, :hint, :quit)")
        lines = []
        while True:
            raw = input("... " if lines else ">>> ").rstrip("
")
            if raw.strip().lower() in (":quit", "exit"):
                print("Exiting task.")
                return False
            if raw.strip().lower() == ":hint":
                hint = task.next_hint()
                if hint:
                    print(f"💡 HINT: {hint}")
                else:
                    print("No more hints.")
                continue
            if raw == "":
                break
            lines.append(raw)
        user_code = "
".join(lines)
        if not user_code.strip():
            print("⚠️ No code entered. Try again.")
            continue

        # Old style: verify via function
        if task.verify_func is not None:
            user_globals = {}
            try:
                exec(user_code, user_globals)
            except Exception as e:
                print("❌ Error during execution:")
                traceback.print_exc()
                continue
            try:
                if task.verify_func(user_globals):
                    print(f"✅ Correct! ({attempts} attempt{'s' if attempts != 1 else ''})")
                    return True
                else:
                    print("❌ Not quite. Try again or type :hint for help.")
            except Exception as e:
                print(f"❌ Verification error: {e}")
            continue

        # New style: compare printed output
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        user_globals = {}
        try:
            exec(user_code, user_globals)
            output = sys.stdout.getvalue()
        except Exception as e:
            sys.stdout = old_stdout
            print("❌ Error during execution:")
            traceback.print_exc()
            continue
        finally:
            sys.stdout = old_stdout

        out_stripped = output.strip()
        if out_stripped == task.expected_output:
            print(f"✅ Correct! ({attempts} attempt{'s' if attempts != 1 else ''})")
            return True
        else:
            print("❌ Output mismatch.")
            print("Expected (first 120 chars):")
            print(task.expected_output[:120])
            print("Got (first 120 chars):")
            print(out_stripped[:120])
