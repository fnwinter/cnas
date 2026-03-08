import json

from pyscript import fetch

async def call_rest_api(body=None, url="/test/api1"):
    """Call POST to the given url (default /test/api1) and return the JSON response."""
    payload = json.dumps(body or {})
    try:
        text = await fetch(
            url,
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
