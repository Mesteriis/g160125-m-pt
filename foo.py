from socketserver import TCPServer, StreamRequestHandler


server_address = ('localhost', 9999)
class MyRequestHandler(StreamRequestHandler):
    def handle(self):
        self.wfile.write(b"Hello, world!\n")

if __name__ == "__main__":
    with TCPServer(server_address, MyRequestHandler) as httpd:
        httpd.serve_forever()