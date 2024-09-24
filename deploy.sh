#!/bin/bash

gcloud functions deploy tutorial \
--gen2 \
--region=asia-northeast2 \
--runtime=python312 \
--entry-point=todo \
--trigger-http \
--allow-unauthenticated \
--env-vars-file .env.yaml