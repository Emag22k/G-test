FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app


RUN python -m playwright install


CMD ["pytest", "--alluredir=allure-results"]
