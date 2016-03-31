# Optimizely Developer Toolkit

## Set up your development environment
### Clone this repo

```
git clone https://github.com/optimizely/optimizely_dev_tools.git
cd optimizely_dev_tools
```

### Set up your Python virtualenv

```
pip install virtualenv
virtualenv venv
source venv/bin/activate
python setup.py install
```

### Install nvm (Node Version Manager)

```
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.31.0/install.sh | bash
```

## Creating a package

When creating a new package, create a directory specifically for integration development (e.g., `optimizely_integrations/`) and `cd` into that directory. From there, use the following commands to initialize and develop your integration package(s).

### Pre-configured

With the pre-configured command, the `opti` tool will provide you with a fully-functional integration package that you can modify to fit your integration.

```
opti new --default_config -config_type {integration type} -package_name {name of package} 
```

### Unconfigured

With the unconfigured command, the `opti` tool will provide you with scaffolding that does not yet constitute a fully-functional integration package, but which includes in-line comments describing how to flesh out the missing pieces.

```
opti new -config_type {integration type} -package_name {name of package}
```

## Validating a package
```
opti validate {name of package}
```

## Running tests (Python and JavaScript) for a package
```
opti test {name of package}
```

## Tips
* Always activate your virtual environment when running the tool
* Don't hesitate to create an issue under this GitHub repo if you run into issues. We're eager to evolve this tooling!
