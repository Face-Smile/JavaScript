var i = 0;
function count(){
    return ++i;
}

// 模块方法的导出
exports.count = count;


// 模块导出为一个函数
// module.exports = function() {
//     return ++i;
// };