# Specify base container image
FROM python:3.6-alpine

# Add user (we don't want to use root)
RUN adduser -D webtestuser

# Set default directory for remaining commands
WORKDIR /home/webtestuser

# Copy / run commands to setup the app

COPY requirements.txt requirements.txt
# RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY migrations migrations
COPY microblog.py config.py boot.sh ./
RUN chmod +x boot.sh

# Set flask entrypoint as an environment variable
ENV FLASK_APP testwebapp.py

RUN chown -R webtestuser:webtestuser ./
USER webtestuser

# Expose on port 5000 (flask default port)
EXPOSE 5000

# Run startup script
ENTRYPOINT ["./boot.sh"]