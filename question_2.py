test_case = int(input())
for _ in range (test_case):
    a,b,c=map(int,input().split())
    count = 0
    array=[a,b,c]
    array.sort()
    a,b,c=array[0],array[1],array[2]
    while a>=0 and b>=0 and c>=0:
        if a>=b and a>=c:
            if a>=b and a-b >=0 and b>=c:
                a=a-b
                count+=1
            elif a>=c and a-c >=0:
                a=a-c
                count+=1
        elif b>=c:
            if b-a>=0 and a>=c:
                b=b-a
                count+=1
            elif b-c>=0:
                b = b-c
                count+=1
        else:
            if a>=b and c-a >=0:
                c=c-a
                count+=1
            elif b>=a and c-b>=0:
                c =c-b
                count+=1
        if a==0 :
            if b==0 or c==0:
                break
        elif b==0:
            if a==0 or c==0:
                break

    print(count-1)



