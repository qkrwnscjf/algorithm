import java.util.Scanner; //입력시 호출 메소드

public class Backjoon15953 {
    public Backjoon15953() {
    }
    public static void main(String[] var0) {
       Scanner scan = new Scanner(System.in); // 입력 메소드
       int var = scan.nextInt(); // 인트 입력
       int [] first = new int[] {500, 300, 200, 50, 30, 10};
       int [] second = new int[] {512, 256, 128, 64, 32};
    
       for(int i = 0; i < var; i++){ // 자바 for문 작성법
            int money = 0;
            int a = scan.nextInt(); //입력 받는 법
            int b = scan.nextInt();
            if (a == 1)
                money += first[0];
            else if (a > 1 && a <= 3)
                money += first[1];
            else if (a > 3 && a <= 6)
                money += first[2];
            else if (a > 6 && a <= 10)
                money += first[3];
            else if (a > 10 && a <= 15)
                money += first[4];
            else if (a > 15 && a <= 21)
                money += first[5];
            else
                money = 0;

            if (b == 1)
                money += second[0];
            else if (b > 1 && b <= 3)
                money += second[1];
            else if (b > 3 && b <= 7)
                money += second[2];
            else if (b > 7 && b <= 15)
                money += second[3];
            else if (b > 15 && b <= 31)
                money += second[4];
            
            System.out.println(money * 10000);
            
       }
       scan.close(); // 스캔 종료시 (필수는 아닌듯)
       
    }
}
