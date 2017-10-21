""" Basic cross-platform utility that launches HTTP server from the current directory.
    Useful when sending static web apps/prototypes to non-technical people. 
    v1 """

import webbrowser, random, sys, os, re
from http.server import SimpleHTTPRequestHandler, HTTPServer
PORT = URL = httpd = None

# Get the path to the executable's directory that will be served -----------------------
path_to_executable = sys.executable if getattr(sys, 'frozen', False) else \
                     os.path.abspath(__file__)

CWD = re.sub(r'\/.[^\/]*$', '', path_to_executable)

# Set current working directory to the exec's one --------------------------------------
os.chdir(CWD)

# Create a server instance on an available port ----------------------------------------
while httpd is None:
    try_new_port = random.randint(6000, 9999)
    try:
        PORT = try_new_port
        httpd = HTTPServer(('', PORT), SimpleHTTPRequestHandler)
        URL = 'http://localhost:{}'.format(PORT)
    except:
        print('Port {} is already occupied, trying another one...'.format(try_new_port))

# Print out out some information and start the simple server ---------------------------
print('\n\n=====================================')
print('Running app from:\n{}\n'.format(CWD))
print('The app is available at:\n{}'.format(URL))
print('=====================================\n\n')

webbrowser.open(URL)
httpd.serve_forever()