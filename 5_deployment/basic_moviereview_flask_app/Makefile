.PHONY: run run-container gcloud-deploy

run:
	@python app.py --server.port=8080 --server.address=127.0.0.1

run-container:
	@docker build . -t app.py
	@docker run -p 8080:8080 app.py

gcloud-deploy:
	@gcloud config set project movie-reviews-313401
	@gcloud app deploy app.yaml --stop-previous-version

