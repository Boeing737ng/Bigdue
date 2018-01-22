#!/usr/bin/env python3

import http.server
import socketserver

server_address = ('', 8000)
httpd = http.server.HTTPServer(server_address, 
                               http.server.CGIHTTPRequestHandler)
httpd.serve_forever()
