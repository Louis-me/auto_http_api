@ECHO OFF
start winrar x -y requests-2.6.0.tar.gz
ping -n 2 localhost>null
cd requests-2.6.0
python setup.py install
cd ..
start winrar x -y xlrd-1.1.0.tar.gz
ping -n 2 localhost>null
cd xlrd-1.1.0
python setup.py install
cd ..
start winrar x -y XlsxWriter-1.0.5.tar.gz
ping -n 2 localhost>null
cd XlsxWriter-1.0.5
python setup.py install
ECHO.[ EXIT ] 按任意键关闭窗口...
PAUSE>null
@ECHO ON