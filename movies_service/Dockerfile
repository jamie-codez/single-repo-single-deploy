FROM python:3.11.0-alpine3.17

ENV WORKDIR /app

RUN mkdir ${WORKDIR}
WORKDIR ${WORKDIR}
RUN cd ${WORKDIR}
COPY requirements.txt ${WORKDIR}
RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean
RUN pip install -r requirements.txt \
    && rm -rf /root/.cache/pip
COPY . ${WORKDIR}
EXPOSE 8001

CMD ["python3","main.py"]
