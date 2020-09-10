#
# NOTE: THIS DOCKERFILE IS GENERATED VIA "update.sh"
#
# PLEASE DO NOT EDIT IT DIRECTLY.
#

FROM alpine:3.12

# ensure local python is preferred over distribution python
ENV PATH /usr/local/bin:$PATH

# http://bugs.python.org/issue19846
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks Python 3*, and that's not OK.
ENV LANG C.UTF-8

# install ca-certificates so that HTTPS works consistently
# other runtime dependencies for Python are installed later
RUN apk add --no-cache ca-certificates

ENV GPG_KEY E3FF2839C048B25C084DEBE9B26995E310250568
ENV PYTHON_VERSION 3.8.5

RUN set -ex \
	&& apk add --no-cache --virtual .fetch-deps \
		gnupg \
		tar \
		xz \
		findutils \
		python3 \
		git

ARG motdpath=motd
ARG destdir=/usr/local/${motdpath}/
ARG http_port=10001

EXPOSE ${http_port}
RUN mkdir -p /usr/local/${motdpath}
# 'COPY' does not copy the source directory itself;;;
COPY ${motdpath} ${destdir}

# do not use 'RUN cd [..]'
WORKDIR ${destdir}
CMD ["python3", "./motd.py"]

