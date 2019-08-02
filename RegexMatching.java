

class RegexMatching {
    public boolean matchRegex(char[] text, char[] pattern) {
        boolean T[][] = new boolean[text.length + 1][pattern.length + 1];

        T[0][0] = true;
        //Deals with patterns like a* or a*b* or a*b*c*
        for (int i = 1; i < T[0].length; i++) {
            if (pattern[i - 1] == '*') {
                T[0][i] = T[0][i - 2];
            }
        }

        for (int i = 1; i < T.length; i++) {
            for (int j = 1; j < T[0].length; j++) {
                if (pattern[j - 1] == '.' || pattern[j - 1] == text[i - 1]) {
                    T[i][j] = T[i - 1][j - 1];
                } else if (pattern[j - 1] == '*') {
                    T[i][j] = T[i][j - 2];
                    if (pattern[j - 2] == '.' || pattern[j - 2] == text[i - 1]) {
                        T[i][j] = T[i][j] | T[i - 1][j];
                    }
                } else {
                    T[i][j] = false;
                }
            }
        }
        return T[text.length][pattern.length];
    }

    public static void main(String args[]) {
        RegexMatching rm = new RegexMatching();
        // System.out.println(rm.matchRegex("Tushar".toCharArray(), "Tushar".toCharArray()));
        // System.out.println(rm.matchRegex("Tusha".toCharArray(), "Tushar*a*b*".toCharArray()));
        // System.out.println(rm.matchRegex("".toCharArray(), "a*b*".toCharArray()));
        // System.out.println(rm.matchRegex("abbbbccc".toCharArray(), "a*ab*bbbbc*".toCharArray()));
        // System.out.println(rm.matchRegexRecursive("abbbbccc".toCharArray(), "aa*bbb*bbbc*".toCharArray()));
        // System.out.println(rm.matchRegexRecursive("abbbbccc".toCharArray(), ".*bcc".toCharArray()));
        // System.out.println(rm.matchRegexRecursive("abbbbccc".toCharArray(), ".*bcc*".toCharArray()));
        // System.out.println(rm.matchRegexRecursive("abbbbccc".toCharArray(), ".*bcc*".toCharArray()));
        // System.out.println(rm.matchRegexRecursive("aaa".toCharArray(), "ab*a*c*a".toCharArray()));

        System.out.println(rm.matchRegex("aa".toCharArray(), "a*".toCharArray()));
    }
}
