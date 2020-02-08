import configuration
passwordPrompt = """
<form method = POST>
<h1>Login</h1>
<p>Your password may be stolen if you aren't on https</p>
<b>Even if you are on https, schools can obtain information via something called SSL Decryption </b> <br />
<input type = password name = password>
<button type=submit>Login</button>
<span>Version 1.0.0(Super dirty edition)</span>
</form>
"""
def controller(req,path):
  assert path == "/admin"
  return passwordPrompt.encode("UTF-8")
  