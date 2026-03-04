import java.util.Scanner;

public class Backjoon10808 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String str = scan.next();
        int[] count = new int[26]; // a~z 26개의 알파벳

        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            count[ch - 'a']++;  // 아스키 안 쓰고 문자 연산으로 처리
        }

        for (int i = 0; i < 26; i++) {
            System.out.print(count[i] + " ");
        }
    }
}

