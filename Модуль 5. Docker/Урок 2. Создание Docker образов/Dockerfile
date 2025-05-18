FROM debian

LABEL maintainer="Alex M <avm@sh-inc.ru>"
LABEL version="1.0"
LABEL description="Python 3.11.11 with Poetry 1.9.0 and pip 23.2.1"
LABEL org.opencontainers.image.source="source"
LABEL org.opencontainers.image.documentation="documentation"
LABEL org.opencontainers.image.licenses="MIT"
LABEL org.opencontainers.image.authors="Alex M <avm@sh-inc.ru>"
LABEL org.opencontainers.image.url="https://test.com"
LABEL org.opencontainers.image.vendor="Test"
LABEL org.opencontainers.image.title="Test"
LABEL org.opencontainers.image.description="Test"
LABEL org.opencontainers.image.created="2023-10-01T00:00:00Z"
LABEL org.opencontainers.image.revision="1.0"
LABEL org.opencontainers.image.version="1.0"
LABEL org.opencontainers.image.base.name="python:3.11.11-alpine3.21"
LABEL org.opencontainers.image.base.url="https://hub.docker.com/_/python"
LABEL org.opencontainers.image.base.version="3.11.11-alpine3.21"
LABEL org.opencontainers.image.base.description="Python 3.11.11 with Poetry 1.9.0 and pip 23.2.1"
LABEL org.opencontainers.image.base.license="MIT"
LABEL org.opencontainers.image.base.authors="Alex M <avm@sh-inc.ru>"
LABEL org.opencontainers.image.base.url="https://test.com"
LABEL org.opencontainers.image.base.documentation="documentation"
LABEL org.opencontainers.image.base.source="source"
LABEL org.opencontainers.image.base.vendor="Test"
LABEL org.opencontainers.image.base.title="Test"
LABEL org.opencontainers.image.base.description="Test"
LABEL org.opencontainers.image.base.created="2023-10-01T00:00:00Z"
LABEL org.opencontainers.image.base.revision="1.0"

COPY ./scripts.sh /

RUN chmod +x /scripts.sh

CMD ["/scripts.sh"]
