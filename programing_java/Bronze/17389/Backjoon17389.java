import java.util.Scanner;

public class Backjoon17389 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int N = scan.nextInt();
        String chart = scan.next();
        char [] arr = new char[N]; //문자열 배열 지정 방법 (꼭 익히기!!)
        int sum = 0;
        int count = 0;
        int bonus = 0;
        for (int i = 0; i < N; i++){
            arr[i] = chart.charAt(i); // charAt 는 char타입을 반환하기 때문에, 배열도 char에 맞는 배열이여야 한다.
        }

        for (int i = 0; i < N; i++) {
            if (arr[i] == 'O'){
                count = i + 1;
                sum += count + bonus;
                bonus += 1;
            } 
            else{
                bonus = 0;
                continue;
            }
        }

        System.out.println(sum);
    }
}
