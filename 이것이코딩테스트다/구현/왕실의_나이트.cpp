/*
행복 왕국의 왕실 정원은 체스판과 같은 8*8 좌표 평면이다. 왕실 정원의 특정한 한 칸에 나이트가 서 있다. 나이트는 매우 충성스러운 신하로서 매일 무술을 연마한다.
나이트는 말을 타고 있기 때문에 이동을 할 떄는 1자 형태로만 이동할 수 있으며 정워 밖으로는 나갈 수 없다. 나이트는 특정한 위치에서 다음과 같은 2가지 경우로 이동할 수 있다.
1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기
이처럼 8*8 좌표 평면상에서 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성하시오. 
이때 왕실의 정원에서 행 위치를 표현할 때는 1부터 8로 표현하며, 열 위치를 표현할 때는 a부터 h로 표현한다.
*/

#include<iostream>
#include<string>
using namespace std;
int main(){
    std::ios::sync_with_stdio(false);
    cin.tie(NULL);cout.tie(NULL);
    string pos;
    int move[8][2]={{-2,1},{-2,-1},{2,1},{2,-1},{1,-2},{-1,-2},{1,2},{-1,2}};
    int ans=0,i,r,c,next_r,next_c;
    cin>>pos;
    r=pos[1]-'1';
    c=pos[0]-'a';
    for(i=0;i<8;i++){
        next_r=r+move[i][0];
        next_c=c+move[i][1];
        if(next_r<8&&next_r>=0&&next_c<8&&next_c>=0){
            ans++;
        }
    }  
    cout<<ans<<'\n';
    return 0;
}