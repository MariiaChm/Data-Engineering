import os
import time
import requests


BASE_DIR = os.getcwd()

JOB1_PORT = '8081'
JOB2_PORT = '8082'

dt = '2022-08-09'

RAW_DIR = os.path.join(BASE_DIR, "file_storage", "raw", "sales", dt)
STG_DIR = os.path.join(BASE_DIR, "file_storage", "stg", "sales", dt)


def run_job1():
    print("Starting job1:")
    resp = requests.post(
        url='http://localhost:{}/'.format(JOB1_PORT),
        json={
            "date": dt,
            "raw_dir": RAW_DIR
        }
    )
    assert resp.status_code == 200
    print("job1 completed!")


def run_job2():
    print("Starting job2:")
    resp = requests.post(
        url=f'http://localhost:{JOB2_PORT}/',
        json={
            "raw_dir": RAW_DIR,
            "stg_dir": STG_DIR
        }
    )
    assert resp.status_code == 200
    print("job2 completed!")


if __name__ == '__main__':
    run_job1()
    time.sleep(3)
    run_job2()
