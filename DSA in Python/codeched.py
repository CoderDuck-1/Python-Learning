T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    S = input()
    zero_count = 0
    for j in range(M):
        if (S[j] == "0"):
            zero_count += 1

    one_count = M - zero_count
    print(f"{zero_count} ,{one_count}")

    if(N%2 != 0):
        print("No")
    elif(one_count==zero_count):
        print("Yes")
    elif(one_count>zero_count):
        if((N-M)>=(one_count-zero_count)):
            print("Yes")
        else:
            print("No")
    elif(one_count<zero_count):
        if((N-M)>=(zero_count-one_count)):
            print("Yes")
        else:
            print("No")

