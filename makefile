make:	pyuic.py
		python -m PyQt5.uic.pyuic -x test.ui -o test.py
		python test.py

e: hom.py
		python hom.py


file: pyuic.py
		python -m PyQt5.uic.pyuic -x file.ui -o file.py
		python file.py

file_w: pyuic.py
	python -m PyQt5.uic.pyuic -x file_widget.ui -o file_widget.py
	python file_widget.py

memo_w: pyuic.py
	python -m PyQt5.uic.pyuic -x memo_widget.ui -o memo_widget.py
	python memo_widget.py

chat_w: pyuic.py
	python -m PyQt5.uic.pyuic -x chat_widget.ui -o chat_widget.py
	python chat_widget.py


chat_test: pyuic.py
	python -m PyQt5.uic.pyuic -x chat_widget_test.ui -o chat_widget_test.py
	python chat_widget_test.py

server: study.pem
	ssh -i "study.pem" ubuntu@ec2-13-124-206-87.ap-northeast-2.compute.amazonaws.com

ftpdown: ftp_download.py
	python ftp_download.py

l:	line_check.py
		python line_check.py
