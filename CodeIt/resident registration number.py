def mask_security_number(security_number):
        # 코드를 입력하세요.
        if(len(security_number) == 14):
                number = security_number[0:10] + '****' 
                return number
        elif(len(security_number) == 13):
                number = security_number[0:9] + '****'
                return number
# 테스트
print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))
        
