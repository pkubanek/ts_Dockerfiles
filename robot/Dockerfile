FROM centos:centos7
MAINTAINER Rob Bovill (trekkie2@gmail.com)
ARG USER=appuser
ARG HOME=/home/${USER}

RUN yum -y install epel-release && \
yum -y install python36 python36-devel python36-setuptools && \
yum -y install git which mlocate && \
yum clean all && \
rm -rf /var/cache/yum

RUN updatedb

RUN curl -s http://dl.fedoraproject.org/pub/epel/7/x86_64/Packages/x/xmlstarlet-1.6.1-1.el7.x86_64.rpm --output xmlstarlet-1.6.1-1.el7.x86_64.rpm
RUN yum -y install xmlstarlet-1.6.1-1.el7.x86_64.rpm

RUN groupadd -g 1001 ${USER} && \
useradd -r -u 1001 -g ${USER} -m ${USER}

USER ${USER}

WORKDIR ${HOME}
RUN mkdir bin && mkdir trunk && mkdir Reports

# Apparently Docker does not support variable expansion in the ADD and COPY context.
# ... Therefore, the ownership must be hardcoded.
ADD --chown=1001:1001 Test_Vars.txt ${HOME}/bin/Test_Vars.txt
ADD --chown=1001:1001 bash_profile ${HOME}/.bash_profile
RUN echo 'source ~/.bash_profile' >> ${HOME}/.bashrc

ENV PATH ${HOME}/.local/bin:$PATH
RUN easy_install-3.6 --user pip && \
python3.6 -m pip install --user --upgrade pip setuptools numpy && \
python3.6 -m pip install --user robotframework