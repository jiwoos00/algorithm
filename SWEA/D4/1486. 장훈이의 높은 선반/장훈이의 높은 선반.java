import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
    static int N, B, ans;
    static int[] height, numbers;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine()), t = 0;
        while(t ++ < T){
            StringTokenizer st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            B = Integer.parseInt(st.nextToken());

            height = new int[N];
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                height[i] = Integer.parseInt(st.nextToken());
            }

            ans = Integer.MAX_VALUE;
            numbers = new int[N];
            recur(0, 0);

            sb.append("#").append(t).append(" ").append(ans).append("\n");
        }
        System.out.println(sb);

    }
    public static void recur(int start, int sum) {
        if (sum >= B) {
            ans = Math.min(ans, sum - B);
            return;
        }
        if (start == N) {
            return;
        }

        for (int i = start; i < N; i ++){
            numbers[i] = height[i];
            recur(i + 1, sum + height[i]);
            numbers[i] = 0;
        }
    }

}


