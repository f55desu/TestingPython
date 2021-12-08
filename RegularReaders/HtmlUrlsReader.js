// var text = document.getElementById('steam').innerHTML;
// var linkRegbyTag = /<a\s.+?>.*?<\/a>/gmi;
// var linkReg = /href=[\'"]?([^\'" >]+)/gmi;
// var urls = Array.from(text.matchAll(linkRegbyTag));
// console.log(urls);

(async function() {
    const {data} = await fetch("https://ru.wikipedia.org/wiki/Valve")
    const regexp = /<a(.+)?href=[\"\'](?<href>.+)[\"\'](.+)?>(?<text>.+)<\/a>/gmi
    const urls = Array.from(regexp.matchAll(data)).map(item => [item.groups.href, item.groups.text]);
    console.log(urls)
    }()) 