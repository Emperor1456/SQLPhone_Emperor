#!/bin/bash
# 🐛 BROKEN – Module 12, Lesson 96 (Installing PostgreSQL)
# Forgot to start the service before creating a database.

apt install postgresql
su - postgres -c "createdb testdb"  # ❌ service not started
