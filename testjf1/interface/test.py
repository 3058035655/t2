# dic = {'a':31, 'bc':5, 'c':3, 'asd':4, 'aa':74, 'd':0}
# dict= sorted(dic.items(), key=lambda d:d[1], reverse = True)
# print(dict)
content_tz = {'access_token': '1b1d5757-9322-4d83-bb79-fed79f973dad',
                              'amount': '100',
                              'biddCode': 'biddcode',
                              'investType': '1',
                              'sessionId': 'sessionid',
                              'sign': 'sign',
                              'signType': 'MD5',
                              'source': '4',
                              'userCode': 'usercode'
                              }
sorted(content_tz.keys())
print(content_tz)
print(content_tz.keys())
l=list(content_tz.keys())
print(l)
#
# my_alphabet = ['a', 'b', 'c']
# my_alphabet=l
# def custom_key(word):
#    numbers = []
#    for letter in word:
#       numbers.append(my_alphabet.index(letter))
#    return numbers
# # python中的整数列表能够比较大小
# # custom_key('cbaba')==[2, 1, 0, 1, 0]
#
# x=['cbaba', 'ababa', 'bbaa']
# x.sort(key=custom_key)