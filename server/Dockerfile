# build stage
FROM python:3.10-slim as build

# set workdir
ARG APP_HOME=/server/
WORKDIR ${APP_HOME}

# install pipenv
RUN pip install --no-cache poetry

# copy dep files
COPY poetry.lock pyproject.toml ${APP_HOME}

# development stage
FROM build as development

# install dependencies
RUN poetry install

# copy project files
COPY ./ ${APP_HOME}

# production stage
FROM build as production

# install dependencies (ignore development deps)
RUN poetry install --without test

# copy project files
COPY ./ ${APP_HOME}