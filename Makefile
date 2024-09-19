clean:
	@find . -name "*.pyc" -exec rm -rf {} \;
	@find . -name "__pycache__" -delete
	@find . -name ".vscode" -type d -exec rm -rf {} \; 2>/dev/null
	@find . -name ".idea" -type d -exec rm -rf {} \; 2>/dev/null
	@find . -name ".pytest_cache" -type d -exec rm -rf {} \; 2>/dev/null


run-tests:
	@echo 'Running tests...'
	pytest -v --color=yes
