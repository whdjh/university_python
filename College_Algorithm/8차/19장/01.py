#W kg까지 넣을 수 있는 가방을 들고 쥬얼리샵에 침입하였다고 가정한다. 
#훔칠수 있는 N 개의 보석이 주어졌고 각각이 서로 다른 무게를 갖는다고 가정한다.
#이때 최대의 갑어치가 되도록 가방에 보석을 넣는 방법을 알아내는 알고리즘을 동적계획법으로 구현하려 한다.
#문제 이해를 위해 다음 경우를 가정한다.

#W = 20
#훔칠 수 있는 보석이 종류별로 1개, 즉 총 5개.
#보석종류	무게	값어치
# 1	       2	   3
# 2	       3	   4
# 3	       4	   8
# 4	       5	   8
# 5        9	   10

#동적계획법을 적용하기 위해 다음 성질을 만족하는 W x N 모양의 2차원 행렬 M을 사용한다.
#M[i][j]: 처음부터 i번 째까지의 물건을 살펴보고, 
#배낭의 용량이 j였을 때 배낭에 들어간 물건들의 가치가 최대일 때의 가치

#1. 앞서 설명한 동적계획법을 적용했을 때 최소 비용이 계산되는 것을 보장하기 위해 먼저 최적의 원칙이 보장됨을 설명
#2. 위 알고리즘을 동적계획법으로 구현하라.

def mybag(W, weight, price, N):
#W 무게 한도, weight 보석 무게, price 보석 가격, N 보석 갯수
    #행은 보석의 총갯수를 의미하고 열은 무게를 의미하게 이중배열생성
    double_list = [[0 for x in range(W + 1)] for x in range(N + 1)]
    for n in range(N + 1):
        for w in range(W + 1):
            #일단 n이 0인 경우는 넣을 보석이 없는 것이므로 다 0이고,
            #w가 0인 경우는 배낭이 없는 것이므로 다 0이다.
            if n == 0 or w == 0:
                double_list[n][w] = 0;
            #최대를 넣을 수 있는 무게를 비교하여 최신화
            elif weight[n - 1] <= w:
                double_list[n][w] = max(price[n - 1] + double_list[n - 1][w - weight[n - 1]], double_list[n - 1][w])
            else:
                double_list[n][w] = double_list[n - 1][w]
    return double_list[N][W]

W = 20
weight = [2, 3, 4, 5, 9]
price = [3, 4, 8, 8, 10]
N = 5

print(mybag(W, weight, price, N))