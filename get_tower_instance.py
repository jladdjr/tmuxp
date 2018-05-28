#!/usr/bin/env python

import os

from jenkinsapi.jenkins import Jenkins

jenkins_url = os.getenv('JENKINS_URL')
jenkins_username = os.getenv('JENKINS_USERNAME')
jenkins_token = os.getenv('JENKINS_TOKEN')
server = Jenkins(jenkins_url, username=jenkins_username, password=jenkins_token)

job_name = os.getenv('JOB_NAME')
build_label = os.getenv('BUILD_LABEL')

def get_latest_matrix_run_for_configuration():
    job = server.get_job(job_name)
    build_ids = sorted([id for id in job.get_build_ids()], reverse=True)

    for id in build_ids:
        build = job.get_build(id)
        matrix_runs = build.get_matrix_runs()
        for run in matrix_runs:
            desc = run.get_description()
            if desc and build_label in desc:
                return run
    return None

def get_inventory_file(run):
    inventory_file = run.get_artifact_dict()['inventory.log']
    return inventory_file.get_data()

def get_tower_hostname(inventory):
    inv = inventory.split('\n')
    for i in range(len(inv)):
        if 'rhel-7.5-x86_64' in inv[i]:
            hostline = inv[i+1]
            break
    else:
        return None
    return hostline.split()[0]


if __name__ == '__main__':
    print('https://tower-hostname')
    """ 
    run = get_latest_matrix_run_for_configuration()
    inventory = get_inventory_file(run)
    hostname = get_tower_hostname(inventory)
    if hostname is None:
        print('notfound')
    else:
        print(hostname)
    """

