import json

from pyscript import fetch
from dispatch_event import register_handler


async def call_test_api(body=None):
    """POST /test/api 를 호출하고 JSON 응답을 반환합니다."""
    payload = json.dumps(body or {})
    try:
        # PyScript: await fetch(...).text() 체이닝으로 응답 본문을 받음 (이중 await 대신)
        text = await fetch(
            "/test/api1",
            method="POST",
            body=payload,
            headers={"Content-Type": "application/json"},
        ).text()
        result = json.loads(text) if text else None
        print("test/api response:", result)
        return result
    except Exception as e:
        print(f"Error calling test/api: {e}")
        return None


async def test_button1(param1, param2, param3):
    print("test_button is called")
    print(param1, param2, param3)
    data = await call_test_api({
        "action": "test_button1",
        "param1": param1,
        "param2": param2,
        "param3": param3,
    })
    print("test/api response:", data)

async def test_button2(param1, param2, param3):
    print("test_button is called")
    print(param1, param2, param3)
    data = await call_test_api({
        "action": "test_button2",
        "param1": param1,
        "param2": param2,
        "param3": param3,
    })
    print("test/api response:", data)

register_handler("test_button1", test_button1)
register_handler("test_button2", test_button2)
