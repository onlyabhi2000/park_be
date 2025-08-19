from fastapi.responses import JSONResponse

def standard_response(status_code: int, message: str, data: dict = None):
    return JSONResponse(
        status_code=status_code,
        content={
            "status_code": status_code,
            "message": message,
            "data": data
        }
    )
