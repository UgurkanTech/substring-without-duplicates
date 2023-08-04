# The longest substring without any duplicate characters

This Python script finds the longest substring without any duplicate characters.

If there are more than one substring of equal length that satisfy
the condition, returning any of these substrings would be a valid
answer.

This script is optimized to use less CPU and memory using CPython, and this repository also contains useful tools.

Time Complexity: O(n), where n is the length of the input string.

## Examples
```
$ python3 solution.py
input: ABBCDDEFGHII
output: DEFGHI length: 6

$ python3 solution.py
input: AABBCCD
output: AB length: 2

$ python3 solution.py
input: ABCD
output: ABCD length: 4
```
## Default Usage

1. Download the repository and make sure you have Python installed in your PATH.
2. Run following command in the project directory, then input a string:
```Shell
python question.py 
```

## Compiled Library Usage (Recommended)

Using the compiled CPython library:

1. Download the repository and make sure you have Python installed in your PATH.
2. Open the command prompt and run "python" to start Python interactive mode.
3. Import the compiled library:
```python
from question_c import execute
```
4. Run with an example string:
```python
execute('ABBCDDEFGHII')
```
## Benchmarks

With the included benchmark script, it is clear that using CPython, optimizes CPU usage more than two times.
```
Benchmarking interpreted Python code:
300000 loops, best of 5: 1.5 usec per loop

Benchmarking Compiled CPython code:
300000 loops, best of 5: 700 nsec per loop
```
CPython also generates an HTML Annotation File. Python interactions in C code can be seen there.

## Compiling CPython Library

For building with CPython, Visual C++ Build Tools are required.
See: https://visualstudio.microsoft.com/visual-cpp-build-tools/

The "RUN_ALL.cmd" script can be executed to perform the following tasks:

1. Clearing the project directory. (clear.cmd)
2. Creating a code copy for CPython and building it. (setup.cmd)
3. Benchmarking and comparing results. (benchmark.cmd)
4. Running Unit Tests. (test.cmd)

## Unit Test Results

The "test.cmd" script can be executed to perform unit tests.
```
test_AABBCCD (test.TestMain) ... ok
test_ABBCDDEFGHII (test.TestMain) ... ok
test_ABCD (test.TestMain) ... ok
test_Empty (test.TestMain) ... ok
test_LargeString (test.TestMain) ... ok
test_LongestAtEnd (test.TestMain) ... ok
test_LongestAtStart (test.TestMain) ... ok
test_LongestInMiddle (test.TestMain) ... ok
test_UnicodeCharacters (test.TestMain) ... ok

----------------------------------------------------------------------
Ran 9 tests in 0.019s.

OK
```
