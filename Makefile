PROJECT=gh-pages-$(shell basename $$(pwd))


dev-server: 
	bundle exec jekyll serve 2>&1 > /tmp/$(PROJECT) &
	sleep 5 ; xdg-open $$(sed -n '/Server address:/s/^[^:]*://p' </tmp/$(PROJECT)) &
	tail -f /tmp/$(PROJECT) &
	echo Hit Any Key to restart dev server; read n; kill -TERM $$(fuser /tmp/$(PROJECT))


push :
	git push
