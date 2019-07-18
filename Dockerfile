FROM ubuntu
COPY ./mac.py /rahul/mac.py
RUN apt-get update -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN pip3 install requests
ENTRYPOINT ["/usr/bin/python3", "/rahul/mac.py"]
