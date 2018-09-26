
# coding: utf-8

# In[1]:


import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

# Chúng ta nhập thư viện datetime vào chương trình
# sau đó khai báo biến now và thiết lập biến now là thời gian (ngày tháng năm và giờ)
# Sau đó chúng ta có câu lệnh in ra màn hình: print ("Current date and time : ")
# Nên màn hình sẽ hiện câu "Current date and time :"
# chuyển biến now thành một string theo dạng năm-tháng-ngày giờ:phút:giây
# Sau đó in kết quả này ra màn hình

def sum(x, y):
    sum = x + y
    if sum in range(15, 20):
        return 20
    else:
        return sum

print(sum(10, 6))
print(sum(10, 2))
print(sum(10, 12))

# Định nghĩa phương thức sum gồm 2 biến là x và y
# khai báo và đặt biến sum = x + y
# nếu giá trị của sum trong khoảng từ 15 đến 20 thì giá trị trả lại của phương thức là 20
# nếu không thì trả lại giá trị của biến sum (sum = x + y)

# print(sum(10,6) -> sum = 15 nằm trong khoảng từ 15 đến 20
# -> giá trị trả lại của phương thức là 20
# -> in ra màn hình giá tri 20

# print(sum(10,2))
# -> sum = 12 không nằm trong khoảng từ 15 đến 20
# -> giá trị trả lại của phương thức là 12
# -> in ra màn hình giá trị 12

# print(sum(10, 12))
# -> sum = 22 không nằm trong khoảng từ 15 đến 20
# -> giá trị trả lại của phương thức là sum = 22
# -> in ra màn hình giá tri 22