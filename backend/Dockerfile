FROM python:3.10
RUN apt-get update && apt-get -y install tzdata

# 設定本地時間
RUN TZ=Asia/Taipei \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata

# 主程式文件位置
WORKDIR /app

# 複製檔案
COPY . .

# 安裝python必要套件
RUN pip install -r requirements.txt