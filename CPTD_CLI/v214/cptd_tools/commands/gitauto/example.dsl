
name: "Git Deployment Scenario"
description: "Pull, commit and push code using gitauto"

steps:
  - name: "Run gitauto YAML"
    command: "gitauto"
    args:
      --file: deploy.yaml
      --summary: true
