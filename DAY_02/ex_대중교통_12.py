# 지하철 시간대별 이용 현황: 엑셀 파일 및 Pandas 활용
import pandas as pd
from tabulate import tabulate

df = pd.read_excel('subway.xls', sheet_name='지하철 시간대별 이용현황', header=[0,1])
print(df.head())

# 특정 컬럼 데이터 가져오기 : 호선명
# 멀티 인덱스의 경우, 튜플 형식으로 접근
# df[('첫 번째 행', '두번째 행')]
print((df['호선명', 'Unnamed: 1_level_1']))

print(df['지하철역', 'Unnamed: 3_level_1'])

print(df.columns)


# df에서 여러 컬럼 선택
commute_time_df= df.iloc[:,[1,3,10,12,14]]
print(tabulate(commute_time_df.head(), headers='keys', tablefmt='psql'))

# Replace commas in the specified columns using .loc
commute_time_df.loc[:, ('07:00:00~07:59:59', '승차')] = commute_time_df.loc[:, ('07:00:00~07:59:59', '승차')].apply(lambda x: x.replace(',', ''))
commute_time_df.loc[:, ('08:00:00~08:59:59', '승차')] = commute_time_df.loc[:, ('08:00:00~08:59:59', '승차')].apply(lambda x: x.replace(',', ''))
commute_time_df.loc[:, ('09:00:00~09:59:59', '승차')] = commute_time_df.loc[:, ('09:00:00~09:59:59', '승차')].apply(lambda x: x.replace(',', ''))

print(tabulate(commute_time_df.head(),	headers='keys',	tablefmt='psql'))

# 데이터	타입	변경:	object에서	int64로	변경
commute_time_df =commute_time_df.astype({('07:00:00~07:59:59','승차'):'int64'})
commute_time_df =commute_time_df.astype({('08:00:00~08:59:59','승차'):'int64'})
commute_time_df =commute_time_df.astype({('09:00:00~09:59:59','승차'):'int64'})
print(commute_time_df.dtypes)

# 각 행(지하철 역)의 승차 인원 수 합 계산
# 행의 합 : df.sum(axis=1)
# 열의 합 : df.sum(axis=0)

# 각 행의 합계 계산
row_sum_df = commute_time_df.sum(axis=1, numeric_only=True)

# 합계 값을 리스트로 변환
passenger_number_list = row_sum_df.tolist()

# 합계 출력
print(row_sum_df)

# 최대값 및 최대값 인덱스 찾기
# 최대 승차 수를 가지는 지하철 역 찾기
# 최대값 계산 : df.max(axis=0)
# 최대값 인덱스: df.idxmax()
max_number = row_sum_df.max(axis=0)
print(max_number)

max_index =	row_sum_df.idxmax()
max_line, max_station =	df.iloc[max_index, [1, 3]] #최대값의	[1]: 호선,[3]: 지하철역명
print(f'출근 시간대 최대 승차 인원역: {max_line} {max_station} {max_number:,}명')

import matplotlib.pyplot as plt

passenger_number_list.sort(reverse=True)
plt.figure(dpi=100)
plt.bar(range(len(passenger_number_list)), passenger_number_list)
plt.show()