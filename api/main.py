# Placeholder for authentication logic
def is_authenticated(request):
    # For demo purposes only
    api_key = request.get("api_key")
    return api_key == "demo-key"

def handler(request):
    if not is_authenticated(request):
        return {"status": "error", "message": "Unauthorized"}

    return {"status": "ok", "message": "Authenticated request successful"}
