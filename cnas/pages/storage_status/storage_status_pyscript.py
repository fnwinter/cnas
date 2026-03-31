import json

from pyscript import document
from dispatch_event import register_handler
from call_rest_api import call_rest_api


def _format_command_response_for_display(data: dict) -> str:
    """Single-line JSON for metadata; only nested stdout (`result.result`) stays multiline."""
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


async def storage_check_status():
    out_el = document.querySelector("#storage_df_result")
    if out_el is not None:
        out_el.textContent = "Loading…"

    data = await call_rest_api(
        {"action": "df_h"},
        url="/storage_status/api_df_h",
    )

    if out_el is not None:
        if data is None:
            out_el.textContent = "No response from server."
        else:
            out_el.textContent = _format_command_response_for_display(data)

    return data


register_handler("storage_check_status", storage_check_status)
