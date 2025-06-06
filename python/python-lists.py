if __name__ == '__main__':
    list_of_values = []
    N = int(input())
    
    for _ in range(N):
        command = input().split(" ")
        if (command[0] == "insert"):
            list_of_values.insert(int(command[1]), int(command[2]))
        elif (command[0] == "print"):
            print(list_of_values)
        elif (command[0] == "remove"):
            list_of_values.remove(int(command[1]))
        elif (command[0] == "append"):
            list_of_values.append(int(command[1]))
        elif(command[0] == "sort"):
            list_of_values.sort()
        elif(command[0] == "reverse"):
            list_of_values.reverse()
        elif (command[0] == "pop"):
            list_of_values.pop()
