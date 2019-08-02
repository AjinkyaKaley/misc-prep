class Solution:
    def findDuplicate(self, paths):
        
        lookup = {}
        
        for path in paths:
            path = path.split(" ")
            root = path.pop(0)
            files = path
            for file in files:
                content_start = file.index('(')
                content_end = file.index(')')
                
                content = file[content_start+1:content_end]
                fileName = file[:content_start]
                if content in lookup:
                    #do something
                    lookup[content].append(root+'/'+fileName)
                else:
                    lookup[content] = [root+'/'+fileName]
        
        solution = []
        for key in lookup:
            if len(lookup[key])>1:
                solution.append(lookup[key])
            
        return solution

sln = Solution()
sln.findDuplicate(["root/a 1.txt(abcd) 2.txt(efsfgh)","root/c 3.txt(abdfcd)","root/c/d 4.txt(efggdfh)"]);