package Day03;

public class 프로_42680_조이스틱 {
    public int solution(String name) {
        int answer = 0;
        int nameLength = name.length();
        int cursorIndex = 0;
        int moveCount = nameLength - 1; // 좌우 움직임

        for(int i = 0; i < nameLength; i++) {
            answer += Math.min(name.charAt(i) - 'A', 'Z' - name.charAt(i) + 1);

            cursorIndex = i + 1;
            while(cursorIndex < nameLength && name.charAt(cursorIndex) == 'A') {
                cursorIndex++;
            }

            moveCount = Math.min(moveCount, i * 2 + nameLength - cursorIndex);
            moveCount = Math.min(moveCount, (nameLength - cursorIndex) * 2 + i);
        }

        return answer + moveCount;
    }
}
