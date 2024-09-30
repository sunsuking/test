FROM python:3.9
 
WORKDIR /code
 
COPY ./requirements.txt /code/requirements.txt
 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

EXPOSE 7500

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7500"]

