import java.math.BigInteger;
public class Problem26 {

    private static int gcd(int a, int b) {
        BigInteger b1 = BigInteger.valueOf(a);
        BigInteger b2 = BigInteger.valueOf(b);
        BigInteger gcd = b1.gcd(b2);
        return gcd.intValue();
    }

    public static int multiplicativeOrder(int n, int a) {
        if (gcd(n, a) != 1) {
            return 0;
        } else {
          /*
            BigInteger bia = BigInteger.valueOf(a);
            BigInteger bik = BigInteger.valueOf(k);
            BigInteger bin = BigInteger.valueOf(n);
            BigInteger one = BigInteger.valueOf(1);
            while (bia.modPow(bik, bin) != one) {
              k += 1;
            }
          */
          int k = 1;
            while (Math.pow(a, k) % n != 1) {
                k += 1;
            }
            return k;
        }
        
    }

    public static void main(String[] args) {
        int greatestLen = 0;
        int greatestNum = 0;
        for (int d = 1000; d > 1; d--) {
            System.out.println(d);
            int currentLen = multiplicativeOrder(d, 10);
            if (currentLen > greatestLen) {
                greatestLen = currentLen;
                greatestNum = d;
            }
            if (greatestLen > d - 1) {
                break;
            }

        }
        //System.out.println(greatestNum);
    }

}
