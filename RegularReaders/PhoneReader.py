import re

phoneReg = r'(\+7|8).*?(\d{3}).*?(\d{3}).*?(\d{2}).*?(\d{2})'
text = "Мой номер телефона (нет) +79204441112 ну или 89204441112 или 8-920-444-11-12"
phones = [
    m.group()
    for m in re.finditer(phoneReg, text)
]
print(phones)