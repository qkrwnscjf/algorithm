import java.util.Scanner;

public class Backjoon2747 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int N = scan.nextInt();
        int a = 0;
        int b = 1;
        for (int i = 0; i < N; i++) {
            int sum = a + b;
            a = b;
            b = sum;


        }

        System.out.println(a);

    }
}
