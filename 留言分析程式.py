data = []
count = 0
count = bool(count)
with open('reviews.txt', 'r') as message:
	for line in message:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print (count)
print (data[0])

print ('----------')

print (data[1])
