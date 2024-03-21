import java.util.HashMap;

class Solution {
    public int solution(String[] friends, String[] gifts) {
        int ans = 0;
        int size = friends.length;
        
        // 해시맵
        HashMap<String, Integer> map = new HashMap<String, Integer>();
        int idx = 0;
        for (String f : friends){
            map.put(f, idx++);
        }
        
        int[][] friendsArr = new int[size][size];
        int[] friendsDegree = new int[size];
        
        // degree, arr
        for (String gift : gifts){
            String[] s = gift.split(" ");
            friendsDegree[map.get(s[0])] ++;
            friendsDegree[map.get(s[1])] --;
            friendsArr[map.get(s[0])][map.get(s[1])] ++;
        }
        
        // 인덱스 돌면서 비교해서 선물 최대개수 
        for (int i = 0; i < size; i ++){
            int cnt = 0;
            for (int j = 0; j < size; j ++){
                if (i == j) continue;
                if (friendsArr[i][j] > friendsArr[j][i]) cnt ++;
                else if (friendsArr[i][j] == friendsArr[j][i]){
                    if (friendsDegree[i] > friendsDegree[j]){
                        cnt ++;
                    }
                }
            }
            if (cnt > ans) ans = cnt;
        }
        
        
        return ans;
    }
}
