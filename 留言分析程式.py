data = []
data_100以下 = []
data_取good = []
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
total = int(total)
graph = int(graph)
while graph != len(data):
	total = total + len(data[graph])
	if 'good' in data[graph]:
		data_取good.append(data[graph])
	if len(data[graph]) < 100:
		data_100以下.append(data[graph])
	graph = graph + 1
print ('我算的字串平均數為', total/len(data))
print ('我算一百以下的字數有', len(data_100以下), '筆資料')
print (data_100以下[0])
print ('我寫的有good的數有',len(data_取good),'筆')
print (data_取good[0])

#老師的程式碼
sum_len = 0
sum_len =int(sum_len)
for d in data:
	sum_len = sum_len + len(d)
print('老師算的平均是', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print ('老師算的一共有', len(new), '筆留言長度小於100')
print (new[0])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print ('老師寫的有good的數有',len(data_取good),'筆')
print (good[0])

#速寫法
good_fast = []
good_fast = [1 for T in data if 'good' in T]
print (good_fast)
bad = []
bad = ['bad' in G for G in data]

for G in data:
	bad.append('bad' in G)
print (bad)