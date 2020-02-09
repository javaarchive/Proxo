# Tools for urls
def stripProto(url):
  if url.startswith("https://"):
    return url[len("https://"):]
  if url.startswith("http://"):
    return url[len("http://"):]
  if url.startswith("ws://"):
    return url[len("ws://"):]
  return url