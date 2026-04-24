

## Tasks

### Compile requirements.txt

```shell {#compile-requirements}
uv pip compile pyproject.toml \
    --format requirements.txt \
    --no-annotate \
    --no-header \
    --no-strip-extras \
    --no-strip-markers \
    --python-platform linux \
    # --offline \
    > requirements.txt
```
