def solution(genres, plays):
    answer,top_list,keys = [[],[],[]]
    genre_list_dic={i:[] for i in genres}
    
    for i,play in enumerate(plays):
        genre_list_dic[genres[i]].append((play,i))
        
    for key in genre_list_dic.keys():
        genre_list_dic[key].sort(key=lambda x:(-x[0],x[1]))
        total=sum(v for v,i in genre_list_dic[key])
        top_list.append((total,key))
        
    for i in [key for total,key in sorted(top_list,reverse=True)]:
        if len(genre_list_dic[i])>=2:
            answer.extend([genre_list_dic[i][0][1],genre_list_dic[i][1][1]])
        else:
            answer.append(genre_list_dic[i][0][1])

    return answer