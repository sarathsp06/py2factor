build:
	 python setup.py sdist bdist_wheel
rtegister:
	twine register dist/project_name-x.y.z.tar.gz
	twine register dist/mypkg-0.1-py2.py3-none-any.whl
.PHONY:
	build upload

