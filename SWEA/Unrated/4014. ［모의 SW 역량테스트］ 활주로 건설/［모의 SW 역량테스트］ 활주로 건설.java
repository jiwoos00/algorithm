import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
public class Solution {

    static int N, L, ans = 0;
    static int[][] mapH, mapW;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine()), t = 0;
        while (t ++ < T) {
            ans = 0;
            StringTokenizer st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            L = Integer.parseInt(st.nextToken());

            mapW = new int[101][101];
            mapH = new int[101][101];
            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < N; j++) {
                    int n = Integer.parseInt(st.nextToken());
                    mapH[i][j] = n;
                    mapW[j][i] = n;
                }
            }

            func(mapH);
            func(mapW);
            sb.append("#").append(t).append(" ").append(ans).append("\n");
        }
        System.out.println(sb);
    }

    static void func(int[][] map) {
        for (int i = 0; i < N; i++) {
            boolean move = true;
            int prev = 1;

            for (int j = 0; j < N - 1; j++) {
                int preVal = map[i][j];
                int curVal = map[i][j + 1];
                int diff = Math.abs(preVal - curVal);

                if (diff == 0) prev++;
                else if (diff == 1) {
                    if (curVal > preVal) {
                        if (prev >= L) prev = 1;
                        else {
                            move = false;
                            break;
                        }
                    } else {
                        for (int k = 1; k <= L; k++) {
                            if (curVal != map[i][j + k]) {
                                move = false;
                                break;
                            }
                        }
                        j += L - 1;
                        prev = 0;
                    }
                } else if (diff >= 2) {
                    move = false;
                    break;
                }
            }
            if (move) ans++;
        }
    }
}

