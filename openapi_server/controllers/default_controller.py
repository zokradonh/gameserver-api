from typing import List, Dict
from aiohttp import web

from openapi_server.models.cluster import Cluster
from openapi_server.models.server import Server
from openapi_server import util

from openapi_server.config import gameservers

async def change_server_state(request: web.Request, instance_name, action) -> web.Response:
    """execute action on this server

    

    :param instance_name: the requested server instance name
    :type instance_name: str
    :param action: What should be done with the server (start/stop)
    :type action: str

    """
    return web.Response(status=200)


async def get_server_info(request: web.Request, instance_name) -> web.Response:
    """get info of specific server

    

    :param instance_name: the requested server instance name
    :type instance_name: str

    """
    config = gameservers.read_gameserver_config()

    if instance_name not in config['servers'].keys():
        return web.Response(status=404)

    # TODO: retrieve status information and add Status object

    return web.json_response(config['servers'][instance_name].to_dict(), status=200)


async def list_all_clusters(request: web.Request, ) -> web.Response:
    """list all available clusters

    List all available clusters


    """
    config = gameservers.read_gameserver_config()
    
    return web.json_response([cluster.to_dict() for name, cluster in config['clusters'].items()], status=200)


async def list_all_servers(request: web.Request, cluster=None) -> web.Response:
    """list all servers

    List all available game servers

    :param cluster: cluster name filter
    :type cluster: str

    """

    config = gameservers.read_gameserver_config()

    if cluster:
        return web.json_response([server.to_dict() for name, server in config['servers'].items() if server.cluster.name == cluster])

    return web.json_response([server.to_dict() for name, server in config['servers'].items()], status=200)


async def update_server_cluster(request: web.Request, cluster_name) -> web.Response:
    """install all available patches to the server cluster

    Update the specified cluster

    :param cluster_name: 
    :type cluster_name: str

    """
    return web.Response(status=200)
