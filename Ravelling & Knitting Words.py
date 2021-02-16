# Soal 3 - Ravelling & Knitting Words (40 Poin)
# Buatlah sebuah file python yang berisi 2 buah return function,
# dengan 1 argumen yang dapat digunakan untuk mengurai & merajut sebuah string
# fungsi ravel(...) akan mengurai string. contoh output yang diharapkan adalah sebagai berikut:

# Function Initialization :
# def ravel(...):
#     ......
    
# Use the function
# print(ravel('Purwadhika'))
# print(ravel('Digital'))
# print(ravel('Coding'))
# print(ravel('School'))

# Output:
# PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika
# DDiDigDigiDigitDigitaDigital
# CCoCodCodiCodinCoding
# SScSchSchoSchooSchool

# Sedangkan fungsi knit(...) akan merajut kembali string yang terurai menjadi bentuk kata asalnya.
# contoh output yang diharapkan adalah sebagai berikut:

# Function Initialization :
# def knit(...):
#     ......
    
# Use the function
# print(knit('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))
# print(knit('DDiDigDigiDigitDigitaDigital'))
# print(knit('CCoCodCodiCodinCoding'))
# print(knit('SScSchSchoSchooSchool'))

# Output:
# Purwadhika
# Digital
# Coding
# School


#####################################################################################
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# num = 0
# while num < 6:
#   print((str(num) + ' ') * num)
#   num += 1
#####################################################################################


user = 'purwadhika'
num = 0
    
for i in user:
    print(i + user[num] * num, end=' ')
    num += 1