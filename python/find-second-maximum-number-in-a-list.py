if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    winner = max(arr)
    runner_up = float("-inf")
    
    for score in arr:
        if (score > runner_up and score < winner):
            runner_up = score
            
    print(runner_up)
