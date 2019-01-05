from web.controller.admin import route_adminfrom common.libs.WebHelper import ops_renderfrom common.model.baoming import BaoMingfrom common.model.department import Departmentfrom application import db, appfrom flask import requestfrom sqlalchemy import or_import pandas, numpy@route_admin.route('/index', methods=['GET', 'POST'])def admin_index():    resp = {'code': 200, 'totalCount': 0, 'pageTotal': 0, 'list': {}, 'curPage': 1}    req = request.values    page = req['page'] if 'page' in req else 1    f0 = req['f0'] if 'f0' in req else -1    f1 = req['f1'] if 'f1' in req else -1    f2 = req['f2'] if 'f2' in req else -1    f3 = req['f3'] if 'f3' in req else -1    f4 = req['f4'] if 'f4' in req else -1    query = BaoMing.query    offset = int(page - 1) * 100    if f0 != -1:        query = query.filter_by(f0=f0)    if f1 != 'null' and f1 != '-1':        query = query.filter_by(f1=f1)    if f2 != 'null' and f2 != '-1':        query = query.filter_by(f2=f2)    if f3 != 'null' and f3 != '-1':        query = query.filter_by(f3=f3)    if f4 != 'null' and f4 != '-1':        query = query.filter_by(f4=f4)    totalCount = query.count()    list = query.offset(offset).limit(100).all()    resp['totalCount'] = totalCount    resp['list'] = list    resp['pageTotal'] = (totalCount // 100)    resp['curPage'] = page    resp['f0'] = f0    resp['f1'] = f1    resp['f2'] = f2    resp['f3'] = f3    resp['f4'] = f4    return ops_render('/admin/apply.html', resp)@route_admin.route('/count', methods=['GET', 'POST'])def admin_count():    resp = {'code': 200, 'list': {}}    req = request.values    page = int(req['page']) if 'page' in req else 1    f0 = req['f0'] if 'f0' in req else -1    f1 = req['f1'] if 'f1' in req else -1    f2 = req['f2'] if 'f2' in req else -1    f3 = req['f3'] if 'f3' in req else -1    f4 = req['f4'] if 'f4' in req else -1    query = Department.query    if f4 != 'null' and f4 != '-1' and f4 != -1:        rule = or_(Department.did == f4, Department.fid == f4)        query = query.filter(rule)    elif (f3 != 'null' and f3 != '-1' and f3 != -1) and (f4 == 'null' or f4 == '-1' or f4 == -1):        rule = or_(Department.did == f3, Department.fid == f3)        query = query.filter(rule)    elif (f2 != 'null' and f2 != '-1' and f2 != -1) and (f3 == 'null' or f3 == '-1' or f3 == -1):        rule = or_(Department.did == f2, Department.fid == f2)        query = query.filter(rule)    elif (f1 != 'null' and f1 != '-1' and f1 != -1) and (f2 == 'null' or f2 == '-1' or f2 == -1):        rule = or_(Department.did == f1, Department.fid == f1)        query = query.filter(rule)    elif (f0 != 'null' and f0 != '-1' and f0 != -1) and (f1 == 'null' or f1 == '-1' or f1 == -1):        rule = or_(Department.did == f0, Department.fid == f0)        query = query.filter(rule)    totalCount = query.count()    list = query.order_by(Department.joinpercent.desc()).offset((page - 1) * 100).limit(100).all()    tmp_data = []    totalNum = 0    father = False    for item in list:        fname = ''        info = {            'did': item.did,            'd_name': item.d_name,            'f_name': fname,            'num': item.num,            'joinpercent': str(item.joinpercent) + '%' if item.joinpercent else '0%',            'joinnum': item.joinnum        }        totalNum += item.num        while item.fid != 0:            s = Department.query.filter_by(did=item.fid).first()            fname = s.d_name + ' - ' + fname            item = s            father = True        info['f_name'] = fname        tmp_data.append(info)    if father:        del tmp_data[0]    resp['list'] = tmp_data    resp['totalCount'] = totalCount    resp['pageTotal'] = (totalCount // 100) if (totalCount // 100 > 0) else 1    resp['curPage'] = page    resp['totalNum'] = totalNum    return ops_render('/admin/count.html', resp)@route_admin.route('/counts', methods=['GET', 'POST'])def admin_counts():    totalCount = BaoMing().query.count()    index = 0    delist = Department.query.all()    for deitem in delist:        count = BaoMing.query.filter_by(f0=deitem.did).count()        if count == 0:            count = BaoMing.query.filter_by(f1=deitem.did).count()        if count == 0:            count = BaoMing.query.filter_by(f2=deitem.did).count()        if count == 0:            count = BaoMing.query.filter_by(f3=deitem.did).count()        if count == 0:            count = BaoMing.query.filter_by(f4=deitem.did).count()        deitem.num += count        db.session.add(deitem)        db.session.commit()        index += 1        print(index)    return 'Success'@route_admin.route('/updateCount', methods=['POST'])def admin_update():    req = request.values    id = req['id'] if 'id' in req else 0    num = req['num'] if 'num' in req else 0    percent = req['percent'] if 'percent' in req else ''    dep = Department.query.filter_by(did=id).first()    dep.joinnum = num    dep.joinpercent = percent    db.session.add(dep)    db.session.commit()    return 'Success'