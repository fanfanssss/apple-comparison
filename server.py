from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
import urllib.parse as urlparse
from pathlib import Path

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # 处理根路径重定向
        if self.path == '/':
            self.path = '/src/index.html'
        # 处理无扩展名的路由
        elif self.path in ['/iphone-compare', '/ipad-compare', '/watch-compare', '/privacy', '/terms']:
            if self.path == '/privacy':
                self.path = '/public/privacy.html'
            elif self.path == '/terms':
                self.path = '/public/terms.html'
            else:
                self.path = f'/src{self.path}.html'
        # 处理 sitemap 和 robots.txt
        elif self.path in ['/sitemap.xml', '/robots.txt']:
            self.path = f'/public{self.path}'
        
        # 检查文件是否存在
        full_path = os.getcwd() + self.path
        if not os.path.exists(full_path):
            self.send_error(404, f"File not found: {self.path}")
            return
            
        return SimpleHTTPRequestHandler.do_GET(self)

def run(server_class=HTTPServer, handler_class=MyHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}...')
    print('\n您可以访问以下链接预览网站：')
    print('1. 主页面: http://localhost:8000/')
    print('2. iPhone 对比: http://localhost:8000/iphone-compare')
    print('3. iPad 对比: http://localhost:8000/ipad-compare')
    print('4. Apple Watch 对比: http://localhost:8000/watch-compare')
    print('5. 隐私政策: http://localhost:8000/privacy')
    print('6. 使用条款: http://localhost:8000/terms')
    print('7. 网站地图: http://localhost:8000/sitemap.xml')
    print('8. 爬虫协议: http://localhost:8000/robots.txt')
    print('\n按 Ctrl+C 停止服务器')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
