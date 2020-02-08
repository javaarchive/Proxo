import configuration
from flask import *
import requests,logging # Put after import flask to stop conflicts
# Optional web controller
from controller import controller
# Longing stuff
logger = logging.getLogger('reverse_proxy')
formatter = logging.Formatter('{[%(asctime)s] %(name)s | %(levelname)s} : %(message)s') # My horrible logging format
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('proxy.log')
fh.setFormatter(formatter)
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)

# TEST LINE Uncomment to enable test http server(Highly insecure)
exec(open("test.py").read())

# Main app init
app = Flask(__name__)
curOrigin = "main"
# Custom modules
# Interchangable middleware
def middleware(req,path):
  # Logging add-on
  logger.info("Request made to "+path+" type "+request.method)
  if configuration.enableController and path == "/admin":
    return controller(req,path)
  return False
def obtainResponse(req,path):
  func = None
  args = {}
  if path in configuration.blocked_paths:
    logger.info("Blocked url "+path+" was accessed")
    return b"<h1>Blocked url</h1><p>The url is blocked in the app</p>"
  if req.method == "GET":
    func = requests.get
    args["params"]= dict(request.args)
    
  elif req.method == "POST":
    func = requests.post
    args["data"] = dict(request.form)
  args["headers"] = {}
  for header in req.headers:
    if header in configuration.forward_headers:
      args["headers"][header] = req.headers[header]
  if configuration.hostRouting:
    args["headers"]["host"] = configuration.origins[curOrigin].replace("https://","").replace("http://","") # Dirty way to strip to host only
  try:
    resp = func(configuration.origins[curOrigin]+path, allow_redirects=not configuration.blockRedirects,**args)
  except Exception as e:
    logger.warn("Internal Error: "+e)
    return ("Error: "+str(e)).encode("UTF-8")
  response = make_response(resp.content)
  if not configuration.minimal:
    for x in resp.headers:
      response.headers.set(x,resp.headers[x])
  else:
    response.headers.set('Content-Type', resp.headers['Content-Type'])
  return response
 
# Core Code
@app.route("/",methods = ["PUT","DELETE","POST","GET","HEAD"])
@app.route("/<path:path>",methods = ["PUT","DELETE","POST","GET","HEAD"])
def serve_request(path=""):
  path = "/"+path
  before = middleware(request,path)
  if before != False and before != None:
    return before # Return intercepted response
  return obtainResponse(request,path)

if __name__ == "__main__":
  # Dev mode
  app.run(host = "0.0.0.0",port = configuration.port)
