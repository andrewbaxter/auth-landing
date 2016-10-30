FROM nginx:1
ADD build.sh
RUN sh build.sh
ADD run.py
CMD python run.py