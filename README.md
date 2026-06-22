# Grokking-Algorithms

[![CI](https://github.com/aryanap07/Grokking-Algorithms/actions/workflows/ci.yml/badge.svg)](https://github.com/aryanap07/Grokking-Algorithms/actions/workflows/ci.yml)

This repository contains hands-on implementations of exercises and examples from the book "Grokking Algorithms" by Aditya Bhargava. It's intended for learning, implementing, and applying the algorithms and data-structure concepts introduced in the book.

**Purpose:** Learn the core ideas from the book by reading short examples, implementing them in code, and running small experiments across multiple languages (Python, Java, C++, etc.).

**What's inside:**
- Chapter folders named to match the book chapters, each containing example implementations in one or more languages.

**Examples you can run:**
- Binary search (Python): [Chapter 1 - Introduction to algorithms/binary_search.py](Chapter%201%20-%20Introduction%20to%20algorithms/binary_search.py)
- Selection sort (Python/C++/Java): [Chapter 2 - Selection Sort/selection_sort.py](Chapter%202%20-%20Selection%20Sort/selection_sort.py)
- Quicksort (Python/C++/Java): [Chapter 4 - Quicksort/quick_sort.py](Chapter%204%20-%20Quicksort/quick_sort.py)
- Hash table examples (Python): [Chapter 5 - Hash Tables/check_voter.py](Chapter%205%20-%20Hash%20Tables/check_voter.py)

How to use

1. Read the corresponding chapter in the book to learn the concept.
2. Open the example implementation in the matching chapter folder and study the code.
3. Run the example locally and modify inputs to experiment.

Run Python examples:

```bash
python3 "Chapter 1 - Introduction to algorithms/binary_search.py"
python3 "Chapter 4 - Quicksort/quick_sort.py"
```

Compile and run Java examples:

```bash
javac "Chapter 2 - Selection Sort/selection_sort.java"
java -cp "Chapter 2 - Selection Sort" selection_sort
```

Compile and run C++ examples:

```bash
g++ -std=c++17 "Chapter 4 - Quicksort/quick_sort.cpp" -o quick_sort
./quick_sort
```

Contributing

- Feel free to open issues or submit pull requests to add new implementations, tests, or improved explanations.

License

This repository is for learning and personal use. No license is specified—treat contents as examples and do not redistribute any proprietary book content.

CI & Tests

- A GitHub Actions workflow runs the Python example runner on push and pull requests. The workflow is defined at `.github/workflows/ci.yml`.
- To run the same checks locally, execute:

```bash
python3 tests/run_examples.py
```
