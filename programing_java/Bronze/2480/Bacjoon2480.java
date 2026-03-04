import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt(); // 첫 번째 주사위
        int b = sc.nextInt(); // 두 번째 주사위
        int c = sc.nextInt(); // 세 번째 주사위
        int prize = 0;

        if (a == b && b == c) {
            prize = 10000 + a * 1000;
        } else if (a == b || a == c) {
            prize = 1000 + a * 100;
        } else if (b == c) {
            prize = 1000 + b * 100;
        } else {
            prize = Math.max(a, Math.max(b, c)) * 100;
        }

        System.out.println(prize);
    }
}

