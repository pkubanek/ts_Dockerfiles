FROM lsstts/develop-env:sal_v4.0.0_salobj_v5.0.0

LABEL maintainer Tiago Ribeiro <tribeiro@lsst.org>

USER saluser

WORKDIR /home/saluser/repos
RUN git clone https://github.com/lsst-ts/ts_dimm.git

WORKDIR /home/saluser/repos/ts_dimm
#RUN git fetch && git checkout "tags/v0.2.0" -b "v0.2.0"
RUN git fetch && git checkout "tickets/DM-21423"

WORKDIR /home/saluser

RUN source /opt/lsst/software/stack/loadLSST.bash && setup lsst_distrib && \
    source /home/saluser/repos/ts_sal/setup.env && \
    setup ts_sal -t current && \
    make_idl_files.py Environment DIMM

WORKDIR /home/saluser/repos/ts_config_ocs
RUN git fetch --all && git checkout tickets/DM-22531
RUN source /opt/lsst/software/stack/loadLSST.bash && setup lsst_distrib && \
    source /home/saluser/repos/ts_sal/setup.env && \
    eups declare -r . -t current


WORKDIR /home/saluser/repos/ts_dimm
RUN source /opt/lsst/software/stack/loadLSST.bash && setup lsst_distrib && \
    source /home/saluser/repos/ts_sal/setup.env && \
    setup ts_salobj -t current && \
    setup ts_sal -t current && \
    setup ts_config_ocs -t current && \
    eups declare -r . ts_dimm -t current && setup ts_dimm -t current && \
    scons

ENV CSC_INDEX=1

WORKDIR /home/saluser/
COPY setup.sh /home/saluser/.setup.sh

ENTRYPOINT ["/bin/bash", "--"]
CMD ["/home/saluser/.setup.sh"]
