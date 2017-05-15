def insert_sort(lists):
    for i in range(1,len(lists)):
        if lists[i-1]>lists[i]:
            temp=lists[i]
            index=i
            while index>0 and lists[index-1]>temp:
                lists[index]=lists[index-1]
                index-=1
            lists[index]=temp

    return lists
