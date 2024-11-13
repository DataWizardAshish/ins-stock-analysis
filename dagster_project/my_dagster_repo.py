from dagster import repository

<<<<<<< HEAD
from jobs.my_job import my_job  # No change required as 'jobs' is already in 'src/'
=======
from jobs.my_job import my_job  # No change required as 'jobs' already in 'src/'
>>>>>>> e4c1299ed3d03b7dd0e783b2b769d3dfc1d9383b


@repository
def my_dagster_repo():
    return [my_job]
