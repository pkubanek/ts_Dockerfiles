FROM lsstts/develop-env:20190610_sal3.10.0_salobj3.12.0

USER saluser
WORKDIR /home/saluser/repos

WORKDIR /home/saluser
COPY setup.sh /home/saluser/.setup.sh

ENTRYPOINT ["/bin/bash", "--"]
CMD ["/home/saluser/.setup.sh"]
