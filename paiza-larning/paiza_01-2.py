# import <ライブラリ名> でライブラリを読み込む
# ライブラリ名の後ろに as (xxx) で別名をつけられる
# import random as rand
import random

# random.raondom() で0.0以上1.0未満の浮動小数点数をランダム生成
float_num = random.random()
print(float_num)

# print(); ← いつものクセで最後にセミコロンつけて怒られました

# random.randint(1, 10) で1~10までの範囲内で整数をランダム生成
int_num = random.randint(1, 10)
print(int_num)