//import java.util.ArrayList;
import java.util.Scanner;

public class Backjoon13909 {

    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);

        int n = scan.nextInt();

        int count = 0;

        int i = 1;

        while (i * i <= n) {
            count ++;
            i ++;
        }

        System.out.println(count);

        
    }
}