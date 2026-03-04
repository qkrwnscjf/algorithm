// 평범한 배낭 - DP
import java.io.*;
import java.util.*;

public class Backjoon12865 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
 
        int [][] dp = new int[N+1][K+1];
 
        int []W = new int[N+1]; // Weight
        int []V = new int[N+1]; // Value
 
        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            W[i] = Integer.parseInt(st.nextToken());
            V[i] = Integer.parseInt(st.nextToken());
        } // for
 
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= K; j++) {
 
                if(j-W[i] < 0){
                    dp[i][j] = dp[i-1][j];
                    continue;
                }
 
                dp[i][j] = Math.max(dp[i-1][j], dp[i-1][j-W[i]] + V[i]);
            } // for
        } // for
 
        System.out.println(dp[N][K]);
    } // main
}