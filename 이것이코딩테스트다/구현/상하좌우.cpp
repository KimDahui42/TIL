#include <iostream>
#include <string>
using namespace std;
int main(){
    int dr[4]={0,0,-1,1};
    int dc[4]={-1,1,0,0};
    int n,current_r=1,current_c=1;
    string op;
    cin>>n;
    cin>>op;
    for(int i=0;i<op.length();i++){
        switch(op[i]){
            case 'L':
                if(current_r+dr[0]>0&&current_r+dr[0]<=n&&current_c+dc[0]>0&&current_c+dc[0]<=n) {
                    current_r+=dr[0];
                    current_c+=dc[0];
                }
                break;
            case 'R':
               if(current_r+dr[1]>0&&current_r+dr[1]<=n&&current_c+dc[1]>0&&current_c+dc[1]<=n) {
                    current_r+=dr[1];
                    current_c+=dc[1];
                }
                break;
            case 'U':
                if(current_r+dr[2]>0&&current_r+dr[2]<=n&&current_c+dc[2]>00&&current_c+dc[2]<=n) {
                    current_r+=dr[2];
                    current_c+=dc[2];
                }
                break;
            default:
               if(current_r+dr[3]>0&&current_r+dr[3]<=n&&current_c+dc[3]>0&&current_c+dc[3]<=n) {
                    current_r+=dr[3];
                    current_c+=dc[3];
                }
                break;
        }
    }
    cout<<current_r<<" , "<<current_c<<endl;
    return 0;
}