# class Solution(object):
#     def findCelebrity(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """

#         # Iterate through each person and find a candidate to be the celebrity

#         # The resulting candidate must be a celebrity by the following logic
#         # If there is a celebrity, they must
#         # a) be known by every person before them (thus, end up as "cand" at some point)
#         # b) not know anyone after them (thus, never relinquish "cand")
#         cand = 0
#         for i in range(n):
#             if knows(cand, i):
#                 cand = i

#         # We've established that cand does not know anyone after it
#         # Let's establish that cand is known by, but does not know everyone before it
#         for i in range (0, cand):
#             if knows(cand, i):
#                 return -1
#             if not knows(i, cand):
#                 return -1
        

#         # Last thing we don't know:
#         # Does everyone after cand know cand?
#         for i in range(cand, n):
#             if not knows(i, cand):
#                 return -1

#         return cand