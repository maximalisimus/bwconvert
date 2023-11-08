DESTDIR=./
POSTDIR=usr/share
INSTALLDIR=/
TARGET=bwconvert
SRC=bwconvert
SCRIPT=bwconvert.py
SYMLINK=bwconvert
LICENSEFILE=LICENSE
READMEFILE=README.md
SETUPDIR=$(DESTDIR)$(POSTDIR)/$(TARGET)
EXEC=$(INSTALLDIR)$(POSTDIR)/$(TARGET)/$(SCRIPT)
SETUPBIN=$(DESTDIR)usr/bin/$(SYMLINK)
#
DESCENG="Converter from Bitwarden json to csv for KeePassXC."
DESCRU="Конвертер для Bitwarden из json в csv для KeePassXC."
#
.PHONY: all install uninstall clear
all: install
	echo "Installation complete!"

install:
	rm -rf $(SETUPDIR)
	mkdir -p $(SETUPDIR) $(DESTDIR)usr/bin/
	install -Dm 755 $(SRC)/$(SCRIPT) $(SETUPDIR)/
	install -Dm 755 $(LICENSEFILE) $(SETUPDIR)/
	install -Dm 755 $(READMEFILE) $(SETUPDIR)/
	ln -s $(EXEC) $(SETUPBIN) 2>/dev/null
	chmod +x $(SETUPDIR)/$(SCRIPT) 2>/dev/null

uninstall:
	rm -rf $(SETUPDIR)
	rm -rf $(SETUPBIN)

clear: uninstall
	echo "Uninstal complete!"
