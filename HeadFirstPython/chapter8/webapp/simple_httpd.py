
from http.server import HTTPServer, CGIHTTPRequestHandler
"""导入http 服务器和CGI 模块"""

port = 8080

httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
print("Starting simple_httpd on port: " + str(httpd.server_port))
httpd.serve_forever()

