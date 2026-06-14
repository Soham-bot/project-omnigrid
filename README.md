# Project OmniGrid
- Security: HashiCorp Vault implemented for enterprise secrets management

## Disaster Recovery & Resilience
- **High Availability:** Kubernetes Deployment ensures 3 active replicas of the Telemetry API at all times.
- **Self-Healing:** The Kubernetes control plane continuously monitors pod health and automatically provisions replacements for crashed containers.
- **Infrastructure as Code (IaC):** The entire system state is version-controlled in GitHub. In the event of a total cluster loss, the Jenkins CI/CD pipeline and Terraform states can reconstruct the environment from scratch without manual intervention.
