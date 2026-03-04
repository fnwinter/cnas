import json

from pyscript import fetch
from pyscript import window

from dispatch_event import register_handler


async def login_handler(login_id: str, password: str) -> None:
    """Send id/password to server. Server compares with config admin id/password via hash_string; on match, login success."""
    payload = json.dumps({"id": login_id, "password": password})
    try:
        resp = await fetch(
            "/login/login",
            method="POST",
            body=payload,
            headers={"Content-Type": "application/json"},
        )
        text = await resp.text()
        result = json.loads(text) if text else {}
        if result.get("success"):
            window.location.href = "/"
        else:
            window.alert(result.get("message", "Login failed."))
    except Exception as e:
        window.alert("Login error: " + str(e))


register_handler("login", login_handler)
