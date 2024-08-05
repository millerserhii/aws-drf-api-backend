

terraform-init:
	@export $(shell cat .env | xargs)
	@cd terraform && terraform init

terraform-apply:
	@export $(shell cat .env | xargs)
	@cd terraform && terraform apply -auto-approve

terraform-plan:
	@export $(shell cat .env | xargs)
	@cd terraform && terraform plan

build-run:
	@export $(shell cat .env | xargs)
	@docker build -t $(DOCKER_IMAGE) --build-arg PORT=$(APP_CONTAINER_PORT) .
	@docker run -p $(APP_HOST_PORT):$(APP_CONTAINER_PORT) $(DOCKER_IMAGE)
