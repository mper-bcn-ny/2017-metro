PROJECT=gh-pages-$(shell basename $$(pwd))
WEBSITE=https://mper-bcn-ny.github.io/$(PROJECT)
GITHUB_REPO=https://github.com/mper-bcn-ny/$(PROJECT)
GITHUB_TOKEN=~/Encfs/credentials/github-tokens/martinvirtel-public_repo

dev-server: 
	. $(GITHUB_TOKEN) ; \
	bundle exec jekyll serve 2>&1 > /tmp/$(PROJECT) & 
	tail -f /tmp/$(PROJECT) & 
	sleep 5 ; xdg-open $$(sed -n '/Server address:/s/^[^:]*://p' </tmp/$(PROJECT)) & 
	read n  && fuser -k -TERM /tmp/$(PROJECT)


view-website:
	xdg-open $(WEBSITE)


view-repo:
	xdg-open $(GITHUB_REPO)


push :
	git push
