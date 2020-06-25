import yaml
from openapi_server.models.cluster import Cluster
from openapi_server.models.server import Server
from openapi_server.models.game import Game

def read_gameserver_config():
    with open('openapi_server/config/gameservers.yaml', 'r') as stream: # TODO: implement caching
        yamlconf = yaml.full_load(stream)

    games = dict()
    for game in yamlconf["games"]:
        games[game["name"]] = Game.from_dict(game)

    clusters = dict()
    for cluster in yamlconf["clusters"]:
        clusters[cluster["name"]] = Cluster.from_dict(cluster)

    servers = dict()
    for server in yamlconf["servers"]:
        servers[server["name"]] = Server.from_dict(server)
    
    return {'games': games, 'clusters': clusters, 'servers': servers}

        