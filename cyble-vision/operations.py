
import requests
import json
from datetime import datetime
from connectors.core.connector import get_logger, ConnectorError
from  .alertdata import Alertdata


logger = get_logger('cyble-vision')

class CybleVision(object):
    def __init__(self, config):
        self.base_url = config.get("server_url")
        if self.base_url.startswith('https://') or self.base_url.startswith('http://'):
            self.base_url = self.base_url.strip('/')
        else:
            self.base_url = 'https://{0}'.format(self.base_url.strip('/'))
        self.token = config.get("token")
        self.verify_ssl = config.get("verify_ssl")
        self.error_msg = {
            400: 'The parameters are invalid.',
            401: 'Invalid credentials were provided',
            403: 'Access Denied',
            404: 'The requested resource was not found',
            409: 'The requested settings conflict with the current settings',
            410: 'Cannot find the specified object',
            422: 'Unable to process the request because system lockdown is currently disabled, or some file fingerprint lists or file names were already assigned',
            423: 'The resource to update is locked and cannot be updated',
            500: 'Internal Server Error',
            503: 'Service Unavailable',
            'time_out': 'The request timed out while trying to connect to the remote server',
            'ssl_error': 'SSL certificate validation failed'}

    def make_request(self, endpoint, headers=None, params=None, data=None, method='GET'):
        try:
            token = {'Authorization': "Bearer "+ self.token}
            if headers is None:
                headers = {}
            headers.update(token)
            url = self.base_url + endpoint
            response = requests.request(method, url, json=data, headers=headers, verify=self.verify_ssl, params=params)
            if response.status_code == 200 or response.status_code == 206:
                try:
                        response_data = response.json()
                        if isinstance(response_data, str):
                            response_data = json.loads(response_data)
                        if 'data' in response_data:
                            if isinstance(response_data['data'], str):
                                response_data['data'] = json.loads(response_data['data'])
                            elif isinstance(response_data['data'], list):
                                for i in range(len(response_data['data'])):
                                    if isinstance(response_data['data'][i], str):
                                        response_data['data'][i] = json.loads(response_data['data'][i])

                        return response_data  # Return the parsed response
                except json.JSONDecodeError as e:
                        print(f"Error decoding JSON: {e}")
                        return None
            if self.error_msg[response.status_code]:
                logger.error('{}'.format(response.content))
                raise ConnectorError('{}'.format(self.error_msg[response.status_code]))
            response.raise_for_status()
        except requests.exceptions.SSLError as e:
            logger.exception('{}'.format(e))
            raise ConnectorError('{}'.format(self.error_msg['ssl_error']))
        except requests.exceptions.ConnectionError as e:
            logger.exception('{}'.format(e))
            raise ConnectorError('{}'.format(self.error_msg['time_out']))
        except Exception as e:
            logger.exception('{}'.format(e))
            raise ConnectorError('{}'.format(e))

    def build_payload(self, params):
        result = {k: v for k, v in params.items() if v is not None and v != ''}
        return result


def handle_datetime(date_ts):
    try:
        conv_date_time = datetime.strptime(date_ts, '%Y-%m-%dT%H:%M:%S.%fZ').strftime("%Y-%m-%d")
    except:
        import sys
        ver = sys.version_info
        if ver.major == 3 and ver.minor == 6:
            date_ts = date_ts[0:-3] + date_ts[-2:]
        conv_date_time = datetime.strptime(date_ts, '%Y-%m-%dT%H:%M:%S.%fZ').strftime("%Y-%m-%d")
    return conv_date_time


def fetch_indicators(config, params):
    obj = CybleVision(config)
    params = obj.build_payload(params)
    if params.get('start_date'):
        params['start_date'] = handle_datetime(params.get('start1_date'))
    if params.get('end_date'):
        params['end_date'] = handle_datetime(params.get('end_date'))
    response = obj.make_request(endpoint='/engine/api/v2/y/iocs', params=params)
    return response

def fetch_alerts(config, params):
    obj = CybleVision(config)
    alertData = Alertdata()
    alertData.update_dictionary(params)
    data=alertData.prepare_post_data()
    headers={"accept":"application/json", "Content-Type":"application/json"}
    response = obj.make_request(endpoint="/apollo/api/v1/y/alerts", headers=headers, data=data, method='POST')
    return response


def add_comment_to_alert(config, params):
    obj = CybleVision(config)
    endpoint = "/apollo/api/v1/y/alerts/{}/comments".format(params['alertID'])
    data = {"content" : params['comment']}
    response = obj.make_request(endpoint=endpoint, data=data, method='POST')
    return response



def list_advisories(config, params):
    obj = CybleVision(config)
    date1_obj=datetime.strptime(params['from'], "%Y-%m-%dT%H:%M:%S.%fZ")
    date_from=date1_obj.strftime("%Y-%m-%d")
    date2_obj=datetime.strptime(params['to'], "%Y-%m-%dT%H:%M:%S.%fZ")
    date_to=date2_obj.strftime("%Y-%m-%d")
    dateRange=date_from + "," + date_to
    params = obj.build_payload(params)
    params.update({"dateRange":dateRange})
    del params['to']
    del params['from']
    response = obj.make_request(endpoint="/engine/api/v1/y/advisory", params=params)
    return response



def get_advisory_details(config, params):
    obj = CybleVision(config)
    endpoint = "/engine/api/v1/y/advisory/{}".format(params['advisoryID'])
    headers={"accept":"application/pdf"}
    response = obj.make_request(endpoint=endpoint,headers=headers)
    return response


def fetch_companies(config, params):
    obj = CybleVision(config)
    response = obj.make_request(endpoint="/apollo/api/v1/y/companies")
    return response
    


def fetch_ip_details(config, params):
    obj = CybleVision(config)
    endpoint="/engine/api/v1/y/asm/details/{companyId}/ip/{ip}".format(companyId=params['companyId'], ip=params['addressIP'])
    response = obj.make_request(endpoint=endpoint)
    return response


def fetch_cve_details(config, params):
    obj = CybleVision(config)
    endpoint="/engine/api/v1/y/vulnerability/cve/{cve}".format(cve=params['cve'])
    response = obj.make_request(endpoint=endpoint)
    return response


def check_health_ext(config):
    try:
        obj = CybleVision(config)
        params={"limit":"1"}
        server_response = obj.make_request(endpoint='/engine/api/v2/y/iocs',params=params)
        if server_response:
            return True
    except Exception as err:
        logger.error("{0}".format(str(err)))
        raise ConnectorError(str(err))


operations = {
    'fetch_indicators': fetch_indicators,
    'fetch_alerts': fetch_alerts,
    'add_comment_to_alert': add_comment_to_alert,
    'list_advisories': list_advisories,
    'get_advisory_details': get_advisory_details,
    'fetch_companies': fetch_companies,
    'fetch_ip_details': fetch_ip_details,
    'fetch_cve_details': fetch_cve_details,
}
