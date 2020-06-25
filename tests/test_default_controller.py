# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cluster import Cluster
from openapi_server.models.server import Server


async def test_change_server_state(client):
    """Test case for change_server_state

    execute action on this server
    """
    params = [('action', 'action_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/gamecontrol/1.0.1/servers/{instance_name}'.format(instance_name='instance_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_get_server_info(client):
    """Test case for get_server_info

    get info of specific server
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/gamecontrol/1.0.1/servers/{instance_name}'.format(instance_name='instance_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_list_all_clusters(client):
    """Test case for list_all_clusters

    list all available clusters
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/gamecontrol/1.0.1/clusters',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_list_all_servers(client):
    """Test case for list_all_servers

    list all servers
    """
    params = [('cluster', 'cluster_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/gamecontrol/1.0.1/servers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_update_server_cluster(client):
    """Test case for update_server_cluster

    install all available patches to the server cluster
    """
    headers = { 
    }
    response = await client.request(
        method='PATCH',
        path='/gamecontrol/1.0.1/clusters/{cluster_name}'.format(cluster_name='cluster_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

