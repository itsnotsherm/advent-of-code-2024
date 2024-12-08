def count_safe_reports(pathfile):
    f = open(pathfile, "r")
    count = 0

    for line in f:
        numbers = line.split(" ")
        if is_safe_report(numbers):
            count += 1

    return count

def count_safe_reports_with_dampener(pathfile):
    f = open(pathfile, "r")
    count = 0

    for line in f:
        numbers = line.split(" ")
        if is_safe_report(numbers):
            count += 1
        else:
            for i in range(len(numbers)):
                new_numbers = numbers[0:i] + numbers[i+1:len(numbers)]
                if is_safe_report(new_numbers):
                    count += 1
                    break

    return count

def is_safe_report(numbers):
    decreasing = int(numbers[0]) > int(numbers[1])
    flag = True
    i = 1

    while flag and i < len(numbers):
        a = int(numbers[i-1])
        b = int(numbers[i])

        if (decreasing and (a <= b)) or ((not decreasing) and (a >= b)):
            flag = False
            
        else:
            diff = abs(a - b)
            if (diff < 1) or (diff > 3):
                flag = False
            
        i += 1
    return flag
    
        
print(count_safe_reports("day2/test.txt"))
print(count_safe_reports("day2/input.txt"))
print(count_safe_reports_with_dampener("day2/test.txt"))
print(count_safe_reports_with_dampener("day2/input.txt"))