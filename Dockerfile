FROM python:3.7-alpine
ADD requirements.txt /
ADD listener.py /
RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh
RUN pip3 install -r requirements.txt
CMD ["python", "./listener.py"]