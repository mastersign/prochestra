from argparse import ArgumentParser, FileType
import json

from mastersign.prochestra import VERSION, Procestra

parser = ArgumentParser(prog='prochestra')
parser.add_argument('jobfile', type=FileType('r', encoding='UTF-8'),
                    help="A path to a JSON file with the job list.")
parser.add_argument('--log', '-l', type=FileType('a', encoding='UTF-8'),
                    help="A path to a log file to write the output to.")
parser.add_argument('--silent', '-s', action='store_true',
                    help="Dismiss the output of the executed processes.")
parser.add_argument('--version', '-v', action='version', version=VERSION)
args = parser.parse_args()

with args.jobfile as job_file:
    jobs = json.load(job_file)

runner = Procestra(log=args.log, silent=args.silent)
result = runner.run(jobs)

exit(0 if result else 1)
