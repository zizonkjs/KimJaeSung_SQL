import pandas as pd

# CSV 파일 경로 설정 (실제 파일 경로로 변경)
file_path = '/mnt/data/your_file.csv'

# CSV 파일 읽기
df = pd.read_csv(file_path, encoding='utf-8')

# 2014년부터 2023년까지의 연도와 월을 조합하여 리스트 생성
years = [f'{year}년{month}월' for year in range(2014, 2024) for month in range(1, 13)]

# 데이터프레임에서 필요한 열만 선택하여 새로운 데이터프레임 생성
selected_columns = [col for col in years if col in df.columns]

# 필요한 열로 데이터프레임 재구성
df_restructured = df[selected_columns]

# 결과 확인
print(df_restructured.head())

# 재구성된 데이터프레임을 CSV 파일로 저장
df_restructured.to_csv('/mnt/data/restructured_file.csv', encoding='utf-8', index=False)
