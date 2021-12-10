import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Social_Network_Ads_2.csv')
df['Purchased'] =df['Purchased'].apply(lambda x:'Đã mua' if x>0 else 'Chưa mua')
df.rename(columns={'Purchased':'Status'},inplace=True)
age,slary,buy=df['Age'],df['EstimatedSalary'],df['Status']
plt.xlim(age.min(),age.max())
plt.ylim(slary.min(),slary.max())
plt.subplot(3,1,1)
plt.bar(age,slary,color=df['Status'].apply(lambda x: 'violet' if x=='Đã mua' else 'red'))
plt.xlabel('SỐ TUỔI')
plt.ylabel('MỨC LƯƠNG')
plt.title('BÀI 2')
plt.legend(['Chưa mua'])
plt.subplot(3,1,3)
plt.scatter(age,slary,color=df['Status'].apply(lambda x: 'violet' if x=='Đã mua' else 'red'))
plt.xlabel('SỐ TUỔI')
plt.ylabel('MỨC LƯƠNG')
plt.title('BÀI 2')
plt.legend(['Chưa mua','Đã mua'])
plt.show()