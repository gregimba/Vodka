function setup(){
	mkvirtualenv Vodka
	workon Vodka
	pip install -r requirements.txt
}


if hash workon 2>/dev/null; then
	setup
    else
        echo "Please install virtualenvwrapper"
    fi



