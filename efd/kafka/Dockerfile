FROM lsstts/develop-env:20190610_sal3.10.0_salobj3.12.0

LABEL maintainer Tiago Ribeiro <tribeiro@lsst.org>

USER root

RUN yum install -y librdkafka-devel

USER saluser

COPY make_efd_writter.sh /home/saluser/repos/ts_sal/bin/

WORKDIR /home/saluser/repos/ts_sal/test

RUN git fetch --all && git checkout "tickets/DM-20529_2"

RUN source /opt/lsst/software/stack/loadLSST.bash && setup lsst_distrib && \
    source /home/saluser/repos/ts_sal/setup.env && \
    setup ts_sal -t current && \
    for COMP in Test ; do make_efd_writter.sh $COMP; done && \
    echo "source ${LSST_SDK_INSTALL}/lsstsal/scripts/genkafkaefd.tcl ; updatekafkaschema" | tclsh

WORKDIR ${HOME}
