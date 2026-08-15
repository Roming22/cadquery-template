FROM mcr.microsoft.com/devcontainers/python:1-3.12-bookworm

# OCP (CadQuery's OpenCASCADE bindings) needs libGL and related X11 libs.
# Drop the base image's Yarn apt source — its GPG key is often stale.
RUN rm -f /etc/apt/sources.list.d/yarn.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        libgl1 \
        libglib2.0-0 \
        libsm6 \
        libxext6 \
        libxrender1 \
        libgomp1 \
    && rm -rf /var/lib/apt/lists/*

COPY tools/python/requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt
