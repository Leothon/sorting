def shellSort(lists):
    step=len(lists)/2
    while step>0:
        for i in range(step,len(lists)):
            while i>=step and lists[i-step]>lists[i]:
                lists[i],lists[i-step]=lists[i-step],lists[i]
                i-=step
        step=step/2
    return lists