SOLUTION DESCRIPTION:
My implementation of local search to solve the N queens problem utilizes a mostly greedy
approach with respect to the value a heuristic gives, while also supporting potential restarts and
non-greedy choices in the case of long runtime. To start, I initialize an nxn board (1-D list with the same
structure as the desired output), where each column contains 1 queen, which is put in a random row. In
my input, aside from n, I have put the additional parameters max_iterations (defaulted to 1000), which
defines how long the main loop should be traversing for the optimum, and random_restarts (defaulted to
50) that defines how many times we can start from scratch with a scrambled board. If a solution is not
found by the end of the max_iterations loop, the program will recursively call itself, in order to re-initialize
and produce a random restart. This random re-start ensures we will not get stuck at a flat plateau or a
local maximum that is not the global maximum/solved game state. Inside the loop is my logic for solving
the board. At each iteration, I start by calling a helper function that gives me the column containing the
queen with the most amount of conflicts (if it's a tie choose at random); as this is one heuristic, I will
greedily decide to act on the said queen. These conflicts are defined as a summation of CSP violations,
and obviously, if there were no conflicts for each piece, we would have reached the global maximum and
returned the solved board. I will then calculate a list of rows that are equivalently the best rows to move
to, along with the second-best row (based on what would produce the least number of CSP violations, and
the second least). Moving to alleviate the most number of conflicts is my second heuristic. Then, 95% of
the time, I will move to one of the best rows, and 5% of the time, I will move to the second-best row. This
process will iteratively work towards improving/reducing the total number of CSP violations summed up
between all rows.

TIME COMPLEXITY OF METHOD:
At each iteration of the main loop over max_iterations, when I call find_most_conflicted_queen(),
this is a quadratic operation; this is so as it may iterate over n elements (s.t n=board length) to find the
position with the most csp violation, and at each iteration i, such that 0 ≤ i ≤ n, it iterates n times again to
find the conflict with respect to the other pieces ⇒ O(n^2). Overall, this quadratic operation can be called
a number of times equal to m = max_iterations * random_restarts. Technically, since I provided the option
to change these values we can view the whole algorithm as O(m * n^2) time complexity. However, since I
set a default to the factors of m, and they don’t need to be provided as input, we can also just think of
them as constants. In this case, the algorithm would be O(n^2).


OVERCOMING LOCAL OPTIMA:
