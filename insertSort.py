
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


def main():
    lists=[7,5,6,3,4,8,1]
    insert_sort(lists)
    print lists



if __name__ == '__main__':
    main()