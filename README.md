install an x server if you use wsl to get an Display to open for this exampel firefox 
install VcXsrv on Windows 

# Starten Sie VcXsrv:
# - Öffnen Sie VcXsrv vom Startmenü oder über die Verknüpfung auf Ihrem Desktop.
# - Wählen Sie bei der Konfiguration "Multiple windows" und setzen Sie die Display-Nummer auf -1. Klicken Sie auf "Next".
# -Wählen Sie "Start no client" und klicken Sie erneut auf "Next".
# -Aktivieren Sie bei den zusätzlichen Optionen "Disable access control" und klicken Sie auf "Next", dann auf "Finish".

in die WSL bash einfügen sucht mein dns ip und configuriert es 
# -echo "export DISPLAY=$(grep nameserver /etc/resolv.conf | sed 's/nameserver //'):0" >> ~/.bashrc
# - source ~/.bashrc

sudo snap install firefox

Download gekodriver 
# - wget https://github.com/mozilla/geckodriver/releases/download/v0.31.0/geckodriver-v0.31.0-linux64.tar.gz
# - tar -xvzf geckodriver-v0.31.0-linux64.tar.gz
# - chmod +x geckodriver
# - sudo mv geckodriver /usr/local/bin/
# - rm -rf geckodriver-v0.31.0-linux64.tar.gz

chrome driver installieren 
- wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
- sudo dpkg -i google-chrome-stable_current_amd64.deb
- sudo apt-get install -f
- google-chrome --version 

driver von chrome installiern 
- wget https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/121.0.6167.85/linux64/chrome-linux64.zip
- options = Options()
gecko_path = '/snap/bin/firefox.geckodriver'
service = Service(executable_path=gecko_path)

options.headless = True
driver = webdriver.Firefox(service=service, options=options)
