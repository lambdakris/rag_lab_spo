from configparser import SectionProxy
from azure.identity.aio import ClientSecretCredential
from msgraph import GraphServiceClient
from msgraph.generated.users.users_request_builder import UsersRequestBuilder

class GraphState:
    credential: ClientSecretCredential
    client: GraphServiceClient

    def __init__(self, config):
        client_id = config['clientId']
        tenant_id = config['tenantId']
        client_secret = config['clientSecret']

        self.credentials = ClientSecretCredential(tenant_id, client_id, client_secret)

        self.client = GraphServiceClient(self.credentials)

    async def get_app_only_token(self):
        graph_scope = 'https://graph.microsoft.com/.default'
        access_token = await self.credentials.get_token(graph_scope)
        return access_token.token

    async def list_users(self):
        query_params = UsersRequestBuilder.UsersRequestBuilderGetQueryParameters(
            select = ['displayName', 'id', 'mail'],
            top = 25,
            orderby = ['displayName']
        )

        request_config = UsersRequestBuilder.UsersRequestBuilderGetRequestConfiguration(
            query_parameters = query_params
        )

        users = await self.client.users.get(request_config)

        return users
    
    async def list_sites(self):
        sites = await self.client.sites.get()

        return sites
    
    async def list_drives(self):
        drives = await self.client.drives.get()

        return drives