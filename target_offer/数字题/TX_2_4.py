import sys
ans = 0
length_limit = int(sys.stdin.readline().strip())
send_message = sys.stdin.readline().strip()
message_length = len(send_message)
sub_number = int(sys.stdin.readline().strip())
for i in range(sub_number):
    sub = sys.stdin.readline().strip()
    sub_length = len(sub)
    m = message_length % sub_length
    # print('sub:',sub[:m])
    # print('sed:',send_message[-m:])
    flag = False
    if sub[:m] == send_message[-m:] or m==0:
        flag = True
        for i in range(0, message_length-m, sub_length):
            if sub!=send_message[i:i+sub_length]:
                flag = False
                break
    if flag:
        ans += 1
print(ans)
        