# Home work 8 Dynamic Programming

### Algorithm: Longest Common Subsequence Length Calculation

Change the Dynamic Programming algorithm for the "Longest Common Subsequence" into a DP algorithm for the "Longest Common Substring" where a substring must be continuous.

* Specify the data structure and the recursion for the problem in a format similar to how the "Longest Common Subsequence" problem is specified and describe the similarity and difference between these two problems.
* Write the latex algorithm for the new problem.
* Analyze the time and space costs of the algorithm by solving the recurrence relation of the algorithm into a mathematical expression for the time complexity of T(n). Do not use Big O notations.
* Implement the algorithm in python and report the testing results. For each testing case, include the input, output, and the content of the data structure used to get the output. Provide extensive testing cases.

```latex
\begin{algorithm}
\caption{Longest Common Subsequence Length Calculation}
\begin{algorithmic}[1]
\Function{Lcs-Length}{$X, Y$}
    \State let $b[1 \ldots m, 1 \ldots n]$ and $c[0 \ldots m, 0 \ldots n]$ be new tables
    \For{$i = 0$ to $m$}
        \State $c[i, 0] = 0$
    \EndFor
    \For{$j = 0$ to $n$}
        \State $c[0, j] = 0$
    \EndFor
    \For{$i = 1$ to $m$}
        \For{$j = 1$ to $n$}
            \If{$x_i == y_j$}
                \State $c[i, j] = c[i-1, j-1] + 1$
                \State $b[i, j] = ``\nwarrow$''
            \ElsIf{$c[i-1, j] \geq c[i, j-1]$}
                \State $c[i, j] = c[i-1, j]$
                \State $b[i, j] = ``\uparrow$''
            \Else
                \State $c[i, j] = c[i, j-1]$
                \State $b[i, j] = ``\leftarrow$''
            \EndIf
        \EndFor
    \EndFor
    \State \Return $c$ and $b$
\EndFunction




\Function{Print-Lcs}{$b, X, i, j$}
    \If{$i == 0$ or $j == 0$}
        \State \Return
    \ElsIf{$b[i, j] == ``\nwarrow$''}
        \State \Call{Print-Lcs}{$b, X, i-1, j-1$}
        \State \textbf{print} $x_i$
    \ElsIf{$b[i, j] == ``\uparrow$''}
        \State \Call{Print-Lcs}{$b, X, i-1, j$}
    \Else
        \State \Call{Print-Lcs}{$b, X, i, j-1$}
    \EndIf
\EndFunction
\end{algorithmic}
\end{algorithm}

```

