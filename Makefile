compile:
	docker build -t django_project_template:build -f docker/Dockerfile --target build . \
	&& docker run -v $$PWD:/project/app --rm django_project_template:build pip-compile --generate-hashes
