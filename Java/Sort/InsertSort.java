import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

public class Main {

    public void solve() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        //BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        ArrayList<Integer> list = new ArrayList<>();

        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            list.add(Integer.parseInt(br.readLine()));
        }
        for (int i = 1; i < n; i++) {
            int elem = list.get(i);
            int j = i - 1;
            for (; j >= 0 && list.get(j) > elem; j--) {
                list.set(j+1, list.get(j));
            }
            list.set(j+1, elem);
        }
        list.forEach(System.out::println);
    }

    public static void main(String[] args) throws IOException {
        new Main().solve();
    }
}