import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) throws IOException {
        new Main().solve();
    }

    public void solve() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        //BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        ArrayList<ConfTimeObj> list = new ArrayList<>();
        int result = 0;

        // 입력 받은거 리스트에 ConfTimeObj 객체로 추가
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            String[] times = br.readLine().split(" ");
            // ConfTimeObj 객체에 생성 및 저장
            list.add(new ConfTimeObj(Integer.parseInt(times[0]), Integer.parseInt(times[1])));
        }
        // 길이별 정렬 사전순 정렬 후 출력
        List<ConfTimeObj> sortedList =  list.stream()
            .sorted(Comparator.comparingInt(ConfTimeObj::getEnd).thenComparing(ConfTimeObj::getStart))
            .collect(Collectors.toList());

        // 개수 세기
        ConfTimeObj temp = null;
        for (int i = 0; i < sortedList.size(); i++) {
            if(i == 0) {
                temp = sortedList.get(i);
                result++;
                continue;
            }
            if (sortedList.get(i).start == sortedList.get(i).end || sortedList.get(i).start >= temp.end) {
                temp = sortedList.get(i);
                result++;
            }
        }
        System.out.println(result);
    }

}
class ConfTimeObj {
    public int start;
    public int end;

    public ConfTimeObj(int start, int end) {
        this.start = start;
        this.end = end;
    }

    public int getStart() {
        return this.start;
    }

    public int getEnd() {
        return this.end;
    }
}