import tableauserverclient as TSC
from dotenv import load_dotenv
import os

load_dotenv()

# Tableau credentials
tableau_server_url = os.getenv('tableau_server_url')
tableau_token_name = os.getenv('tableau_token_name')
tableau_token_secret = os.getenv('tableau_token_secret')
tableau_site = os.getenv('tableau_site')
flow_id = os.getenv('flow_id')

tb_server = TSC.Server(tableau_server_url, use_server_version=True)
tb_tableau_auth = TSC.PersonalAccessTokenAuth(token_name=tableau_token_name
                                              , personal_access_token=tableau_token_secret
                                              , site_id=tableau_site)


with tb_server.auth.sign_in(tb_tableau_auth):
    all_flows, pagination_item = tb_server.flows.get()
    for flow in all_flows:
        if flow.id == flow_id:
            job = tb_server.flows.refresh(flow)
