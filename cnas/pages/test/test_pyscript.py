from dispatch_event import register_handler

def test_button(param1, param2, param3):
    print("test_button is called")
    print(param1, param2, param3)

register_handler("test_button", test_button)
