# docker build -f portal.dockerfile --platform linux/amd64 -t docker.homejota.net/geoos/portal:latest -t docker.homejota.net/geoos/portal:0.93 .
# docker push docker.homejota.net/geoos/portal:0.93

# FROM node:14-alpine
# FROM ubuntu:18.04
FROM ubuntu

# Install Node.js, Yarn and required dependencies
RUN apt-get update \
  && apt-get install -y curl gnupg build-essential \
  && curl --silent --location https://deb.nodesource.com/setup_14.x | bash - \
  && curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
  && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
  && apt-get remove -y --purge cmdtest \
  && apt-get update \
  && apt-get install -y nodejs yarn python3-pip\
  && pip3 install netCDF4==1.6.5
  && pip3 install geojson==3.1.0 
  # remove useless files from the current layer
  && apt-get install -y wine \
  && rm -rf /var/lib/apt/lists/* \
  && rm -rf /var/lib/apt/lists.d/* \
  && apt-get autoremove \
  && apt-get clean \
  && apt-get autoclean

# RUN apt-get update
# RUN apt-get install -y cmake pkg-config
# RUN apt-get install -y wget

# RUN wget -O- https://apt.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS.PUB \ | gpg --dearmor | tee /usr/share/keyrings/oneapi-archive-keyring.gpg > /dev/null
# RUN echo "deb [signed-by=/usr/share/keyrings/oneapi-archive-keyring.gpg] https://apt.repos.intel.com/oneapi all main" | tee /etc/apt/sources.list.d/oneAPI.list
# RUN apt-get update
# RUN apt-get install -y intel-basekit
# RUN apt-get install -y intel-hpckit

# RUN which cmake pkg-config make gcc g++

# RUN WORKDIR /usr/src/app
# RUN wget "http://zlib.net/$zlib.tar.gz"
# RUN tar -xf "$zlib.tar.gz"
# RUN cd $zlib
# RUN ./configure --prefix=$DIRINSTALL/$zlib || exit 1
# RUN make
# RUN make install
# RUN echo "###### $zlib #########" >> ~/.bashrc
# RUN echo "ZLIB=$DIRINSTALL/$zlib" >> ~/.bashrc
# RUN echo 'export PATH=$PATH:$ZLIB/lib:$ZLIB/include' >> ~/.bashrc
# RUN echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ZLIB/lib' >> ~/.bashrc
# RUN echo >> ~/.bashrc

EXPOSE 8090
WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install --production

COPY . .
CMD ["node", "index"]