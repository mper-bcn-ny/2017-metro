PROJECT=gh-pages-$(shell basename $$(pwd))


dev-server: 
	bundle exec jekyll serve 2>&1 > /tmp/$(PROJECT) & 
	sleep 5 ; xdg-open $$(sed -n '/Server address:/s/^[^:]*://p' </tmp/$(PROJECT)); echo Hit 'Enter' to stop server & 
	tail -f /tmp/$(PROJECT) & 
	read n; kill -TERM $$(fuser /tmp/$(PROJECT))




push :
	git push
