# 🐍 CS50P — Introduction to Programming with Python

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Harvard](https://img.shields.io/badge/Harvard-CS50P-A51C30?style=flat-square&logoColor=white)
![Progress](https://img.shields.io/badge/Progress-7%2F9%20Weeks-4CAF50?style=flat-square)
![pytest](https://img.shields.io/badge/pytest-passing-43B02A?style=flat-square&logo=pytest&logoColor=white)

My solutions to **Harvard's CS50P: Introduction to Programming with Python** — a rigorous, project-based course teaching Python from conditionals through regular expressions.

> 🔗 Course: [cs50.harvard.edu/python](https://cs50.harvard.edu/python)

---

## 📁 Repository Structure

```
CS50P/
├── week_one_conditionals/           # if/elif/else, match statements
├── week_two_loops/                  # for/while loops, iteration
├── week_three_exceptions/           # try/except, error handling
├── week_four_libraries/             # pip packages, APIs, modules
├── week_five_unit_tests/            # pytest, test-driven development
├── week_six_file_io/                # CSV, file reading & writing, Pillow
├── week_seven_regular_expressions/  # re module, pattern matching
└── tests/                           # additional test files
```

---

## 📚 Problem Sets

### Week 1 — Conditionals
`if` / `elif` / `else`, `match` statements, Boolean logic

### Week 2 — Loops
`for` and `while` loops, iteration patterns, list comprehensions

### Week 3 — Exceptions
`try` / `except` blocks, raising exceptions, input validation

### Week 4 — Libraries
Working with pip packages, third-party APIs, and Python modules including the **Bitcoin Price Index** problem using live API data

### Week 5 — Unit Tests ⭐
Writing and running tests with **pytest** — includes:
- `test_twttr` — testing string manipulation functions
- `test_bank` — asserting conditional return values
- `test_plates` — validating vanity plate rules
- `test_fuel` — testing fraction-to-percentage conversion

### Week 6 — File I/O
Reading and writing files, parsing **CSV** data, working with the **Pillow** image library — includes:
- Lines of Code counter
- Pizza Py (tabulate CSV output)
- Scourgify (CSV transformation)
- CS50 P-Shirt (image manipulation with Pillow)

### Week 7 — Regular Expressions
Pattern matching with Python's `re` module — includes:
- NUMB3RS (IPv4 address validation)
- Watch on YouTube (URL extraction)
- Working 9 to 5 (time format parsing)
- Regular, um, Expressions (filler word detection)
- Response Validation (yes/no input parsing)

---

## 💡 Why Week 5 & 7 Matter for SDET Roles

**Week 5 (Unit Tests)** directly mirrors professional QA work — writing test cases, covering edge cases, and using pytest to assert expected vs actual outputs. This is the same workflow used in test automation engineering.

**Week 7 (Regex)** is heavily used in log parsing, response validation, and data extraction within automation pipelines — a practical skill for any SDET.

---

## 🚀 How to Run

### Prerequisites
- Python 3.10+
- pip

### Clone & Run

```bash
git clone https://github.com/mail-adila/CS50P.git
cd CS50P

# Run any solution
python week_one_conditionals/solution.py

# Run unit tests (Week 5)
pip install pytest
pytest week_five_unit_tests/
```

---

## 👩‍💻 Author

**Adila Karim** — [LinkedIn](https://www.linkedin.com/in/adila-karim) · [GitHub](https://github.com/mail-adila)
