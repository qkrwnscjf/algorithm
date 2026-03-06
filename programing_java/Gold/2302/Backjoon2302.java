// 극장 좌석 - DP 
import java.io.*;

public class Backjoon2302 {

	static int N, M;
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		//StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(br.readLine());
		M = Integer.parseInt(br.readLine());
        if(N == 1) {
            System.out.println(1);
            return;
        }
		int[] arr = new int[N+1];

		for (int i = 0; i < M; i++) {
            int temp = Integer.parseInt(br.readLine());
            arr[temp] = -1; // 고정석은 -1로
        }
        int[] dp = new int[N+1];
        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3; i < N+1; i++) {
            dp[i] = dp[i-1] + dp[i-2];
        }

        int answer = 1;
        int cnt = 0;
        for (int i = 1; i<N+1; i++) {
            if(arr[i] == -1) {
                if(cnt == 0) {
                    continue;
                }
                else {
                    answer *= dp[cnt];
                    cnt = 0;
                }
            }
            else {
                cnt ++;
            }
        }

        if(cnt != 0) {
        	// 마지막 좌석이 고정석이 아닌 경우를 고려해 마지막 count를 곱합니다.
            answer *= dp[cnt];
        }
        
        System.out.println(answer);
        br.close();
    }

}
