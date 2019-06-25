FROM lsstts/develop-env:20190610_sal3.10_salobj3.12 

WORKDIR /home/saluser/repos
RUN cd ts_config_attcs && git pull

WORKDIR /home/saluser
COPY setup.sh /home/saluser/.setup.sh

ENTRYPOINT ["/bin/bash", "--"]
CMD ["/home/saluser/.setup.sh"]
