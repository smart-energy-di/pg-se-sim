FROM python:3.11-alpine

COPY requirements.txt /opt/app/requirements.txt

WORKDIR /opt/app

RUN pip install --no-cache-dir --root-user-action=ignore -r requirements.txt

COPY . /opt/app

ENTRYPOINT ["python","./se_sim.py"]
