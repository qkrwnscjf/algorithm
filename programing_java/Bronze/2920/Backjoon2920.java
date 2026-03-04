import java.util.Scanner;

public class Backjoon2920 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int[] arr = new int[8];

        for (int i = 0; i < 8; i++) {
            arr[i] = scan.nextInt();
        }

        boolean isAscending = true;
        boolean isDescending = true; //boolean조건을 이용하여 오름/내림차순 구분하기, 이때 안쓰고 하는 방법도 있지만, 코드가 복잡해짐

        for (int i = 0; i < 7; i++) {
            if (arr[i] < arr[i + 1]) {
                isDescending = false; 
            } else if (arr[i] > arr[i + 1]) {
                isAscending = false;
            }
        }

        if (isAscending) {
            System.out.println("ascending");
        } else if (isDescending) {
            System.out.println("descending");
        } else {
            System.out.println("mixed");
        }
    }
}

