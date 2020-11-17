#!/usr/bin/env python3

from aws_cdk import core

from stacks.cloudFront_stack import CloudFrontStack


app = core.App()
CloudFrontStack(app, "cloudFront")

app.synth()
