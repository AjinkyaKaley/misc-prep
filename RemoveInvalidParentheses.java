
public class RemoveInvalidParentheses {
    
    public List<String> removeInvalidParentheses(String s) {
        List<String> rst = new ArrayList<>();
        if (s == null || s.length() == 0) {
            rst.add(s);
            return rst;
        }

        dfs(rst, s, 0, 0, '(', ')');
        return rst;
    }

    private void dfs(List<String> rst, String s, int x, int y, char open, char close) {
        // for loop start from i to validate all chars
        for (int count = 0, i = x; i < s.length(); i++) {
            if (s.charAt(i) == open)
                count++;
            if (s.charAt(i) == close)
                count--;
            if (count < 0) {
                // remove char if invalid: try all candidates from [j ~ i], but skip consecutive close parenthese
                for (int j = y; j <= i; j++) {
                    if (s.charAt(j) == close && (j == y || s.charAt(j - 1) != close)) {
                        dfs(rst, s.substring(0, j) + s.substring(j + 1), i, j, open, close);
                    }
                }
                return;
            }
        }
        // reverse s, and reverse open/close, call dfs
        String reverse = new StringBuffer(s).reverse().toString();
        if (open == '(') {
            dfs(rst, reverse, 0, 0, close, open);
        } else { // return result if all validations passed
            rst.add(reverse);
        }
    }
    
    public static void main(String[] args) {
        Solution s = new Solution();
        s.removeInvalidParentheses("()())()");
    }
}