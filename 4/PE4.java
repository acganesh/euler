public class PE4 {
    public static boolean isPalindrome(String s) {
        int i1 = 0;
        int i2 = s.length() - 1;

        while (i2 > i1) {
            if (s.charAt(i1) != s.charAt(i2)) {
                return false;
            }
            i1++;
            i2--;
        }

        return true;
    }
    public static void main(String[] args) {
        int maxProd = 0;
        // Use the fact that six-digit palindromes
        // must be multiples of 11
        for (int a = 990; a > 99; a = a-11) {
            for (int b = 999; b > 99; b--) {
                int prod = a*b;
                if (isPalindrome(String.valueOf(prod))) {
                    maxProd = Math.max(maxProd, prod);
                }
            }
        }
        System.out.println(maxProd);
    }
}
