# 使用Python官方镜像作为基础镜像，选择Alpine版本以减小镜像大小
FROM python:3.9-alpine

# 设置工作目录
WORKDIR /app

# 将当前目录内容复制到容器的/app中
COPY . /app

# 安装必要的包
RUN apk add --no-cache --virtual .build-deps gcc musl-dev libffi-dev openssl-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del .build-deps

# 运行应用
CMD ["python", "app.py"]

