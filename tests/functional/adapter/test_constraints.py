import pytest
from dbt.tests.util import relation_from_name
from dbt.tests.adapter.constraints.test_constraints import (
    BaseConstraintsColumnsEqual,
    BaseConstraintsRuntimeEnforcement
)

_expected_sql_snowflake = """
create or replace transient table {0} (
    id integer not null primary key ,
    color text ,
    date_day date
) as (
    select
        1 as id,
        'blue' as color,
        cast('2019-01-01' as date) as date_day
);
"""

class TestSnowflakeConstraintsColumnsEqual(BaseConstraintsColumnsEqual):
    pass


class TestSnowflakeConstraintsRuntimeEnforcement(BaseConstraintsRuntimeEnforcement):
    @pytest.fixture(scope="class")
    def expected_sql(self, project):
        relation = relation_from_name(project.adapter, "my_model")
        return _expected_sql_snowflake.format(relation)

    @pytest.fixture(scope="class")
    def expected_error_messages(self):
        return ["NULL result in a non-nullable column"]
