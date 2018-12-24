from flask import Blueprint

route_admin = Blueprint('admin_page', __name__)


@route_admin.route('/admin')
def admin():
    pass
