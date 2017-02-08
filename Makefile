NAME ?= python

image:
	docker build -t $(NAME) .

publish: image
	docker tag $(NAME) $(REPO)/$(NAME)
	docker push $(REPO)/$(NAME)
