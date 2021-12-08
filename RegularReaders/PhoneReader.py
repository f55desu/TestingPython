import re

phoneReg = r'(\+?(?:[ .-]?[(]?\d+[)]?)+)'
text = "Мой номер телефона (нет) +79204441112 ну или 89204441112 или +7-920-444-11-12 или +7(920)-444-11-12 или +7 920 444 11 12, американский номер +12308002211, японский номер +812308002211"
phones = re.findall(phoneReg, text, re.M|re.I)
print(phones)
# for phone in phones:
#     print (phone[0])