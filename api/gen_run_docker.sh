#!/bin/bash
docker-compose build
docker-compose up -d --force-recreate
docker-compose logs -f api
