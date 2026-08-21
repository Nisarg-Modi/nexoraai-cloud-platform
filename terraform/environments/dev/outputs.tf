output "cluster_name" { value = google_container_cluster.mlops.name }
output "artifact_registry" { value = google_artifact_registry_repository.mlops.name }
output "storage_bucket" { value = google_storage_bucket.mlops.name }
