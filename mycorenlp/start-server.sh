#!/usr/bin/env bash

TIMEOUT=5000

for PORT in {9000..9009} ; do
    nohup java -cp "$CORENLP_HOME/*" \
            edu.stanford.nlp.pipeline.StanfordCoreNLPServer \
            -port $PORT \
            -timeout $TIMEOUT > /dev/null &
done
