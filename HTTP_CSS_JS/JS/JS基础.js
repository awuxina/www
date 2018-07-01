//单行注释
/*多行注释*/
//获取今天星期几
var x = (new Date()).getDay();
// console.log(x)
if (x ==6 || x==0 ) {
    // alert('今天周末');
    $('#day').text='今天周末'
} else {
    // alert('工作日');
    $('#day').text='工作日'
}
