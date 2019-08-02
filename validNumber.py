class Solution:
    def isNumber(self, s: str) -> bool:
        #construct DFA
        S = dict({"-": "P", "+": "P", "num": "N", " ": "S", ".": "D"})
        P = dict({"num": "N", ".": "D"})
        N = dict({"num": "N", ".": "D", "e": "SC", " ": "NS"})
        D = dict({"num": "N"})
        # DN = dict({"e": "SC", "num": "DN", " ": "NS"})
        SC = dict({"-": "PS", "+": "PS", "num": "SN"})
        PS = dict({"num": "SN"})
        SN = dict({"num": "SN", " ": "NS"})
        NS = dict({" ": "NS"})
        total_states = dict({"N": N, "SN": SN, "S": S,
                             "P": P, "D": D, "SC": SC, "PS": PS, "NS": NS})
        acc_states = set({"N", "SN", "NS","D"})

        #the starting state is S
        cur_state = "S"

        for indx in range(len(s)):
            input_type = s[indx]
            if s[indx] in '0123456789':
                input_type = "num"
            try:
                cur_state = total_states[cur_state][input_type]
            except:  # if the transition is not defined, go to reject state
                return False

        if cur_state in acc_states:
            return True
        else:
            return False

sln = Solution()
sln.isNumber("3.")
