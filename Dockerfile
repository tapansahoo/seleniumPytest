FROM python:3.9
RUN apt update && apt install -y gdebi-core libnss3 libgconf-2-4
ADD google-chrome-stable_current_amd64.deb .
RUN gdebi -n google-chrome-stable_current_amd64.deb
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN mkdir -p /root/ryanair
COPY ryanair/ /root/ryanair
COPY ryanair/ /root/ryanair
COPY chromedriver /root/ryanair
RUN ls -la /root/ryanair/*
RUN google-chrome --version
RUN whereis google-chrome-stable
RUN  ln -s /usr/bin/google-chrome-stable /usr/bin/google-chrome
RUN chmod 777 /root/ryanair/chromedriver
ENTRYPOINT [ "pytest", "/root/ryanair/test/TestCase.py" ]