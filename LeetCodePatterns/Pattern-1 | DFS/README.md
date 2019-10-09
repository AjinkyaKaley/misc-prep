https://medium.com/leetcode-patterns/leetcode-pattern-1-bfs-dfs-25-of-the-problems-part-1-519450a84353

It is amazing how many graph, tree and string problems simply boil down to a DFS (Depth-first search) / BFS (Breadth-first search). Today we are going to explore this basic pattern in a novel way and apply the intuition gained to solve some medium problems on Leetcode.
Let us build on top of pattern 0. First of, a tree can be thought of as a connected acyclic graph with N nodes and N-1 edges. Any two vertices are connected by exactly one path. So naturally the question arises, what about a DFS or a BFS on binary trees ? well there are 6 possible DFS traversals for binary trees ( 3 rose to fame while the other 3 are just symmetric )

left, right, root ( Postorder) ~ 4. right, left, root
left, root, right ( Inorder) ~ 5. right, root, left
root, left, right ( Preorder) ~ 6. root, right, left

And there is one BFS which is the level order traversal ( can be done using queue). Let us analyze the DFS pattern using a stack which we are already familiar with.
DFS is all about diving as deep as possible before coming back to take a dive again. Below is the iterative DFS pattern using a stack that will allow us to solve a ton of problems. ( iterative introduced first so as to develop intuition)
DFS magic spell: 1]push to stack, 2] pop top , 3] retrieve unvisited neighbours of top, push them to stack 4] repeat 1,2,3 while stack not empty. Now form a rap !

Refer Preorder diagram

Two things to ponder on as we move further:
1] Why are we using stack for DFS , couldn’t we use a queue ? ( always remember : stack for DFS, imagine a vertical flow | queue for BFS, horizontal flow, more on this later)
2] How do we extend this DFS process to general graphs or graphs disguised as matrices ( as in most LC problems). ( Include a mechanism to track visited)


DFS - STACK
BFS - QUEUE

why?? refer Queue vs Stack

So using a stack I could pop 2 and push it’s kids and keep doing so eventually exhausting 2’s subtrees, 3 stays calmly in the stack just below the part where the real push-pop action is going, we pop 3 when all subtrees of 2 are done. This feature of stack is essential for DFS.
While in a queue, I could dequeue 2 and enqueue it’s subtrees which go behind 3 as it was already sitting in the queue. So the next time I dequeue I get 3 and only after that do I move on to visiting 2’s subtrees, this is essentially a BFS !
For me this revelation was pure bliss. Take a moment to celebrate the history of Computer Science and the geniuses behind these simple yet powerful ideas.