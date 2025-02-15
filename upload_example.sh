#! /bin/bash

cd /app/trunking_recorder_upload
python3 trunking_recorder_upload.py -a "${1}" -s "${2}"
status=$?

# Exit with 0 status, even if there is an error.
if [ $status -ne 0 ]; then
    echo "Error with python script, exit status: $status"
    exit 0
else
    exit 0
fi