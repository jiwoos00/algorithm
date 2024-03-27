
import java.io.*;
import java.util.*;

public class Main {
    static int[][] map = new int[9][9];
    static boolean[][] rows = new boolean[9][10];
    static boolean[][] cols = new boolean[9][10];
    static boolean[][] smap = new boolean[9][10];
    static boolean flag;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        // input
        for (int i = 0; i < 9; i++) {
            String tmp = br.readLine();
            for (int j = 0; j < 9; j++) {
                map[i][j] = tmp.charAt(j) - '0';
                rows[i][map[i][j]] = true;
                cols[j][map[i][j]] = true;

                smap[3 * (i / 3) + (j / 3)][map[i][j]] = true;
            }
        }
        sudoku(0);
    }


    static void sudoku(int num) {
        if (flag) return;
        if (num >= 81){
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < 9; i ++){
                for (int j = 0; j < 9; j ++){
                    sb.append(map[i][j]);
                }
                sb.append("\n");
            }

            System.out.println(sb.toString());
            flag = true;
            return;
        }

        int r = num / 9;
        int c = num  % 9;

        if (map[r][c] != 0) sudoku(num + 1);
        else {
            for (int i = 1; i < 10; i ++){
                if (rows[r][i] || cols[c][i] || smap[3 * (r / 3) + c / 3][i]) continue;
                rows[r][i] = true;
                cols[c][i] = true;
                smap[3 * (r / 3) + c / 3][i] = true;
                map[r][c] = i;

                sudoku(num + 1);

                rows[r][i] = false;
                cols[c][i] = false;
                smap[3 * (r / 3) + c / 3][i] = false;
                map[r][c] = 0;
            }
        }
    }
}