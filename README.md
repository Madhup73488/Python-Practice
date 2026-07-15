# Python Practice — 30 Programs Roadmap

---

# Phase 1 — Python Fundamentals (5 Programs)

These refresh Python syntax, collections, comprehensions, functions, modules, exceptions, file handling.

## 1. Student Management System (CLI)

Implement

- Add student
- Delete
- Update
- Search
- Sort
- Save to JSON
- Load from JSON

Concepts covered

- list
- dict
- functions
- loops
- comprehensions
- json module
- file handling
- exception handling
- lambda
- sorted()

---

## 2. Expense Tracker

Store expenses

```
Date
Category
Amount
Description
```

Features

- Add expense
- Monthly report
- Highest spending category
- Export CSV
- Filter by date

Concepts

- datetime
- csv
- collections
- defaultdict
- lambda
- generators

---

## 3. Library Management System

Books, Members, Borrow, Return, Late fee calculation

Concepts

- Classes
- Objects
- Composition
- datetime
- decorators (logging)

---

## 4. Log File Analyzer

Input: Large Apache log

Find

- Top IPs
- Failed requests
- Response code count
- Peak traffic hour

Concepts

- regex
- Counter
- generators
- file iteration
- collections

---

## 5. Mini Banking System

Accounts: Savings, Current — Transactions, Transfer, Balance

Concepts

- OOP
- inheritance
- polymorphism
- encapsulation
- exceptions

---

# Phase 2 — Intermediate Python (7 Programs)

---

## 6. Sudoku Validator

Given board, check validity.

Concepts

- sets
- matrix
- comprehensions
- helper functions

---

## 7. CSV Data Analytics Tool

Read `employees.csv`, Generate: Average salary, Highest salary, Department-wise report, Export report

Concepts

- csv
- statistics
- defaultdict
- sorting

---

## 8. URL Shortener Backend (In Memory)

Implement

```
shorten(url)
expand(short_url)
```

Concepts

- hashing
- uuid
- dictionary
- random
- base62 encoding

---

## 9. Command Line Todo App

Support

```
todo add
todo delete
todo update
todo list
todo search
```

Concepts

- argparse
- pathlib
- json
- packages

---

## 10. Password Manager

Store encrypted passwords, Master password, Generate strong passwords

Concepts

- hashlib
- secrets
- os
- encryption basics

---

## 11. File Organizer

Automatically organize Downloads into:

```
Images/
Videos/
Documents/
Archives/
```

Concepts

- os
- shutil
- pathlib
- glob

---

## 12. Multi-threaded File Downloader

Download multiple files simultaneously.

Concepts

- threading
- concurrent.futures
- requests
- queue

---

# Phase 3 — Advanced Python (8 Programs)

---

## 13. REST API Client

Consume any REST API — Retry, Timeout, Pagination, Caching

Concepts

- requests
- decorators
- sessions
- json

---

## 14. Web Scraper

Scrape product information, Export CSV

Concepts

- BeautifulSoup
- requests
- regex
- csv

---

## 15. Mini ORM

Implement

```
save()
delete()
filter()
update()
```

using SQLite.

Concepts

- sqlite3
- metaclasses (optional)
- decorators

---

## 16. Chat Server

TCP Socket Server — Clients can join, Broadcast messages

Concepts

- socket
- threading
- networking

---

## 17. Async Web Crawler

Crawl 100 pages concurrently.

Concepts

- asyncio
- aiohttp
- async / await

---

## 18. Mini Shell

Commands: `ls`, `pwd`, `mkdir`, `touch`, `rm`

Concepts

- subprocess
- os
- pathlib

---

## 19. LRU Cache

Implement from scratch

Concepts

- OrderedDict
- decorators
- classes

---

## 20. Rate Limiter

Implement: Sliding Window, Token Bucket, Leaky Bucket

Concepts

- deque
- datetime
- decorators

---

# Phase 4 — Pythonic Features (8 Programs)

These are specifically designed to make you think like a Python developer rather than writing Java in Python.

---

## 21. Build Your Own `zip()`, `map()`, `filter()`, and `reduce()`

Concepts

- iterators
- generators
- yield

---

## 22. Build a Custom Iterator

Examples: `PrimeGenerator`, `FibonacciGenerator`, `EvenNumberIterator`

Concepts

- `__iter__`
- `__next__`

---

## 23. Build a Decorator Library

Implement decorators: `@timer`, `@retry`, `@cache`, `@logger`, `@authenticate`

Concepts

- decorators
- functools
- wraps

---

## 24. Build Context Managers

Create: `DatabaseConnection`, `FileManager`, `Timer`

Concepts

- `__enter__` / `__exit__`
- contextlib

---

## 25. Build a Tiny Testing Framework

Implement: `assert_equal`, `assert_true`, `run_tests`

Concepts

- introspection
- decorators
- exceptions

---

## 26. Build an Event Dispatcher

Like Java listeners.

Concepts

- callbacks
- first-class functions
- closures

---

## 27. Build a Plugin System

Automatically load Python files from a plugins folder.

Concepts

- importlib
- modules
- packages

---

## 28. Build a Mini Template Engine

Input: `Hello {{name}}` → Output: `Hello Madhu`

Concepts

- regex
- parsing
- classes

---

# Final Challenge (Highly Recommended)

## 29. Build a Flask/FastAPI REST Backend

Features

- CRUD
- Authentication
- SQLite/Postgres
- Pagination
- Logging
- JWT
- File Upload

This combines nearly everything.

---

## 30. Build a Python Package

Create your own installable package:

```
myutils/
    math_utils.py
    string_utils.py
    file_utils.py
setup.py (or pyproject.toml)
README.md
tests/
```

Learn

- Package structure
- Imports
- Virtual environments
- Publishing basics
- Unit tests

---

# Topics These 30 Programs Cover

By the end, you'll have practiced nearly every major part of Python:

- ✅ Variables and data types
- ✅ Strings, lists, tuples, sets, dictionaries
- ✅ Comprehensions
- ✅ Functions (`*args`, `**kwargs`, keyword-only args)
- ✅ Lambdas and higher-order functions
- ✅ Modules and packages
- ✅ File I/O (text, CSV, JSON)
- ✅ Exception handling
- ✅ Object-Oriented Programming
- ✅ Dataclasses
- ✅ Iterators and generators
- ✅ Decorators
- ✅ Context managers
- ✅ Regular expressions
- ✅ Collections (`Counter`, `defaultdict`, `deque`)
- ✅ `pathlib`, `os`, `shutil`
- ✅ `datetime`
- ✅ `argparse`
- ✅ `sqlite3`
- ✅ Networking (`socket`)
- ✅ Multithreading
- ✅ Async programming (`asyncio`)
- ✅ Web requests (`requests`, `aiohttp`)
- ✅ Web scraping (`BeautifulSoup`)
- ✅ Testing (`unittest`/`pytest` concepts)
- ✅ Packaging and virtual environments
- ✅ Pythonic coding patterns and standard library usage

---

## My Plan — 2 Days Intensive (4–5 hrs/day)

Since DSA is already strong and comfortable with Java, moving fast:

- **Day 1 (4–5 hrs):** Programs 1–15 — Fundamentals, Intermediate, start Advanced
- **Day 2 (4–5 hrs):** Programs 16–30 — Advanced, Pythonic features, Flask/FastAPI, Packaging

Goal: Interview-ready Python in 2 days by focusing on idiomatic Python patterns rather than just translating Java into Python.
