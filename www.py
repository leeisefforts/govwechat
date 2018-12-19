from application import app

from web.controller.index import route_index
from web.controller.static import route_static

app.register_blueprint(route_index, url_prefix='/')
app.register_blueprint(route_static, url_prefix='/static')
