def sortSegments(s):
    ptr = 0
    anchor = 0
    solution = ''
    while ptr < len(s):
        if s[ptr].isalpha():
            while s[ptr].isalpha():
                ptr +=1
        elif s[ptr].isdigit():
            while s[ptr].isalpha():
                ptr +=1
        segement = s[anchor:ptr]
        solution += ''.join(sorted(segement))
        anchor = ptr
    
    segement = s[anchor:len(s)-1]
    solution += segement
    return solution
    
if __name__ == "__main__":
    sortSegments("AXQF01234")