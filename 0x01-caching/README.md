# 0x01. Caching

## Back-end Project

**Weight:** 1

**Status:** Ongoing second chance project (Started May 13, 2025 06:00 AM — Deadline May 17, 2025 06:00 AM)

An auto QA review will run at the deadline.

---

## In a nutshell…

* **Auto QA review:** 0.0/89 mandatory & 0.0/18 optional
* **Overall completion:** 0.0%
* **Mandatory tasks:** 0.0%
* **Optional tasks:** 0.0%
* **Calculation:** 0.0% + (0.0% \* 0.0%) == 0.0%

---

## Background Context

Learn different caching algorithms by implementing a variety of cache replacement policies.

---

## Resources

* Cache replacement policies – FIFO
* Cache replacement policies – LIFO
* Cache replacement policies – LRU
* Cache replacement policies – MRU
* Cache replacement policies – LFU

---

## Learning Objectives

By the end of this project, you should be able to explain without external help:

1. What a caching system is
2. What FIFO, LIFO, LRU, MRU, and LFU mean
3. The purpose and limitations of a caching system

---

## Requirements

* All scripts must run on **Ubuntu 18.04 LTS** with **Python 3.7+**
* Each file must:

  * End with a newline
  * Start with `#!/usr/bin/env python3`
  * Be executable (`chmod +x`)
  * Conform to **pycodestyle** (v2.5)
  * Pass line count checks via `wc`
  * Include module-level documentation:

    ```bash
    python3 -c 'print(__import__("my_module").__doc__)'
    ```
  * Include class-level documentation:

    ```bash
    python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    ```
  * Include function-level documentation:

    ```bash
    python3 -c 'print(__import__("my_module").my_function.__doc__)'
    python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
    ```
  * Use real sentences for all docstrings

### BaseCaching Parent Class

All cache classes must inherit from the provided `BaseCaching` in `base_caching.py`:

```python
class BaseCaching():
    """BaseCaching defines cache storage and MAX_ITEMS"""
    MAX_ITEMS = 4
    def __init__(self):
        self.cache_data = {}
    def put(self, key, item):
        raise NotImplementedError
    def get(self, key):
        raise NotImplementedError
```

---

## Project Structure

```
0x01-caching/
├── base_caching.py          # Parent class
├── 0-basic_cache.py         # Task 0: BasicCache
├── 1-fifo_cache.py          # Task 1: FIFOCache
├── 2-lifo_cache.py          # Task 2: LIFOCache
├── 3-lru_cache.py           # Task 3: LRUCache
├── 4-mru_cache.py           # Task 4: MRUCache
├── 100-lfu_cache.py         # Task 5: LFUCache (advanced)
└── README.md                # Project overview (this file)
```

---

## Tasks

### 0. Basic dictionary (mandatory)

* **File:** 0-basic\_cache.py
* **Class:** BasicCache
* **Behavior:** No size limit; implement `put` and `get` using `self.cache_data`.

### 1. FIFO caching (mandatory)

* **File:** 1-fifo\_cache.py
* **Class:** FIFOCache
* **Behavior:** Discard oldest entry when limit exceeded; print DISCARD: <key>

### 2. LIFO caching (mandatory)

* **File:** 2-lifo\_cache.py
* **Class:** LIFOCache
* **Behavior:** Discard most recent entry when limit exceeded; print DISCARD: <key>

### 3. LRU caching (mandatory)

* **File:** 3-lru\_cache.py
* **Class:** LRUCache
* **Behavior:** Discard least recently used on overflow; update usage on `get`; print DISCARD: <key>

### 4. MRU caching (mandatory)

* **File:** 4-mru\_cache.py
* **Class:** MRUCache
* **Behavior:** Discard most recently used on overflow; print DISCARD: <key>

### 5. LFU caching (advanced)

* **File:** 100-lfu\_cache.py
* **Class:** LFUCache
* **Behavior:** Discard least frequently used; on tie, apply LRU; print DISCARD: <key>

---

## Usage Examples

Each task includes a `*-main.py` demonstrating expected output. Run with:

```bash
./0-main.py
./1-main.py
./2-main.py
./3-main.py
./4-main.py
./100-main.py
```

Ensure scripts are executable:

```bash
chmod +x *.py
```

