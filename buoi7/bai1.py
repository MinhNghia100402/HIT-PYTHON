import numpy as  np
import pandas as pd
import  matplotlib.pyplot as plt
df = pd.read_csv('Mall_Customers_2.csv')
"""dùng pandas để đọc CV"""
age,score,gender=df['Age'],df['Spending Score (1-100)'],df['Genre']
"""gán các cột thành các seri có tên tương ứng"""
def color(gender):  #sử dụng hàm color để trả về một mảng có các tên màu cần tô
    cols = []    # tạo mảng rỗng
    for i in gender:
        if i=='Male': #kiểm tra nếu là nam thì thêm màu xanh và kiểm tra tương tự với nữ thì thêm màu hồng
            cols.append('blue')
        if i=='Female': cols.append('pink')
    return cols
plt.subplot(2,1,1)
plt.scatter(score,age,c=color(gender))
"""dùng matplotlib để vẽ biểu đồ scatter"""
plt.ylabel('TUỔI')
plt.xlabel("ĐIỂM CHỈ TIÊU")
plt.title("Bài 1")
plt.legend(['Nam'])
'''ý b'''
plt.subplot(2,1,2)
income = df['Annual Income (k$)']
plt.plot(age,income)
plt.ylabel('THU NHẬP')
plt.xlabel('TUỔI')
y = income.max()
x= age[y]
print(x,y)
plt.annotate('Max',xy=(x,y),xytext=(x+5,y+10),arrowprops=dict(facecolor='red'))
plt.show()
