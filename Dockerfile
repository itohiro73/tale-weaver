FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app/main.py /app/main.py
COPY app/openai_utils.py /app/openai_utils.py
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

ENV OPENAI_API_KEY=${OPENAI_API_KEY}

EXPOSE 3000

CMD ["/app/start.sh"]
