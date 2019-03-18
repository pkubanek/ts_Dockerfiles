FROM queue-env:latest

LABEL maintainer Tiago Ribeiro <tribeiro@lsst.org>

USER saluser

WORKDIR /home/saluser
COPY pub_telemetry.py /home/saluser/pub_telemetry.py

WORKDIR /home/saluser/repos/fake_telemetry
RUN source /opt/lsst/software/stack/loadLSST.bash && setup lsst_distrib && \
    source /home/saluser/repos/ts_sal/setup.env && \
    setup ts_sal -t $USER && \
    make_salpy_libs.py ATMCS ATPneumatics

WORKDIR /home/saluser/
COPY setup.sh /home/saluser/.setup.sh
