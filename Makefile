PREFIX ?= /usr/local
PROJECT=example-platform-app

all: $(PROJECT)

example-app: example-platform-app.c

install: all
	install -D $(PROJECT) $(DESTDIR)/$(PREFIX)/bin/$(PROJECT)

clean:
	$(RM) $(PROJECT)
