from webob import Request, Response
from jinja2 import Environment, FileSystemLoader

assets = [
  'app.js',
  'react.js',
  'leaflet.js',
  'D3.js',
  'moment.js',
  'math.js',
  'main.css',
  'bootstrap.css',
  'normalize.css',
  ]

links = []
scripts = []

for item in assets:
  str = item.split('.')
  //Отбираем файлы с расширением .css
  if str[1] == 'css':
    links.append(item)
  //Отбираем файлы с расширением .js
  elif str[1] == 'js':
    scripts.append(item)
class WsgiTopBottomMiddleware(object):
  //Заполняем список файлов
  def __init__(self, app):
    self.app = app

  def __call__(self, environ, start_response):
    response = self.app(environ, start_response).decode()
    if response.find('<head>'and'<body>') > -1:
      head1, head = response.split('<head>')
      datahead, endhead = head.split('</head>')
      head2, body = endhead.split('<body>')
      databody, endbody = body.split('</body>')
   
      yield (head1 + data + endbody).encode() 
    else:
      yield (response).encode()

def app(environ, start_response):
  response_code = '200 OK'
  response_type = ('Content-Type', 'text/HTML')
  start_response(response_code, [response_type])
  return ''''''

app = WsgiTopBottomMiddleware(app)

//вместо "index.html" можно подставить "about/aboutme.html"
request = Request.blank('/index.html')

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('index.html')
print(template.render(script=scripts, style=links))

print(request.get_response(app))
