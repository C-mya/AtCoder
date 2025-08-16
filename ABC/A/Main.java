import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();  // Nは使わないが読み込む必要あり
        String S = sc.next();

        if (S.length() >= 3 && S.substring(S.length() - 3).equals("tea")) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }

        sc.close();
    }
}
