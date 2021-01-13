import json
import os
import urllib3

http = urllib3.PoolManager()


def handler(event, context):
    url = os.environ["WEBHOOK_URL"]
    text = event["Records"][0]["Sns"]["Message"]
    if event["Records"][0]["Sns"]["Message"] != "Test Message from Cloud Conformity":
        msg = json.loads(event["Records"][0]["Sns"]["Message"])
        message = msg["message"]
        ruletitle = msg["ruleTitle"]
        kburl = msg["resolutionPageUrl"]
        risk = msg["riskLevel"]
        region = msg["region"]
        resource = msg["resource"]
        provider = msg["provider"].upper()
        providerid = msg["cloudProviderId"]
        text = f"""<b>{message}</b>
<a href=\"{kburl}\">Rule: {ruletitle}</a>
A new violation has been introduced on cloud account: <b>{provider} {providerid}</b>

<b>Risk level: {risk}</b>
<b>Region: {region}</b>
<b>Resource: {resource}</b>"""
    webhookbody = {
        "cards": [{"sections": [{"widgets": [{"textParagraph": {"text": text}}]}]}]
    }
    encoded_msg = json.dumps(webhookbody).encode("utf-8")
    resp = http.request("POST", url, body=encoded_msg)
    return {
        "message": event["Records"][0]["Sns"]["Message"],
        "encoded_msg": encoded_msg,
        "status_code": resp.status,
        "response": resp.data,
    }
