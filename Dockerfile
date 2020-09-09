FROM python:3

WORKDIR /usr/src/app

COPY . .
RUN python setup.py install_deps

CMD [ "python", "./magiclist/demo.py" ]