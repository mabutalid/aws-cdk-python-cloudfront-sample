from aws_cdk import (
    aws_s3 as s3, 
    aws_cloudfront as cloudfront, 
    aws_cloudfront_origins as origins,
    aws_iam as iam, 
    core
)

# cloudfront stack/resource/construct wont work when you specifiy a region for it


class CloudFrontStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        bucket = s3.Bucket(self, 'cloudfronttestbucket', 
            bucket_name="testcloudfrontbuckettoday",
            public_read_access=False,
            removal_policy=core.RemovalPolicy.DESTROY,
        )

        s3identity = cloudfront.OriginAccessIdentity(self, 'accessidentity', comment="access-identity-")

        s3Origin = origins.S3Origin(
            bucket = bucket,
            origin_access_identity = s3identity
        )

        current_behavior = cloudfront.BehaviorOptions(
            origin = s3Origin,
            viewer_protocol_policy = cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS
        )

        skull_distribution = cloudfront.Distribution(self, 'skulldistibution', 
            default_behavior = current_behavior
        )

        bucket.grant_read(identity=s3identity.grant_principal)
