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


wc = {} # word_count
for d in data:
	words =	d.split()
	for word in words:
		if word in wc:
			wc[word] = wc[word] + 1
		else: 
			wc[word] = 1 #只要右邊有等號，就會新增一個KEY進字典
for word in wc:
	if wc[word] > 1000000:
		print(word,wc[word])

print (len(wc))

print (wc['Allen'])

while True:
	user_input = input('請輸入要查找的字典')
	if user_input == 'q':
		break
	elif user_input not in wc:
		print('這個字沒有出現過喔')
	else:
		print (user_input,'出現過的次數是',wc[user_input],'次')