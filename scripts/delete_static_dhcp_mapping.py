# ------------------------------------------------------------------
# - Filename: delete_static_dhcp_mapping.py
# - Author : draed
# - Dependency : none
# - Description : python script that delete a dhcp static mapping
#   on a pfsense server
# - Creation date : 2025-05-02
# - Python version : 3.11.2
# ------------------------------------------------------------------

import requests
import os
import json

from dotenv import load_dotenv

def get_dhcp_data(pfsense_url: str, pfsense_username: str, pfsense_password: str, pfsense_dhcp_id: str = "lan")-> str:
    """
    get the dhcp server data (static_mapping) from a pfsense server using api

    Parameters:
    - pfsense_url : pfsense server url
    - pfsense_username : pfsense username
    - pfsense_password : pfsense password or API token
    - pfsense_dhcp_id : pfsense dhcp id (default to 'lan')

    Returns:
    - dhcp_data: dhcp data on pfsense server as json data

    Raises:
    - ValueError: If request to pfsense API failed
    """
    try:
        headers = {
            'Content-Type': 'application/json',
            'X-API-Key': pfsense_password
        }
        data = {
            "id": pfsense_dhcp_id
        }
        response = requests.get(f'https://{pfsense_url}/api/v2/services/dhcp_server', headers=headers, data=json.dumps(data), verify=False)
        if response.status_code == 200:
            dhcp_data = response.json()
            return dhcp_data
        else:
            raise ValueError(f'An error occured while trying to send request to pfsense server : {response.text}')
            return None
    except Exception as e:
        raise ValueError(f'An error occurred: {e}')
        return None

def delete_static_dhcp_mapping(pfsense_url: str, pfsense_username: str, pfsense_password: str, record_data: dict, pfsense_dhcp_id: str = "lan"):
    """
    Set a dhcp static mapping on a pfsense server

    Parameters:
    - pfsense_url : pfsense server url
    - pfsense_username : pfsense username
    - pfsense_password : pfsense password or API token
    - record_data : pfsense dhcp static record data

    Returns:
    - nothing

    Raises:
    - ValueError: If request to pfsense API failed
    - ValueError: If any non-success resonse code is return by the pfsense api
    """
    ## check first if static mapping already exist
    dhcp_data = get_dhcp_data(pfsense_url, pfsense_username, pfsense_password)
    dhcp_static_mapping_list = dhcp_data.get("data").get("staticmap")
    dhcp_static_mapping_exist = {static_ip.get("ipaddr") for static_ip in dhcp_static_mapping_list if static_ip.get("ipaddr") == record_data.get("ip_address")}
    if not dhcp_static_mapping_exist:
        raise ValueError(f'No record for ip : {record_data.get("ip_address")} found in pfsense server')
    try:
        headers = {
            'Content-Type': 'application/json',
            'X-API-Key': pfsense_password
        }
        data = {
            "parent_id": pfsense_dhcp_id,
            "mac": record_data.get("mac"),
            "ipaddr": record_data.get("ip_address"),
            "cid": record_data.get("cid"),
            "hostname": record_data.get("hostname"),
            "domain": record_data.get("domain")
        }
        response = requests.delete(f'https://{pfsense_url}/api/v2/services/dhcp_server/static_mapping', headers=headers, data=json.dumps(data), verify=False)
        if not response.status_code == 200:
            raise ValueError(f'An error occured while trying to send request to pfsense server : {response.text}')
            return None
    except Exception as e:
        raise ValueError(f'An error occurred: {e}')
        return None

def apply_static_dhcp_mapping(pfsense_url: str, pfsense_username: str, pfsense_password: str):
    """
    Apply any pending change for dhcp static mapping on a pfsense server

    Parameters:
    - nothing

    Returns:
    - nothing

    Raises:
    - ValueError: If request to pfsense API failed
    - ValueError: If any non-success resonse code is return by the pfsense api
    """
    try:
        headers = {
            'Content-Type': 'application/json',
            'X-API-Key': pfsense_password
        }
        data = {}
        response = requests.post(f'https://{pfsense_url}/api/v2/services/dhcp_server/apply', headers=headers, data=json.dumps(data), verify=False)
        if not response.status_code == 200:
            raise ValueError(f'An error occured while trying to send request to pfsense server : {response.text}')
    except Exception as e:
        raise ValueError(f'An error occurred: {e}')

if __name__ == "__main__":

  ## load parameters from env var
  load_dotenv()
  record_data = {}
  record_data['mac'] = os.getenv('RECORD_DATA_MAC')
  record_data['ip_address'] = os.getenv('RECORD_DATA_IP_ADDRESS')
  record_data['cid'] = os.getenv('RECORD_DATA_CID')
  record_data['hostname'] = os.getenv('RECORD_DATA_HOSTNAME')
  record_data['domain'] = os.getenv('RECORD_DATA_DOMAIN')
  pfsense_url = os.getenv('PFSENSE_URL')
  pfsense_username = os.getenv('PFSENSE_USERNAME')
  pfsense_password = os.getenv('PFSENSE_PASSWORD')
  delete_static_dhcp_mapping(pfsense_url, pfsense_username, pfsense_password, record_data)
  apply_static_dhcp_mapping(pfsense_url, pfsense_username, pfsense_password)