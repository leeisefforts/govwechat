from application import db, app
from flask import Blueprint, request, g, jsonify , redirect
from common.libs.WebHelper import ops_render
from common.model.department import Department
from common.model.profession import Profession
from common.model.baoming import BaoMing
import time, asyncio

route_index = Blueprint('index_page', __name__)
loop = asyncio.get_event_loop()


@route_index.route('/')
@route_index.route('/index')
def index():
    resp = {}
    resp['info'] = Profession.query.order_by(Profession.pid.desc()).first()
    return ops_render('index.html', resp)


@route_index.route('/next')
def index_next():
    resp = {}
    req = request.values
    id = req['id'] if 'id' in req else 0

    resp['profession'] = Profession.query.order_by(Profession.pid.desc()).first()
    info = Department.query.filter_by(did=id).first()
    list = Department.query.filter_by(fid=id).all()

    resp['list'] = list
    resp['info'] = info
    return ops_render('index_next.html', resp)


@route_index.route('/form_name', methods=['GET', 'POST'])
def form_name():
    resp = {}
    req = request.values
    id = req['id'] if 'id' in req else -1
    pro = Profession.query.order_by(Profession.pid.desc()).first()
    if request.method == 'GET':
        info = Department.query.filter_by(did=id).first()
        resp['profession'] = pro
        resp['info'] = info
        resp['data'] = {
            'id': req['id'] if 'id' in req else -1,
            'f2': req['f2'] if 'f2' in req else -1,
            'f3': req['f3'] if 'f3' in req else -1,
            'f4': req['f4'] if 'f4' in req else -1,
            'f0': req['f0'] if 'f0' in req else -1
        }

        return ops_render('form_name.html', resp)
    f1 = req['f1'] if 'f1' in req else -1
    f2 = req['f2'] if 'f2' in req else -1
    f3 = req['f3'] if 'f3' in req else -1
    f4 = req['f4'] if 'f4' in req else -1
    f0 = req['f0'] if 'f0' in req else -1
    sid = pro.pid
    name = req['x_name'] if 'x_name' in req else -1

    b_info = BaoMing()
    b_info.sid = sid
    b_info.name = name
    b_info.f0 = f0
    b_info.f1 = f1
    b_info.f2 = f2
    b_info.f3 = f3
    b_info.f4 = f4
    db.session.add(b_info)
    db.session.commit()
    return redirect("http://h5.cyol.com/special/daxuexi/daxuexi2o9/m.php")


@route_index.route('/f1')
def f1():
    req = request.values
    id = req['id'] if 'id' in req else -1

    list = Department.query.filter_by(fid=id).all()
    resp = {}
    resp['list'] = list
    tmp_data = []
    for item in list:
        resp = {
            'did': item.did,
            'd_name': item.d_name,
            'fid': item.fid,
            'flg': item.flg,
            'num': item.num
        }
        tmp_data.append(resp)

    return jsonify(tmp_data)


@route_index.route('/test')
def test():
    loop.run_until_complete(SignUp())
    return '报名成功1234'


async def SignUp():
    time.sleep(5)
    print('Hello World:%s' % time.time())
