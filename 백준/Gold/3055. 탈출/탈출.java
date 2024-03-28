import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static class Pos {
        int x, y;
        Pos(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
    static final int[] dx = {0, 0, 1, -1};
    static final int[] dy = {1, -1, 0, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int R = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());
        char[][] forest = new char[R][C];

        Queue<Pos> water = new LinkedList<>();
        Queue<Pos> hedgehog = new LinkedList<>();

        for (int i = 0; i < R; i++) {
            String tmp = br.readLine();
            for (int j = 0; j < C; j++) {
                forest[i][j] = tmp.charAt(j);
                if (forest[i][j] == '*') {
                    water.offer(new Pos(i, j));
                } else if (forest[i][j] == 'S') {
                    hedgehog.offer(new Pos(i, j));
                }
            }
        }

        int time = 0;
        boolean flag = false;

        while (!hedgehog.isEmpty()) {
            time++;

            int waterSize = water.size();
            for (int i = 0; i < waterSize; i ++) {
                Pos w = water.poll();
                for (int d = 0; d < 4; d++) {
                    int nx = w.x + dx[d];
                    int ny = w.y + dy[d];
                    if (nx < 0 || nx >= R || ny < 0 || ny >= C || forest[nx][ny] == 'D' || forest[nx][ny] == 'X' || forest[nx][ny] == '*')
                        continue;
                    forest[nx][ny] = '*';
                    water.offer(new Pos(nx, ny));
                }
            }


            int hedgehogSize = hedgehog.size();
            for (int i = 0; i < hedgehogSize; i++) {
                Pos h = hedgehog.poll();
                for (int d = 0; d < 4; d++) {
                    int nx = h.x + dx[d];
                    int ny = h.y + dy[d];
                    if (nx < 0 || nx >= R || ny < 0 || ny >= C) continue;
                    if (forest[nx][ny] == 'D') {
                        flag = true;
                        break;
                    }
                    if (forest[nx][ny] == '.') {
                        forest[nx][ny] = 'S';
                        hedgehog.offer(new Pos(nx, ny));
                    }
                }
                if (flag) break;
            }
            if (flag) break;
        }

        if (flag) {
            System.out.println(time);
        } else {
            System.out.println("KAKTUS");
        }
    }
}
