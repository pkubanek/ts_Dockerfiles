echo "#"
echo "# Loading LSST Stack"
. /opt/lsst/software/stack/loadLSST.bash
setup lsst_distrib
echo "#"
echo "# Loading sal environment"
. ~/repos/ts_sal/setup.env
echo "#"
echo "# Setting up sal, salobj and scriptqueue"

setup ts_xml -t current
setup ts_sal -t current
setup ts_idl -t current
setup ts_salobj -t current

python ~/repos/ts_linearStage/scripts/linear_stage_csc.py /dev/ttyUSB0 1 1
