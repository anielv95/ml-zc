settings:
	git config --global user.email ${GITEMAIL}
	git config --global user.name ${GITNAME}

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt