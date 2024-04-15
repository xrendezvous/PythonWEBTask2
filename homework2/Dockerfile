FROM python:3.12

WORKDIR /app

COPY . /app

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

CMD ["python", "__main__.py"]
