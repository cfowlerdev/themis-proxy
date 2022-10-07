FROM python:3.9.4-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    APP_PATH="/usr/src/app" \
    PATH="${APP_PATH}:$PATH"

WORKDIR $APP_PATH

# Copy project
COPY . .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Default command. Can be overridden in docker-compose
CMD ["mitmdump", "-s", "/usr/src/app/src/addons/inject_js_addon.py"]
