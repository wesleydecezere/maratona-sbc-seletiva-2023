import re

n = int(input())
msg = input()
sep = ' .,'

def subs(s):
    return re.sub(r'[ .,]+', '', s)

msg_sem_letras = ''
for i, char in enumerate(msg):
    if char.isalpha():
        continue 
    if char in sep and i > 0 and msg[i-1].isalpha():
        continue
    if char.isnumeric() and i > 0 and msg[i-1].isalpha():
        continue
    msg_sem_letras += char

nums = re.split(r'[ .,]{2,}', msg_sem_letras)
nums = list(map(subs, nums))
print(nums)

nums = [n for n in nums if not n.isnumeric()]

# nums = list(map(lambda s: int(s) if s.isnumeric() else int(), nums))
print(nums)


# split por sep unico
# se 

for i in range(len(nums)):
    if i > 0 and nums[i-1]+1 != nums[i]:
        print(nums[i-1]+1, nums[i])
        break

if i != 0 and i == len(nums)-1:
    print('123')
else:
    print(':)')


