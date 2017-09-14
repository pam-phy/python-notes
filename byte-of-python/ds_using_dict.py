#!/usr/bin/env python3

# “ab”是地址（Adress）薄（Book）的缩写

ab = {
	'Swaroop': 'swaroop@swaroopch.com',
	'Larry': 'larry@wall.org',
	'Matsumoto': 'matz@ruby-lang.org',
	'Spammer': 'spammer@hotmail.com'
}

print("Swaroop's adress is", ab['Swaroop'])

# 删除一对键值-值配对
del ab['Spammer']

print('\nThere are {} contacts in the adress-book\n'.format(len(ab)))

for name, adress in ab.items():
	print('Contact {} at {}'.format(name, adress))

# 添加一对键值-值配对
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
	print("\nGuido's address is", ab['Guido'])
