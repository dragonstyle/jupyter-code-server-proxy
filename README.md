# jupyter-code-server-proxy

This package was built using the [`jupyter-server-proxy` cookiecutter template](https://github.com/illumidesk/cookiecutter-jupyter-server-proxy).

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/dragonstyle/jupyter-code-server-proxy/main?urlpath=code-server)

## Requirements

- [Python 3.6+](https://www.python.org/downloads/)
- [Jupyter Notebook 6.0+](https://pypi.org/project/notebook/)
- [JupyterLab 2.1+](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html)

(Optional) For testing:

- [Docker](https://docs.docker.com/get-docker/)
- [docker-compose](https://docs.docker.com/compose/install/)

This package executes the standard `code-server` command. This command assumes the `code-server` command is available in the environment's `PATH`. For convenience, the tests include cases that assert outputs when running the `code-server` command from a docker container. If you don't need to run tests with this setup running in a docker container, then remove the `tests/test_code-server_docker.py` file or comment out the code in the file.

## Quick Starts

### Launch with `binder`

This test requires you to have a database instance available as a public endpoint or installed within the notebook container itself.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/illumidesk/jupyter-code-server-proxy/main?urlpath=code-server)

## The Hard Way

### Create and Activate Environment

```bash
virtualenv -p python3 venv
source venv/bin/activate
```

### Install jupyter-code-server-proxy

```bash
pip install git+https://github.com/dragonstyle/jupyter-code-server-proxy.git
```

### Enable jupyter-code-server-proxy Extensions

1. For Jupyter Classic, activate the `jupyter-server-proxy` extension:

```bash
jupyter serverextension enable --sys-prefix jupyter_server_proxy
```

2. For Jupyter Lab, install the `@jupyterlab/server-proxy` extension:

```bash
jupyter labextension install @jupyterlab/server-proxy
jupyter lab build
```

3. Start Jupyter Classic or Jupyter Lab

4. Click on the `code-server` icon from the Jupyter Lab Launcher or the `code-server` item from the `New` dropdown in Jupyter Classic.

## Credits

- [`jupyter-server-proxy`](https://github.com/jupyterhub/jupyter-server-proxy)

## License

BSD 3-Clause
