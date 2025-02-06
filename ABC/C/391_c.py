N, Q = list(map(int, input().split(" ")))
N_list = [1] * N
# 鳩Pを巣Hに
# 鳩の識別、何？
for i in range(Q):
    query = list(map(int, input().split(" ")))
    
    if query[0] == 2:
        count = 0
        for i in range(N):       
            if N_list[i] >= 2:
                count += 1
        print(count)
    else:
        if N_list[query[1] - 1] != 0:
            N_list[query[1] - 1] = N_list[query[1] - 1] - 1
            N_list[query[2] - 1] = N_list[query[2] - 1] + 1

    print(N_list)
if
