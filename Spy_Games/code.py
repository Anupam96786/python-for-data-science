# --------------
def read_file(path):
    file = open(path, 'r')
    sentence = file.readline()
    file.close()
    return sentence


sample_message = 'This is a sample message.'

message_1 = '2222'
message_2 = '2477'
def fuse_msg(message_a,message_b):
    quotient = str(int(message_b) // int(message_a))
    return quotient


secret_msg_1 = fuse_msg(message_1, message_2)
message_3 = 'Green'


def substitute_msg(message_c):
    if message_c == 'Red':
        sub = 'Army General'
    if message_c == 'Green':
        sub = 'Data Scientist'
    if message_c == 'Blue':
        sub = 'Marine Biologist'
    return sub


secret_msg_2 = substitute_msg(message_3)
message_4 = 'I hope you are good now'
message_5 = 'I hope good things happen in your life.'


def compare_msg(message_d,message_e):
    a_list = message_d.split()
    b_list = message_e.split()
    c_list = [i for i in a_list if i not in b_list]
    final_msg = ' '.join(c_list)
    return final_msg


secret_msg_3 = compare_msg(message_4, message_5)
message_6 = 'The man was one step closer towards his quest to become a spy'


def extract_msg(message_f):
    a_list = message_f.split()
    even_word = lambda x : (len(x)%2 == 0)
    b_list = list(filter(even_word, a_list))
    final_msg = ' '.join(b_list)
    return final_msg


secret_msg_4 = extract_msg(message_6)


message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]
secret_msg = ' '.join(message_parts)


final_path= user_data_dir + '/secret_message.txt'


def write_file(secret_msg,path):
     file1 = open(path, 'a+')
     file1.write(secret_msg)
     file1.close()


write_file(secret_msg, final_path)
print(secret_msg)


