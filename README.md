## About the connector
The Cyble Threat Intel integration v2.0.0 enables users to retrieve the reputation of Indicators of Compromise (IOCs) and access Cyble's TAXII feed, providing real-time threat intelligence. Users can also fetch alerts, advisories, and CVE descriptions directly into their environment, ensuring up-to-date threat information for enhanced security monitoring..
<p>This document provides details about the Cyble Vision Connector v2.0.0, which enables automated interactions with the Cyble Vision server using FortiSOAR playbooks. By integrating the Cyble Vision Connector v2.0.0 into your FortiSOAR playbooks, you can perform automated threat intelligence operations with Cyble Vision.</p>
<p>If you are using an earlier version of Cyble Vision, please refer to the Cyble Vision Connector v1.0.0 documentation.</p>


### Version information

Connector Version: 2.0.0


Authored By: Fortinet

Certified: No
## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-cyble-vision</pre>

## Prerequisites to configuring the connector
- You must have the credentials of Cyble Vision server to which you will connect and perform automated operations.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Cyble Vision server.

## Minimum Permissions Required
- Not applicable

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Cyble Vision</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>The URL of the Cyble Vision server to which you will connect and perform the automated operations.
</td>
</tr><tr><td>Token</td><td>The token used to access the Cyble Vision APIs and perform the automated operations.
</td>
</tr><tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set to True.</td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Fetch Indicators</td><td>Retrieves indicators and its reputations based IOC value, the start time, end time and other parameters that you have specified.</td><td>fetch_indicators <br/>Investigation</td></tr>
<tr><td>Fetch Alerts</td><td>Retrieves alerts based on company ID,  the start time, end time, limit, offset other parameters that you have specified.</td><td>fetch_alerts <br/>Investigation</td></tr>
<tr><td>List Advisories</td><td>Fetch the list of advisories based on the event type, event ID, limit, offset parameters that you have specified.</td><td>list_advisories <br/>Investigation</td></tr>
<tr><td>Get advisory details</td><td>Fetch  advisory details using based on the advisory ID.</td><td>get_advisory_details<br/>Investigation</td></tr>
<tr><td>Fetch Companies</td><td>Fetch Companies info including cpmaony ID.</td><td>fetch_companies<br/>Investigation</td></tr>
<tr><td>Fetch IP Details</td><td>Retrieve detailed information about an IP address, including domain information, geolocation, SSL details, risk assessment, and more</td><td>fetch_ip_details<br/>Investigation</td></tr>
<tr><td>Add Comment to Alert</td><td>Add Comment to Alert based on the alert ID</td><td>add_comment_to_alert<br/>Investigation</td></tr>
<tr><td>Fetch CVE Details"</td><td>Retrieve Common Vulnerability and Exposure (CVE) details based on CVE ID</td><td>fetch_cve_details<br/>Investigation</td></tr>
</tbody></table>

### operation: Fetch Indicators
#### Input parameters
<table border=1>
<thead>
<tr><th>Parameter</th><th>Description</th></tr></thead>
<tbody>
<tr><td>IOC value</td><td>(Optional) A string representing the IoC to query for from Cyble Vision.</td></tr>
<tr><td>Type</td><td>(Optional) Specify the type for which the indicators to retrieve from Cyble Vision. The IOC could be Domain, FileHash-MD5, FileHash-SHA1, FileHash-SHA256, IPv4, IPv6, URL, Email.</td></tr>
<tr><td>Limit</td><td>(Optional) The maximum number of results to return. Default value is 10.</td></tr>
<tr><td>Order</td><td>(Optional) string indicating the order of the results. It can be asc for ascending or desc for descending. Optional, defaults to asc.</td></tr>
<tr><td>Sort By</td><td>(Optional) A string indicating the field to sort based on the columns confident_rating, risk_rating, last_seen, and first_seen.</td></tr>
<tr><td>Start Time</td><td>(Optional) Specify the start date and time till when to retrieve the list of executed reports from Cyble Vision.</td></tr>
<tr><td>End Time</td><td>(Optional) Specify the end date and time till when to retrieve the list of executed reports from Cyble Vision.</td></tr>
</tbody></table>

### operation: Fetch Alerts
#### Input parameters
<table border=1>
<thead>
<tr><th>Parameter</th><th>Description</th></tr></thead>
<tbody>
<tr><td>Company ID</td><td>(Required) Company UUID registered on Cyble Vision used to fetch alert from.</td></tr>
<tr><td>Sort by</td><td>(Optional) The order by which you want to sort the alerts, It cloud be asc, desc .</td></tr>
<tr><td>Start Time</td><td>(Optional) Specify the start date and time from when to retrieve the alerts from Cyble Vision.</td></tr>
<tr><td>End Time</td><td>(Optional) Specify the end date and time till when to retrieve the list of alerts from Cyble Vision.</td></tr>
<tr><td>Severity</td><td>(Optional) Specify the Severity to retrieve the list of alerts from Cyble Vision.</td></tr>
<tr><td>Status</td><td>(Optional) Specify the Status to retrieve the list of alerts from Cyble Vision. it could be multi-selection of VIEWED, UNREVIEWED, CONFIRMED_INCIDENT,  UNDER_REVIEW, INFORMATIONAL.</td></tr>
<tr><td>Service</td><td>(Optional) Specify the service to retrieve the list of alerts from Cyble Vision.</td></tr>
<tr><td>Limit</td><td>(Optional) The maximum number of results to return. Default value is 50.</td></tr>
</tbody></table>

#### Output

 The output contains a non-dictionary value.


### operation: List Advisories
#### Input parameters
<table border=1>
<thead>
<tr><th>Parameter</th><th>Description</th></tr></thead>
<tbody>
<tr><td>From</td><td>(Optional) Specify the start date and time from when to retrieve the advisories from Cyble Vision.</td></tr>
<tr><td>To</td><td>(Optional) Specify the end date and time from when to retrieve the advisories from Cyble Vision.</td></tr>
<tr><td>Sort By</td><td>(Optional) The field to sort the advisories by. Possible values: publish_date.</td></tr>
<tr><td>Order</td><td>(Optional) The order in which advisories should be sorted. Possible values: asc (ascending), desc (descending). Default: desc.</td></tr>
<tr><td>Limit</td><td>(Optional) The maximum number of results to return. Default value is 10.</td></tr>
<tr><td>Page</td><td>(Optional) The page number of the results to retrieve. Default: 1.</td></tr>
<tr><td>Custom Tags</td><td>(Optional) Custom tags to filter advisories. Commas can separate multiple values.</td></tr>
<tr><td>Countries</td><td>(Optional) Countries to filter advisories. Commas can separate multiple values.</td></tr>
<tr><td>Vulnerabilities</td><td>(Optional) Vulnerabilities to filter advisories. Commas can separate multiple values.</td></tr>
</tbody></table>

#### Output

 The output contains a non-dictionary value.


### operation: Get advisory details
#### Input parameters
<table border=1>
<thead>
<tr><th>Parameter</th><th>Description</th></tr></thead>
<tbody>
<tr><td>Advisory ID</td><td>(Required) Advisory ID to get all related details from Cyble Vision.</td></tr>
</tbody></table>

#### Output

 The output contains a non-dictionary value.


### operation: Fetch Companies
#### Input parameters
<table border=1>
<thead>
<tr><th>Parameter</th><th>Description</th></tr></thead>
<tbody>
<tr><td> No inputs needed.</td></tr>
</tbody></table>

#### Output

 The output contains a non-dictionary value.



### operation: Fetch IP Details
#### Input parameters
<table border=1>
<thead>
<tr><th>Parameter</th><th>Description</th></tr></thead>
<tbody>
<tr><td>company Id</td><td>(Required) the Company UUID - Cyble Vision registered companies. you can use Fetch Companies action to get the registred companies IDs. </td></tr>
<tr><td>Address IP</td><td>(Required) the IP address representing the IoC to query for from Cyble Visions in the selected company.</td></tr>
</tbody></table>

#### Output

 The output contains a non-dictionary value.


### operation: Add Comment to Alert
#### Input parameters
<table border=1>
<thead>
<tr><th>Parameter</th><th>Description</th></tr></thead>
<tbody>
<tr><td>Alert ID</td><td>(Required) The unique identifier of the alert for which you want to add comments. </td></tr>
<tr><td>Comment</td><td>(Optional) to  add a new comment. Use this parameter to specify the comment content you want to add to the alert.</td></tr>
</tbody></table>

#### Output

 The output contains a non-dictionary value.

### operation: Fetch CVE Details
#### Input parameters
<table border=1>
<thead>
<tr><th>Parameter</th><th>Description</th></tr></thead>
<tbody>
<tr><td>CVE ID</td><td>(Required) CVE identifier for the specific vulnerability you want to retrieve details for.. </td></tr>
</tbody></table>

#### Output

 The output contains a non-dictionary value.


## Included playbooks
The `Sample - cyble-vision - 2.0.0` playbook collection comes bundled with the Cyble Vision connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the Cyble Vision connector.

- Get IOC Reputation
- Fetch Indicators
- Get advisory Details
- Cyble Vision  > Fetch and Create
- Cyble Vision > Ingest
- Get Indicators

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.
## Data Ingestion Support
Use the Data Ingestion Wizard to easily ingest data into FortiSOAR&trade; by pulling IOC/alerts/incidents, based on the requirement.

**TODO:** provide the list of steps to configure the ingestion with the screen shots and limitations if any in this section.
