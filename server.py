#!/usr/bin/env python3
"""本地预览用的静态 HTTP 服务。

serve 整个 tools 目录，浏览器打开 /android/ 即可预览。
"""

import os
import socket
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

ROOT = os.path.dirname(os.path.abspath(__file__))


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)


def lan_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("223.5.5.5", 80))  # 只为取得出网网卡地址，不实际发包
        ip = s.getsockname()[0]
        s.close()
        return ip
    except OSError:
        return "127.0.0.1"


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    srv = ThreadingHTTPServer(("0.0.0.0", port), Handler)
    srv.daemon_threads = True
    ip = lan_ip()
    print("静态服务已启动：", flush=True)
    print("  本机   http://127.0.0.1:%d/android/" % port, flush=True)
    print("  局域网 http://%s:%d/android/" % (ip, port), flush=True)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
