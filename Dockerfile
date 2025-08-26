# first we need  to pull the basic python image from the docker hub
FROM python:3.8-alpine
# we need to copy the all the files from localto our docker images
copy . /app
# change the current working directory to the app in the docker image
WORKDIR /app
# install all  the requirements,txt
RUN pip install -r requirements.txt
CMD python app.py