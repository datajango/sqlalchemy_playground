import pytest

@pytest.fixture
def some_db(request):
    #app.config['TESTING'] = True
    #app.config['CSRF_ENABLED'] = False
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
    #db.create_all()
    #def end():
    #    db.session.remove()
    #    db.drop_all()
    #request.addfinalizer(fin)
    pass

def test_foo(some_db):
    pass