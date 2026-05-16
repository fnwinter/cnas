from pyscript import document
from dispatch_event import register_handler
from call_rest_api import call_rest_api


def _value_of(selector: str) -> str:
    el = document.querySelector(selector)
    if el is None:
        return ""
    return (el.value or "").strip()


async def save_folders():
    result_el = document.querySelector("#setting_result")
    if result_el is not None:
        result_el.textContent = "Saving…"

    data = await call_rest_api(
        {
            "gallery_path": _value_of("#gallery_path"),
            "music_path": _value_of("#music_path"),
        },
        url="/setting/api_save_folders",
    )

    if result_el is None:
        return data

    if data is None:
        result_el.textContent = "No response from server."
        return data

    if data.get("status") == "ok":
        result_el.textContent = "Saved."
        gallery_el = document.querySelector("#gallery_path")
        music_el = document.querySelector("#music_path")
        if gallery_el is not None:
            gallery_el.value = data.get("gallery_path") or gallery_el.value
        if music_el is not None:
            music_el.value = data.get("music_path") or music_el.value
    else:
        result_el.textContent = f"Error: {data.get('message', 'unknown')}"

    return data


register_handler("save_folders", save_folders)
