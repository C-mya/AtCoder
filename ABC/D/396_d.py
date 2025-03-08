N, M = list(map(int, input().split()))

# 全部入りリスト作成
all_list = []
for i in range(M):
    u, v, w = list(map(int, input().split()))
    if [u, v, w] not in all_list:
        all_list += [[u, v, w]]

# uが1のもの
u_1_list = []




# vがNのもの 
v_N_list = []
for i in range(len(all_list)):
    if all_list[i][1] == N:
        if [all_list[i][0], all_list[i][2]] not in v_N_list:
            v_N_list += [[all_list[i][0], all_list[i][2]]]



# 中間の点の組み合わせをどうやって出す？
