## Notes

Got it to run finally with this command

```
(venv) ➜  SMARTS git:(comp-1) ✗ scl run --envision examples/single_agent.py scenarios/sumo/loop --sumo-port=8082
```

Screenshot taken for reference

environment variable is set as follows:

```
export SUMO_HOME=export SUMO_HOME=/home/cksash/Documents/proj/SMARTS/venv/lib/python3.7/site-packages/sumo
```

First I install python 3.7

`sudo apt-get install python3.7`

Then I created a venv with python3.7

`virtualenv -p python3.7 venvname`

Then I started running the main setup steps in the readme

Then i built the scenario with the command given, and then ran it with the
command above


