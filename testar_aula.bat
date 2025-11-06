@echo off
echo ====================================================
echo 🧪 ETAPA 1 - Executando testes unitarios com PYTEST
echo ====================================================
pause
python -m pytest --cache-clear -v

echo.
echo ====================================================
echo ✅ Testes executados! Agora vamos rodar com COVERAGE
echo ====================================================
pause
python -m coverage run -m pytest -v

echo.
echo ====================================================
echo 📊 ETAPA 2 - Exibir relatorio de cobertura no terminal
echo ====================================================
pause
python -m coverage report -m

echo.
echo ====================================================
echo 🌐 ETAPA 3 - Gerar relatorio HTML visual
echo ====================================================
pause
python -m coverage html

echo.
echo ====================================================
echo 🚀 Relatorio HTML gerado em: htmlcov/index.html
echo Abra no navegador para visualizar a cobertura completa.
echo ====================================================
pause
