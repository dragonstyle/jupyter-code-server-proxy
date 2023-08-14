import setuptools
from os import path


# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setuptools.setup(
    name="jupyter-code-server-proxy",
    version='0.1.0',
    url="https://github.com/dragonstyle/jupyter-code-server-proxy",
    author="Charles Teague",
    description="charles@posit.co",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
	keywords=['jupyter', 'VSCode', 'jupyterhub'],
	classifiers=['Framework :: Jupyter'],
    install_requires=[
        'jupyter-server-proxy>=1.5.0'
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            'code-server = jupyter_code-server_proxy:setup_code-server',
        ]
    },
    package_data={
        'jupyter_code-server_proxy': ['icons/vscode.svg'],
    },
)
