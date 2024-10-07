# age.csv 파일의 index 계산

import csv

def get_index_age_csv():
    f=open('age.csv', encoding='euc_kr')
    data = csv.reader(f)
    header = next(data)

    print('-'*60)
    print(' age.csv.index ')
    print('-'*60)
    for i in range(len(header)):
        print(f'[{i:3}]: {header[i]}')
    f.close()

get_index_age_csv()