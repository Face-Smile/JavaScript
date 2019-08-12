// 导入http模块
const http = require('http');

// 导入URL解析模块, 从而拿到 pathname 和 query
const urlModule = require('url');

// 创建一个http服务器
const server = http.createServer();

// 监听http服务器的request请求
server.on('request', function (req, res){
    // 下面的pathname: url 含义： 给返回的参数pathname 起一个别名 url 
    const { pathname: url, query } = urlModule.parse(req.url, true);
    if(url === '/getScript') {
        // 拼接一个合法的JS脚本，这里拼接的是一个方法的调用
        // var scriptStr = 'show()';

        let data = {
            name: 'Ting Ting',
            age: 21,
            gender: '女孩子' 
        };
        let scriptStr = `${query.callback}(${JSON.stringify(data)})`;
        
        // res.end 发送给客户端， 客户端去把 这个字符串，当成JS代码去解析执行
        res.end(scriptStr);

    }else{
        res.end('404');
    }
});

// 指定端口号并启动服务器进行监听
server.listen(3000, function() {
    console.log('server listen at http://127.0.0.1:3000')
});