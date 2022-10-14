import csv

data_for_record = ''


def init_for_record(data):
    global data_for_record
    data_for_record = data


def record():
    with open('phone_book.csv', 'a', newline='\n', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(data_for_record)


def import_data(source):
    s_ext = source.split('.')[1]
    if s_ext == 'txt':
        with open(f'{source}', encoding='utf-8') as s:
            data_list = s.read().split('\n\n')
            print(data_list)
            for line in data_list:
                with open('phone_book.csv', 'a', newline='\n', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(line.split('\n'))
    elif s_ext == 'csv':
        with open(f'{source}', newline='\n', encoding='utf-8') as s:
            pre_data = csv.reader(s)
            for line in pre_data:
                with open('phone_book.csv', 'a', newline='\n', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(line)


def export_data(destiny):
    d_ext = destiny.split('.')[1]
    if d_ext == 'txt':
        with open('phone_book.csv', newline='\n', encoding='utf-8') as s:
            pre_data = csv.reader(s)
            for line in pre_data:
                line.append('\n')
                data = '\n'.join(line)
                with open(f'{destiny}', 'a', encoding='utf-8') as f:
                    f.write(data)
    elif d_ext == 'csv':
        with open('phone_book.csv', newline='\n', encoding='utf-8') as s:
            pre_data = csv.reader(s)
            for line in pre_data:
                with open(f'{destiny}', 'a', newline='\n', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(line)
