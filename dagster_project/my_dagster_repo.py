from dagster import repository

from jobs.my_job import my_job  # No change required as 'jobs' is already in 'src/'


@repository
def my_dagster_repo():
    return [my_job]
