
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static class Pos {
        int r, c;
        Pos(int r, int c){
            this.r = r;
            this.c = c;
        }
    }
    public static void main(String[] args) throws IOException {
        int[] dr = {0, 0, -1, 1};
        int[] dc = {-1, 1, 0, 0};

        Deque<Pos> deque = new ArrayDeque<>();

        // input, queue : 1
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int M = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());
        int[][] map = new int[N][M];
        boolean[][] visited = new boolean[N][M];

        for (int i = 0; i < N; i ++){
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j ++){
                int num = Integer.parseInt(st.nextToken());
                if (num == 1){
                    deque.add(new Pos(i, j));
                    visited[i][j] = true;
                }
                map[i][j] = num;
            }
        }


        // 토마토 BFS, visited
        int day = 0;
        while (!deque.isEmpty()) {
            day ++;
            int size = deque.size();
            for (int i = 0; i < size; i++) {

                Pos cur = deque.poll();

                for (int d = 0; d < 4; d++) {
                    int r = cur.r + dr[d];
                    int c = cur.c + dc[d];

                    if (r < 0 || r >= N || c < 0 || c >= M || visited[r][c] || map[r][c] != 0) continue;
                    map[r][c] = 1;
                    deque.add(new Pos(r, c));
                }
            }
        }


        // 인덱스 돌면서 0 있으면 -1 반환, 아니면 날짜 반환
        for (int[] i : map){
            for (int j : i){
                if (j == 0){
                    System.out.println(-1);
                    return;
                }
            }
        }

        System.out.println(day - 1);
    }
}
