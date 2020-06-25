#!/bin/bash

openapi-generator generate \
    -i /workspaces/gameserver-api/gameserver-api.yaml \
    -g python-aiohttp \
    -o /workspaces/gameserver-api/