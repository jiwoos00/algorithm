
import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();

        int T = sc.nextInt();
        for (int tc = 1; tc < T + 1; tc ++) {
            int N = sc.nextInt();
            int[] arr = new int[N];
            int[] LIS = new int[N];

            for (int i = 0; i < N; i++) {
                arr[i] = sc.nextInt();
            }

            int max = 0;
            for (int i = 0; i < N; i++) {
                LIS[i] = 1;

                for (int j = 0; j < N; j++) {
                    if (arr[j] < arr[i] && LIS[i] < LIS[j] + 1) LIS[i] = LIS[j] + 1;
                }

                if (max < LIS[i]) max = LIS[i];
            }

            sb.append("#").append(tc).append(" ").append(max).append("\n");
        }

        System.out.println(sb);
    }
}
