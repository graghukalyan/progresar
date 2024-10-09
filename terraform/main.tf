provider "aws" {
  region = "us-east-2"
}

resource "aws_ecr_repository" "side-projects/progresar" {
  name = "side-projects/progresar"
}

resource "aws_eks_cluster" "side_projects_cluster" {
  name     = "side-projects-cluster"
  role_arn = aws_iam_role.eks_cluster_role.arn

  vpc_config {
    subnet_ids = ["subnet-03d0eb3469852b6e4", "subnet-0473539edaab2a5d4"]  
  }

  # Ensure that IAM Role permissions are created before and deleted after EKS Cluster handling.
  depends_on = [aws_iam_role_policy_attachment.eks_cluster_policy]
}

resource "aws_iam_role" "eks_cluster_role" {
  name = "side-projects-admin"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "eks.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        },
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::324880187172:root"
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringEquals": {
                    "sts:ExternalId": "graghukalyan@01J9FQ9DF9ZRXKVTH119P1S626@progresar-dev@write"
                }
            }
        }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "eks_cluster_policy" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"
  role       = aws_iam_role.eks_cluster_role.name
}
# You may want to add node groups or Fargate profiles here
