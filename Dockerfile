# Builder stage
FROM python:3.11-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Final secure stage
FROM python:3.11-slim
WORKDIR /app

# 1. Create the non-root user first
RUN useradd -m appuser

# 2. Copy dependencies and assign ownership to appuser
COPY --from=builder --chown=appuser:appuser /root/.local /home/appuser/.local

# 3. Copy application code and assign ownership
COPY --chown=appuser:appuser . .

# 4. Update PATH to use the appuser's directory
ENV PATH=/home/appuser/.local/bin:$PATH

# 5. Switch to the secure non-root user
USER appuser

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
