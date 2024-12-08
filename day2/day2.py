def count_safe_reports(pathfile):
    f = open(pathfile, "r")
    count = 0

    for line in f:
        numbers = line.split(" ")
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
        
        if flag:
            count += 1

    return count
        
print(count_safe_reports("day2/test.txt"))
print(count_safe_reports("day2/input.txt"))
