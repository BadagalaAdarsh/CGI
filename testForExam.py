test_case = int(input())
for _ in range (test_case):
    n = int(input())
    array = list(map(int,input().split()))
    ali=0
    bob=0
    count=0
    count1=0

    for i in range (len(array)-1):
        if array[i]<=array[i+1]:
            if array[i]<array[i+1]:
                ali+=1
                bob+=1
                if ali>count:
                    count = ali

                if bob > count1:
                    count1 = bob
            elif array[i]==array[i+1]:
                ali=0

        else:
            ali = 0
            bob = 0

    print(count1-count)

