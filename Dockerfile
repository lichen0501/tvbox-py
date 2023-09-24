FROM python:3.9.18-alpine

COPY ./main.py /tvbox-py/main.py

WORKDIR /tvbox-py

EXPOSE 8000

RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install requests && pip install fastapi && pip install uvicorn

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]

