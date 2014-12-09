git pull
python setup.py sdist --format=zip
rm ../../downloads/dist/UNEP-*
mv dist/*.zip ../../pypi_local/
