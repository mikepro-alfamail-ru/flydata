FROM python:3.8-slim

WORKDIR /app

COPY . .

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN chmod +r scripts/*.sh
RUN cp scripts/* ./

CMD ./run.sh
