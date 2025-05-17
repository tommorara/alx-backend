# 0x00. Pagination

## Back-end Project

**Weight:** 1

**Status:** Ongoing second chance project (Started May 8, 2025 06:00 AM — Deadline May 17, 2025 06:00 AM)

An auto QA review will run at the deadline.

---

## In a nutshell…

* **Auto QA review:** 0.0/15 mandatory
* **Overall completion:** 0.0%
* **Mandatory tasks:** 0.0%
* **Optional tasks:** None

---

## Resources

* [REST API Design: Pagination](#)
* [HATEOAS](#)

---

## Learning Objectives

By the end of this project, you should be able to explain without external help:

1. How to paginate a dataset using simple `page` and `page_size` parameters.
2. How to paginate a dataset with hypermedia metadata.
3. How to implement deletion-resilient pagination.

---

## Requirements

* All files must run on **Ubuntu 18.04 LTS** with **Python 3.7+**.
* Each file must:

  * End with a newline.
  * Start with the shebang: `#!/usr/bin/env python3`.
  * Conform to **pycodestyle** (v2.5.\*).
  * Pass line count checks via `wc`.
  * Include module-level documentation:

    ```bash
    python3 -c 'print(__import__("my_module").__doc__)'
    ```
  * Include function-level documentation:

    ```bash
    python3 -c 'print(__import__("my_module").my_function.__doc__)'
    ```
  * Provide real sentences (not single words) for all docstrings.
  * Include type annotations on all functions and coroutines.

---

## Setup

The dataset `Popular_Baby_Names.csv` is provided in the project root. Ensure it is present before running any scripts.

---

## Project Structure

```
0x00-pagination/
├── 0-simple_helper_function.py   # Task 0: index_range helper
├── 1-simple_pagination.py        # Task 1: pagination class with get_page()
├── 2-hypermedia_pagination.py    # Task 2: hypermedia pagination get_hyper()
├── 3-hypermedia_del_pagination.py# Task 3: deletion-resilient pagination get_hyper_index()
├── Popular_Baby_Names.csv        # Dataset
└── README.md                     # Project overview (this file)
```

---

## Tasks

### 0. Simple helper function (mandatory)

* **File:** `0-simple_helper_function.py`
* **Function:** `index_range(page: int, page_size: int) -> Tuple[int, int]`
* **Description:** Return start and end index for pagination parameters (1-indexed pages).

### 1. Simple pagination (mandatory)

* **File:** `1-simple_pagination.py`
* **Class:** `Server`
* **Method:** `get_page(page: int = 1, page_size: int = 10) -> List[List]`
* **Description:** Reads `Popular_Baby_Names.csv`, validates inputs, and returns the requested page of data.

### 2. Hypermedia pagination (mandatory)

* **File:** `2-hypermedia_pagination.py`
* **Class:** `Server`
* **Method:** `get_hyper(page: int = 1, page_size: int = 10) -> Dict`
* **Description:** Returns a dict with:

  * `page_size`, `page`, `data`, `next_page`, `prev_page`, `total_pages`.

### 3. Deletion-resilient hypermedia pagination (mandatory)

* **File:** `3-hypermedia_del_pagination.py`
* **Class:** `Server`
* **Method:** `get_hyper_index(index: int = None, page_size: int = 10) -> Dict`
* **Description:** Provides resilient pagination by index, handling deleted rows without skipping data.

---

## Usage Examples

Each task comes with a corresponding `*-main.py` script demonstrating expected behavior:

```bash
./0-main.py
./1-main.py
./2-main.py
./3-main.py
```

Ensure executables have execute permissions:

```bash
chmod +x *.py
```

