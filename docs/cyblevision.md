## About the connector
Cyble Threat Intel that enables users to access and enrich Indicators of Compromise (IOCs) from Cyble's TAXII Feed service within their environment.
<p>This document provides information about the Cyble Vision Connector, which facilitates automated interactions, with a Cyble Vision server using FortiSOAR&trade; playbooks. Add the Cyble Vision Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Cyble Vision.</p>

### Version information

Connector Version: 2.0.0

Contributor: ABelkhiri

Authored By: Fortinet

Certified: No
## Release Notes for version 2.0.0
Following enhancements have been made to the Cyble Vision Connector in version 2.0.0:
<ul>
<li>Introduced <code>IOC</code>, <code>Order By</code> and <code>Sort By</code> parameters into the <code>Fetch Indicators</code> operation.</li>
<li>Removed <code>Offset</code> parameter from <code>Fetch Indicators</code> operation.</li>
<li>Introduced <code>Company ID</code>, <code>Severity</code>, <code>Service</code> and <code>Status</code> parameters into the <code>Fetch Alerts</code> operation.</li>
<li>Removed <code>Offset</code> and <code>Priority</code> parameters from <code>Fetch Alerts</code> operation.</li>
<li>Removed <code>Fetch Event Detail</code> operation.</li>
<li><p>Added the new following actions and playbooks:</p>

<ul>
<li>List Advisories</li>
<li>Get Advisory Details</li>
<li>Fetch All Users for a Company</li>
<li>Fetch IP Details</li>
<li>Add Comment to Alert</li>
<li>Fetch CVE Details</li>
</ul></li>
</ul>

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
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>Specify the URL of the Cyble Vision server to which you will connect and perform automated operations.
</td>
</tr><tr><td>Token</td><td>Specify the token used to access the Cyble Vision server to which you will connect and perform the automated operations.
</td>
</tr><tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set to True.</td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Fetch Indicators</td><td>Retrieves a list of indicators from Cyble Vision based on the input parameters you have specified.</td><td>fetch_indicators <br/>Investigation</td></tr>
<tr><td>Fetch Alerts</td><td>Retrieves a list of alerts from Cyble Vision based on the company ID, and other parameters you have specified.</td><td>fetch_alerts <br/>Investigation</td></tr>
<tr><td>List Advisories</td><td>Retrieves a list of advisories from Cyble Vision based on the input parameters you have specified.</td><td>list_advisories <br/>Investigation</td></tr>
<tr><td>Get Advisory Details</td><td>Retrieves specific advisory details from Cyble Vision based on the advisory ID you have specified.</td><td>get_advisory_details <br/>Investigation</td></tr>
<tr><td>Fetch All Users for a Company</td><td>Retrieves a list of all users for an company from Cyble Vision.</td><td>fetch_companies <br/>Investigation</td></tr>
<tr><td>Fetch IP Details</td><td>Retrieve detailed information about an IP address from Cyble Vision server.</td><td>fetch_ip_details <br/>Investigation</td></tr>
<tr><td>Add Comment to Alert</td><td>Add a comment to a specific alert in the Cyble Vision server.</td><td>add_comment_to_alert <br/>Utilities</td></tr>
<tr><td>Fetch CVE Details</td><td>Retrieve the specific common vulnerability and exposure (CVE) details from Cyble Vision.</td><td>fetch_cve_details <br/>Investigation</td></tr>
</tbody></table>

### operation: Fetch Indicators
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>IOC</td><td>Specify a value for the IOC to query in Cyble Vision.
</td></tr><tr><td>Indicator Type</td><td>Select the indicator type based on which you want to filter the indicators retrieved from Cyble Vision. You can choose from the following options: Domain, FileHash-MD5, FileHash-SHA1, FileHash-SHA256, IPv4, IPv6, URL, or Email.
</td></tr><tr><td>Start Time</td><td>Specify the starting DateTime from when you want to retrieve indicators from Cyble Vision.
</td></tr><tr><td>End Time</td><td>Specify the ending DateTime till when you want to retrieve indicators from Cyble Vision.
</td></tr><tr><td>Order By</td><td>Select an option in which to order the indicators retrieved. You can choose from Ascending or Descending. By default, this option is set as Ascending.
</td></tr><tr><td>Sort By</td><td>Select an option in which to sort the indicators retrieved. You can choose from the following options: Confident Rating, Risk Rating, Last Seen, or First Seen. By default, this option is set as First Seen.
</td></tr><tr><td>Limit</td><td>Specify the maximum number of results this operation should return, per page, in the response. By default, this value is set to 10.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "data": {
        "data": {
            "iocs": [
                {
                    "ioc": "",
                    "sources": [],
                    "ioc_type": "",
                    "last_seen": "",
                    "first_seen": "",
                    "risk_score": "",
                    "behaviour_tags": [],
                    "is_whitelisted": "",
                    "target_regions": [],
                    "related_malware": [],
                    "target_countries": [],
                    "confidence_rating": "",
                    "target_industries": [],
                    "related_threat_actors": ""
                }
            ],
            "pagination": {
                "page": "",
                "limit": "",
                "total_count": ""
            }
        },
        "success": ""
    }
}</pre>

### operation: Fetch Alerts
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Company ID</td><td>Specify a ID (UUID) of the company to filter the list of alerts retrieved from Cyble Vision.
</td></tr><tr><td>Order By</td><td>Select an option in which to order the alerts retrieved. You can choose from Ascending or Descending. By default, this option is set as Descending.
</td></tr><tr><td>Start Time</td><td>Specify the starting DateTime from when you want to retrieve alerts from Cyble Vision.
</td></tr><tr><td>End Time</td><td>Specify the ending DateTime till when you want to retrieve alerts from Cyble Vision.
</td></tr><tr><td>Severity</td><td>Select multiple severity using which you want to retrieve alerts from Cyble Vision. You can specify the following values: LOW, MEDIUM, or HIGH.
</td></tr><tr><td>Status</td><td>Select multiple status using which you want to retrieve alerts from Cyble Vision. You can specify the following values: VIEWED, UNREVIEWED, CONFIRMED_INCIDENT, UNDER_REVIEW, or INFORMATIONAL.
</td></tr><tr><td>Service</td><td>Select the service using which you want to retrieve alerts from Cyble Vision. You can specify the following values: Data Breaches, Ransomware Forum Mentions, Compromised Endpoints, etc. By default, this option is set as Data Breaches.
</td></tr><tr><td>Limit</td><td>Specify the maximum number of results this operation should return, per page, in the response. By default, this value is set to 50.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "data": {
        "data": [
            {
                "id": "",
                "hash": "",
                "tags": {
                    "data": []
                },
                "status": "",
                "data_id": "",
                "service": "",
                "archived": "",
                "metadata": {
                    "entity": {
                        "wallet": "",
                        "keyword": {
                            "id": "",
                            "tag_name": "",
                            "bucket_id": "",
                            "company_id": "",
                            "created_at": "",
                            "updated_at": "",
                            "display_name": ""
                        },
                        "website": "",
                        "software": "",
                        "entity_id": "",
                        "entity_type": "",
                        "watermarking_website": ""
                    }
                },
                "severity": "",
                "created_at": "",
                "deleted_at": "",
                "risk_score": "",
                "updated_at": "",
                "assignee_id": "",
                "description": "",
                "archive_date": "",
                "user_severity": "",
                "alert_group_id": "",
                "assignment_date": ""
            }
        ],
        "cached": "",
        "success": "",
        "ids_error": [],
        "additional_data": ""
    }
}</pre>

### operation: List Advisories
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>From DateTime</td><td>Specify the starting DateTime from when you want to retrieve advisories from Cyble Vision.
</td></tr><tr><td>To DateTime</td><td>Specify the ending DateTime till when you want to retrieve advisories from Cyble Vision.
</td></tr><tr><td>Sort By</td><td>Select this option (default is selected) to sort the advisories from Cyble Vision. Possible values: publish_date.
</td></tr><tr><td>Sort Order</td><td>Select an option in which to sort the advisories retrieved. You can choose from Ascending or Descending. By default, this option is set as Descending.
</td></tr><tr><td>Limit</td><td>Specify the maximum number of results this operation should return, per page, in the response. By default, this value is set to 10.
</td></tr><tr><td>Page</td><td>Index of the first item to be returned by this operation. This parameter is useful if you want to get a subset of records, say advisories starting from the 10th advisories. By default, this is set as 1.
</td></tr><tr><td>Custom Tags</td><td>Specify a comma-separated list of custom tags using which you want to filter advisories in Cyble Vision.
</td></tr><tr><td>Countries</td><td>Specify a comma-separated list of countries using which you want to filter advisories in Cyble Vision.
</td></tr><tr><td>Vulnerabilities</td><td>Specify a comma-separated list of vulnerabilities using which you want to filter advisories in Cyble Vision.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "data": {
        "data": {
            "reports": [
                {
                    "id": "",
                    "tags": {
                        "regions": [],
                        "countries": [],
                        "customTags": [],
                        "industries": [],
                        "vulnerabilities": []
                    },
                    "title": "",
                    "status": "",
                    "classified": "",
                    "risk_score": "",
                    "tlp_rating": "",
                    "publish_date": ""
                }
            ],
            "pagination": {
                "page": "",
                "total": "",
                "items_per_page": ""
            }
        },
        "success": ""
    }
}</pre>

### operation: Get Advisory Details
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Advisory ID</td><td>Specify the ID of the advisory for which you want to retrieve details from Cyble Vision.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.

### operation: Fetch All Users for a Company
#### Input parameters
None.

#### Output
The output contains the following populated JSON schema:

<pre>{
    "data": {
        "data": [
            {
                "uuid": "",
                "displayName": ""
            }
        ],
        "meta": {},
        "success": ""
    }
}</pre>

### operation: Fetch IP Details
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Company ID</td><td>Specify a ID (UUID) of the company based on which you want to retrieve IP details from Cyble Vision.
</td></tr><tr><td>IP Address</td><td>Specify a IP address based on which you want to retrieve details from Cyble Vision.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.

### operation: Add Comment to Alert
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Alert ID</td><td>Specify the alert ID for the specific alert where you would like to add a comment in Cyble Vision.
</td></tr><tr><td>Comment</td><td>Specify the comment you would like to add to the alert in Cyble Vision.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "data": {
        "data": {
            "uuid": "",
            "alertId": "",
            "content": "",
            "createdAt": "",
            "createdBy": "",
            "updatedAt": "",
            "parentCommentId": ""
        },
        "meta": {},
        "success": ""
    }
}</pre>

### operation: Fetch CVE Details
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>CVE ID</td><td>Specify the CVE ID for which you want to retrieve details from Cyble Vision.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "data": {
        "data": {
            "cve": {
                "data_type": "",
                "references": {
                    "reference_data": [
                        {
                            "url": "",
                            "name": "",
                            "tags": [],
                            "refsource": ""
                        }
                    ]
                },
                "data_format": "",
                "description": {
                    "description_data": [
                        {
                            "lang": "",
                            "value": ""
                        }
                    ]
                },
                "problemtype": {
                    "problemtype_data": [
                        {
                            "description": [
                                {
                                    "lang": "",
                                    "value": ""
                                }
                            ]
                        }
                    ]
                },
                "data_version": "",
                "CVE_data_meta": {
                    "ID": "",
                    "ASSIGNER": ""
                }
            },
            "impact": {
                "baseMetricV2": {
                    "cvssV2": {
                        "version": "",
                        "baseScore": "",
                        "accessVector": "",
                        "vectorString": "",
                        "authentication": "",
                        "integrityImpact": "",
                        "accessComplexity": "",
                        "availabilityImpact": "",
                        "confidentialityImpact": ""
                    },
                    "severity": "",
                    "acInsufInfo": "",
                    "impactScore": "",
                    "obtainAllPrivilege": "",
                    "exploitabilityScore": "",
                    "obtainUserPrivilege": "",
                    "obtainOtherPrivilege": "",
                    "userInteractionRequired": ""
                },
                "baseMetricV3": {
                    "cvssV3": {
                        "scope": "",
                        "version": "",
                        "baseScore": "",
                        "attackVector": "",
                        "baseSeverity": "",
                        "vectorString": "",
                        "integrityImpact": "",
                        "userInteraction": "",
                        "attackComplexity": "",
                        "availabilityImpact": "",
                        "privilegesRequired": "",
                        "confidentialityImpact": ""
                    },
                    "impactScore": "",
                    "exploitabilityScore": ""
                }
            },
            "publishedDate": "",
            "configurations": {
                "nodes": [
                    {
                        "children": [],
                        "operator": "",
                        "cpe_match": [
                            {
                                "cpe23Uri": "",
                                "cpe_name": [],
                                "vulnerable": "",
                                "versionEndExcluding": "",
                                "versionStartIncluding": ""
                            }
                        ]
                    }
                ],
                "CVE_data_version": ""
            },
            "lastModifiedDate": "",
            "ImpactVersionDetails": ""
        },
        "success": ""
    }
}</pre>
## Included playbooks
The `Sample - Cyble Vision - 2.0.0` playbook collection comes bundled with the Cyble Vision connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the Cyble Vision connector.

- Cyble Vision  > Fetch and Create
- Add Comment to Alert
- Cyble Vision > Ingest
- Fetch Alerts
- Fetch CVE Details
- Fetch All Users for a Company
- Fetch IP Details
- Fetch Indicators
- File Hash / Domain / IP / URL > Cyble Vision Threat Intelligence > Enrichment
- Get Advisory Details
- List Advisories

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.
## Data Ingestion Support
Use the Data Ingestion Wizard to easily ingest data into FortiSOAR&trade; by pulling events/alerts/incidents, based on the requirement.

**TODO:** provide the list of steps to configure the ingestion with the screen shots and limitations if any in this section.