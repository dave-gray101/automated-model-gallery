# Readme Rump State

### Dave's Junk Drawer
Not currently needed but it may come back.
```
def load_yaml_file_to_config(path: Path):
    with open(path, "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            raise ValueError("invalid path")
```