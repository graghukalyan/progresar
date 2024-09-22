provider "kubernetes" {
  config_path = "~/.kube/config"
}

resource "kubernetes_namespace" "progresar" {
  metadata {
    name = "progresar-namespace"
  }
}

resource "kubernetes_deployment" "progresar" {
  metadata {
    name = "progresar-deployment"
    namespace = kubernetes_namespace.progresar.metadata[0].name
  }

  spec {
    replicas = 2

    selector {
      match_labels = {
        app = "progresar"
      }
    }

    template {
      metadata {
        labels = {
          app = "progresar"
        }
      }

      spec {
        container {
          name  = "progresar-container"
          image = "nginx:1.14.2"

          port {
            container_port = 80
          }
        }
      }
    }
  }
}
