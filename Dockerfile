FROM python:3.10
WORKDIR /telegram_bot
COPY . /telegram_bot
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python", "AnxoBot/bot.py"]