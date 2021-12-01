import  pandas as  pd
import  numpy as np
from sklearn.impute import SimpleImputer
df= pd.read_csv('categorical_data.csv')
imputer = SimpleImputer(missing_values=np.NaN, strategy='mean')
"""SimpleImputer nhận hai đối số như giá trị thiếu và chiến lược.
Phương thức fit_transform được gọi trên phiên bản của SimpleImputer để xác định các giá trị còn thiếu."""
df.age = imputer.fit_transform(df['age'].values.reshape(-1,1))[:,0]
"""tìm kiếm và thay thế các giá trị còn thiếu bằng giá trị trung bình của cột age"""
df.salary = imputer.fit_transform(df['salary'].values.reshape(-1,1))[:,0]
"""tương tự với cột age"""
print(df)
print(df)
print(df.mean())
"""hiển thị ra giá trị trung bình của các cột"""
print(df.fillna(df.mean()))
"""thay thế giá trị NaN bằng giá trị trung bình của cột """
b = df['age'].mean()
print(b)
"""em thử nhưng không làm ra được ý tính gtri TB bằng cộng tay ạ """