port = 3000 # To be changed to get the env variable
origins = {
  "main":"https://httpbin.org/" # Automatically selected
}
forward_headers = ["User-Agent","Accept","Accept-Language","Accept-Encoding"] # Headers you want to forwards
blocked_paths = ["/sw.js","/___glitch_loading_status___","/favicon.ico"]
# blocked_paths = []
enableController = False # Still WIP
blockRedirects = False
hostRouting = False # Send host header
minimal = True
fixAbsoluteUrls = True
encoding = "UTF-8"
APP_URL = "epic-proxy.glitch.me"