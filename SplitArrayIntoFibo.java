import java.util.ArrayList;
import java.util.*;

public class SplitArrayIntoFibo {

    public static List<Integer> splitIntoFibonacci(String S) {
        List<Integer> ans = new ArrayList<>();
        helper(S, ans, 0);
        return ans;
    }

    public static boolean helper(String s, List<Integer> ans, int idx) {
        System.out.println("Answer : "+ans);
        if (idx == s.length() && ans.size() >= 3) {
            return true;
        }
        for (int i = idx; i < s.length(); i++) {
            if (s.charAt(idx) == '0' && i > idx) {
                break;
            }
            long num = Long.parseLong(s.substring(idx, i + 1));
            System.out.println("Num: "+num);
            if (num > Integer.MAX_VALUE) {
                break;
            }
            int size = ans.size();
            // early termination
            if (size >= 2 && num > ans.get(size - 1) + ans.get(size - 2)) {
                System.out.println("early termination: " + num);
                break;
            }
            if (size <= 1 || num == ans.get(size - 1) + ans.get(size - 2)) {
                System.out.println("consider int: " + num);

                ans.add((int) num);
                // branch pruning. if one branch has found fib seq, return true to upper call
                if (helper(s, ans, i + 1)) {
                    return true;
                }
                ans.remove(ans.size() - 1);
            }
        }
        return false;
    }
    
    public static void main(String[] args) {

        splitIntoFibonacci("123456579");
    }
}
