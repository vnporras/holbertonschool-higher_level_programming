from http.server import HTTPServer, BaseHTTPRequestHandler

class VnHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')

        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"name": "John", "age": 30, "city": "New York"}')

        elif self.path == '/status':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'OK')

        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"version": "1.0", "description": "A simple API built with http.server"}')

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Endpoint not found')

httpd = HTTPServer(('', 8000), VnHandler)
httpd.serve_forever()