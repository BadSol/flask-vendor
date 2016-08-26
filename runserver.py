from vendor import create_app
# from vendor.models import db


app = create_app()
app.run('192.168.33.33', 8000, debug=True)


# print 'create_all start'
# app = create_app()
# db.create_all(app=app)
# print 'create_all done'
