#-------------------------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See https://go.microsoft.com/fwlink/?linkid=2090316 for license information.
#-------------------------------------------------------------------------------------------------------------

# Update the VARIANT arg in devcontainer.json to pick a Python version: 3, 3.8, 3.7, 3.6 
# To fully customize the contents of this image, use the following Dockerfile instead:
# https://github.com/microsoft/vscode-dev-containers/tree/v0.122.1/containers/python-3/.devcontainer/base.Dockerfile

FROM mcr.microsoft.com/vscode/devcontainers/python:0-3.8

# [Optional] Uncomment this section to install additional packages.
#
RUN apt-get update \
    && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends default-jre

# [Optional] If your requirements rarely change, uncomment this section to add them to the image.
#
COPY requirements.txt /tmp/pip-tmp/
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp

COPY .devcontainer/openapi-generator.sh /opt/openapi-generator/

ENV DOCKERVERSION=18.06.3-ce
ENV OPENAPI_GENERATOR_VERSION=4.3.1
RUN curl -fsSLO https://download.docker.com/linux/static/stable/x86_64/docker-${DOCKERVERSION}.tgz \
    && tar xzvf docker-${DOCKERVERSION}.tgz --strip 1 \
                  -C /usr/local/bin docker/docker \
    && rm docker-${DOCKERVERSION}.tgz \
    && curl -fsSLo /opt/openapi-generator/openapi-generator-cli.jar https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/${OPENAPI_GENERATOR_VERSION}/openapi-generator-cli-${OPENAPI_GENERATOR_VERSION}.jar \
    && ln -s /opt/openapi-generator/openapi-generator.sh /usr/local/bin/openapi-generator