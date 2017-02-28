PROJECT=gh-pages-$(shell basename $$(pwd))
WEBSITE=https://mper-bcn-ny.github.io/$(PROJECT)
GITHUB_REPO=https://github.com/mper-bcn-ny/$(PROJECT)

dev-server: 
	bundle exec jekyll serve 2>&1 > /tmp/$(PROJECT) & 
	sleep 5 ; xdg-open $$(sed -n '/Server address:/s/^[^:]*://p' </tmp/$(PROJECT)); echo Hit 'Enter' to stop server & 
	tail -f /tmp/$(PROJECT) & 
	read n; kill -TERM $$(fuser /tmp/$(PROJECT))


view-website:
	xdg-open $(WEBSITE)


view-repo:
	xdg-open $(GITHUB_REPO)


push :
	git push
