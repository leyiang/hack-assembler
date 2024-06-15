run:
	python main.py ./asm-example/PongL.asm ./tests/PongL.hack

debug:
	python debug.py ./asm-example/Add.asm

edit:
	nvim main.py