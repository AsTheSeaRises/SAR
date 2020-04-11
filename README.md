## Summary:
This application creates an API Gateway (http), a Lambda function and a Kinesis data stream.

## Purpose:
By POSTing to the API endpoint using fields in the following format -  {"create":"<integer value 1-100>"}, the lambda function will generate that amount of simulated financial transactions, including fake names, IP addresses and countries and place them into a Kinesis data stream using the name given during application launch.

The format of these records are JSON formatted as show in this example:

{
  "AccountNum": "19111696",
  "EventTime": "2020-04-11 16:51:55.583480",
  "Name": "Linda Hansen",
  "IP_Address": "10.75.221.39",
  "TransactionID": "JL6c5g9EUKtFTl0C",
  "Amount": "58",
  "Country": "Serbia"
}

You can tweak the shape and schema of the records in the lambda function if needed, or just read from the Kinesis stream to simulate how your analytics tools, ML pipeline or applications would handle this type of traffic.

## Usage:
You can curl from the terminal. Use the endpoint URL found in the CloudFormation Output tab for the key: ServerlessHttpApi

The example below generates 3 transactions
curl -v https://your_API_ID.execute-api.eu-west-2.amazonaws.com/?create=3

Alternatively you can use Postman to test this.

To view these events you can tail your Kinesis logs using Lumigo for example.
https://www.npmjs.com/package/lumigo-cli#lumigo-cli-tail-kinesis