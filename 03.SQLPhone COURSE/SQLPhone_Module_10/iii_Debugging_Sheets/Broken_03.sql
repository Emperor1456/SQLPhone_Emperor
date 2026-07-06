-- 🐛 BROKEN – Module 10, Lesson 85 (Backup)
-- .dump creates text SQL, but .backup creates binary copy.
-- Using .dump to restore can be slow; but the mistake is not using .backup for speed.

-- Actually, a common error is to use .dump without redirecting output.
.dump
-- ❌ no .output specified, just prints to screen
