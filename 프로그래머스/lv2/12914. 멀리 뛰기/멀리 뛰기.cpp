#include <string>
#include <vector>

using namespace std;

long long arr[2002];
long long solution(int n) {    
    arr[1] = 1;
    arr[2] = 2;
    
    for(int i = 3; i < n + 1; i++){
        arr[i] = (arr[i - 1] + arr[i - 2]) % 1234567; 
    }
    return arr[n];
}