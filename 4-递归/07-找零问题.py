# -*- coding: utf-8 -*-

# 递归（记忆化搜索）
def rec_make_change(coins, change, memo={}):
    if change in coins:
        return 1

    if change not in memo:
        min_coins = change
        for coin in (c for c in coins if c < change):
            min_coins = min(min_coins, rec_make_change(coins, change - coin) + 1)
        memo[change] = min_coins

    return memo[change]


# 动态规划
def dp_make_change(coins, change):
    coin_used = [0] * (change + 1)
    dp = [float('inf')] * (change + 1)
    dp[0] = 0
    for coin in coins:
        for cents in range(coin, change + 1):
            # dp[cents] = min(dp[cents], dp[cents - coin] + 1)
            if (coin_count := dp[cents - coin] + 1) <= dp[cents]:
                dp[cents] = coin_count
                coin_used[cents] = coin

    return dp[change], coin_used


# 动态规划2
def dp_make_change_2(coins, change):
    coin_used = [0] * (change + 1)
    dp = [cents for cents in range(change + 1)]
    for cents in range(change + 1):
        for coin in (c for c in coins if c <= cents):
            # dp[cents] = min(dp[cents], dp[cents - coin] + 1)
            if (coin_count := dp[cents - coin] + 1) <= dp[cents]:
                dp[cents] = coin_count
                coin_used[cents] = coin

    return dp[change], coin_used


def print_coins(change, coin_used):
    print(f'{change} 的找零方案:', end=' ')
    coins = []
    while change > 0:
        coin = coin_used[change]
        change -= coin
        coins.append(coin)
    print(', '.join(str(coin) for coin in coins))


if __name__ == '__main__':
    print(rec_make_change([1, 5, 10, 25], 63))
    print(dp_make_change([1, 5, 10, 25], 63)[0])
    print(dp_make_change_2([1, 5, 10, 25], 63)[0])
    print('*' * 50)

    cl = [1, 5, 10, 21, 25]

    _, coin_used = dp_make_change(cl, 63)
    print_coins(63, coin_used)
    print_coins(52, coin_used)

    print('*' * 50)

    _, coin_used_2 = dp_make_change_2(cl, 63)
    print_coins(63, coin_used_2)
    print_coins(52, coin_used_2)
