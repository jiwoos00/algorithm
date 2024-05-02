
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;

public class Main {
    static class Pos {
        int num;
        String cmd;

        Pos (int num, String cmd){
            this.num = num;
            this.cmd = cmd;
        }
    }
    static int T;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        T = Integer.parseInt(br.readLine());
        for (int tc = 0; tc < T; tc ++){
            String[] tmp = br.readLine().split(" ");
            int A = Integer.parseInt(tmp[0]);
            int B = Integer.parseInt(tmp[1]);
            String ans = DSLR(A, B);

            System.out.println(ans);
        }
        
    }

    static String DSLR(int A, int B){
        Queue<Pos> queue = new ArrayDeque<>();
        queue.add(new Pos(A, ""));
        boolean[] visited = new boolean[10001];

        while (!queue.isEmpty()){
            Pos tmp = queue.poll();
            int num = tmp.num;
            String cmd = tmp.cmd;

            if (num == B) return cmd;

            // D
            int temp = (num * 2) % 10000;
            if (!visited[temp]){
                visited[temp] = true;
                queue.add(new Pos(temp, cmd + 'D'));
            }

            // S
            temp = (num - 1 + 10000) % 10000;
            if (!visited[temp]){

                visited[temp] = true;
                queue.add(new Pos(temp, cmd + 'S'));
            }

            // L
            temp = (num % 1000) * 10 + (num / 1000);
            if (!visited[temp]){
                visited[temp] = true;
                queue.add(new Pos(temp, cmd + 'L'));
            }

            // R
            temp = (num % 10) * 1000 + (num / 10 + 10000) % 10000;
            if (!visited[temp]){
                visited[temp] = true;
                queue.add(new Pos(temp, cmd + 'R'));
            }
        }
        return "";
    }

}
