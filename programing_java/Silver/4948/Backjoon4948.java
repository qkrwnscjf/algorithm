import java.io.*;

public class Backjoon4948 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	    //StringTokenizer st = new StringTokenizer(br.readLine());
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        boolean test = true;
        
		
        while (test){
            int n = Integer.parseInt(br.readLine());
            if (n == 0) {
                test = false;
            }

            int result = bertrang(n);
            bw.write(result + "\n");
            bw.flush();



        }
        //bw.flush();
        bw.close();
    }

    public static int bertrang(int n) {
        
        int count = 0;    
        for (int i = n+1; i <= 2*n; i++){
            if (is_prime(i) == 1) {
                count ++;
            }
        }
        return count;
    }

    public static int is_prime(int n) {
    if (n < 2) return 0;  // 2보다 작은 수는 소수 아님
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return 0;
        }
    return 1;
    }

}        

