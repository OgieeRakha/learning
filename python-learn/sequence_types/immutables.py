result = True
another_result = result
print(id(result))
print(id(another_result))

result = False
print(id(result))

result_two = "correct"
another_result_two = result
print(id(result_two))
print(id(another_result_two))
result_two += "ish"
print(id(result_two))