# Cloud-One-Conformity-SNS-to-Google-Chat-Webhook
## Solution Overview

This CloudFormation stack configures the required resources (SNS, KMS, Lambda) to send Cloud Conformity notifications through to Google Chat incoming-webhooks.

### Services leveraged
- AWS CloudFormation
- AWS IAM
- AWS KMS
- AWS Lambda using Python 3.8 Runtime
- AWS SNS

## Getting Started

### Prerequisites

Information / access you need to install the solution

  1. Access to Google Chat 'Manage Incoming Webhooks' feature
  2. Administrator or Power User access to Cloud One Conformity.
  3. Access to AWS and write permissions to the following services: CloudFormation, IAM, SNS, Lambda, KMS

## Deployment

### Deployment Steps
  1. Log into Google Chat and create an incoming webhook in your desired channel (Channel Settings -> Manage Webhooks -> Add Webhook). Copy the Webhook URL to your clipboard as you will need this in the following steps. 
  2. Log into the AWS Account you plan on running the stack in and open the CloudFormation Service. Select "Create Stack".
  3. Under the specify template section select "Upload a template file" and upload the provided template file and select Next. Give the stack a name and fill in the WebhookUrl parameter which the URL you copied in step 1. Click next and acknowledge the creation of IAM resources. Click Create Stack and wait for create complete status.
  4. Once the stack creation completes, browse to the "Outputs" tab and copy down the ARN of the resulting SNS Topic.
  5. Log into Conformity and navigate to the communication settings page for the account you wish to setup the webhook for. Select "Amazon SNS" as the communication channel type.
  6. Select your desired triggers eg: Status "Failure", Risk level: Extreme, Very high, High and click Save.
  7. Select 'Configure Now...' to set the Amazon SNS Topic. Paste in the value you copied from the Cloudformation output tabs. Ensure there are no leading or trailing spaces and select save.
  8. Turn on either Automatic or Manual notifications and the webhook setup is now complete.

## Authors

* **Tom Ryan** - *Initial work* - [TomRyan-321](https://github.com/TomRyan-321)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## For more information about Trend Micro Cloud One & Cloud One Conformity visit:

* [CloudConformity Official Website](https://www.cloudconformity.com)
* [Trend Micro Cloud One](https://www.trendmicro.com/en_us/business/products/hybrid-cloud.html)
