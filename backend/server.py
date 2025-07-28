import http.server
import socketserver
import os
from pathlib import Path
from constants import APP_PATH, HOST, PORT

socketserver.TCPServer.allow_reuse_address = True

project_root = Path(__file__).resolve().parent
print("Project Root:", project_root)
full_path = os.path.join(project_root, "/site/app.html")
print("Full Path:", full_path)

class HttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        #self.path = "app.html"
        self.path = "/home/omegazerg/github.com/OmegaZerg/MealPrep/site/app.html"
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

handler = HttpRequestHandler

with socketserver.TCPServer((HOST, PORT), handler) as httpd:
    print(f"Http server serving at port: {PORT}")
    httpd.serve_forever()
