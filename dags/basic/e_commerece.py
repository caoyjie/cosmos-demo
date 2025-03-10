from datetime import datetime

from cosmos import DbtDag, ProjectConfig

from include.profiles import athena
from include.constants import e_commerece_shop_path, venv_execution_config

simple_dag = DbtDag(
    # dbt/cosmos-specific parameters
    project_config=ProjectConfig(e_commerece_shop_path),
    profile_config=athena,
    execution_config=venv_execution_config,
    # normal dag parameters
    schedule_interval="@daily",
    start_date=datetime(2025, 3, 10),
    catchup=False,
    dag_id="e_commerece_dag",
    tags=["simple"],
)

