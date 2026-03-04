import java.io.*;
import java.util.*;

public class Backjoon2609 {
    public static void main(String[] args) throws IOException {



        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
        
		int num1 = Integer.parseInt(st.nextToken());
		int num2 = Integer.parseInt(st.nextToken());

        int gcd = getGCD(num1, num2);

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        bw.write(gcd + "\n");
        bw.write(((num1 * num2)/gcd) + "\n");
        bw.flush();
        bw.close();

        //최대공약수 출력
       // System.out.println(gcd);
        //최소공배수 출력
        //System.out.println(((num1 * num2)/gcd));
    }

        public static int getGCD(int num1, int num2) {
            if (num1 % num2 == 0) return num2;

            return getGCD(num2, num1%num2);

        
        }
        
}