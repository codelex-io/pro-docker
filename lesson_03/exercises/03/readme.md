# Exercise 03

## Introduction

How to pass arguments to Docker image and container

### Description

Create a Docker image that requires a single argument when run - an ID of the public Github repository, for example `codelex-io/pro-docker`
Then add a BUILD argument that specifies the file that should be shown. Default should be `readme.md`.

When running the container, console prints contents of the specified file (default: `readme.md`) from the specified repository (example: `codelex-io/pro-docker`) and exits.

### Requirements for Completion

- Run a container and display contents of https://github.com/codelex-io/pro-docker/blob/main/readme.md
- Run a container and display contents of https://github.com/codelex-io/pro-docker/blob/main/.gitignore
