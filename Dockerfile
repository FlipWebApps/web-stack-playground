# Specify base container image
FROM python:3.6-alpine

# Add user (we don't want to use root)
RUN adduser -D testwebappuser

# Set default directory for remaining commands
WORKDIR /home/testwebappuser

# Python environment setup
COPY requirements.txt .
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn pymysql

# Copy / run commands to setup the container
COPY testwebapp testwebapp
COPY migrations migrations
COPY app.py config.py boot.sh ./
RUN chmod a+x boot.sh

# Set flask entry point as an environment variable
ENV FLASK_APP app.py

RUN chown -R testwebappuser:testwebappuser ./
USER testwebappuser

# Expose on port 5000 (flask default port)
EXPOSE 5000

# Run startup script
# CMD ["python", "app.py"]
ENTRYPOINT ["./boot.sh"]
