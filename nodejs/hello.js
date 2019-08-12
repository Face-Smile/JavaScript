function hello(){
    console.log("hello world");
}
hello();

// 模块只导入一次，不会重复导入
var count = require("./counter");
var count1 = require("./counter");

// console.log(count());


// console.log(count.count());
console.log(count1.count());


