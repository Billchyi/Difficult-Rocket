Set-Location .\libs\Difficult_Rocket_rs\src

python3.8 setup.py build
python3.9 setup.py build
python3.11 setup.py build

python3.8 after_build.py

Set-Location ..\..\..\
