import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String S = sc.nextLine().trim();
        sc.close();

        ArrayList<Integer> countT = new ArrayList<>();

        // "t" の位置を記録
        for (int i = 0; i < S.length(); i++) {
            if (S.charAt(i) == 't') {
                countT.add(i);
            }
        }

        BigDecimal ans = BigDecimal.ZERO;

        if (countT.size() >= 3) {
            BigDecimal a = BigDecimal.valueOf(countT.size() - 2);
            BigDecimal b = BigDecimal.valueOf(countT.get(countT.size() - 1) - countT.get(0) + 1 - 2);
            if (b.compareTo(BigDecimal.ZERO) != 0) {
                ans = a.divide(b, 30, RoundingMode.HALF_UP); // 小数点30桁で計算
            }
        }

        System.out.println(ans.toPlainString());
    }
}
