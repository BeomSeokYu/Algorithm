import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashSet;

class Main {

    public void solve() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        //BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        ArrayList<WordObj> list = new ArrayList<>();
        ArrayList<String> l = new ArrayList<>();

        // 입력 받은거 리스트에 추가
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            l.add(br.readLine());
        }
        // 중복 제거
        l = new ArrayList<String>(new HashSet<String>(l));
        // WordObj 객체에 생성 (단어길이와 단어를 저장)
        l.forEach(word -> list.add(new WordObj(word.length(), word)));
        l = null;
        // 길이별 정렬 사전순 정렬 후 출력
        list.stream()
            .sorted(Comparator.comparingInt(WordObj::getLength).thenComparing(WordObj::getWord))
            .forEach(s -> System.out.println(s.word));
    }

    public static void main(String[] args) throws IOException {
        new Main().solve();
    }

    public class WordObj{
        public int length;
        public String word;

        public int getLength() {
            return this.length;
        }

        public String getWord() {
            return this.word;
        }

        public WordObj(int length, String word) {
            this.length = length;
            this.word = word;
        }
    }
}