import java.util.*;

public class Backjoon22942 {

    static class Point {
        int index;
        int point;

        public Point(int index, int point) {
            this.index = index;
            this.point = point;
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();

        List<Point> list = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            int x = scanner.nextInt();
            int d = scanner.nextInt();
            list.add(new Point(i, x - d));
            list.add(new Point(i, x + d));
        }

        list.sort(Comparator.comparingInt(o -> o.point));

        System.out.println(stack(N, list));
    }

    private static String stack(int N, List<Point> list) {
        Stack<Point> stack = new Stack<>();
        boolean[] visited = new boolean[N];

        for (Point point : list) {
            int idx = point.index;

            if (!visited[idx]) {
                visited[idx] = true;
                stack.push(point);
            } else {
                Point pop = stack.pop();
                if (idx != pop.index) {
                    return "NO";
                }
            }
        }

        return "YES";
    }

}

