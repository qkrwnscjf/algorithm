import java.io.*;
import java.util.*;

public class Backjoon1966 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder(); // 객체 선언 함수

        int T = Integer.parseInt(br.readLine()); // 테스트 케이스 개수

        while (T-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken()); // 문서 개수
            int m = Integer.parseInt(st.nextToken()); // 찾고자 하는 문서의 위치

            Queue<int[]> queue = new LinkedList<>();
            PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());

            // 문서 입력
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                int priority = Integer.parseInt(st.nextToken());
                queue.add(new int[]{i, priority}); // [인덱스, 중요도]
                pq.add(priority); // 우선순위 큐에 중요도 추가
            }

            int printOrder = 0; // 출력 순서

            while (!queue.isEmpty()) {
                int[] current = queue.poll(); //최상위 요소 검색 후 제거
                int index = current[0];  // 문서의 원래 위치
                int priority = current[1];  // 문서의 중요도

                // 현재 문서가 가장 높은 중요도를 가진 경우 출력
                if (priority == pq.peek()) {
                    pq.poll();  // 해당 중요도를 우선순위 큐에서 제거
                    printOrder++;  // 출력 순서 증가

                    if (index == m) {  // 우리가 찾는 문서인 경우
                        sb.append(printOrder).append("\n");
                        break;
                    }
                } else {
                    queue.add(current); // 다시 큐에 삽입 (맨 뒤로 이동)
                }
            }
        }

        System.out.print(sb);
        br.close();
    }
}