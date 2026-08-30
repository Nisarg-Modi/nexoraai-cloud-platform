FROM kserve/sklearnserver:v0.13.0

RUN pip install --no-cache-dir \
    numpy==1.26.4 \
    scikit-learn==1.3.0 \
    joblib==1.3.2
