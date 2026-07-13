import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE products (id INTEGER, name TEXT, price REAL);
INSERT INTO products VALUES (1,'Laptop',999.99),(2,'Mouse',24.99),(3,'Keyboard',79.99);
SELECT name FROM products WHERE price > ANY (SELECT price FROM products WHERE name LIKE 'K%');
"""

EXPECTED = "[('Laptop',)]"

HINTS = [
    "The subquery selects prices from products where name starts with 'K', which returns 79.99 (Keyboard).",
    "ANY means greater than at least one of those values. So prices > 79.99 would include Laptop (999.99) and maybe Mouse (24.99 is not >79.99). So result should be Laptop. That matches expected. So the query seems correct.",
    "The bug is that the subquery returns multiple rows, but ANY expects a list – that's fine. However, the parentheses around the subquery might be missing? They are there.",
    "I'll introduce a mistake: the keyword 'ANY' is misspelled as 'SOME'? No, SOME is valid. I'll make the broken code use 'ALL' instead of 'ANY', which would return only products greater than ALL prices returned (i.e., greater than 79.99, which is Laptop). But the expected output is Laptop, same. Not a good bug.",
    "I'll craft a different bug: the subquery uses 'name LIKE 'K%'' but there is no product starting with 'K'? There is Keyboard. So it works. I'll change the broken code to miss the closing parenthesis on the subquery after the LIKE condition. That's a syntax error. So BROKEN: '... FROM products WHERE name LIKE 'K%' )' maybe missing a closing parenthesis? I'll set BROKEN to have missing ) after the subquery's WHERE clause. Then hints to add the missing parenthesis."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L45 – ANY & ALL – Advanced Comparisons",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
