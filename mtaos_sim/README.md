# MT AOS Software Simulation Environment

*This is the software environment for the MT AOS software simulator.*

## Overview
This docker is based off the lsstts/mtaos_dev image with everything required to
run the MT AOS software.

## Instructions
- *LSST_DDS_DOMAIN*
    - The default is **mtaos**
    - To change this utilize *-e LSST_DDS_DOMAIN='**NEWDOMAIN**'*
- sudo docker run -it --net host --rm -u root lsstts/mtaos_sim:v0.2
- Just run *run_mtaos.py* from command line.

## Tag List
- *v0.3*
    - *python* - (ver: 3.7.2)
    - *ts_sal* - master branch (commit: ac2ca6b)
    - *ts_xml* - develop branch (commit: 994918f)
    - *ts_opensplice* - master branch (commit: dba3466) using OpenSpliceDDS v6.9.0
    - *ts_config_ocs* - develop branch (commit: 0da9278)
    - *ts_config_mttcs* - develop branch (commit: 0efe216)
    - *ts_salobj* - master branch (commit: 4fea586)
    - *ts_MTAOS* - master branch (commit: d018609)
- *v0.2*
    - *python* - (ver: 3.7.2)
    - *ts_sal* - master branch (commit: ac2ca6b)
    - *ts_xml* - master (commit: db3b535)
    - *ts_opensplice* - master branch (commit: dba3466) using OpenSpliceDDS v6.4.1
    - *ts_config_ocs* - develop branch (commit: 0da9278)
    - *ts_config_mttcs* - develop branch (commit: 0efe216)
    - *ts_salobj* - master branch (commit: 4fea586)
- *v0.1*
    - *python* - (ver: 3.6.7)
    - *ts_sal* - develop branch (commit: 10d2039e33031f9d10ecd4fef776e25f99eb79a2)
    - *ts_xml* - develop branch (commit: e644c6b7d1a8dec77ae7fa2e1db92118b1d05893)
    - *ts_opensplice* - master branch (commit: d0661fb) using OpenSpliceDDS v6.4.1
    - *ts_salobj* - master branch (commit: abfecf20819721c021980dd9abde7189d9edd743)
