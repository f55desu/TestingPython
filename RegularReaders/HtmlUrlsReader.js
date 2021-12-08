var text = document.getElementById('steam').innerHTML;
var linkRegbyTag = /<a href=("|')(.+)("|')>(.+)<\/a>/gmi;
var linkReg = /href=[\'"]?([^\'" >]+)/gmi;
var urls = Array.from(text.matchAll(linkReg));
console.log(urls);