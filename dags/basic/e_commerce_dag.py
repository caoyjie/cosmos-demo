from datetime import datetime

from airflow import DAG
from cosmos import DbtDag, ProjectConfig

from include.profiles import athena  # 或 athena，取决于你的配置
from include.constants import e_commerece_shop_path, venv_execution_config # 或 e_commerece_shop_path

e_commerce_dag_test = DbtDag(
    # dbt/cosmos-specific parameters
    project_config=ProjectConfig(e_commerece_shop_path),
    profile_config=athena,
    execution_config=venv_execution_config,
    # normal dag parameters
    schedule_interval="@daily",
    start_date=datetime(2024, 3, 11),
    catchup=False,
    dag_id="e_commerce_dag",
    tags=["simple"],
)
