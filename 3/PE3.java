public class PE3 {
    public static boolean isPrime(int n) {
        int limit = (int) Math.ceil(Math.sqrt(n));
        for (int i = 2; i < limit; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
    public static void main(String[] args) {
        long N = 600851475143L;
        int limit = (int) Math.ceil(Math.sqrt(N));
        for (int i = limit; i > 1; i--) {
            if ((N % i == 0) && isPrime(i)) {
                System.out.println(i);
                break;
            }
        }
    }
}
