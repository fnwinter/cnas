import json

from pyscript import document
from dispatch_event import register_handler
from call_rest_api import call_rest_api


def _format_command_response_for_display(data: dict) -> str:
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


async def minecraft_run(action: str):
    out_el = document.querySelector("#minecraft_command_result")
    if out_el is not None:
        out_el.textContent = "요청 중…"

    data = await call_rest_api(
        {"action": action},
        url="/minecraft/api_run",
    )

    if out_el is not None:
        if data is None:
            out_el.textContent = "응답을 받지 못했습니다."
        else:
            out_el.textContent = _format_command_response_for_display(data)

    return data


register_handler("minecraft_run", minecraft_run)
