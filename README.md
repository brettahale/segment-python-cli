CLI python adapted from https://github.com/bufferapp/segment-config-api/

Install:

    python -m venv venv
    source venv/bin/activate
    python setup.py install
    segapi --help

Design:
    
    segapi -w <workspace> sources list
    segapi -w <workspace> sources get <source_name> 
    segapi -w <workspace> destinations list <source_name>
    segapi -w <workspace> destinations get <source_name> <destination_name>
    segapi -w <workspace> filters list <source_name> <destination_name>
    segapi -w <workspace> filters get <source_name> <destination_name> <filter_name>
    segapi -w <workspace> functions list [--source,-src --destination,-dst]
    segapi -w <workspace> functions get <function_id>
    segapi -w <workspace> regulations create <file_name with userIds>
    segapi -w <workspace> regulations list


Uses:

    segapi -f yaml -p ../data/sources/ -w workspace-sandbox sources get leon_test_python_source
    segapi -w workspace-sandbox sources list | jq -r '.sources[].name| sub("^workspaces/workspace-sandbox/sources/"; "")' | while read -r line; do segapi -f yaml -p ../data/sources/ -w workspace-sandbox sources get $line; done
    segapi -w workspace-sandbox destinations list | jq -r '.sources[].name| sub("^workspaces/workspace-sandbox/sources/"; "")' | while read -r line; do segapi -f yaml -p ../data/sources/ -w workspace-sandbox sources get $line; done