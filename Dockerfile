# Dockerfile

# FROM directive instructing base image to build upon
FROM python:2-onbuild

# COPY startup script into known file location in container
COPY start.sh /start.sh
COPY Corpus.csv /Corpus.csv

# EXPOSE port 8000 to allow communication to/from server
EXPOSE 8000

# CMD specifcies the command to execute to start the server running.
CMD ["/start.sh"]
# done!
