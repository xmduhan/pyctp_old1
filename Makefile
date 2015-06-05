
all : generate


generate: channel.py CTPStruct.py examples.py query_api_tests.py


channel.py : template/channel.py.tpl
	python generate.py channel.py.tpl


CTPStruct.py : template/CTPStruct.py.tpl
	python generate.py CTPStruct.py.tpl


examples.py : template/examples.py.tpl
	python generate.py examples.py.tpl


query_api_tests.py : template/query_api_tests.py.tpl
	python generate.py query_api_tests.py.tpl


clean :
	touch template/*
	rm *.pyc *.pk
