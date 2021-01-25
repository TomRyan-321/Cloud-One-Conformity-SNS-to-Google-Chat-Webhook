import json
import os
import urllib3

http = urllib3.PoolManager()
url = os.environ["WEBHOOK_URL"]


def handler(event, context):

    if event["Records"][0]["Sns"]["Message"] == "Test Message from Cloud Conformity":
        webhooktext = event["Records"][0]["Sns"]["Message"]
    else:
        msg = json.loads(event["Records"][0]["Sns"]["Message"])
        if msg["status"] != "FAILURE":
            webhooktext = "SUCCESS check message received, please check your Conformity SNS Communication Channels settings are set to send only FAILURE notifcations"
        else:
            message = msg["message"]
            ruletitle = msg["ruleTitle"]
            kburl = msg["resolutionPageUrl"]
            risk = msg["riskLevel"]
            region = msg["region"]
            provider = msg["provider"].upper()
            providerid = msg["cloudProviderId"]
            webhooktext = f"""<b>{message}</b>
<a href=\"{kburl}\">Rule: {ruletitle}</a>
A new violation has been introduced on cloud account: <b>{provider} {providerid}</b>

<b>Risk level: {risk}</b>
<b>Region: {region}</b>
"""
            try:
                msg["resource"]
            except KeyError:
                print("No resource id included")
            else:
                resource = msg["resource"]
                webhooktext += f"""<b>Resource: {resource}</b>
"""
            try:
                msg["link"]
            except KeyError:
                print("No link to resource included")
            else:
                resourceurl = msg["link"]
                webhooktext += f"""
<a href=\"{resourceurl}\">View Resource</a>"""

    webhookbody = {
        "cards": [
            {"sections": [{"widgets": [{"textParagraph": {"text": webhooktext}}]}]}
        ]
    }
    encoded_msg = json.dumps(webhookbody).encode("utf-8")
    resp = http.request("POST", url, body=encoded_msg)
    print(
        {
            "message": event["Records"][0]["Sns"]["Message"],
            "encoded_msg": encoded_msg,
            "status_code": resp.status,
            "response": resp.data,
        }
    )
