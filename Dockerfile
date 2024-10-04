# Use the base image
FROM bitgo/express:latest

# Ensure we are running as root to install dependencies
USER root

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libtool \
    autotools-dev \
    automake \
    pkg-config \
    bsdmainutils \
    python3 \
    git \
    && rm -rf /var/lib/apt/lists/*

# Clone and install secp256k1
RUN git clone https://github.com/bitcoin-core/secp256k1.git && \
    cd secp256k1 && \
    ./autogen.sh && \
    ./configure --enable-module-recovery && \
    make && \
    make install && \
    ldconfig

# Set environment variables
ENV NODE_ENV=production
ENV BITGO_ENV=production
ENV LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH

# Expose port 4000
EXPOSE 4000

# Command to run the BitGo Express server
CMD ["bitgo-express", "-p", "4000", "-k", "/private/cert.key", "-c", "/private/cert.crt"]
