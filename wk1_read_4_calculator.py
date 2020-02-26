f= open("./input.txt")
Lines = f.readlines() 

import calculator
cal = calculator.Solution()

results = []
t = []
# Strips the newline character 
for num_str in Lines: 
	res = cal.calculator_2(num_str)
	results.append(res)
	print(results)


new_file = open('out2.txt', 'w') 
for result in results:
	new_file.writelines(str(result) + "\n") 
new_file.close() 

print(results)