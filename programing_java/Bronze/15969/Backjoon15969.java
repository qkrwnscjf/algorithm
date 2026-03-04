import java.util.Scanner;

public class Backjoon15969 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int N = scan.nextInt(); // Tip: 자바에서 입력은 한 줄에 공백으로 숫자를 입력해도, 줄바꿈으로 입력해도 잘 작동한다.
        int[] arr = new int[N];

        for(int i = 0; i < N; i++) {
            arr[i] = scan.nextInt();
        }

        int num_max = arr[0];
        int num_min = arr[0];

        for (int i = 1; i < N; i++) {
            if (arr[i] > num_max) {
                num_max = arr[i];
            }
            if (arr[i] < num_min) {
                num_min = arr[i];
            }
        }

        System.out.println(num_max - num_min);
    }
}

