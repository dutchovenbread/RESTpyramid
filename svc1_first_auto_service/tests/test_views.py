from svc1_first_auto_service.views.default import home
from svc1_first_auto_service.views.notfound import notfound_view


def test_default(app_request):
    info = home(app_request)
    assert app_request.response.status_int == 200
    assert info['project'] == 'First Auto Service'

def test_notfound_view(app_request):
    info = notfound_view(app_request)
    assert app_request.response.status_int == 404
    assert info == {}
