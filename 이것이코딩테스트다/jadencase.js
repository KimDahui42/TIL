function solution(s) {
    return s.split(' ').reduce((acc,item) => {
        acc.push(item.substr(0,1).toUpperCase()+item.substr(1,).toLowerCase());
        return acc;
    },[]).join(' ');
}
