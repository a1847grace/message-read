data = []
count = 0
count = bool(count)
with open('reviews.txt', 'r') as message:
	for line in message:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print (len(data))
print ('檔案讀取完了，總共有：', len(data), '筆資料')			
#下列為我自行寫的程式碼
graph = 0 
total = 0
total =int(total)
graph = int(graph)
while graph != len(data):
	total = total + len(data[graph])
	graph = graph + 1
print ('我算的字串平均數為', total/len(data))

#老師的程式碼
sum_len = 0
sum_len =int(sum_len)
for d in data:
	sum_len = sum_len + len(d)
print('老師算的平均是', sum_len/len(data))
