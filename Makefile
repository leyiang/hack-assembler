run:
	python main.py ./asm-example/Add.asm ./tests/Add.hack

debug:
	python debug.py ./asm-example/Add.asm

edit:
	nvim main.py