"Contains profile mappings used in the project"

from cosmos import ProfileConfig
from cosmos.profiles import PostgresUserPasswordProfileMapping
from cosmos.profiles import AthenaAccessKeyProfileMapping

airflow_db = ProfileConfig(
    profile_name="airflow_db",
    target_name="dev",
    profile_mapping=PostgresUserPasswordProfileMapping(
        conn_id="airflow_metadata_db",
        profile_args={"schema": "dbt"},
    ),
)
athena=ProfileConfig(
    profile_name="e_commerece",
    target_name="dev",
    profile_mapping=AthenaAccessKeyProfileMapping(
        conn_id="aws_athena_conn",
        profile_args={
            "schema":"test",
            "s3_staging_dir":"s3://cyj-athena-query-results/airflow/",
            "region_name":"us-east-1",
            "database":"AwsDataCatalog"
        }
    )
)