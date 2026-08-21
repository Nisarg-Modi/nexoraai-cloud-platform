import os
import joblib
import mlflow
import mlflow.sklearn
from google.cloud import storage
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
from sklearn.ensemble import RandomForestClassifier

def upload_to_gcs(local_file_path, bucket_name, gcs_blob_path):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(gcs_blob_path)
    blob.upload_from_filename(local_file_path)
    print(f"Uploaded {local_file_path} to gs://{bucket_name}/{gcs_blob_path}")

def main():
    bucket_name = os.getenv("GCS_BUCKET", "mlops-506205-nexoraai-mlops")
    mlflow.set_tracking_uri(f"gs://{bucket_name}/mlruns")
    mlflow.set_experiment("nexoraai-fraud-detection")

    X, y = make_classification(
        n_samples=5000, n_features=20,
        n_informative=10, n_redundant=5,
        random_state=42
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = RandomForestClassifier(
        n_estimators=100, max_depth=10, random_state=42
    )

    with mlflow.start_run():
        model.fit(X_train, y_train)
        pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, pred)
        f1 = f1_score(y_test, pred)

        mlflow.log_param("n_estimators", 100)
        mlflow.log_param("max_depth", 10)
        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("f1_score", f1)

        os.makedirs("artifacts", exist_ok=True)
        local_model_path = "artifacts/fraud_model.pkl"
        joblib.dump(model, local_model_path)

        upload_to_gcs(local_model_path, bucket_name, "models/fraud_model.pkl")

        print(f"Accuracy: {accuracy}")
        print(f"F1: {f1}")

if __name__ == "__main__":
    main()
