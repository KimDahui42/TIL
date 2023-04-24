function solution(n, words) {
    var answer = [];
    var m=new Map();
    var idx,break_flag=false,tmp=words[0];
    for(idx=0;idx<words.length;){
        if(m.has(words[idx])||(idx!=0&&tmp[tmp.length-1]!==words[idx][0])){
            answer[0]=idx%n+1;
            answer[1]=Math.floor(idx/n)+1;
            break_flag=true;
            break;
        }
        m.set(words[idx],idx%n);
        tmp=words[idx++];
    }
    if(idx==words.length) return [0,0];
    return answer;
}
