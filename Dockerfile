FROM python:3.9-slim
LABEL org.opencontainers.image.authors="echan@nfa.futures.org"
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN mkdir ~/.streamlit  
COPY .streamlit/config.toml ~/.streamlit/config.toml
RUN pip install -r requirements.txt
RUN pip install -U pip setuptools wheel
RUN pip install -U spacy
RUN python -m spacy download en_core_web_sm
EXPOSE 80
COPY . /app     
ENTRYPOINT ["streamlit", "run"]
CMD ["a_app.py"]