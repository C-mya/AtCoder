# 入力を受け取る
A1, A2, A3, A4 = map(int, input().split())

# 色の頻度を数える
color_counts = [0] * 5  # 色は1～4なのでインデックス0～4を用意

# 各色のカウントを手動で増やす
for color in [A1, A2, A3, A4]:
    color_counts[color] += 1

# ペアの数を計算
max_operations = sum(count // 2 for count in color_counts)

# 結果を出力
print(max_operations)

## chat gptに書かせたけど何！？
