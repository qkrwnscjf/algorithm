import java.util.*;

public class Baackjoon11047 {
    public static void main(String args[]){

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();

        int[] coin = new int[n];
        int cnt = 0;

        for (int i = 0; i < n; i++){
            coin[n-i-1] = sc.nextInt();
        }

        while(k != 0){
            for(int x = 0; x < n; x++){
                if(k >= coin[x]){
                    cnt += k/coin[x];
                    k = k % coin[x];
                }
            }
        }

        System.out.println(cnt);
    }
}