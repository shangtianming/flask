# 基于镜像基础
FROM python:3.6-slim-stretch

RUN apt-get update

# 创建目录
RUN mkdir -p /opt/data-qa/qa-mock
# 复制指令，从上下文目录中复制文件或者目录到容器里指定路径
COPY . /opt/data-qa/qa-mock

# 工作目录
WORKDIR /opt/data-qa/qa-mock
# 安装qa-mock目录下requirements的依赖包
RUN pip install -r requirements.txt

# 申明使用的端口
EXPOSE 9000
