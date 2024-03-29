#include <vector>
#include <string>
#include<queue>
#include <sstream>
#include<map>

using namespace std;

vector<string> split(string str) {
    vector<string>tmp;
    stringstream ss(str);
    string temp;
    while (getline(ss,temp,' ')) {
        tmp.push_back(temp);
    }
    return tmp;
}
vector<string> solution(vector<string> record) {
    map<string, pair<string, queue<string>>>temp;
    //userid,name,command stack
    vector<string> answer;
    int i;
    for (i = 0; i < record.size(); i++) {
        vector<string>tmp = split(record[i]);
        if (tmp[0] == "Enter") {
            if (temp.find(tmp[1]) == temp.end()) {
                queue<string>q;
                q.push(tmp[0]);
                temp.insert(make_pair(tmp[1], make_pair(tmp[2], q)));
                answer.push_back(tmp[1]);
            }
            else {
                temp[tmp[1]].second.push(tmp[0]);
                temp[tmp[1]].first = tmp[2];
                answer.push_back(tmp[1]);
            }
        }
        else if (tmp[0] == "Leave") {
            answer.push_back(tmp[1]);
            temp[tmp[1]].second.push(tmp[0]);
        }
        else if (tmp[0] == "Change") {
            temp[tmp[1]].first = tmp[2];
        }
    }
    for (i = 0; i < answer.size(); i++) {
        string command = temp[answer[i]].second.front();
        temp[answer[i]].second.pop();
        if (command == "Enter") {
            answer[i] = temp[answer[i]].first + "님이 들어왔습니다.";
        }
        else{
            answer[i] = temp[answer[i]].first + "님이 나갔습니다.";
        }
    }
    return answer;
}
