
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static class Pos {
        int r, c;
        Pos(int r, int c){
            this.r = r;
            this.c = c;
        }
    }

    static int N, M, ans;
    static List<Pos> chickenShop, houses;
    static int[] numbers;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        chickenShop = new ArrayList<>();
        houses = new ArrayList<>();

        // input
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        for (int i = 0 ; i < N; i ++){
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j ++){
                int num = Integer.parseInt(st.nextToken());
                if (num == 1) houses.add(new Pos(i, j));
                if (num == 2) chickenShop.add(new Pos(i, j));
            }
        }

        // max M
        ans = Integer.MAX_VALUE;
        visited = new boolean[chickenShop.size()];
        recur(0, 0);

        System.out.println(ans);
    }

    static void recur(int start, int cnt){
        if (cnt == M){
            // chicken - home distance
            int dis = 0;
            for (Pos house : houses) {
                int minDis = Integer.MAX_VALUE;
                for (int c = 0; c < chickenShop.size(); c++) {
                    if (!visited[c]) continue;
                    minDis = Math.min(minDis, getDistance(house.r, house.c, chickenShop.get(c).r, chickenShop.get(c).c));
                }
                dis += minDis;
            }
            ans = Math.min(ans, dis);
            return;
        }

        for (int i = start; i < chickenShop.size(); i ++){
            visited[i] = true;
            recur(i + 1, cnt + 1);
            visited[i] = false;

        }
    }

    static int getDistance(int r1, int c1, int r2, int c2){
        return Math.abs(r1 - r2) + Math.abs(c1 - c2);
    }
}
