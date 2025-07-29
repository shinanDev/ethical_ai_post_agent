# callback_server.py
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class CallbackHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed_path.query)
        auth_code = params.get('code', [None])[0]

        if auth_code:
            print(f"\n🔐 Authorization Code erhalten:\n{auth_code}\n")
            message = "Authorization successful. You can close this window."
        else:
            message = "No code received."

        self.send_response(200)
        self.end_headers()
        self.wfile.write(message.encode())

def run(server_class=HTTPServer, handler_class=CallbackHandler):
    server_address = ('', 3000)
    httpd = server_class(server_address, handler_class)
    print("🚀 Callback-Server läuft unter http://localhost:3000 ...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()