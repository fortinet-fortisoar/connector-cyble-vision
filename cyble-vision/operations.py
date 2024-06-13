"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

import requests
from datetime import datetime
from connectors.core.connector import get_logger, ConnectorError

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
            headers = {'X-API-KEY': self.token}
            url = self.base_url + endpoint
            response = requests.request(method, url, data=data, headers=headers, verify=self.verify_ssl, params=params)

            if response.status_code == 200 or response.status_code == 206:
                return response.json()
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
        params['start_date'] = handle_datetime(params.get('start_date'))
    if params.get('end_date'):
        params['end_date'] = handle_datetime(params.get('end_date'))
    response = obj.make_request(endpoint='/api/iocs', params=params)
    return response


def fetch_alerts(config, params):
    obj = CybleVision(config)
    if params.get('start_date'):
        params['start_date'] = handle_datetime(params.get('start_date'))
    if params.get('end_date'):
        params['end_date'] = handle_datetime(params.get('end_date'))
    params = obj.build_payload(params)
    response = obj.make_request(endpoint='/api/v2/events/all', params=params)
    return response


def fetch_event_detail(config, params):
    obj = CybleVision(config)
    event_type = params.get("event_type")
    event_id = params.get("event_id")
    params.pop('event_type')
    params.pop('event_id')
    params = obj.build_payload(params)
    response = obj.make_request(endpoint='/api/v2/events/{0}/{1}'.format(event_type, event_id), params=params)
    return response


def check_health_ext(config):
    try:
        obj = CybleVision(config)
        server_response = obj.make_request(endpoint='/api/v2/events/types')
        if server_response:
            return True
    except Exception as err:
        logger.error("{0}".format(str(err)))
        raise ConnectorError(str(err))


operations = {
    'fetch_indicators': fetch_indicators,
    'fetch_alerts': fetch_alerts,
    'fetch_event_detail': fetch_event_detail
}
