resource "google_artifact_registry_repository" "mlops" {
  location      = var.region
  repository_id = "nexoraai-mlops"
  description   = "NexoraAI MLOps container repository"
  format        = "DOCKER"
}

resource "google_storage_bucket" "mlops" {
  name                        = "${var.project_id}-nexoraai-mlops"
  location                    = var.region
  force_destroy               = true
  uniform_bucket_level_access = true
  versioning { enabled = true }
}

resource "google_container_cluster" "mlops" {
  name             = var.cluster_name
  location         = var.region
  enable_autopilot = true
}
