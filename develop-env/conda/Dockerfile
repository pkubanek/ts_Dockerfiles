FROM centos:7
ARG PYTHON_VERSION=3.7m
ARG CONDA_VERSION=4.5.4
USER root
RUN yum install -y mlocate
RUN adduser -u 1004 -m -s /bin/bash saluser
RUN yum install -y gcc-c++ make ncurses-libs xterm xorg-x11-fonts-misc java-1.7.0-openjdk-devel maven python-devel swig git tk-devel wget bzip2
COPY lsst-ts.repo /tmp/lsst-ts.repo
RUN cat /tmp/lsst-ts.repo >> /etc/yum.conf && yum install -y OpenSpliceDDS-6.9.0-1
USER saluser
WORKDIR /home/saluser
ENV LSST_SDK_INSTALL=/home/saluser/repos/ts_sal
ENV OSPL_HOME=/opt/OpenSpliceDDS/V6.9.0/HDE/x86_64.linux
ENV LSST_DDS_DOMAIN=citest
ENV PYTHON_BUILD_VERSION=${PYTHON_VERSION}
ENV PYTHON_BUILD_LOCATION=/home/saluser/miniconda3
ENV TS_IDL_DIR=/home/saluser/repos/ts_idl/
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh && chmod +x miniconda.sh && ./miniconda.sh -b
RUN source ~/miniconda3/bin/activate && conda install -c lsstts python=3.7 ts-salobj cython
ARG sal_branch=v3.10.0
RUN mkdir repos && cd repos && git clone https://github.com/lsst-ts/ts_sal \ 
    && cd ts_sal && git checkout ${sal_branch} && chmod -R +x bin.src
RUN source ~/miniconda3/bin/activate && mkdir dds && cd dds && \
tar xvzf /opt/OpenSpliceDDS/V6.9.0/HDE/x86_64.linux/tools/python-support.tgz && cd python/src \
&& source ~/repos/ts_sal/setup.env && python setup.py install
ARG xml_branch=v3.10.2
RUN cd repos && git clone https://github.com/lsst-ts/ts_xml && cd ts_xml \ 
    && git checkout ${xml_branch}
RUN cd repos && git clone https://github.com/lsst-ts/ts_idl
COPY setup.sh /home/saluser/.setup.sh
ENTRYPOINT ["/bin/bash", "--"]
CMD ["/home/saluser/.setup.sh"]