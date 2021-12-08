var phoneReg = /(\+?([ .-]?[(]?\d+[)]?)+)/gmi
var text = "+79204441112 \n  89204441112 \n  +7-920-444-11-12 \n +7(920)-444-11-12\n +12308002211  +812308002211"
var phones = text.match(phoneReg)
console.log(phones)