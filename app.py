#!/usr/bin/env python3

import aws_cdk as cdk

from aws_oapi3.aws_oapi3_stack import AwsOapi3Stack


app = cdk.App()
AwsOapi3Stack(app, "aws-oapi3")

app.synth()
