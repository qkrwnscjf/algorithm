// 스타후르츠
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Backjoon17496 {

   public Backjoon17496() {
   }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken()); // 여름의 일 수
        int t = Integer.parseInt(st.nextToken()); // 자라는데 걸리는 일 수
        int c = Integer.parseInt(st.nextToken()); // 심을 수 있는 칸의 수
        int p = Integer.parseInt(st.nextToken()); // 개당 가격 정수

        int day = 1;
        int income = 0;
        while (true) {
            day += t;
            if (day > n) { break; }
            income += c * p;
        }

        System.out.println(income);
    }
}