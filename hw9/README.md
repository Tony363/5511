# Homework 9

Given n tasks, where task $a_i$ requires $p_i$ units of processing time to complete. You have one computer to run these tasks one by one (i.e., no interruption or time-sharing is allowed). Let $c_i$ be the completion time of task $a_i$, that is, its processing time ($p_i$) plus waiting time. The goal is to find an order of processing that minimizes the average completion time of all tasks. 

For example, suppose there are two tasks, $a_1$ and $a_2$, with $p_1$ = 5 and $p_2$ = 3. If the order is ($a_1$, $a_2$), then $c_1$ = 5, $c_2$ = 5 + 3 = 8, and the average completion time is (5 + 8)/2 = 6.5. If the order is ($a_2$, $a_1$), then $c_2$ = 3, $c_1$ = 3 + 5 = 8, and the average completion time is (3 + 8)/2 = 5.5, which is lower.

Tasks:

* Write a greedy algorithm that accepts a list of given tasks with their processing time and decides their processing order to minimize the average completion time. 
* Prove that your algorithm indeed finds the minimum average completion time.
* Find the time complexity of your algorithm in the form of O(f(n)) and justify the conclusion.
* Implement this algorithm and test it with sample inputs.

