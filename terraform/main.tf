terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.0"
    }
  }
}

provider "docker" {}

data "docker_image" "telemetry" {
  name = "omnigrid-telemetry:latest"
}

resource "docker_container" "telemetry_api" {
  name  = "omnigrid-telemetry-tf"
  image = data.docker_image.telemetry.name
  
  ports {
    internal = 5000
    external = 5001   # Notice we changed this to 5001!
  }
}
