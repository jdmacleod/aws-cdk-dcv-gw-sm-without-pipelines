#!/usr/bin/env python3

import aws_cdk as cdk

from aws_cdk_nice_dcv_linux.aws_cdk_nice_dcv_linux_stack import AwsCdkNiceDcvLinuxStack


app = cdk.App()
AwsCdkNiceDcvLinuxStack(app, "AwsCdkNiceDcvLinuxStack")

app.synth()
