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


#### Output

{
  "data": {
    "data": {
      "iocs": [
        {
          "ioc": "",
          "sources": [],
          "ioc_type": "IPv4",
          "last_seen": 1727586486,
          "first_seen": 1601164800,
          "risk_score": 70,
          "behaviour_tags": [],
          "is_whitelisted": false,
          "target_regions": [],
          "related_malware": [],
          "target_countries": [ ],
          "confidence_rating": "",
          "target_industries": [],
          "related_threat_actors": null
        }
      ],
      "pagination": {
        "page": 1,
        "limit": 1,
        "total_count": 1
      }
    },
    "success": true
  }
}  

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

{
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
        "archived": null,
        "metadata": {
          "entity": {
            "wallet": null,
            "keyword": {
              "id": 71581,
              "tag_name": "",
              "bucket_id": 1289,
              "company_id": 252,
              "created_at": "",
              "updated_at": "",
              "display_name": ""
            },
            "website": null,
            "software": null,
            "entity_id": 71581,
            "entity_type": 0,
            "watermarking_website": null
          }
        },
        "severity": "",
        "created_at": "",
        "deleted_at": null,
        "risk_score": null,
        "updated_at": "",
        "assignee_id": null,
        "description": null,
        "archive_date": null,
        "user_severity": "",
        "alert_group_id": "2",
        "assignment_date": null
      }
    ],
    "cached": false,
    "success": true,
    "ids_error": [],
    "additional_data": null
  }
}



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

{
  "data": {
    "data": {
      "reports": [
        {
          "id": 0,
          "tags": {
            "regions": [],
            "countries": [
              "Spain",
              "Portugal"
            ],
            "customTags": [],
            "industries": [],
            "vulnerabilities": []
          },
          "title": "",
          "status": "",
          "classified": 0,
          "risk_score": "",
          "tlp_rating": "",
          "publish_date": ""
        }
      ],
      "pagination": {
        "page": "2",
        "total": 338,
        "items_per_page": "20"
      }
    },
    "success": true
  }
}


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


<p> No inputs needed.</p>


#### Output

{
  "data": {
    "data": [
      {
        "uuid": "",
        "displayName": ""
      },
      {
        "uuid": "",
        "displayName": ""
      },
      {
        "uuid": "",
        "displayName": ""
      }
    ],
    "meta": {},
    "success": true
  }
}



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

{
  "data": {
    "data": {
      "uuid": "",
      "alertId": "",
      "content": "",
      "createdAt": "",
      "createdBy": "",
      "updatedAt": null,
      "parentCommentId": null
    },
    "meta": {},
    "success": true
  }
}

### operation: Fetch CVE Details
#### Input parameters
<table border=1>
<thead>
<tr><th>Parameter</th><th>Description</th></tr></thead>
<tbody>
<tr><td>CVE ID</td><td>(Required) CVE identifier for the specific vulnerability you want to retrieve details for.. </td></tr>
</tbody></table>

#### Output

{
  "data": {
    "data": {
      "cve": {
        "data_type": "CVE",
        "references": {
          "reference_data": [
            {
              "url": "",
              "name": "N/A",
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
                  "lang": "en",
                  "value": ""
                }
              ]
            }
          ]
        },
        "data_version": "",
        "CVE_data_meta": {
          "ID": "CVE-2020-2020",
          "ASSIGNER": ""
        }
      },
      "impact": {
        "baseMetricV2": {
          "cvssV2": {
            "version": "",
            "baseScore": 2.1,
            "accessVector": "LOCAL",
            "vectorString": "",
            "authentication": "",
            "integrityImpact": "",
            "accessComplexity": "",
            "availabilityImpact": "",
            "confidentialityImpact": ""
          },
          "severity": "",
          "acInsufInfo": false,
          "impactScore": 2.9,
          "obtainAllPrivilege": false,
          "exploitabilityScore": 3.9,
          "obtainUserPrivilege": false,
          "obtainOtherPrivilege": false,
          "userInteractionRequired": false
        },
        "baseMetricV3": {
          "cvssV3": {
            "scope": "",
            "version": "",
            "baseScore": 5.5,
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
          "impactScore": 3.6,
          "exploitabilityScore": 1.8
        }
      },
      "publishedDate": "",
      "configurations": {
        "nodes": [
          {
            "children": [],
            "operator": "OR",
            "cpe_match": [
              {
                "cpe23Uri": "",
                "cpe_name": [],
                "vulnerable": true,
                "versionEndExcluding": "",
                "versionStartIncluding": ""
              }
            ]
          }
        ],
        "CVE_data_version": ""
      },
      "lastModifiedDate": "",
      "ImpactVersionDetails": null
    },
    "success": true
  }
}


## Included playbooks
The `Sample - cyble-vision - 2.0.0` playbook collection comes bundled with the Cyble Vision connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the Cyble Vision connector.

- Get IOC Reputation
- Fetch Alert
- Add Comment to alert
- Get advisory Details
- Fetch IP details
- List Of Advisories
- Fetch Companies
- Fetch CVE details
- File Hash / Domain / IP / URL > Cyble Vision Threat Intelligence > Enrichment
- Cyble Vision  > Fetch and Create
- Cyble Vision > Ingest


**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.
## Data Ingestion Support
Use the Data Ingestion Wizard to easily ingest data into FortiSOAR&trade; by pulling IOC/alerts/incidents, based on the requirement.

**TODO:** provide the list of steps to configure the ingestion with the screen shots and limitations if any in this section.
