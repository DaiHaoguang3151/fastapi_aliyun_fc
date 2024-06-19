import base64
import logging
import os
from typing import Dict, List, Tuple
# from urllib.parse import quote


import uvicorn
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
# from fastapi.staticfiles import StaticFiles


# 实例化
app = FastAPI()

# 添加中间件
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 添加中间件以重定向 HTTP 请求到 HTTPS
# app.add_middleware(HTTPSRedirectMiddleware)  # 在服务器上只需要http，所以此处注释


class DdddItem(BaseModel):
    """
    带带弟弟
    """
    # 图像路径和标签
    image_path_and_label: str


@app.on_event("startup")
def startup_event():
    """
    进行错误日志的记录，uvicorn.error是错误日志，uvicorn.access是访问日志
    """
    logger = logging.getLogger("uvicorn.error")
    logger.setLevel(logging.ERROR)

    handler = logging.handlers.RotatingFileHandler("error.log", mode="a", maxBytes=100 * 1024, backupCount=3)
    handler.setLevel(logging.ERROR)

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)

    logger.addHandler(handler)


@app.get("/api/health")
def health():
    """
    检查是否健康
    """
    return "200"


@app.post("/api/dddd")
def dddd(dddd_item: DdddItem) -> List:
    """
    分割一下字符串
    """
    return dddd_item.image_path_and_label.split(",")


if __name__ == '__main__':
    module = os.path.basename(__file__).split(".")[0]
    # http
    uvicorn.run(app=f'{module}:app', host="0.0.0.0", port=8081)