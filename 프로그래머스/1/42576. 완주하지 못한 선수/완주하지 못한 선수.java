import java.io.*;
import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String ans = "";
        HashMap<String,Integer> mp = new HashMap<>();
        for (String par : participant) {
            mp.put(par, mp.getOrDefault(par,0) +1);
        }
        for (String name : completion) {
            mp.put(name, mp.get(name) -1);
            if(mp.get(name) == 0) mp.remove(name);
        }
        for (String name : mp.keySet()) {
            ans += name;
        }
        return ans;
    }
}