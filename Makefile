run:
	python main.py ./asm-example/Rect.asm ./tests/RectL.hack

debug:
	python debug.py ./asm-example/Add.asm

edit:
	nvim main.py