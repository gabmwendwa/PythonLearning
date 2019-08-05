# With the while loop we can execute a set of statements as long as a condition is true.
i = 1
while i <= 10:
	print(i)
	i += 1

print("---------")
# Break while loop
i = 1
while i <= 10:
	print(i)
	if i == 5: break
	i += 1

print("---------")
# With the continue statement we can stop the current iteration, and continue with the next:
i = 0
while i < 10:
	i += 1
	if i == 5: continue
	print(i)
