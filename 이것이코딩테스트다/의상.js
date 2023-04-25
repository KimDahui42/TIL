function solution(clothes){
    let obj={};
    clothes.forEach((curr)=>{
        if(!(curr[1] in obj)) obj[curr[1]]=[curr[0]];
        else obj[curr[1]].push(curr[0]);
    });
    console.log(obj);
    return Object.keys(obj).reduce((acc,curr)=>{
        return acc*(obj[curr].length+1);
    },1)-1;
}
