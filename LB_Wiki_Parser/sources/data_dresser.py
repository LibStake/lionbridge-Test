import re
pt_num = re.compile('([0-9]{4}|[0-9]{1,2})')
pt_len = re.compile('([0-9][\.]?[0-9]{0,2})')
pt_spec_team = re.compile('(국기그림\|[a-zA-Z가-힣0-9]{1,10})\s([a-zA-Z가-힣0-9]*)\s.*')
def dressBirthDate(string):
    if string == 'None' or None:
        return 'None'

    ptlist = pt_num.findall(string)
    out = ''
    if len(ptlist) >= 1:
        out += ptlist[0] + '년'
    if len(ptlist) >= 2:
        if len(ptlist[1]) == 1:
            ptlist[1] = '0' + ptlist[1]
        out += (ptlist[1] + '월')
    if len(ptlist) >= 3:
        if len(ptlist[2]) == 1:
            ptlist[2] = '0' + ptlist[2]
        out += (ptlist[2] + '일')
    return out

def dressHeight(string):
    if string == 'None' or None:
        return 'None'

    pt = pt_len.findall(string)
    if len(pt) > 0:
        h = float(pt[0])
        if h >= 10:
            return str(int(h))
        else:
            return str(int(h * 100))

    return 'None'

def dressTeam(string):
    if string == 'None' or None:
        return 'None'

    brk = 0
    stk = []

    for ch in string:
        if ch == '[':
            brk += 1
            stk = []
        elif ch == ']':
            brk -= 1
            if brk == 0:
                return ''.join(stk).strip()
        elif ch == '|':
                stk = []
        elif ch == '<':
            return ''.join(stk).strip()
        else:
            stk.append(ch)

    return 'None'

# print(dressBirthDate('1992년 2월 3일'))
# print(dressBirthDate('[[1992년]][[3월]][[5일]]'))
# print(dressBirthDate('1992년'))
# print(dressBirthDate('2008년 2월'))
# print(dressBirthDate('[[1996년]][[3월]]'))
# print(dressHeight('183cm'))
# print(dressHeight('2m'))
# print(dressHeight('2.35m'))
# print(dressHeight('168'))
# print(dressTeam('국기그림|대한민국 [[서울FC|서울FC]]'))
# print(dressTeam('[[서울FC]]'))
# print(dressTeam('국기그림|대한민국 [[서울FC|서울FC]]'))
# print(dressTeam('청룡FC <br>'))
# print(dressTeam('국기그림|대한민국 청룡FC'))
# print(dressTeam('국기그림|독일 바이에른뮌헨FC <br>'))








