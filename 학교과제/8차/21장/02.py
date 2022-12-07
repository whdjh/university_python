def mybag(W, N):
    if W == 0 or N == 0:
        return 0
    
    if weight[N - 1] > W:
        return mybag(W, N - 1)
    
    else:
        return max(price[N - 1] + mybag(W - weight[N - 1], N - 1), mybag(W, N - 1))


weight = [2, 3, 4, 5, 9]
price = [3, 4, 8, 8, 10]
print(mybag(20, 5))