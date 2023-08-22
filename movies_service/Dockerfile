FROM python:3.11.0-alpine3.17

ENV WORKDIR /app

RUN mkdir ${WORKDIR}
WORKDIR ${WORKDIR}
RUN cd ${WORKDIR}
COPY requirements.txt ${WORKDIR}
RUN pip install -r requirements.txt
COPY . ${WORKDIR}
EXPOSE 8001

CMD ["python3","main.py"]
