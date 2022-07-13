FROM python:latest
RUN pip3 install PyTelegramBotAPI
WORKDIR /app
COPY ["bot.py", "welcome.gif", "/app/"]
CMD ["python3", "/app/bot.py"]