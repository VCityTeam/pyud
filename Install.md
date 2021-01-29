## Install
```
python3 -m pip install git+https://github.com/VCityTeam/pyud.git
```
and uninstalling goes
```
python3 -m pip uninstall -y pyud        # No confirmation asked
```
Quick importation check
```
python3 -c "import ud"
```

## For developers
## Setting up the development context
```
$ git clone https://github.com/VCityTeam/pyud.git
$ cd pyud
$ virtualenv -p python3 venv
$ . venv/bin/activate
(venv)$ pip install -r requirements.txt      # Installs pyud
```

### For direnv adepts
If you happen to use the [direnv](https://github.com/direnv/direnv) utility
you can make this directory direnv aware by
 1. patch you shell-rc file to use direnv with 
    e.g. `echo 'eval "$(direnv hook bash)"' >> ~/.bashrc`
 
 2. marking the directory as using direnv
    ```
    $ git clone https://github.com/VCityTeam/pyud.git
    $ ls venv    # Make sure this directory holds the virtual environment
    $ ln -s .envrc.tpl .envrc
    $ direnv allow
    (venv)
    ```

## Running the examples
```
(venv) cd `git rev-parse --show-toplevel`/examples
(venv) python FIXME
```
