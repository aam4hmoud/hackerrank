if __name__ == '__main__':
    grades = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        grades.append([name, score])
        
    grades = list(sorted(grades, key=lambda x:x[1]))
    lowest = grades[0][1]
    second_lowest = None
    visited_second_lowest = False
    names = []
    
    for grade in grades:
        if (grade[1] > lowest and not visited_second_lowest):
            names.append(grade[0])
            second_lowest = grade
            visited_second_lowest = True
            
        elif (visited_second_lowest):
            if grade[1] == second_lowest[1]:
                names.append(grade[0])
                
    names.sort()
    for name in names:
        print(name)
