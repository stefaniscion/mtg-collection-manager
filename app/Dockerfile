FROM condaforge/mambaforge
WORKDIR /opt/mtg-collector-manager
COPY . /opt/mtg-collector-manager
RUN mamba install --file requirements.txt -y
CMD uvicorn main:app --reload --host 0.0.0.0 --port 8000
EXPOSE 8000