build:
	 python setup.py sdist bdist_wheel
upload:
	twine upload  dist/*
clean:
	rm -rf build dist  py2factor.egg-info

.PHONY:	build upload clean