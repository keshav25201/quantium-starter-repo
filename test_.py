from task3 import app

def test_header001(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region", timeout=10)
