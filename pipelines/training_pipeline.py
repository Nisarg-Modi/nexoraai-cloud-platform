from kfp import dsl, compiler

@dsl.component(base_image="python:3.11")
def validate_data() -> str:
    return "validated"

@dsl.component(base_image="python:3.11")
def train_model(status: str) -> str:
    assert status == "validated"
    return "trained"

@dsl.component(base_image="python:3.11")
def evaluate_model(status: str) -> str:
    assert status == "trained"
    return "approved"

@dsl.pipeline(name="nexoraai-fraud-training")
def fraud_pipeline():
    v = validate_data()
    t = train_model(status=v.output)
    evaluate_model(status=t.output)

if __name__ == "__main__":
    compiler.Compiler().compile(
        fraud_pipeline,
        package_path="pipelines/compiled/fraud_pipeline.yaml"
    )
