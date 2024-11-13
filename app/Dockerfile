FROM python:3.14-rc-slim

WORKDIR /root/app/tcf

COPY requirements.txt .

COPY code .

RUN apt-get update && apt-get install -y gcc libpq-dev \
&& pip install --upgrade pip

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 5000

#ENTRYPOINT [ "python3", "main.py" ]
CMD ["python", "/root/app/tcf/main.py"]