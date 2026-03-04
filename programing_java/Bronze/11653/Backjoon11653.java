import java.io.*;
import java.util.*;

public class Backjoon11653 {
    public static void main(String[] args) throws IOException {



        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
        
		int n = Integer.parseInt(st.nextToken());
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int d_cnt = 2;

        while (n > 1) {
            if (n % d_cnt == 0) {
                bw.write(d_cnt + "\n");
                n = n / d_cnt;
            }
            else {
                d_cnt ++;
            }
        }

        bw.flush();
        bw.close();
    }

        
        
}