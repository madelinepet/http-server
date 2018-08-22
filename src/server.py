
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import os
from textwrap import dedent
from cowpy import cow
import json


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """ sets a status code, sets headers, sets body, and ends headers
        """
        raw_html = dedent('''
        <html>
        <head>
            <title> cowsay </title>
        </head>
        <body>
            <header>
                <nav>
                <ul>
                    <li><a href="/cow">cowsay</a></li>
                </ul>
                </nav>
            <header>
            <main>
                <!-- project description defining how users can further interact with the application -->
            </main>
        </body>
        </html>''')
        parsed_path = urlparse(self.path)
        parsed_qs = parse_qs(parsed_path.query)

        # set a status code
        # set any headers
        # set any body data on the response
        # end headers

        if parsed_path.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(raw_html.encode())
            return

        elif parsed_path.path == '/cow':
            print(parsed_qs)
            # {'msg': ['gohard2018']}
            parsed_message = parsed_qs['msg'][0]
            bunny = cow.Bunny()
            msg = bunny.milk(parsed_message)
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(msg.encode())
            return

        self.send_response(404)
        self.end_headers()

    def do_POST(self):
        """ Posts to the server
        """
        parsed_path = urlparse(self.path)
        parsed_qs = parse_qs(parsed_path.query)

        if parsed_path.path == '/cow':
            try:
                parsed_message = parsed_qs['msg'][0]
                bunny = cow.Bunny()
                msg = bunny.milk(parsed_message)
                json_message = json.dumps({'content': msg})
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json_message.encode())
                return

            except KeyError:
                self.send_response(400)
                self.end_headers()
                dragon = cow.DragonAndCow()
                msg = dragon.milk('400 Bad Request')
                self.wfile.write(msg.encode())
        else:
            self.send_response(404)
            self.end_headers()
            dragon = cow.DragonAndCow()
            msg = dragon.milk('404 Not Found')
            self.wfile.write(msg.encode())


def create_server():
    return HTTPServer(
        ('127.0.0.1', int(os.environ['PORT'])),
        SimpleHTTPRequestHandler
    )


def run_forever():
    server = create_server()

    try:
        print(f'Server running on {os.environ["PORT"]}')
        server.serve_forever()

    except KeyboardInterrupt:
        server.shutdown()
        server.server_close()


if __name__ == '__main__':
    run_forever()
