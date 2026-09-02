"""
Given a list of numbers, use filter() with a lambda to get only the numbers divisible
by both 3 and 5, then use map() with a lambda to square each of those numbers.
"""
nums = [3, 5, 9, 10, 15, 18, 30, 45, 50]

filtered_nums = list(filter(lambda num: num % 3 == 0 and num % 5 == 0, nums))
print(list(map(lambda num: num * num, filtered_nums)))

print(list(map(lambda x: x * x, filter(lambda x: x % 3 == 0 and x % 5 == 0, nums))))

"""
Logged: Lambdas | Problem #3 (filter+map divisible-by-3-and-5, squared) 
| Correct (first try, both compact and verbose versions) | Articulation: mostly clear, 
minor imprecision ("iterables" instead of "elements") | Referred: no | Insight: solid 
grasp of filter/map/lambda composition; will revisit lazy-eval advantage properly once 
Generators/Iterators topic starts.


"""