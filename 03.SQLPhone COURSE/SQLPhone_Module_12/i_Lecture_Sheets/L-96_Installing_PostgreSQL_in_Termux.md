# 📘 SQLPhone Emperor · SQL Module 12
# 📖 L‑96 – Installing PostgreSQL in Termux

## 🎯 OBJECTIVE
Set up a PostgreSQL server inside Termux using
`proot-distro` for a full Linux environment.

## 🧱 BRICK 1 – Prerequisites
PostgreSQL cannot run natively in Termux due to
system limitations. We use `proot-distro` to run
a lightweight Linux distribution (e.g., Debian) inside Termux.

**Install proot-distro:**
```bash
pkg install proot-distro
proot-distro install debian
proot-distro login debian
```

Now you are inside a Debian environment.

## 🧱 BRICK 2 – Installing PostgreSQL
Inside the Debian shell:
```bash
apt update && apt install postgresql -y
service postgresql start
su - postgres
createuser --interactive
createdb testdb
psql -d testdb
```

You now have a running PostgreSQL server on your phone.
Exit with `\q` and `exit` to return to Termux.

**Note:** This is optional for the course. The core SQL skills
you’ve learned in SQLite apply directly to PostgreSQL.

## 💡 Real‑world Usage
- Testing PostgreSQL‑specific features locally.
- Running full‑stack applications on a phone.
- Learning administration commands.

## 📌 Key Takeaway
With `proot-distro`, your phone can run a real PostgreSQL server.
It’s a heavy setup, but proves that your device is a
full‑fledged development machine.

*Your phone now runs the same database as Instagram.*