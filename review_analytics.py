data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data))

wc = {} #word_count
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1

while True:
	word = input('你想查什麼字?')
	if word == 'q':
		break
	if word in wc:
		print(wc[word])
	else:
		print('此字沒有出現過！')

print('感謝使用')



# sum_len = 0
# for d in data:
# 	sum_len += len(d)

# print('留言的平均長度為', sum_len/len(data))

# new = []
# for d in data:
# 	if len(d) < 100:
# 		new.append(d)
# print ('一共有', len(new), '比留言長度小於100')


# good = []
# for d in data:
# 	if 'good' in d:
# 		good.append(d)

# good = [d for d in data if 'good' in d]
# bad = ['bad' in d for d in data]
# print(bad)