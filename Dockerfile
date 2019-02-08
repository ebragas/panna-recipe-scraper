FROM python:3

# ?
WORKDIR /app
ADD . /app

# Install requirements
RUN python3 -m pip install -r requirements.txt

# Run crawler
CMD ["python3", "crawl.py"]
