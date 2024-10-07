# 인구수 출력

import csv
import matplotlib.pyplot as plt
import re # 정규식 복잡한 문자열 처리
import koreanize_matplotlib

f = open('age.csv', encoding='euc_kr')
data = csv.reader(f)
result=[]
city= ''
# row[0] : 행정구역
for row in data:
    if '산격3' in row[0]: # 산격 3동이 포함된 자료출력
        str_list = re.split('[()]', row[0]) #row[0]:'대구광역시 북구 산격3동(2723063000)'
                # ()를 없애고 [대구광역시 북구 산격3동, '2723063000', ''] 으로 만들어줌.
        city= str_list[0]
        for data in row[3:]: # 0세 부터 100세 이상까지 데이터
            data = data.replace(',', '')
            result.append(int(data))
f.close()
print(result)

plt.title(f'{city} 인구현황')
plt.xlabel('나이')
plt.ylabel('인구수')
plt.plot(result)
plt.show()


