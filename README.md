# Optimal-embedding
This algorithm aims at creating a n-1 dimension embedding of n points given the pairwise distance matrix.
It will be proven here that this algorithm creates an embedding that minimizes the difference between the pairwise distance matrix of the embedding and M'=M+eps * E for any eps>0, where M is the original parirwise distance matrix, E is a bounded perturbation, and eps is arbitrarely small.

Base :
Suppose we start by placing choosing two points A and B. Given d, the distance between A1 and A2, we place A1 and A2 as follwos :
A1 (0)
A2 (d)
The distance between A1 and A2 is d.

Induction :
Suppose that the first k points have been placed and the pariwise distance between them is respected.
We want to place a new point X.
We add an extra dimension to our points, and for existing points, the extra dimension will have a coordinate of 0.
If this step was used for all point previously, then the first added point A1 will have all zero coordinates, the second point A2 will have only the first coordinate being non-zero :
A1 (0,0,...,0)
A2 (x21,0,...,0)
A3 (x31,x32,0,...,0)
...
Ak (xk1,...x{k}{k-1})
As a result, if we compute the distance of each point to the new point A{k+1} = (x1,...,xk), the first distance (between A1 and A{k+1}) will always be :
x1^2 + ... + xk^2
The second will be :
(x1-x21)^2 + x2^2 + ... + xk^2
etc...
If we subtract the first and the second line, we can cancel out all but the first variable, which enables us to solve for x1, using a quadratic equation.
More precisely, we will have (x1-x21)^2-x1^2 = x1^2 - 2x1x21 + x21^2 - x1^2 = x21^2-2x1x21 = d, where d is the distance between x1 and x{k+1}.
This is a linear equation that can be solved easily.
Once we have done this, we can replace x1 with its value in all subsequent lines, and once this has been done, we can repeat the process we have done with the second line and recursively get all the coordinates.
Once we reach the last couple of lines (between the second-to-last and the last line), one value remains to be calculated : x{k+1}.
We can go back to the first line : x1^2 + ... + xk^2 = d' where d' is the distance between A{k+1} and A1.
If we replace all the Xi up to X{k-1}, we will have an equation of the form xk^2 = r.
If r is negative, we can accept an imaginary solution at this point.
The perturbation from M to M' ensures that, with a probability of 1, the linear equation will be solvable, as the perturbation suppresses alignments without creating new ones with a probability of 1.

It is interesteing to note here that since the formula to get to coordinate for the next point is a real linear function of the same coordinate for the previous point, it follows that for a given coordinate rank, all point have a real index on that coordinate, or they all have an imaginary index on that coordinate.


We have proven that the embedding e we have created, with imaginary numbers, satisfies the pairise distance matrix M'.
Now, let's prove that by creating an embedding e' where all the imaginary numbers are replaced with 0, we minimize the difference between the e and e'.

First off, given a placement of points, all the embeddings that satisfy the pairwise distances are a combination of rotations and reflections of each other.
Since these transformations can be defined by a real linear matrix, it follows that they can be applied seperately and independantely to the real and the imaginary part of the coordinates of the points in the embedding.
Hence, any solution of the embedding that has imaginary numbers, has a real part with the same norm, and an imaginary part with the same norm, because they are rotations/reflections of each other.


Let x be a real number and a+bi a complex number :
f = abs(x-(a+bi)) = abs(x-a+bi) = (x-a)^2+b^2
We see that f is minimized for x=a.
Therefore, to minimize the difference between the embedding e that has complex numbers and embedding e' that does not, we can just replace the complex numbers with their real part, and we will get the closest match.
This is what my program does.
