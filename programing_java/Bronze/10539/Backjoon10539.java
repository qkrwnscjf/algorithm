import java.util.Scanner;


public class Backjoon10539 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int N = scan.nextInt();
        int [] A = new int[N];
        int [] B = new int[N];

        for (int i = 0; i < N; i++) {
            B[i] = scan.nextInt();
        }

        int sum = 0;
        for (int i = 0; i < N; i++) {
            A[i] = B[i] * (i + 1) - sum; // A[i] = B[i] * (i+1) - (A[0] + ... + A[i-1])
            sum += A[i];
        }

        for (int i = 0; i < N; i++) {
            System.out.print(A[i] + " "); // 가로 출력시 println는 세로, 그냥 print 가로
        }
        
    }
}
