# -*- coding:utf-8 -*-
'''
    python 版本：2.7.10
    第三方包：web.py==0.39
    简单的HTML服务器:实现对vuejs中html，css，js等文件的访问
'''



import web
import os
urls = (
    "/", "Index",
    "/script", "Script",
    "/lib/([^/]+)", "Vue",
    "/([^/]+)/(.*)", 'CodeHtml',
    "/([^/]+)", "CodeDir"
)

web_path = 'vuejs'
# web.header('Content-Type', 'text/html; charset=utf-8')
# web.header('Access-Control-Allow-Origin', '*')

# 列出所有的文件目录
class Index:
    def GET(self):
        web.header('Content-Type', 'text/html; charset=utf-8')
        web.header('Access-Control-Allow-Origin', '*')
        _,dirnames,_ = os.walk(web_path).next()
        template = []
        dirnames.sort()
        for dirname in dirnames:
            s = u'<a href=/%s>%s</a>' %(dirname, dirname)
            template.append(s)
        return '</br>'.join(template)
    def POST(self):
        web.header('Access-Control-Allow-Methods', '*')
        web.header('Access-Control-Allow-Origin', '*')
        return self.GET()

# class Spec:
#     def GET(self, file_name):
#         web.header('Content-Type', 'text/html; charset=utf-8')
#         web.header('Access-Control-Allow-Origin', '*')
#         # if  file_name is None:
#         #     file_name = '02.v-cloak的学习.html'
#         print "file_name", file_name
#         try:
#             with open('vuejs/' + code + '/' + file_name) as f:
#                 return f.read()
#         except Exception as e:
#             print e
#             return web.NotFound()

# 列出指定文件夹的html文件
class CodeDir:
    def GET(self, dirpath):
        web.header('Content-Type', 'text/html; charset=utf-8')
        web.header('Access-Control-Allow-Origin', '*')
        realdirpath = web_path + '/' + dirpath
        if os.path.isdir(realdirpath):
            _,_,filenames = os.walk(realdirpath).next()
            template = []
            filenames.sort()
            for filename in filenames:
                if filename.endswith('.html') or dirpath == u'lib':
                    s = u'<a href=/{0}/{1}>{1}</a>'.format(dirpath, filename)
                    template.append(s)
            return '</br>'.join(template)
        else:
            return web.NotFound()


# 获取指定的html 文件
class CodeHtml:
    def GET(self, dirpath, filename):
        file_path = web_path + '/' + dirpath + '/' + filename
        web.header('Content-Type', 'text/html; charset=utf-8')
        web.header('Access-Control-Allow-Origin', '*')
        web.header('Access-Control-Allow-Methods', '*')
        if os.path.isfile(file_path):
            try:
                with open(file_path) as f:
                    return f.read()
            except Exception as e:
                print e
                return web.InternalError()
        else:
            print 'the file not exist:', file_path
            return web.NotFound()


# 获取js，css等
class Vue:
    def GET(self, name):
        print name
        if name.endswith('js'):
            contentType = 'text/javascript; charset=utf-8'
        elif name.endswith('css') or name.endswith('css.map'):
            contentType = 'text/css; charset=utf-8'
            # print('contentType:' + contentType)
        else:
            contentType = 'text/html; charset=utf-8'
        web.header('Content-Type', contentType)
        try:
            with open(web_path + '/lib/' + name) as f:
                return f.read()
        except Exception:
            return web.NotFound()

# javascript回调函数接口，比如jsonp跨域加载
class Script:
    def GET(self):
        web.header('Content-Type', 'text/javascript; charset=utf-8')
        function = web.input(script = "console.log('no script to execute')")
        return function.script


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()