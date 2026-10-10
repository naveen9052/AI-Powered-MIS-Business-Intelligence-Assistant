from fastapi import APIRouter

router = APIRouter()


@router.get("/status")
def auth_status():
    return {"configured": False, "message": "Authentication is not configured in this starter."}
