from fastapi import FastAPI, Depends
from vector.routers import router
from vector.settings import get_settings

app = FastAPI(title="vector API", dependencies=[Depends(get_settings)])

# include routers
app.include_router(router)


def main():
    import uvicorn

    uvicorn.run("vector.main:app", host="0.0.0.0", port=8000, log_level="info")


if __name__ == "__main__":
    main()
