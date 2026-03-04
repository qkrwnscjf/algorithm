import java.io.*;
import java.util.*;

public class Backjoon2346 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sbd = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        Deque<int[]> deque = new ArrayDeque<>();
        int[] arr = new int[N];
        int idx = 0;

        // 배열에 값을 넣기 위한 반복문
        while(st.hasMoreTokens()) {
            int num = Integer.parseInt(st.nextToken());
            arr[idx++] = num;
        }

        // 1부터 시작하는 이유는 첫번쨰 인덱스 값을 터트리고 시작하기 때문에
        // 그 다음 인덱스인 1부터 시작하는 것
        // i+1를 한 이유는 순서가 1-based position이기 때문
        for(int i = 1; i < N; i++) {
            deque.offer(new int[]{arr[i], i+1 }); // {풍선 값, 인덱스 위치}
        }

        sbd.append(1).append(" ");

        // 첫 번째는 반드시 터트린다고 했으니, 첫 번째 배열에 있는 값을 넣어준다.
        int move = arr[0];

        for(int i = 1; i < N; i++) {

            /*
             * move가 양수라면
             */
            if(move > 0) {
                for(int j = 1; j < move; j++) {
                    deque.offer(deque.poll());
                }

                int[] move_arr = deque.poll();
                move = move_arr[0];
                sbd.append(move_arr[1]).append(" ");
            }
            /*
             * move가 음수라면
             */
            else {
                for(int j = 1; j <-move; j++) {
                    deque.offerFirst(deque.pollLast());
                }

                int[] move_arr = deque.pollLast();
                move = move_arr[0];
                sbd.append(move_arr[1]).append(" ");
            }
        }

        System.out.println(sbd);

    }
} 