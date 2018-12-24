from flask import Blueprint, request
from common.libs.WebHelper import ops_render

route_admin = Blueprint('admin_page', __name__)


@route_admin.route('/', methods=['GET', 'POST'])
def admin():
    if request.method == 'GET':
        return ops_render('/admin/index.html')
