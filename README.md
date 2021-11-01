CLI python adapted from https://github.com/bufferapp/segment-config-api/

Install:

    python -m venv venv
    source venv/bin/activate
    python setup.py install
    segapi --help

Design:
    
    segapi -w <workspace> sources --list,-ls
    segapi -w <workspace> sources --get,-g <source_name> 
    segapi -w <workspace> destinations --list,-ls <source_name>
    segapi -w <workspace> destinations --get,-g <source_name> <destination_name>
    segapi -w <workspace> filters --list,-ls <source_name> <destination_name>
    segapi -w <workspace> filters --get,-g <source_name> <destination_name> <filter_name>
    segapi -w <workspace> functions --list,-ls [--source,-src --destination,-dst]
    segapi -w <workspace> functions --get,-g <function_id>


Uses:

    segapi -f yaml -p ../data/sources/ -w workspace-sandbox sources get leon_test_python_source
    segapi -w workspace-sandbox sources list | jq -r '.sources[].name| sub("^workspaces/workspace-sandbox/sources/"; "")' | while read -r line; do segapi -f yaml -p ../data/sources/ -w workspace-sandbox sources get $line; done
    segapi -w workspace-sandbox destinations list | jq -r '.sources[].name| sub("^workspaces/workspace-sandbox/sources/"; "")' | while read -r line; do segapi -f yaml -p ../data/sources/ -w workspace-sandbox sources get $line; done