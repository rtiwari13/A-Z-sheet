# ⚡recursion notes

# breaking a problem into smaller versions of itself, until it's small enough to solve directly
# Structure of a Recursive Function:- A recursive function must have:
# 1- ⚡ Base Case – when to stop recursion
# 2- ⚡ Recursive Case – when to keep calling the function again


# How Recursion Works (Call Stack) :- Every time a function calls itself, Python:
# 1- Stores the current state in memory (Call Stack)
# 2- Processes the inner function
# 3- Returns back to previous function when done

# ⚡ Tail Recursion : A tail-recursive function is a recursive function where 
#    the recursive call is the last operation in the function 
#    In some languages (like C, Scheme), tail recursion can be optimized (Tail Call Optimization, or TCO) 
#    to avoid adding new stack frames — essentially making recursion as efficient as a loop.
#    BUT Python does not support tail call optimization — 
#    so tail-recursive functions in Python still use stack frames.

# ⚡ Head Recursion: In head recursion, the recursive call is made before performing any operation in the current function.

# Head recursion builds up the call stack before doing anything.
# Tail recursion does the work before the call and doesn’t wait for return.
