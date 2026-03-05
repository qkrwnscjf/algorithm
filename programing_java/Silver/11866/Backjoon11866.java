// 요세푸스 문제 - 자료구조(큐)
import java.io.*;
import java.util.*;

public class Backjoon11866 {

    static Queue<Integer> queue = new LinkedList<>();// 정수를 저장하는 큐

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        br.close();

        for(int i = 1; i<= N; i++) {
            queue.add(i);
        }

        sb.append("<");

        while(queue.size()>1){
            for (int i = 0; i < K-1; i++) {
                queue.offer(queue.poll());
            }
            sb.append(queue.poll()).append(", ");
        }

        sb.append(queue.poll()).append(">"); //닫는 괄호

        System.out.println(sb);
    } 
}