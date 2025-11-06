@echo off
echo ====================================================
echo Testando arquivo individual com PYTEST
echo ====================================================
pause
python -m pytest service_tag_manager/tests/test_equipment_model.py -v

echo ====================================================
echo Testando o mesmo arquivo com COVERAGE
echo ====================================================
pause
python -m coverage run -m pytest service_tag_manager/tests/test_equipment_model.py -v
python -m coverage report -m
pause
