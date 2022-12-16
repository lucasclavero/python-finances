.DEFAULT_GOAL := help
SHELL = /bin/sh

build: ## (Re)build dockerfiles.
	docker-compose build

generate: ## Generate PDF
	docker-compose run python python /app/invoice-generator/invoice_generator.py

shell: ## Python shell
	docker-compose run python /bin/sh

# todo: consider this https://gist.github.com/prwhite/8168133
help: ## Show this help.
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
