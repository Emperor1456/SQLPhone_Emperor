# 04.SQLPhone NOTES/Module_10_Security_Optimization.md
# SQLPhone Emperor — The Best Phone‑First SQL Curriculum

# 📝 Module 10 – Security, Optimization & Best Practices

## SQL Injection Prevention
- Never concatenate user input into SQL strings.
- Always use parameterized queries: `?` placeholders.
- Validate and sanitize input.

## Indexes
- Speed up `WHERE`, `JOIN`, `ORDER BY`.
- Create: `CREATE INDEX idx_name ON table(col);`
- Check usage with `EXPLAIN QUERY PLAN`.
- Avoid over‑indexing (slows writes).

## Transactions
- `BEGIN; ... COMMIT;` or `ROLLBACK;`
- In Python: `with conn:` auto‑commits/rollbacks.

## Backup & Restore
- `.dump` to SQL file, `.backup` binary copy.
- Python: `src.backup(dst)`.

## Schema Design
- Normalize to reduce redundancy (1NF–3NF).
- Naming: snake_case, singular table names.
- Document your schema.
