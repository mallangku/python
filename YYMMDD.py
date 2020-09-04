# 접근법 1
# 문자열은 수정이 불가능합니다. 하지만 문자열과 유사한 리스트는 수정이 가능하죠?
# 그러면 문자열 security_number를 리스트로 변환한 후, 마지막 네 원소를 '*'로 바꿔 주면 됩니다.
# 그리고 나서 그 리스트를 다시 하나의 문자열로 합치면 되겠죠?
def mask_security_number(security_number):
    num_list = list(security_number)
    for i in range(len(num_list) - 4, len(num_list)):
        num_list[i] = '*'
    return ''.join(num_list)


# 접근법 2
# 사실 더 쉬운 방법이 있습니다. 문자열 슬라이싱을 이용하는 건데요.
# security_number의 마지막 네 자리만 제외해서 슬라이싱을 하고, 문자열 "****"과 연결하면 끝입니다!
def mask_security_number(security_number):
    return security_number[:-4] + '****'


# 테스트
print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))