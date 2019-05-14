FROM lsstts/develop-env:20190418

MAINTAINER Andres Anania <aanania@lsst.org>

USER saluser

WORKDIR /home/saluser/repos
ENV TSREPOS=/home/saluser/repos

RUN git clone https://github.com/lsst-ts/pythonFileReader.git -b develop
RUN git clone https://github.com/lsst-ts/pythonFitsfile.git -b develop
RUN git clone https://github.com/lsst-ts/pythonCommunicator.git -b develop
RUN git clone https://github.com/lsst-ts/ts_electrometer2.git -b tickets/DM-18674

RUN source /opt/lsst/software/stack/loadLSST.bash && setup lsst_distrib && \
    cd ${TSREPOS}/pythonFileReader && \
    pip install . && \
    cd ${TSREPOS}/pythonCommunicator && \
    pip install . && \
    cd ${TSREPOS}/pythonFitsfile && \
    pip install . && \
    setup ts_xml -t current && \
    setup ts_sal -t current && \
    conda install -y -c conda pyqt && \
    conda install -y -c conda pyqtgraph && \
    eups declare -r ${TSREPOS}/ts_electrometer2 ts_electrometer git -t current && \
    source ${TSREPOS}/ts_sal/setup.env && \
    make_salpy_libs.py Electrometer

WORKDIR /home/saluser/

COPY setup.sh /home/saluser/.setup.sh
