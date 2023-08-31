#!/bin/bash

curl -L \
-X POST \
-H "Accept: application/vnd.github+json" \
-H "Authorization: Bearer <ACCESS TOKEN>" \
-H "X-GitHub-Api-Version: 2022-11-28" \
https://api.github.com/repos/danyalmck/chrold/actions/workflows/train-latest.yml/dispatches \
-d '{"ref":"main","inputs":{}}'