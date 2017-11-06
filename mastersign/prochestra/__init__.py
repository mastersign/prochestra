import subprocess
import datetime

VERSION = '1.0.0'


class Procestra(object):

    def __init__(self, log=None, log_prefix="PROCHESTRA ", silent=False):
        self.log_file = log
        self.log_prefix = log_prefix
        self.silent = silent
        self.state = {}

    def info(self, text, *args):
        if self.log_file:
            ts = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            print(ts + ' ' + self.log_prefix + text.format(*args),
                  file=self.log_file, flush=True)

    def run(self, job_list):
        jobs = job_list['jobs']
        self.state = dict.fromkeys(list(map(lambda j: j['id'], jobs)), None)
        for job in jobs:
            job_id = job['id']
            dependencies = job['dependencies'] if 'dependencies' in job else []
            if not all(map(lambda dep: self.state[dep] if dep in self.state else None, dependencies)):
                self.info("{} SKIPPED", job_id)
                continue
            cmd = job['cmd']
            args = job['args'] if 'args' in job else []
            self.info("{} STARTED", job_id)
            p = subprocess.run([cmd] + args, shell=True,
                               stderr=subprocess.DEVNULL if self.silent else self.log_file,
                               stdout=subprocess.DEVNULL if self.silent else self.log_file)
            self.state[job_id] = p.returncode == 0
            if p.returncode != 0:
                print("Procestra: job '{}' exited with code {}.".format(job_id, p.returncode))
                self.info("{} FAILED WITH CODE {}.", job_id, p.returncode)
            else:
                self.info("{} FINISHED", job_id)

        return all(self.state.values())
