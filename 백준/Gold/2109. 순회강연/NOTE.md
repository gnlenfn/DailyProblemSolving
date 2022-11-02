### 우선순위 큐를 활용한 그리디 알고리즘

처음에 푼 풀이는 
```C++
#include <bits/stdc++.h>
using namespace std;

int n;
int arr[10001];
int main() {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n;
    for(int i = 1; i < n + 1; i++){
        int d, p;
        cin >> p >> d;
        if(arr[d] < p) arr[d] = p;
    }

    cout << accumulate(arr, arr + 10000, 0) << "\n";
    
    return 0;
}
```

이렇게 해서 d일에 받을 수 있는 가장 큰 pay를 찾고 총 합을 구하도록 했다.

하지만 `각 대학에서는 d(1 ≤ d ≤ 10,000)일 안에 와서 강연을 해 주면` 이라는 조건이 있기 때문에
```
10 2
10 2
3 1
```
이러한 케이스는 내 풀이의 반례가 된다. 10원씩 2일안에 하면 되기 때문에 이틀간 10원짜리 두 개 강연을 하면 더 많은 돈을 받기 때문이다. 

---
 
우선순위 큐를 활용하여 최대 힙을 만들고 힙의 크기가 d일 안에 와달라는 요청에서의 최대 d값이 된다.  
그리고 우선순위 큐에 일단 pay를 모두 push한 후에 `pq.size()`와 d의 값을 비교하여 pop할지 말지 결정한다.
