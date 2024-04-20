
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int N, K;
    static int[] weight, values;
    static int[][] dp;
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] tmp = br.readLine().split(" ");
        N = Integer.parseInt(tmp[0]);
        K = Integer.parseInt(tmp[1]);

        weight = new int[N + 1];
        values = new int[N + 1];

        for (int i = 1; i < N + 1; i ++){
            tmp = br.readLine().split(" ");
            weight[i] = Integer.parseInt(tmp[0]);
            values[i] = Integer.parseInt(tmp[1]);
        }

        dp = new int[N + 1][K + 1];
        for (int i = 1; i < N + 1; i ++){
            for (int j = 0; j < K + 1; j ++){
                if (weight[i] <= j){
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i - 1][j - weight[i]] + values[i]);
                }
                else dp[i][j] = dp[i - 1][j];
            }
        }

        System.out.println(dp[N][K]);
    }
}
