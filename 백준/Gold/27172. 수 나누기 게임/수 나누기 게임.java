import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        int[] num = new int[N];

        boolean[] visited = new boolean[1000001];
        int[] ans = new int[1000001];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i ++){
            num[i] = Integer.parseInt(st.nextToken());
            visited[num[i]] = true;
        }


        for (int number : num){
            for (int n = number * 2; n < 1000001; n += number) {
                if (visited[n]) {
                    ans[n] --;
                    ans[number] ++;
                }
            }
        }

        for (int number : num){
            sb.append(ans[number]).append(" ");
        }

        System.out.println(sb.toString());

    }
}
