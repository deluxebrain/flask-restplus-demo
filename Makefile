install:
	pipenv install

run:
	# --host=0.0.0.0
	# Listen on all public IP addresses
	pipenv run flask run --host=0.0.0.0

