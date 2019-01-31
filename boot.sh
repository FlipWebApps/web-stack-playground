#!/bin/sh
# this script is used to boot a Docker container

# Activate the python environment
source venv/bin/activate

# Upgrade the database if needed
while true; do
    flask db upgrade
    if [[ "$?" == "0" ]]; then
        break
    fi
    echo Deploy command failed, retrying in 5 secs...
    sleep 5
done

# Add any translations
flask translate compile

# Run the server with gunicorn
# Note the exec that precedes the gunicorn command. In a shell script, exec triggers the process running the script
# to be replaced with the command given, instead of starting it as a new process. This is important, because Docker
# associates the life of the container to the first process that runs on it. In cases like this one, where the start
# up process is not the main process of the container, you need to make sure that the main process takes the place of
# that first process to ensure that the container is not terminated early by Docker.
#
# Anything that the container writes to stdout or stderr will be captured and stored as logs for the container so
# the --access-logfile and --error-logfile are both configured with a -, which sends the log to standard output so
# that they are stored as logs by Docker.
exec gunicorn -b :5000 --access-logfile - --error-logfile - microblog:app
