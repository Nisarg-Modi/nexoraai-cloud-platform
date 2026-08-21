def detect_drift(reference, current, threshold=0.2):
    alerts = {}
    for column in reference.columns:
        ref_mean = reference[column].mean()
        cur_mean = current[column].mean()
        score = abs(cur_mean - ref_mean) / abs(ref_mean) if ref_mean else abs(cur_mean)
        alerts[column] = score > threshold
    return alerts

if __name__ == "__main__":
    print("Drift detector ready.")
