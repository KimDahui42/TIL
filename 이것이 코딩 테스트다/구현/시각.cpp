// 정수 n이 입력되면 00시 00분 00초부터 n시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오.
// 예를 들어 1을 입력했을 때 다음은 3이 하나라도 포함되어 있으므로 세어야하는 시각이다.

#include <iostream>
using namespace std;
#define endl '\n'

int main(){
    int n,ans=0,i,j,k,temp;
    cin>>n;
    for(i=0;i<=n;i++){
        for(j=0;j<60;j++){
            for(k=0;k<60;k++){
               if(i%10==3||j/10==3||j%10==3||k%10==3||k/10==3)ans++;
            }
        }
    }
    cout<<ans<<endl;
    return 0;
}