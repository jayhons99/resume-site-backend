# backend-python

This project contains src files and resources to deploy a serverless workflow with API Gateway, Lambda, and DynamoDB. It is also continously deployed to AWS using Github Actions CI/CD

Source code was initialized using a Serverless Application Model (SAM) template. The YAML template configures all the necessary resources that is needed for the project's backend.

To build:

`sam build`

To deploy:

`sam deploy --guided`
