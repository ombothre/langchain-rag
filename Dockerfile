FROM ubuntu:22.04

RUN apt-get update && apt-get install -y curl sudo
RUN curl -fsSL https://ollama.com/install.sh | sh

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 11434
ENTRYPOINT ["/entrypoint.sh"]
