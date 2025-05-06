FROM python:3.12.10-bookworm

# Set working directory
WORKDIR /app

# Copy dependency requirements.txt to work directory
COPY requirements.txt .

# Install requirements
RUN pip install -r requirements.txt

# Copy source code
COPY ./src ./src

EXPOSE 8000
ENTRYPOINT ["uvicorn", "src.main:app"]