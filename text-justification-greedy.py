import math
class Solution:
    def fullJustify(self, words, maxWidth):

        # Handle corner cases

        n = len(words)
        if n == 0:
            return words
        if words[0] == "":
            return [" " * maxWidth]

        # Greedily put words in words_line until full

        words_line = [words[0]]
        i, len_words, len_spaces = 1, len(words[0]), 0
        while i < len(words) and len_spaces + len_words <= maxWidth:
            words_line.append(words[i])
            len_words += len(words[i])
            len_spaces += 1
            i += 1

        # Remove last word if went beyond maxWidth

        if len_spaces + len_words > maxWidth:
            a = words_line.pop()
            len_words -= len(a)
            len_spaces -= 1

        # Need to fill slots with spaces

        slots = len(words_line) - 1 if len(words_line) > 1 else 1
        spaces = maxWidth - len_words
        padding = []

        # Fill padding between words depending on the case

        spaces_, slots_ = spaces, slots
        while spaces_ % slots_ != 0:
            sp = int(math.ceil(spaces_/float(slots_)))
            padding += [sp]
            spaces_ -= sp
            slots_ -= 1
        padding += [int(spaces_ // slots_)] * slots_

        # Last line, padding is different

        if len(words[len(words_line):]) == 0:
            padding = [1] * (len(words_line) - 1) + [spaces - (len(words_line) - 1)]

        # Construct line

        i, line = 0, ""
        for word in words_line:
            line += word
            if i < len(padding):
                line += " " * padding[i]
            i += 1

        # Recursive call on rest of phrase

        further_lines = self.fullJustify(words[len(words_line):], maxWidth)
        return [line] + further_lines
sln = Solution()
print(sln.fullJustify(["This", "is", "an", "example",
                 "of", "text", "justification."], 16))
