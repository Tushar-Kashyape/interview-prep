def minimum_time(cur: int, pos: list, time: list) -> int:
    min_time = 0

    for i in range(len(time)):
        if abs(cur - pos[i]) == 0: return 0

        if i == 0:
            min_time = abs(cur - pos[0]) * time[0]
        else:
            min_time = min(min_time, abs(cur - pos[i]) * time[i])

    return min_time

cur = 4
pos = [1, 5, 6]
time = [2, 3, 1]
print(minimum_time(cur, pos, time))