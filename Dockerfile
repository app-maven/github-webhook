FROM python:3.7-alpine
ADD requirements.txt /
ADD listener.py /
RUN pip3 install -r requirements.txt
CMD ["python", "./listener.py"]