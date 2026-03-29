import json

from pyscript import document
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


def _format_command_response_for_display(data: dict) -> str:
    """Single-line JSON for metadata; only nested command stdout (`result.result`) stays multiline."""
    inner = data.get("result")
    if isinstance(inner, dict) and "result" in inner:
        stdout = inner.get("result")
        inner_meta = {k: v for k, v in inner.items() if k != "result"}
        envelope = {
            "status": data.get("status"),
            "message": data.get("message"),
            "result": inner_meta,
        }
        meta_line = json.dumps(envelope, ensure_ascii=False)
        if isinstance(stdout, str) and stdout != "":
            return f"{meta_line}\n\n{stdout}"
        return meta_line

    return json.dumps(data, ensure_ascii=False)


async def test_command():
    out_el = document.querySelector("#ls_command_result")
    if out_el is not None:
        out_el.textContent = "요청 중…"

    data = await call_rest_api(
        {"action": "test_command"},
        url="/test/api_command",
    )
    print("test/api_command response:", data)

    if out_el is not None:
        if data is None:
            out_el.textContent = "응답을 받지 못했습니다."
        else:
            out_el.textContent = _format_command_response_for_display(data)

    return data


register_handler("test_button1", test_button1)
register_handler("test_button2", test_button2)
register_handler("test_button3", test_button3)
register_handler("test_command", test_command)