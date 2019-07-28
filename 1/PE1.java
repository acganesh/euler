public class PE1 {

    public static void main(String[] args) {
       int N = 1000;

       int lim1 = (N-1)/3;
       int lim2 = (N-1)/5;
       int lim3 = (N-1)/15;

       int total = (3*lim1*(lim1+1) + 5*lim2*(lim2+1) - 15*lim3*(lim3+1))/2;
       System.out.println(total);
    }

}
