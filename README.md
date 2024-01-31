[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=aleandre6579_testing-warmup&metric=coverage)](https://sonarcloud.io/summary/new_code?id=aleandre6579_testing-warmup)

[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=aleandre6579_testing-warmup&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=aleandre6579_testing-warmup)

## Setup Instruction
```
poetry install
```

## Run Test
```
poetry run pytest
```

## What to do next

### Install Pre-commit (Recommended)
```
poetry run pre-commit install
```
If you wish to edit pre-commit behavior see ```.pre-commit-config.yaml```.
Normally it checks only the file you are committing. But if you wish to run it manually for all files do
```
poetry run pre-commit run --all
```
