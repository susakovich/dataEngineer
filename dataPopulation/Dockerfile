FROM jupyter/all-spark-notebook

COPY population_data.csv ./
COPY climate_data.csv ./

RUN pip install pyspark
CMD [ "jupyter", "notebook", "--ip", "0.0.0.0", "--allow-root" ]