import aws_cdk as core
import aws_cdk.assertions as assertions
from aws_oapi3.aws_oapi3_stack import AwsOapi3Stack


def test_sqs_queue_created():
    app = core.App()
    stack = AwsOapi3Stack(app, "aws-oapi3")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::SQS::Queue", {
        "VisibilityTimeout": 300
    })


def test_sns_topic_created():
    app = core.App()
    stack = AwsOapi3Stack(app, "aws-oapi3")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::SNS::Topic", 1)
