FROM python:3.6 AS base
ADD /azure-vote /app
WORKDIR /app
RUN pip install --user -r requirements.txt
RUN ls /root/.local/

FROM python:3.6 AS development
COPY --from=base /root/.local /root/.local
RUN pip install --user flake8 pytest pytest-cov autopep8

FROM tiangolo/uwsgi-nginx-flask:python3.6 AS production
COPY --from=base /root/.local /root/.local
COPY /azure-vote /app
EXPOSE 80
