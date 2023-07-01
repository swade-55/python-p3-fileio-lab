
# import ipdb
# ipdb.set_trace()
def write_file(file_name, file_content):
    print(f'--------------------i am here')
    print(f'{file_name} I am here inside of here now')
    with open(f'{file_name}.txt',mode='w',encoding='utf-8') as log_file:
        log_file.write(file_content)

def append_file(file_name, append_content):
    with open(f'{file_name}.txt',mode='a') as log_file:
        log_file.write(append_content)

def read_file(file_name):
    text_file = open(f'{file_name}.txt', encoding='utf-8')
    return text_file.read()