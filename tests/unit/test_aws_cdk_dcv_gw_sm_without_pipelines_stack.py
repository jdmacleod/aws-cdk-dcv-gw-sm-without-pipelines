import aws_cdk as core
import aws_cdk.assertions as assertions

from stacks.dcv_gw_sm_infra import DcvInfra


def test_sqs_queue_created():
    app = core.App()
    stack = DcvInfra(app, "aws-cdk-dcv-gw-sm-without-pipelines")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::SQS::Queue", {"VisibilityTimeout": 300})


def test_sns_topic_created():
    app = core.App()
    stack = DcvInfra(app, "aws-cdk-dcv-gw-sm-without-pipelines")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::SNS::Topic", 1)
