# Optimizely Developer Toolkit

## Installing
```
git clone https://github.com/optimizely/optimizely_dev_tools.git
cd optimizely_dev_tools
virtualenv venv
source venv/bin/activate
python setup.py install
```

## Creating a package
### Pre-configured
```
opti new --default_config -config_type {integration type} -package_name {name of package} 
```

### Unconfigured
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
