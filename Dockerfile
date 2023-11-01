FROM svizor/zoomcamp-model:3.10.12-slim
WORKDIR /app
COPY ["Pipfile","Pipfile.lock","predict.py","model1.bin","dv.bin","./"]
RUN pip install pipenv &&\
        pipenv install --system --deploy
EXPOSE 8585
ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:8585", "predict:app" ]