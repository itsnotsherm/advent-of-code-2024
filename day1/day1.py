def sum_of_sorted_distances(pathfile):
    f = open(pathfile, "r")

    left_list = []
    right_list = []

    for line in f:
        numbers = line.split("   ")
        left_list.append(int(numbers[0]))
        right_list.append(int(numbers[1]))

    f.close()

    left_list.sort()
    right_list.sort()

    sum = 0

    for i in range(len(left_list)):
        sum += abs(left_list[i] - right_list[i])

    return sum

def similarity_score(pathfile):
    f = open(pathfile, "r")

    left_list = []
    right_list = []

    for line in f:
        numbers = line.split("   ")
        left_list.append(int(numbers[0]))
        right_list.append(int(numbers[1]))

    f.close()

    score = 0
    for n in left_list:
        score += n * right_list.count(n)
    
    return score

print(sum_of_sorted_distances("day1/input.txt"))
print(sum_of_sorted_distances("day1/test.txt"))

print(similarity_score("day1/input.txt"))
print(similarity_score("day1/test.txt"))