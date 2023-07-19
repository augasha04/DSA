def lineup_students(string):
    stud = string.split()
    stud.sort()
    new= sorted(stud, key=len)
    
    return new[::-1]