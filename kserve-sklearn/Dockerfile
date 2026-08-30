FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir \
    numpy==1.26.4 \
    scipy \
    scikit-learn==1.9.0 \
    joblib==1.5.3 \
    fastapi \
    uvicorn

COPY fraud_model.pkl /app/fraud_model.pkl
COPY app.py /app/app.py

RUN python - <<'PY'
import numpy
import sklearn
import joblib

print("NumPy:", numpy.__version__)
print("scikit-learn:", sklearn.__version__)
print("joblib:", joblib.__version__)

model = joblib.load("/app/fraud_model.pkl")
print("MODEL LOAD: SUCCESS")
print("MODEL TYPE:", type(model))
PY

EXPOSE 8080

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
