FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN python -m pip install -r requirements.txt

CMD [ "python", "./magiclist/demo.py" ]