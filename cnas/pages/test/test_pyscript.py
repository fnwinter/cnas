import json

from pyscript import fetch
from dispatch_event import register_handler


async def call_test_api(body=None):
    """POST /test/api 를 호출하고 JSON 응답을 반환합니다."""
    payload = json.dumps(body or {})
    response = await fetch(
        "/test/api",
        method="POST",
        body=payload,
        headers={"Content-Type": "application/json"},
    )
    return await response.json()


async def test_button(param1, param2, param3):
    print("test_button is called")
    print(param1, param2, param3)
    data = await call_test_api({
        "action": "test_button",
        "param1": param1,
        "param2": param2,
        "param3": param3,
    })
    print("test/api response:", data)


register_handler("test_button", test_button)
