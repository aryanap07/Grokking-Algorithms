#!/usr/bin/env python3
import os
import sys
import subprocess

root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
examples = []
for dirpath, dirnames, filenames in os.walk(root):
    # skip this tests folder and hidden directories
    if os.path.basename(dirpath).startswith('.') or 'tests' in dirpath.split(os.sep):
        continue
    # Only include files in chapter folders
    if 'Chapter' not in dirpath:
        continue
    for fn in filenames:
        if fn.endswith('.py'):
            examples.append(os.path.join(dirpath, fn))

if not examples:
    print('No example Python files found.')
    sys.exit(0)

failures = []
for ex in sorted(examples):
    print('\nRunning', ex)
    proc = subprocess.run([sys.executable, ex], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode != 0:
        print('FAILED:', ex)
        print(proc.stdout.decode())
        print(proc.stderr.decode())
        failures.append(ex)
    else:
        print('OK:', ex)

if failures:
    print('\nFailures:', len(failures))
    for f in failures:
        print('-', f)
    sys.exit(2)

print('\nAll examples ran successfully.')
