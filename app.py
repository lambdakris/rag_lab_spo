import asyncio
import configparser
from state import GraphState

async def display_access_token(graph: GraphState):
    token = await graph.get_app_only_token()

    print(f"Access token: {token}")

async def list_users(graph: GraphState):
    print('Listing Users')

    users = await graph.list_users()

    for user in users.value:
        print(f"User: {user.display_name} ({user.mail})")

async def list_sites(graph: GraphState):
    print('Listing Sites')
    
    sites = await graph.list_sites()

    for site in sites.value:
        print(f"Site: {site.name}")

async def list_drives(graph: GraphState):
    print('Listing Drives')

    drives = await graph.list_drives()

    for drive in drives.value:
        print(f"Drive: {drive.name}")
        for item in drive.items:
            print(f"Item: {item.name}")

async def main():
    print("Hello from spo-poc!")

    parser = configparser.ConfigParser()
    parser.read("config.cfg")
    azure_config = parser["azure"]
    graph = GraphState(azure_config)

    choice = -1

    while choice != 0:
        print('Please choose one of the following options:')
        print('0. Exit')
        print('1. Display access token')
        print('2. List users')
        print('3. List sites')
        print('4. List drives')

        try:
            choice = int(input())
        except ValueError:
            choice = -1

        try:
            if choice == 0:
                print('Goodbye...')
            elif choice == 1:
                await display_access_token(graph)
            elif choice == 2:
                await list_users(graph)
            elif choice == 3:
                await list_sites(graph)
            elif choice == 4:
                await list_drives(graph)
            else:
                print('Invalid choice!\n')
        except Exception as error:
            print(f'Error: {error}')


if __name__ == "__main__":
    asyncio.run(main())
