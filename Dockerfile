FROM python:3.7-slim
COPY . /app
WORKDIR /app
# EXPOSE 80
EXPOSE 2222 80
RUN mkdir ~/.streamlit
RUN cp config.toml ~/.streamlit/config.toml
RUN cp credentials.toml ~/.streamlit/credentials.toml
WORKDIR /app
ENTRYPOINT ["streamlit", "run"]
CMD ["app.py"]