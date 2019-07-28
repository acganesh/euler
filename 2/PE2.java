public class PE2 {
    public static void main(String[] args) {
        int N = 4000000;

        int total = 0;
        int f1 = 0;
        int f2 = 1;
        int temp;

        while (f2 < N) {
            temp = f2;
            f2 = f1+f2;
            f1 = temp;

            if (f2 % 2 == 0) {
                total += f2;
            }
        }
        System.out.println(total);
    }
}
