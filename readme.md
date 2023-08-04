# The longest substring without any duplicate characters

This python script find the longest substring without any duplicate characters.

If there are more than one substrings in equal length that satisfy
the condition, returning any of these substrings would be a valid
answer.

This script is optimized to use less CPU and Memory, using CPython and this repository also contains useful tools.

Time Complexity: O(n), where n is the length of the input string.

## Examples:

$ python3 solution.py
input: ABBCDDEFGHII
output: DEFGHI length: 6

$ python3 solution.py
input: AABBCCD
output: AB length: 2
output: BC length: 2
output: CD length: 2
<any of the above 3 would be accepted>

$ python3 solution.py
input: ABCD
output: ABCD length: 4

## Default Usage:

1. Download the repository and make sure you have python installed in your PATH.
2. Run "python question.py" in the project directory then input a string.

## Compiled Library Usage (Recommended)

Using with a 2x faster compiled CPython library: 

1. Download the repository and make sure you have python installed in your PATH.
2. Open the command propt and run "python" to start python interactive mode.
3. Import the compiled library:
>>> from question_c import execute
4. Run with an example string:
>>> execute('ABBCDDEFGHII')

## Benchmarks

With included benchmark script, it is clear that using CPython, optimizes cpu usage more than two times.

Benchmarking interpreted python code:
300000 loops, best of 5: 1.5 usec per loop

Benchmarking Compiled CPython code:
300000 loops, best of 5: 700 nsec per loop

CPython also generates and HTML Annotation File. Python interactions from C code can be seen there.

## Compiling CPython Library

For building with CPython, Visual Cpp Build Tools are required. 
See: https://visualstudio.microsoft.com/visual-cpp-build-tools/

"RUN_ALL.cmd" script can be executed to perform following tasks:

1. Clearing project directory. (clear.cmd)
2. Creating a code copy for CPython and building it. (setup.cmd)
3. Benchmarking and comparing results. (benchmark.cmd)
4. Running Unit Tests. (test.cmd)

## Unit Test Results

"test.cmd" script can be executed to perform unit tests.

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
Ran 9 tests in 0.019s

OK
