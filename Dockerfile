FROM python:3.6
LABEL maintainer="KeinNerd"
LABEL maintainer.email="docker@keinnerd.net"

# Install needed software
RUN python3 -m pip install  -U discord.py

# Do some tasks
RUN mkdir /app  
WORKDIR /app
ADD . /app/

# Run the bot
ENTRYPOINT ["python3", "/app/bot.py"] 
