if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    marks_obtained_by_student = student_marks[query_name]
    total_marks = 0
    
    for mark in marks_obtained_by_student:
        total_marks += mark
        
    print(f"{total_marks / len(marks_obtained_by_student):.2f}")
