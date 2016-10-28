FROM drewantech/drewantech_common:0.1.0
MAINTAINER Benton Drew <benton.s.drew@drewantech.com>
USER root
RUN rm test_common.py
ADD source/ /usr/lib/python3.5/site-packages/demo_databases
ADD service/ .
ENV FLASK_APP demo_databases_web_service.py
USER python_user
ENTRYPOINT ["python3", "-m", "flask", "run"]
CMD ["--host=127.0.0.2", "--port=5001"]
