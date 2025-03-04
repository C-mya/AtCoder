N, Q = list(map(int, input().split()))

house = {}
pigeon = {}
for i in range(1, N + 1):
    house[i] = [i]
    pigeon[i] = i

many_pigepn_house = set()

for i in range(Q): # Q個のクエリ
    query = list(map(int, input().split()))
    if query == [2]: # valueが複数ある巣の数を出力
        print(len(many_pigepn_house))

    else:
        P = query[1] # pigeon
        H = query[2] # house
        house[pigeon[P]].remove(P) # 鳩の取り出し ### listなので遅い、setにすることでO(1)にできる
        if pigeon[P] in many_pigepn_house and len(house[pigeon[P]]) <= 1: ### setにすることでO(1)
            many_pigepn_house.discard(pigeon[P])
        pigeon[P] = H # 鳩の巣移動
        house[H] += [P] # 鳩の移動
        if len(house[H]) > 1:
            many_pigepn_house.add(H)

