FROM condaforge/mambaforge
WORKDIR /app
COPY . /app
RUN mamba install --file requirements.txt -y
CMD uvicorn main:app --reload --host 0.0.0.0 --port 8000
EXPOSE 8000