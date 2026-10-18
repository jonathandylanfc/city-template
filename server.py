"""A tiny server for the city template: serves the page, config.json and data.json, and /api/data.
Put your own data logic in get_data() (read a database, call an API, ...) or just edit data.json.
  python3 server.py            (then open http://localhost:8095)
  PORT=8080 python3 server.py  (any port; hosts like Railway set PORT for you)"""
import json, os
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

HERE = os.path.dirname(os.path.abspath(__file__))
PORT = int(os.environ.get("PORT", "8095"))


def get_data():
    """Return the city's data as a dict (see data.json for the shape). Replace this with your own source."""
    with open(os.path.join(HERE, "data.json")) as f:
        return json.load(f)


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=HERE, **k)

    def do_GET(self):
        if self.path.split("?")[0] == "/api/data":
            body = json.dumps(get_data()).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Cache-Control", "no-store")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        if self.path.split("?")[0].endswith((".py", ".md")):     # never serve the server's own files
            self.send_error(404)
            return
        super().do_GET()


if __name__ == "__main__":
    host = "0.0.0.0" if os.environ.get("PORT") else "127.0.0.1"   # local only unless a host gives you a PORT
    print(f"City on http://{'localhost' if host == '127.0.0.1' else host}:{PORT}")
    ThreadingHTTPServer((host, PORT), Handler).serve_forever()
