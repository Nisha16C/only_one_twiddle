#!/bin/bash

openssl dgst -sha256 -binary static/css/style.min.css | openssl base64 -A
echo "style.min.css"
openssl dgst -sha256 -binary static/css/style.css | openssl base64 -A
echo "style.css"
openssl dgst -sha256 -binary static/favicon.ico | openssl base64 -A
echo "favicon.ico"
openssl dgst -sha384 -binary <(curl -s https://kit.fontawesome.com/faa629c1cc.js) | openssl base64 -A
echo "kit fontawesome"
openssl dgst -sha384 -binary <(curl -s https://code.jquery.com/jquery-3.5.1.min.js) | openssl base64 -A
echo "code.jquery"
openssl dgst -sha256 -binary static/js/tweets/modal.js | openssl base64 -A
echo "modal.js"
openssl dgst -sha384 -binary <(curl -s https://unpkg.com/@popperjs/core@2.9.1/dist/umd/popper.min.js) | openssl base64 -A
echo "unpkg"
openssl dgst -sha384 -binary <(curl -s https://cdn.jsdelivr.net/gh/alpinejs/alpine@v2.x.x/dist/alpine.min.js) | openssl base64 -A
echo "cdn jsdelivr"
openssl dgst -sha256 -binary static/js/profiles/main.js | openssl base64 -A
echo "profile main.js"