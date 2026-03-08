from pyscript import window
from dispatch_event import register_handler
from call_rest_api import call_rest_api

async def test_button1(param1):
    print("test_button is called")
    print(param1)
    data = await call_rest_api({
        "action": "test_button1",
        "param1": param1,
    })
    print("test/api response:", data)

async def test_button2(param1, param2):
    print("test_button is called")
    print(param1, param2)
    data = await call_rest_api({
        "action": "test_button2",
        "param1": param1,
        "param2": param2,
    })
    print("test/api response:", data)

def test_button3():
    window.test3_callback()
    pass

async def test_command():
    data = await call_rest_api(
        {"action": "test_command"},
        url="/test/api_command",
    )
    print("test/api_command response:", data)
    return data


register_handler("test_button1", test_button1)
register_handler("test_button2", test_button2)
register_handler("test_button3", test_button3)
register_handler("test_command", test_command)