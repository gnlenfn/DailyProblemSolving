### 홀짝 경우를 나눠야 함

- 특정 위치에 도착하는 경우의 수가 2가지 생김 (홀수 번째 이동, 짝수 번째 이동)
- 따라서 `visited`를 2차원으로 만들었음
- 또한 몇 번째 이동인지에 (`turn`) 따라 최종 목적지에 변화가 있으므로 같은 턴에는 모든 경우의 수를 한꺼번에 확인  
--> 큐에 다음 이동할 곳을 푸쉬한 후 이번 턴에 푸쉬된 것들만 순회를 한 후 `turn++`를 하고 다음 턴 진행


플래티넘 문제는 처음 풀어봤는데 어렵다. 내가 푼 것도 사실 아니고 답을 보고 아이디어를 모두 얻었다. 코드 구현 자체도 조금 참고를 했고..

### ***다시 풀어보기***
