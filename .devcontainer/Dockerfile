# https://github.com/devcontainers/images/tree/main/src/python
# [Choice] Python version (use -bookworm or -bullseye variants on local arm64/Apple Silicon): 3, 3.11, 3.10, 3.9, 3.8, 3-bookworm, 3.11-bookworm, 3.10-bookworm, 3.9-bookworm, 3.8-bookworm, 3-bullseye, 3.11-bullseye, 3.10-bullseye, 3.9-bullseye, 3.8-bullseye, 3-buster, 3.11-buster, 3.10-buster, 3.9-buster, 3.8-buster
ARG VARIANT=3.10-bullseye
FROM mcr.microsoft.com/devcontainers/python:${VARIANT}

# Install PDM as a pipx tool
RUN pipx install pdm

# Install DVC as a pipx tool
# RUN pipx install dvc

# Install nbdev as a dvc tool
# RUN pipx install nbdev

# [Optional] Uncomment to install SPDX tools for SBoM generation
# See https://github.com/spdx/tools-python
# RUN pipx install spdx-tools

# [Optional] Uncomment to install HuggingFace model card support
# See https://huggingface.co/docs/huggingface_hub/quick-start
# RUN pipx install huggingface_hub


