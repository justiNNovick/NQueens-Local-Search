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
On the first draft of my code, I was often times encountering local optimum. In the context of this
problem, a local optimum is when the total summation of all conflicts/csp violations, over all pieces is
minimized relative to previous iterations; however, this differs from the global optimum, which is where the
sum of conflicts over all pieces is 0. When I encountered this, my program wasn’t necessarily getting
closer to the solution in a timely manner, so I employed random restarts and randomized hill climbing. The
random restarts occur if max_iterations have been reached without finding a solution; this technique
re-scrambles the board (re-initializes) so it won't waste too much time solving the problem at an
arrangement that could potentially lead to stifling runtime in the future. As well, I also employ a technique
similar to randomized hill climbing by additionally keeping track of the second-most desirable place a
given queen should move —that is the row producing the second smallest number of csp violations.
Then, when making a decision as to which row to move a given queen to, with probability=0.95, I consider
the list of most desirable rows, and with probability=.05, I consider the second most greedily attractive
row. To take this further, I could further refine this approach by implementing simulated annealing (by
making these probabilities proportionate to the iteration number), however, given that the TA solution is
around 50 lines of code, I did not choose to do so. Overall, my technique allows for wiggle room to
escape local maximums and plateaus by allowing for possible random resets and, occasionally, some
non-greedy moves.
