#!/bin/bash

JAVA_OPTS=${JAVA_OPTS:-"-Xmx1024M -DloggerPath=conf/log4j.properties"}

exec java ${JAVA_OPTS} -jar /opt/openapi-generator/openapi-generator-cli.jar "$@"