FROM lsstts/develop-env:20190610_sal3.10.0_salobj3.12.0

WORKDIR /home/saluser/repos/ts_config_attcs
RUN git fetch && git checkout develop

WORKDIR /home/saluser
COPY setup.sh /home/saluser/.setup.sh

ENTRYPOINT ["/bin/bash", "--"]
CMD ["/home/saluser/.setup.sh"]
