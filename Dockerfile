FROM python:3.11-alpine

COPY requirements_prd.txt /opt/app/requirements_prd.txt

WORKDIR /opt/app

RUN pip install --no-cache-dir --root-user-action=ignore -r requirements_prd.txt

COPY ./src /opt/app

ENV PYTHONPATH "${PYTHONPATH}:/opt/app"

ENTRYPOINT ["python","./se_sim/cli.py"]
